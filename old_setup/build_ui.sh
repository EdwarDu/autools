#!/bin/sh
pyuic5 setup_main.ui -o setup_main_ui.py

declare -a replace_strings=(
    "s/from measurement_plot_widget/from ..MeasurementPlot.measurement_plot_widget/g"
)

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

pyuic5 save_settings.ui -o save_settings_ui.py
