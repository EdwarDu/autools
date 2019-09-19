#!/bin/sh
pyuic5 setup_main.ui -o setup_main_ui.py

declare -a replace_strings=(
    "s/from sr830_plot_widget/from ..SRS.sr830_plot_widget/g"
    "s/from laser_profiler_widget/from ..LaserProfiler.laser_profiler_widget/g"
    "s/from laser_profiler_zdepth_widget/from ..LaserProfiler.laser_profiler_zdepth_widget/g"
    "s/from measurement_plot_widget/from ..MeasurementPlot.measurement_plot_widget/g"
    "s/from pdv_plot_widget/from .pdv_plot_widget/g"
    "s/from lockin_plot_widget/from .lockin_plot_widget/g"
    "s/from pcali_plot_widget/from .pcali_plot_widget/g")

unameOut="$(uname -s)"

for rplr in "${replace_strings[@]}";
do
    case "${unameOut}" in
        Darwin*)    
            sed -i '' -e "$rplr" setup_main_ui.py;;
        *)  
            sed -i -e "$rplr" setup_main_ui.py;;
    esac
done

pyuic5 laser_alignment_z_dists.ui -o laser_alignment_z_dists_ui.py
pyuic5 pcali_wlen_power.ui -o pcali_wlen_power_ui.py
pyuic5 lim_xy.ui -o lim_xy_ui.py

