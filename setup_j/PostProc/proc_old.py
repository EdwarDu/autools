import sys
import os
import argparse
import re
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import concurrent.futures
import matplotlib.pyplot as plt


# Fitting function. I(x,y) = M(x,y)cos^2(Beta(x,y) - Theta) + C(x,y)
def intensity_func(theta, m, beta, c):
    return m*np.power(np.cos(beta-theta), 2) + c


def intensity_fit(theta, intensity):
    popt, pcov = curve_fit(intensity_func, theta, intensity,
                           p0=[0, 0, 0],
                           bounds=([-np.inf, -360, -np.inf],
                                   [np.inf, 360, np.inf]),
                           maxfev=2000)
    return popt


def intensity_para_fit(data: dict, data_size):
    m = np.zeros(data_size)
    beta = np.zeros(data_size)
    cons = np.zeros(data_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=6) as executor:
        height, width = data_size
        future_to_loc = {}
        for r in range(0, height):
            for c in range(0, width):
                theta = data.keys()
                intensity = [data[angle]["in"][r][c] for angle in theta]
                future_to_loc[executor.submit((intensity_fit, theta, intensity))] = (r, c)

        for future in concurrent.futures.as_completed(future_to_loc):
            r, c = future_to_loc[future]
            m_, beta_, con_ = future.result()
            m[r][c] = m_
            beta[r][c] = beta_
            cons[r][c] = con_

    return m, beta, cons

def display_image(data):
    fig = plt.figure()
    axes = fig.addsubplot(111, aspect="")


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input folder')
    args = parser.parse_args()

    data_dict = {}
    if os.path.exists(args.input):
        sub_folders = [x for x in os.listdir(args.input) if os.path.isdir(x) and x not in (".", "..")]
        for sub_folder in sub_folders:
            sub_folder_path = os.path.join(args.input, sub_folder)
            data_files = [x for x in os.listdir(sub_folder_path) if os.path.isfile(x)]

            lockin_in_data, lockin_out_data, trans_data = None, None, None
            for data_file in data_files:
                file_path = os.path.join(sub_folder_path, data_file)
                print(f"Loading information from {file_path}")
                if file_path.endswith("_info.txt"):
                    with open(file_path, "r") as f_info:
                        for line in f_info:
                            if line.startswith("DPPTTT polar"):
                                line_parts = re.split(line, " ")
                                polar_angle = int(line_parts[2])
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

        data_m, data_beta, data_cons = intensity_para_fit(data_dict, data_size)
