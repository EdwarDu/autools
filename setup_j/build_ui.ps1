pyuic5 setup_main.ui -o setup_main_ui.py
(get-content setup_main_ui.py) -replace "from sr830_plot_widget","from ..SRS.sr830_plot_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from laser_profiler_widget","from ..LaserProfiler.laser_profiler_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from laser_profiler_zdepth_widget","from ..LaserProfiler.laser_profiler_zdepth_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from measurement_plot_widget","from ..MeasurementPlot.measurement_plot_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from pdv_plot_widget","from .pdv_plot_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from lockin_plot_widget","from .lockin_plot_widget" | Set-Content setup_main_ui.py
(get-content setup_main_ui.py) -replace "from pcali_plot_widget","from .pcali_plot_widget" | Set-Content setup_main_ui.py
pyuic5 laser_alignment_z_dists.ui -o laser_alignment_z_dists_ui.py
pyuic5 pcali_wlen_power.ui -o pcali_wlen_power_ui.py

