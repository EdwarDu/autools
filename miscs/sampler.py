import os
import argparse
import re
import logging
import matplotlib.pyplot as plt
import numpy as np
import sys
import pickle


sampler_logger = logging.getLogger("sampler")
sampler_logger.setLevel(logging.INFO)
#sampler_logger_fh = logging.FileHandler("sampler.log")
sampler_logger_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
#sampler_logger_fh.setFormatter(sampler_logger_formatter)
#sampler_logger.addHandler(sampler_logger_fh)

sampler_logger_ch = logging.StreamHandler()
sampler_logger_ch.setFormatter(sampler_logger_formatter)
sampler_logger.addHandler(sampler_logger_ch)


def show_dis(fig_title: str, r_ts: np.ndarray, r_p: np.ndarray, bin_duration: float):
    fig = plt.figure(fig_title)
    axes_dis: plt.Axes = fig.add_subplot(111)
    axes_dis.vlines(r_ts, ymin=0, ymax=0.1, linestyles='dotted')
    axes_dis.vlines(r_p, ymin=0, ymax=1, color='red')
    axes_dis.set_title(fig_title)

    axes_his: plt.Axes = axes_dis.twinx()
    bin_seq = np.arange(0, np.min(r_p), bin_duration)
    hist_n, hist_bins, _ = axes_his.hist(r_ts, bins=bin_seq,
                                         ls='dashed', edgecolor='green',
                                         lw=1.2, fc=(0, 0, 1, 0.5))
    for n, b in zip(hist_n, hist_bins):
        axes_his.text(b + bin_duration/2, n,
                      f"{int(n)}", rotation='vertical',
                      verticalalignment='bottom',
                      horizontalalignment='center')

    # p_bin_seq = np.arange(np.min(r_p), max(np.max(r_p), np.min(r_p)+0.021), 0.02)
    # p_hist_n, p_hist_bins, _ = axes_his.hist(r_p, bins=p_bin_seq,
    #                                          ls='dashed', edgecolor='red',
    #                                          lw=1.2, fc=(1, 0, 0, 0.2))
    # for n, b in zip(p_hist_n, p_hist_bins):
    #     axes_his.text(b + 0.01, n,
    #                   f"{int(n)}", rotation='vertical',
    #                   verticalalignment='bottom',
    #                   horizontalalignment='center')

    axes_dis.set_ylim(bottom=0)
    axes_dis.set_xlim(left=0)  # , right=0.22)
    fig.tight_layout()
    fig.show()


def process_file(m_filename: str, eps: float, bin_duration: float, load_pickle: bool, period_cut_off: float = 0.22):
    if os.path.exists(m_filename):
        if not os.path.exists(m_filename + ".pickle") or not load_pickle:
            with open(m_filename, 'r') as f_input:
                sampler_logger.info(f"Processing {m_filename} with eps={eps}")
                sample_periods = {}
                current_period_ts = None
                pre_sample_value = None
                pre_time_ts = None
                prepre_sample_value = None
                prepre_time_ts = None

                row_index = 1
                for line in f_input:
                    line_parts = [float(x) for x in re.split('[, \t\r\n]', line) if x != '']
                    time_ts = line_parts[0] * 81e-12
                    sample_value = line_parts[1]
                    if sample_value == 3:
                        if current_period_ts is not None:
                            sampler_logger.info(f"new period at row {row_index} time_ts={time_ts}, "
                                                f"previous period: {time_ts-current_period_ts:g}")
                            if time_ts-current_period_ts > period_cut_off:
                                sampler_logger.error(f'Previous period longer than {period_cut_off}, throwing away'
                                                     f'{sample_periods[current_period_ts]}')
                                del sample_periods[current_period_ts]
                        else:
                            sampler_logger.info(f"new period at row {row_index} time_ts={time_ts}")
                        current_period_ts = time_ts

                    elif sample_value == 1:
                        if prepre_sample_value == 1 and pre_sample_value == 2:
                            sampler_logger.debug(f"1-2-1 pattern found at row {row_index}")
                            # Found the 1-2-1 pattern
                            if 0 < pre_time_ts - prepre_time_ts <= eps or 0 < time_ts - pre_time_ts <= eps:
                                # Pattern valid
                                sampler_logger.debug(f"pattern timing valid")
                                if current_period_ts is not None:
                                    sampler_logger.debug(f"pattern within valid period")
                                    if current_period_ts not in sample_periods.keys():
                                        sample_periods[current_period_ts] = []

                                    sample_periods[current_period_ts].append(pre_time_ts)  # put 2's time stamp
                                    sampler_logger.info(f'valid pattern found at row {row_index}')
                                else:
                                    sampler_logger.error(
                                        f"pattern NOT within valid period at row {row_index}")
                            else:
                                sampler_logger.debug(
                                    f"pattern timing NOT valid: "
                                    f"1-<{pre_time_ts - prepre_time_ts:g}>-2-<{time_ts - pre_time_ts:g}>-1")

                    row_index += 1
                    # prepare for next row
                    prepre_time_ts = pre_time_ts
                    pre_time_ts = time_ts
                    prepre_sample_value = pre_sample_value
                    pre_sample_value = sample_value

            sample_periods_ts = sorted(sample_periods.keys())
            relative_sample_ts = []

            for ts in sample_periods_ts:
                for s_ts in sample_periods[ts]:
                    relative_sample_ts.append(s_ts - ts)

            relative_sample_ts = np.array(relative_sample_ts)

            periods = []
            for i in range(1, len(sample_periods_ts)):
                p_i = sample_periods_ts[i] - sample_periods_ts[i-1]
                if p_i <= period_cut_off:
                    periods.append(p_i)

            periods = np.array(periods)
            with open(m_filename+'.pickle', 'wb') as f_pickle:
                pickle.dump([relative_sample_ts, periods], f_pickle)
        else:
            with open(m_filename + ".pickle", 'rb') as f_pickle:
                relative_sample_ts, periods = pickle.load(f_pickle)
        show_dis(m_filename, relative_sample_ts, periods, bin_duration)
        return relative_sample_ts, periods
    else:
        sampler_logger.error(f"{m_filename} does not exist")
        return None, None


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--input', nargs='+', required=True, help='input files')
    parser.add_argument('-e', '--eps', type=float, required=True, help='The epsilon value to check 1-2-1 pattern')
    parser.add_argument('-b', '--bin_duration', type=float, required=True,
                        help='the histgram interval')
    parser.add_argument('-c', '--cut_off', type=float, default=0.22,
                        help='periods longer than this will be thrown away')
    parser.add_argument('-l', '--load_pickle', action='store_true', help='load pickle file if exists')
    args = parser.parse_args()

    r_time_ts_all = np.array([])
    r_periods_all = np.array([])
    for f in args.input:
        sampler_logger.info(f'Processing {f}')
        t, p = process_file(f, args.eps, args.bin_duration, args.load_pickle, args.cut_off)
        plt.pause(0.01)
        if t is not None:
            r_time_ts_all = np.concatenate((r_time_ts_all, t))
            r_periods_all = np.concatenate((r_periods_all, p))

    show_dis('ALL', r_time_ts_all, r_periods_all, args.bin_duration)

    plt.pause(1)
    input('Enter to exit')
    sys.exit(0)

