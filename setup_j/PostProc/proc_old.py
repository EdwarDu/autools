import sys
import os
import argparse
import re
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import concurrent.futures
import matplotlib.pyplot as plt
import traceback
import pickle


# Fitting function. I(x,y) = M(x,y)cos^2(Beta(x,y) - Theta) + C(x,y)
def intensity_func(theta, m, beta, c):
    return m*np.power(np.cos(np.deg2rad(beta-theta)), 2) + c


def intensity_fit(theta, intensity):
    print(f"Fitting for {theta} and {intensity}")
    popt, pcov = curve_fit(intensity_func, theta, intensity,
                           p0=[np.max(intensity)-np.min(intensity), 0, np.min(intensity)],
                           bounds=([-np.inf, -90, -np.inf],     # Lower bounds for M beta C
                                   [np.inf, 90, np.inf]),    # Higher bounds
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
def display_image(data: np.ndarray, title: str = "Image", with_arrow: bool = False):
    fig = plt.figure(title)
    axes: plt.Axes = fig.add_subplot(111, aspect='equal')
    hm_v = axes.imshow(data, cmap=plt.cm.rainbow)
    axes.set_title(title)
    fig.colorbar(hm_v, ax=axes)

    if with_arrow:
        height, width = data.shape
        x, y = np.meshgrid(np.arange(0, width, 1), np.arange(0, height, 1))
        unit = np.ones(data.shape) * 2
        data_deg = np.deg2rad(data)
        # TODO: angle function needs to be fixed
        u = unit * np.cos(data_deg)
        v = unit * np.sin(data_deg)
        axes.quiver(x, y, u, v, units='dots', scale=2, scale_units='xy', width=1, headwidth=4, headlength=6)

    fig.show()
    return fig


def show_fitting(data: dict, r: int, c: int, m: np.ndarray, beta: np.ndarray, cons: np.ndarray):
    fig = plt.figure("Fitting")
    axes: plt.Axes = fig.add_subplot(111, aspect="equal")
    axes.set_xlabel("Degree (Theta)")
    axes.set_ylabel("Intensity")

    theta = np.array([x for x in data.keys()])
    intensity = np.array([data[angle]["in"][r][c] / data[angle]["trans"][r][c] for angle in theta])
    axes.scatter(theta, intensity, label="Measurement")
    theta_360 = np.linspace(-180, 180, 360)
    intensity_360 = intensity_func(theta_360, m[r][c], beta[r][c], cons[r][c])
    axes.plot(theta_360, intensity_360, '--r', label="Curve fitting")
    axes.legend()
    fig.show()
    return fig


def show_fitting_errors(data: dict, m: np.ndarray, beta: np.ndarray, cons: np.ndarray):
    err = np.zeros(m.shape)
    height, width = m.shape
    for r in range(0, height):
        for c in range(0, width):
            theta = np.array([x for x in data.keys()])
            intensity = np.array([data[angle]["in"][r][c] / data[angle]["trans"][r][c] for angle in theta])
            intensity_fit_v = intensity_func(theta, m[r][c], beta[r][c], cons[r][c])
            err[r][c] = np.sum(np.abs(intensity_fit_v-intensity))

    display_image(err, "Fitting Error")
    return err


def show_intensity(data: dict):
    theta_v = data.keys()
    for theta in theta_v:
        display_image(data[theta]["in"]/data[theta]["trans"], f"Intensity @THETA={theta}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input folder')
    parser.add_argument('-p', '--parallel_worker', type=int, default=4,
                        help='number of parallel workers for curve fitting')
    parser.add_argument('-l', '--load', action="store_true", help="load pickle files")
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

        show_intensity(data_dict)

        if args.load and os.path.exists("m_beta_c.pickle"):
            with open("m_beta_c.pickle", "rb") as f_p:
                data_m, data_beta, data_cons = pickle.load(f_p)
        else:
            data_m, data_beta, data_cons = intensity_para_fit(data_dict, data_size, args.parallel_worker)
            with open("m_beta_c.pickle", "wb") as f_p:
                pickle.dump([data_m, data_beta, data_cons], f_p)

        display_image(data_m, "M")
        display_image(data_beta, "BETA", with_arrow=True)
        display_image(data_cons, "C")

        data_a = data_m / (data_m + 2*data_cons)
        display_image(data_a, "A")

        show_fitting_errors(data_dict, data_m, data_beta, data_cons)

        fig_fit = None
        while True:
            row = int(input("ROW? (-1) to break"))
            if row == -1:
                break
            col = int(input("COL?"))

            if fig_fit is not None:
                plt.close(fig_fit)
            fig_fit = show_fitting(data_dict, row, col, data_m, data_beta, data_cons)


        plt.pause(1)
        input('Enter to close')
        plt.close()
    else:
        raise IOError(f"{args.input} does NOT exist.")
