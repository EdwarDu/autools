import sys
import os
import argparse
import re
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import concurrent.futures
import matplotlib.pyplot as plt
import traceback


# Fitting function. I(x,y) = M(x,y)cos^2(Beta(x,y) - Theta) + C(x,y)
def intensity_func(theta, m, beta, c):
    return m*np.power(np.cos(np.deg2rad(beta-theta)), 2) + c


def intensity_fit(theta, intensity):
    print(f"Fitting for {theta} and {intensity}")
    popt, pcov = curve_fit(intensity_func, theta, intensity,
                           p0=[0, 0, 0],
                           bounds=([0, 0, 0],     # Lower bounds for M beta C
                                   [np.inf, 360, np.inf]),    # Higher bounds
                           maxfev=2000)
    return popt


def intensity_para_fit(data: dict, data_size, n_workers: int = 4):
    m = np.zeros(data_size)
    beta = np.zeros(data_size)
    cons = np.zeros(data_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        height, width = data_size
        future_to_loc = {}
        for r in range(0, height):
            for c in range(0, width):
                theta = np.array([x for x in data.keys()])
                intensity = np.array([data[angle]["in"][r][c]/data[angle]["trans"][r][c] for angle in theta])
                future_to_loc[executor.submit(intensity_fit, theta, intensity)] = (r, c)

        for future in concurrent.futures.as_completed(future_to_loc):
            r, c = future_to_loc[future]
            try:
                m_, beta_, con_ = future.result()
            except Exception as exc:
                print(f"Fitting for ({r},{c}) failed due to except")
                break
                # traceback.print_tb(exc.__traceback__)
            else:
                m[r][c] = m_
                beta[r][c] = beta_
                cons[r][c] = con_

    return m, beta, cons


# noinspection DuplicatedCode
def display_image(data: np.ndarray, title: str = "Image"):
    fig = plt.figure()
    axes: plt.Axes = fig.add_subplot(111, aspect='equal')
    hm_v = axes.imshow(data, cmap=plt.cm.rainbow)
    axes.set_title(title)
    fig.colorbar(hm_v, ax=axes)

    # height, width = data.shape
    # x, y = np.meshgrid(np.arange(0, width, 1), np.arange(0, height, 1))
    # unit = np.ones(data.shape) * 2
    # data_deg = (data - np.min(data)) / (np.max(data) - np.min(data)) * np.pi * 2
    # # TODO: angle function needs to be fixed
    # u = unit * np.sin(data_deg)
    # v = unit * np.cos(data_deg)
    # axes.quiver(x, y, u, v, units='dots', scale=2, scale_units='xy', width=1, headwidth=4, headlength=6)
    fig.show()


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input folder')
    parser.add_argument('-p', '--parallel_worker', type=int, default=4,
                        help='number of parallel workers for curve fitting')
    args = parser.parse_args()

    if args.parallel_worker <= 0:
        args.parallel_worker = 4

    data_dict = {}
    if os.path.exists(args.input):
        sub_folders = [x for x in os.listdir(args.input) if os.path.isdir(os.path.join(args.input, x)) and x not in (".", "..")]
        for sub_folder in sub_folders:
            print(f"Found dataset folder {sub_folder}")
            sub_folder_path = os.path.join(args.input, sub_folder)
            data_files = [x for x in os.listdir(sub_folder_path) if os.path.isfile(os.path.join(sub_folder_path, x))]

            lockin_in_data, lockin_out_data, trans_data, polar_angle = None, None, None, None
            for data_file in data_files:
                file_path = os.path.join(sub_folder_path, data_file)
                print(f"Loading information from {file_path}")
                if file_path.endswith("_info.txt"):
                    with open(file_path, "r") as f_info:
                        for line in f_info:
                            if line.startswith("DPPTTT"):
                                line_parts = [x for x in re.split("[ \t]", line) if x != ""]
                                polar_angle = int(line_parts[1])
                                print(f"Polar angle {polar_angle}")
                                break
                elif file_path.endswith("_LockInIN.dat"):
                    lockin_in_data = np.loadtxt(file_path)
                    print(f"Loaded lockin IN data size: {lockin_in_data.shape}")
                elif file_path.endswith("_LockInOUT.dat"):
                    lockin_out_data = np.loadtxt(file_path)
                    print(f"Loaded lockin OUT data size: {lockin_out_data.shape}")
                elif file_path.endswith("_Transmission.dat"):
                    trans_data = np.loadtxt(file_path)
                    print(f"Loaded transmission data size: {trans_data.shape}")

            data_dict[polar_angle] = {}
            data_dict[polar_angle]["in"] = lockin_in_data
            data_dict[polar_angle]["out"] = lockin_out_data
            data_dict[polar_angle]["trans"] = trans_data

        # Verify all data has the same size
        data_size = None
        for polar_angle, angle_data in data_dict.items():
            if data_size is None:
                data_size = angle_data["in"].shape
                print(f"Data size should be {data_size}")

            if not (data_size == angle_data["in"].shape and
                data_size == angle_data["out"].shape and
                data_size == angle_data["trans"].shape):
                raise ValueError(f"data size inconsistent for {polar_angle}")

        data_m, data_beta, data_cons = intensity_para_fit(data_dict, data_size, args.parallel_worker)
        display_image(data_m, "M")
        display_image(data_beta, "BETA")
        display_image(data_cons, "C")

        plt.pause(1)
        input('Enter to close')
        plt.close()
    else:
        raise IOError(f"{args.input} does NOT exist.")
