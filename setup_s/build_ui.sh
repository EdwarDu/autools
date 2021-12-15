#!/usr/bin/env zsh
pyuic5 setup_main.ui -o setup_main_ui.py

replace_strings=(
    "s/from laser_profiler_widget/from ..LaserProfiler.laser_profiler_widget/g"
)

unameOut=$(uname -s)

for rplr in ${replace_strings[@]}; do
    case ${unameOut} in
        Darwin*)
            sed -i '' -e "$rplr" setup_main_ui.py;;
        *)
            sed -i -e "$rplr" setup_main_ui.py;;
    esac
done

pyuic5 save_settings.ui -o save_settings_ui.py

