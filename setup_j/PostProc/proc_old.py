import sys
import os
import argparse
import re
import numpy as np
from scipy.optimize import curve_fit, OptimizeWarning
import concurrent.futures
import matplotlib.pyplot as plt
import matplotlib as mpl
import traceback
import pickle
import warnings
from lmfit import Model
import matplotlib.style as mplstyle
mplstyle.use('fast')

# warnings.simplefilter("error", OptimizeWarning)
plt.ion()


# Fitting function. I(x,y) = M(x,y)cos^2(Beta(x,y) - Theta) + C(x,y)
def intensity_func(theta, m, beta, c):
    return m*(np.cos(np.deg2rad(beta-theta))**2) + c


def intensity_fit(theta, intensity):
    # intensity_a = (np.max(intensity)-np.min(intensity))
    # con_up = np.mean(intensity)

    popt, pcov = curve_fit(intensity_func, theta, intensity,
                           method='trf',
                           # p0=[0, 0, 0],
                           bounds=([0, -90, 0],     # Lower bounds for M beta C
                                   [np.inf, 90, np.inf]),    # Higher bounds
                           maxfev=200000
                          )

    return popt


def intensity_lmfit(theta, intensity):
    imodel = Model(intensity_func)
    # intensity_a = (np.max(intensity) - np.min(intensity))
    con_up = np.mean(intensity)

    imodel.set_param_hint('m', value=1e-14, min=0, max=np.inf)
    imodel.set_param_hint('beta', value=0, min=-90, max=90)
    imodel.set_param_hint('c', value=1e-14, min=0, max=con_up)

    result = imodel.fit(intensity, theta=theta)
    params = result.params
    param_names = ('m', 'beta', 'c')
    return [params[x].value for x in param_names]


def intensity_para_fit(data: dict, data_size, n_workers: int = 4, fit_type: str = "scipy"):
    m = np.zeros(data_size)
    beta = np.zeros(data_size)
    cons = np.zeros(data_size)

    with concurrent.futures.ThreadPoolExecutor(max_workers=n_workers) as executor:
        height, width = data_size

        print(f"Fitting for H{height}xW{width}")
        future_to_loc = {}
        for r in range(0, height):
            for c in range(0, width):
                theta = np.array([x for x in data.keys()],
                                 dtype=np.float64)
                intensity = np.array([data[angle]["intensity"][r][c] for angle in theta],
                                     dtype=np.float64)
                if fit_type == "scipy":
                    future_to_loc[executor.submit(intensity_fit, theta, intensity)] = (r, c)
                elif fit_type == "lmfit":
                    future_to_loc[executor.submit(intensity_lmfit, theta, intensity)] = (r, c)
                else:
                    raise ValueError(f"Unknown fit type {fit_type}")

        res_count = 0
        for future in concurrent.futures.as_completed(future_to_loc):
            r, c = future_to_loc[future]
            try:
                m_, beta_, con_ = future.result()
                res_count += 1
                if res_count % width == 0:
                    print(".")
                elif res_count % width == 1:
                    print(f":{int(res_count/width):02d}:.", end='')
                else:
                    print(".", end='')
                # print(f"{r}, {c}:", m_, beta_, con_)
            except Exception as exc:
                print(f"Fitting for ({r},{c}) failed due to except")
                # traceback.print_tb(exc.__traceback__)
            else:
                m[r][c] = m_
                beta[r][c] = beta_
                cons[r][c] = con_

    return m, beta, cons


# noinspection DuplicatedCode
def display_image(data: np.ndarray, title: str = "Image", with_arrow: bool = False, cbar_norm = None):
    fig = plt.figure(title)
    axes: plt.Axes = fig.add_subplot(111, aspect='equal')
    hm_v = axes.imshow(data, cmap=plt.cm.rainbow, norm=cbar_norm)
    axes.set_title(title)
    if not 0.001 <= np.max(np.abs(data)) <= 1000:
        fig.colorbar(hm_v, ax=axes, format='%.0e')
    else:
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


def show_fitting(data: dict, r: int, c: int, m: np.ndarray, beta: np.ndarray, cons: np.ndarray, axes: plt.Axes = None):
    if axes is None:
        fig = plt.figure("Fitting")
        axes: plt.Axes = fig.add_subplot(111)
        axes.autoscale(enable=True, axis='both')
        axes.set_xlabel("Degree (Theta)")
        axes.set_ylabel("Intensity")
        axes.set_title(f"M:{m[r][c]}, Beta:{beta[r][c]}, C:{cons[r][c]}")

    theta = np.array([x for x in data.keys()])
    intensity = np.array([data[angle]["intensity"][r][c] for angle in theta],
                         dtype=np.float64)
    print(f"Theta: {theta}, I: {intensity}: {m[r][c]}, {beta[r][c]}, {cons[r][c]}")
    axes.plot(theta, intensity, 'x', label="Measurement")
    theta_360 = np.linspace(-180, 180, 360)
    intensity_360 = intensity_func(theta_360, m[r][c], beta[r][c], cons[r][c])
    axes.plot(theta_360, intensity_360, '--', label="Curve fitting")
    # axes.set_ylim(bottom=np.min(intensity, intensity_360)*0.8, top=1.2*np.max(intensity, intensity_360))
    # axes.set_xlim(left=-180, right=180)
    axes.relim()
    axes.autoscale_view(tight=True)

    if axes is None:
        axes.legend()
        fig.show()
        return fig


def show_fitting_errors(data: dict, m: np.ndarray, beta: np.ndarray, cons: np.ndarray):
    err = np.zeros(m.shape)
    r2 = np.zeros(m.shape)
    height, width = m.shape
    for r in range(0, height):
        for c in range(0, width):
            theta = np.array([x for x in data.keys()])
            intensity = np.array([data[angle]["intensity"][r][c] for angle in theta])
            intensity_fit_v = intensity_func(theta, m[r][c], beta[r][c], cons[r][c])
            err[r][c] = np.sum((intensity_fit_v-intensity)**2)
            ss_tot = np.sum((intensity-np.mean(intensity))**2)
            r2[r][c] = 1 - (err[r][c]/ss_tot)

    display_image(err, "Fitting Error")
    display_image(r2, "Fitting R^2",)  # cbar_norm=mpl.colors.Normalize(vmin=0, vmax=1))
    return err


def show_intensity(data: dict):
    theta_v = data.keys()
    for theta in theta_v:
        display_image(data[theta]["intensity"], f"Intensity @THETA={theta}")


def manual_patch_data(data: np.ndarray):
    height, width = data.shape
    directions = ((-1, -1), (-1, 0), (-1, 1), (0, 1), (0, -1), (-1, -1), (-1, 0), (-1, 1))
    for r in range(0, height):
        for c in range(0, width):
            if data[r][c] < 0:
                n = 0
                sum = 0
                for d in directions:
                    r_n = r + d[0]
                    c_n = c + d[1]
                    if 0 <= r_n < height and 0 <= c_n < width:
                        n += 1
                        sum += data[r][c]
                data[r][c] = sum / n

    return data


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', help='input folder')
    parser.add_argument('-p', '--parallel_worker', type=int, default=4,
                        help='number of parallel workers for curve fitting')
    parser.add_argument('-l', '--load', action="store_true", help="load pickle files")
    parser.add_argument('-t', '--fit_type', choices=["scipy", "lmfit"], default='scipy',
                        help='Fitting type')
    parser.add_argument('-c', '--check', choices=['single', 'row'], required=False,
                        help='chekcing fitting')
    parser.add_argument('-m', '--material', type=str, required=True, help='Material name to extract the angle')
    args = parser.parse_args()

    if args.parallel_worker <= 0:
        args.parallel_worker = 4

    data_dict = {}
    if os.path.exists(args.input):
        sub_folders = [x for x in os.listdir(args.input) if os.path.isdir(os.path.join(args.input, x)) and x not in (".", "..")]
        for sub_folder in sub_folders:
            if sub_folder.startswith("_"):
                continue
            print(f"Found dataset folder {sub_folder}")
            sub_folder_path = os.path.join(args.input, sub_folder)
            data_files = [x for x in os.listdir(sub_folder_path) if os.path.isfile(os.path.join(sub_folder_path, x))]

            lockin_in_data, lockin_out_data, trans_data, polar_angle, sensitivity = None, None, None, None, None
            for data_file in data_files:
                file_path = os.path.join(sub_folder_path, data_file)
                print(f"Loading information from {file_path}")
                if file_path.endswith("_info.txt"):
                    with open(file_path, "r") as f_info:
                        for line in f_info:
                            if line.startswith(args.material):
                                line_parts = [x for x in re.split("[ \t]", line) if x != ""]
                                polar_angle = int(line_parts[1])
                                print(f"Polar angle {polar_angle}")
                            elif line.startswith("Sensitivity:"):
                                line_parts = [x for x in re.split("[ \t]", line) if x != ""]
                                sensitivity = int(line_parts[1])
                                print(f"Sensitivity: {sensitivity} {line_parts[2]}")
                elif file_path.endswith("_LockInIN.dat"):
                    lockin_in_data = np.loadtxt(file_path, dtype=np.float64) * 1e-6
                    print(f"Loaded lockin IN data size: {lockin_in_data.shape}")
                elif file_path.endswith("_LockInOUT.dat"):
                    lockin_out_data = np.loadtxt(file_path, dtype=np.float64) * 1e-6
                    print(f"Loaded lockin OUT data size: {lockin_out_data.shape}")
                elif file_path.endswith("_Transmission.dat"):
                    trans_data = np.loadtxt(file_path, dtype=np.float64)
                    print(f"Loaded transmission data size: {trans_data.shape}")

            if polar_angle is None:
                continue

            if sensitivity == 20:
                lockin_in_data = lockin_in_data * 2
                lockin_out_data = lockin_out_data * 2
            elif sensitivity == 50:
                lockin_in_data = lockin_in_data * 5
                lockin_out_data = lockin_out_data * 5
            elif sensitivity == 100:
                lockin_in_data = lockin_in_data * 10
                lockin_out_data = lockin_out_data * 10
            elif sensitivity == 200:
                lockin_in_data = lockin_in_data * 20
                lockin_out_data = lockin_out_data * 20
            elif sensitivity == 5:
                lockin_in_data = lockin_in_data / 2
                lockin_out_data = lockin_out_data / 2
            elif sensitivity == 500:
                lockin_in_data = lockin_in_data * 50
                lockin_out_data = lockin_out_data * 50
            else:
                raise ValueError(f"Unknown sensitivity {sensitivity}")

            data_dict[polar_angle] = {}
            data_dict[polar_angle]["in"] = lockin_in_data
            data_dict[polar_angle]["out"] = lockin_out_data
            data_dict[polar_angle]["trans"] = trans_data
            data_dict[polar_angle]["intensity"] = lockin_in_data / trans_data

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

        # # FIXME: for testing individual fitting
        # theta = np.array([x for x in data_dict.keys()])
        # intensity = np.array([data_dict[angle]["in"][18][5] / data_dict[angle]["trans"][18][5] for angle in theta])
        # print(theta, intensity)
        # print(intensity_fit(theta, intensity))
        # sys.exit(0)

        show_intensity(data_dict)

        pickle_path = os.path.join(args.input, "m_beta_c.pickle")
        if args.load and os.path.exists(pickle_path):
            with open(pickle_path, "rb") as f_p:
                data_m, data_beta, data_cons = pickle.load(f_p)
        else:
            data_m, data_beta, data_cons = intensity_para_fit(data_dict, data_size, args.parallel_worker,
                                                              fit_type=args.fit_type)
            with open(pickle_path, "wb") as f_p:
                pickle.dump([data_m, data_beta, data_cons], f_p)

        display_image(data_m, "M")
        display_image(data_beta, "BETA", with_arrow=True)
        display_image(data_cons, "C")

        data_a = data_m / (data_m + 2*data_cons)
        display_image(data_a, "A")

        show_fitting_errors(data_dict, data_m, data_beta, data_cons)

        fig_fit = plt.figure("Fitting")
        axes: plt.Axes = fig_fit.add_subplot(111)
        fig_fit.show()
        axes.autoscale(enable=True, axis='both')
        height, width = data_size

        if args.check == 'row':
            while True:
                try:
                    row = int(input("ROW?(-1) to break "))
                    if row == -1:
                        break
                    if 0 <= row < height:
                        axes.clear()
                        for c in range(0, width):
                            show_fitting(data_dict, row, c, data_m, data_beta, data_cons, axes)
                        fig_fit.canvas.draw_idle()
                        fig_fit.canvas.flush_events()
                except:
                    pass
        elif args.check == 'single':
            while True:
                try:
                    row = int(input("ROW?(-1) to break "))
                    if row == -1:
                        break
                    col = int(input("COL?"))
                    if 0 <= row < height and 0 <= col < width:
                        axes.clear()
                        show_fitting(data_dict, row, col, data_m, data_beta, data_cons, axes)
                        fig_fit.canvas.draw_idle()
                        fig_fit.canvas.flush_events()
                except:
                    pass

        plt.pause(1)
        input('Enter to close')
        plt.close()
    else:
        raise IOError(f"{args.input} does NOT exist.")
