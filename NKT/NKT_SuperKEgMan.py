import traceback

from .NKTMan import NKTMan, nkt_logger
from .NKT_M66 import NKT_M66  # as NKT_SuperKRF
from .NKT_M60 import NKT_M60  # as NKT_SuperK
from .NKT_M67 import NKT_M67  # as NKT_SuperKSelect

from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QObject, pyqtSignal
from .NKT_SuperKEg_config_ui import Ui_NKT_SuperKEgConfigWindow
import serial
import serial.tools.list_ports
from typing import Union


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


# noinspection PyPep8Naming
class NKT_SuperKEgMan(QObject):
    # TODO: Unify the API to control the setup (different operations have to be done with different modules)
    def __init__(self):
        super().__init__()
        self.config_window = None
        self.com_man = NKTMan()
        self.m60: Union[NKT_M60, None] = None
        self.m66 = None
        self.m67 = None

    def scan_modules(self):
        modules = self.com_man.get_all_modules()
        for module_addr, module_type, module_name in modules:
            nkt_logger.info(f"Found module {module_type} - {module_name} at {hex(module_addr)}", extra={"component": "NKT"})
            if module_type == 0x60:
                self.m60 = NKT_M60(self.com_man, module_addr)
            elif module_type == 0x66:
                self.m66 = NKT_M66(self.com_man, module_addr)
            elif module_type == 0x67:
                self.m67 = NKT_M67(self.com_man, module_addr)

        if self.m60 is None or self.m66 is None or self.m67 is None:
            raise IOError(f"Not all modules are located {self.m60} {self.m66} {self.m67}")

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = NKT_SuperKEgConfigWindow(self)

        self.config_window.show()


# noinspection PyPep8Naming
class NKT_SuperKEgConfigWindow(Ui_NKT_SuperKEgConfigWindow):
    def __init__(self, nkt_superk_man: NKT_SuperKEgMan):
        self.nkt_s_man = nkt_superk_man
        self.window = QWidget()
        Ui_NKT_SuperKEgConfigWindow.__init__(self)
        self.setupUi(self.window)

        # COMM setting
        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.comboBox_COM_BaudRate.currentTextChanged.connect(self.baudrate_changed)
        self.comboBox_COM_Parity.currentTextChanged.connect(self.parity_changed)
        self.comboBox_CONN.currentIndexChanged.connect(self.conn_changed)

        # Force to change
        self.baudrate_changed(self.comboBox_COM_BaudRate.currentText())
        self.parity_changed(self.comboBox_COM_Parity.currentText())
        self.conn_changed(self.comboBox_CONN.currentData())

        self.refresh_comlist()

        self.pushButton_M60_SystemTypeRead.clicked.connect(self.m60_system_type_read)
        self.pushButton_M60_InLetTempRead.clicked.connect(self.m60_inlet_temp_read)
        self.pushButton_M60_EmissionRead.clicked.connect(self.m60_emission_read)
        self.pushButton_M60_EmissionSet.clicked.connect(self.m60_emission_set)
        self.pushButton_M60_SetupRead.clicked.connect(self.m60_setup_read)
        self.pushButton_M60_SetupSet.clicked.connect(self.m60_setup_set)
        self.pushButton_M60_InterLockRead.clicked.connect(self.m60_interlock_read)
        self.pushButton_M60_InterLockSet.clicked.connect(self.m60_interlock_set)
        self.pushButton_M60_PulsePickerRatioRead.clicked.connect(self.m60_pulse_picker_ratio_read)
        self.pushButton_M60_PulsePickerRatioSet.clicked.connect(self.m60_pulse_picker_ratio_set)
        self.pushButton_M60_WatchDogIntervalRead.clicked.connect(self.m60_watchdog_interval_read)
        self.pushButton_M60_WatchDogIntervalSet.clicked.connect(self.m60_watchdog_interval_set)
        self.pushButton_M60_PowerLevelRead.clicked.connect(self.m60_power_level_read)
        self.pushButton_M60_PowerLevelSet.clicked.connect(self.m60_power_level_set)
        self.pushButton_M60_CurrentLevelRead.clicked.connect(self.m60_current_level_read)
        self.pushButton_M60_CurrentLevelSet.clicked.connect(self.m60_current_level_set)
        self.pushButton_M60_ErrorCodeRead.clicked.connect(self.m60_error_code_read)
        self.pushButton_M60_StatusRead.clicked.connect(self.m60_status_read)
        self.pushButton_M60_ReadAll.clicked.connect(self.m60_read_all)

        self.pushButton_M66_RFPowerRead.clicked.connect(self.m66_RF_power_read)
        self.pushButton_M66_RFPowerSet.clicked.connect(self.m66_RF_power_set)
        self.pushButton_M66_SetupBitsRead.clicked.connect(self.m66_setup_bits_read)
        self.pushButton_M66_SetupBit0.clicked.connect(self.m66_setup_bit0)
        self.pushButton_M66_SetupBit1.clicked.connect(self.m66_setup_bit1)
        self.pushButton_M66_SetupBit2.clicked.connect(self.m66_setup_bit2)
        self.pushButton_M66_SetupBitsSet.clicked.connect(self.m66_setup_bits_set)
        self.pushButton_M66_MinWaveLengthRead.clicked.connect(self.m66_min_wavelength_read)
        self.pushButton_M66_MaxWaveLengthRead.clicked.connect(self.m66_max_wavelength_read)
        self.pushButton_M66_CrystalTempRead.clicked.connect(self.m66_crystal_temp_read)
        self.pushButton_M66_FSKModeRead.clicked.connect(self.m66_FSK_mode_read)
        self.pushButton_M66_FSKModeSet.clicked.connect(self.m66_FSK_mode_set)
        self.pushButton_M66_DaughterBoardRead.clicked.connect(self.m66_daughter_board_read)
        self.pushButton_M66_DaughterBoardSet.clicked.connect(self.m66_daughter_board_set)
        self.pushButton_M66_ConnCrystalRead.clicked.connect(self.m66_conn_crystal_read)
        self.pushButton_M66_ConnCrystalSet.clicked.connect(self.m66_conn_crystal_set)
        self.pushButton_M66_ChWaveLengthRead.clicked.connect(self.m66_ch0_wavelength_read)
        self.pushButton_M66_ChWaveLengthSet.clicked.connect(self.m66_ch0_wavelength_set)
        self.pushButton_M66_ChAmplitudeRead.clicked.connect(self.m66_amplitude_read)
        self.pushButton_M66_ChAmplitudeSet.clicked.connect(self.m66_amplitude_set)
        self.pushButton_M66_ModulationGainRead.clicked.connect(self.m66_modulation_gain_read)
        self.pushButton_M66_ModulationGainSet.clicked.connect(self.m66_modulation_gain_set)
        self.pushButton_M66_StatusRead.clicked.connect(self.m66_status_read)
        self.pushButton_M66_ErrorCodeRead.clicked.connect(self.m66_error_code_read)
        self.pushButton_M66_ReadAll.clicked.connect(self.m66_read_all)

        self.pushButton_M67_Monitor1Read.clicked.connect(self.m67_monitor1_read)
        self.pushButton_M67_Monitor2Read.clicked.connect(self.m67_monitor2_read)
        self.pushButton_M67_Monitor1GainRead.clicked.connect(self.m67_monitor1_gain_read)
        self.pushButton_M67_Monitor1GainSet.clicked.connect(self.m67_monitor1_gain_set)
        self.pushButton_M67_Monitor2GainRead.clicked.connect(self.m67_monitor2_gain_read)
        self.pushButton_M67_Monitor2GainSet.clicked.connect(self.m67_monitor2_gain_set)
        self.pushButton_M67_RFSwitchRead.clicked.connect(self.m67_RF_switch_read)
        self.pushButton_M67_RFSwitchSet.clicked.connect(self.m67_RF_switch_set)
        self.pushButton_M67_MonitorSwitchSet.clicked.connect(self.m67_monitor_switch_set)
        self.pushButton_M67_MonitorSwitchRead.clicked.connect(self.m67_monitor_switch_read)
        self.pushButton_M67_Crystal1MinWaveLengthRead.clicked.connect(self.m67_crystal1_min_wavelength_read)
        self.pushButton_M67_Crystal1MaxWaveLengthRead.clicked.connect(self.m67_crystal1_max_wavelength_read)
        self.pushButton_M67_Crystal2MinWaveLengthRead.clicked.connect(self.m67_crystal2_min_wavelength_read)
        self.pushButton_M67_Crystal2MaxWaveLengthRead.clicked.connect(self.m67_crystal2_max_wavelength_read)
        self.pushButton_M67_StatusRead.clicked.connect(self.m67_status_read)
        self.pushButton_M67_ErrorCodeRead.clicked.connect(self.m67_error_code_read)
        self.pushButton_M67_ReadAll.clicked.connect(self.m67_read_all)

    def conn_changed(self, i: int):
        self.nkt_s_man.com_man.com_dev = self.comboBox_CONN.currentData()

    def parity_changed(self, p: str):
        if p == 'None':
            self.nkt_s_man.com_man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.nkt_s_man.com_man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.nkt_s_man.com_man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.nkt_s_man.com_man.ser_baudrate = b

    def refresh_comlist(self):
        self.comboBox_CONN.clear()
        com_dict = get_available_COMs()
        for com_dev in com_dict.keys():
            self.comboBox_CONN.addItem(com_dev + ':' + com_dict[com_dev], com_dev)

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_conn()
        else:
            # FIXME: Actually open connection
            self.open_conn()

    def open_conn(self):
        try:
            self.nkt_s_man.com_man.open()
            self.nkt_s_man.scan_modules()
            self.pushButton_COM_Open.setText("Close")
            self.pushButton_COM_Open.setChecked(True)
            # Disable the COM configuration input
            self.comboBox_CONN.setDisabled(True)
            self.comboBox_COM_BaudRate.setDisabled(True)
            self.comboBox_COM_Parity.setDisabled(True)
            self.pushButton_COM_Refresh.setDisabled(True)
            # Enable the settings input
            self.groupBox_M60.setDisabled(False)
            self.groupBox_M66.setDisabled(False)
            self.groupBox_M67.setDisabled(False)
            self.label_COM_Status.setStyleSheet("background: green")

            # update current settings
            nkt_logger.info(f"NKT SuperK Sys COM connection opened", extra={"component": "NKT"})
            nkt_logger.debug(f"NKT SuperK Sys COM: {self.nkt_s_man.com_man.com_dev} "
                             f"B:{self.nkt_s_man.com_man.ser_baudrate} "
                             f"P:{self.nkt_s_man.com_man.ser_parity} "
                             f"S:{self.nkt_s_man.com_man.ser_stopbits}", extra={"component": "NKT"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            nkt_logger.error(f"Failed to open NKT SuperK Sys COM connection", extra={"component": "NKT"})
            self.close_conn()

    def close_conn(self):
        self.nkt_s_man.com_man.close()
        # FIXME: stop all the SR830 update activities
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
        self.comboBox_CONN.setDisabled(False)
        self.comboBox_COM_BaudRate.setDisabled(False)
        self.comboBox_COM_Parity.setDisabled(False)
        self.pushButton_COM_Refresh.setDisabled(False)
        # Disable the settings input
        self.groupBox_M60.setDisabled(True)
        self.groupBox_M66.setDisabled(True)
        self.groupBox_M67.setDisabled(True)
        self.label_COM_Status.setStyleSheet("background: red")
        nkt_logger.info(f"NKT SuperK Sys COM connection closed", extra={"component": "NKT"})

    def m60_system_type_read(self):
        s_t = self.nkt_s_man.m60.system_type
        if s_t == 0:
            self.lineEdit_M60_SystemType.setText(f"SuperK Extreme")
        elif s_t == 1:
            self.lineEdit_M60_SystemType.setText(f"SuperK Fianium")
        else:
            self.lineEdit_M60_SystemType.setText(f"Unknown")

    def m60_inlet_temp_read(self):
        self.lineEdit_M60_InLetTemp.setText(f"{self.nkt_s_man.m60.inlet_temperature/10}")

    def m60_emission_read(self):
        emission_i = self.nkt_s_man.m60.emission
        if emission_i == 0:
            self.comboBox_M60_Emission.setCurrentText("OFF")
        elif emission_i == 3:
            self.comboBox_M60_Emission.setCurrentText("ON")

    def m60_emission_set(self):
        self.nkt_s_man.m60.emission = self.comboBox_M60_Emission.currentText() == "ON"
        self.m60_emission_read()

    def m60_setup_read(self):
        self.comboBox_M60_Setup.setCurrentIndex(self.nkt_s_man.m60.setup)

    def m60_setup_set(self):
        self.nkt_s_man.m60.setup = self.comboBox_M60_Setup.currentIndex()
        self.m60_setup_read()

    def m60_interlock_read(self):
        lsb, msb = self.nkt_s_man.m60.interlock
        if lsb == 0:
            msg = "OFF; "
            if msb == 1:
                msg += "Front panel interlock / key switch OFF"
            elif msb == 2:
                msg += "Door switch open"
            elif msb == 3:
                msg += "External module interlock"
            elif msb == 4:
                msg += "Application interlock"
            elif msb == 5:
                msg += "Internal module interlock"
            elif msb == 6:
                msg += "Interlock power failure"
            elif msb == 7:
                msg += "Interlock disabled by light source"
            else:
                msg += "UNKNOWN"
        elif lsb == 1:
            msg = "WAITING FOR RESET"
        elif lsb == 2:
            msg = "OKAY"
        else:
            msg = "UNKNOWN"

        if msb == 255:
            msg += " - Interlock circuit failure"

        self.lineEdit_M60_Interlock.setText(msg)

    def m60_interlock_set(self):
        self.nkt_s_man.m60.interlock = self.comboBox_M60_InterLock.currentText() == "ON"
        self.m60_interlock_read()

    def m60_pulse_picker_ratio_read(self):
        self.spinBox_M60_PulsePickerRatio.setValue(self.nkt_s_man.m60.pulse_picker_ratio)

    def m60_pulse_picker_ratio_set(self):
        self.nkt_s_man.m60.pulse_picker_ratio = self.spinBox_M60_PulsePickerRatio.value()
        self.m60_pulse_picker_ratio_read()

    def m60_watchdog_interval_read(self):
        self.spinBox_M60_WatchDogInterval.setValue(self.nkt_s_man.m60.watchdog_interval)

    def m60_watchdog_interval_set(self):
        self.nkt_s_man.m60.watchdog_interval = self.spinBox_M60_WatchDogInterval.value()
        self.m60_watchdog_interval_read()

    def m60_power_level_read(self):
        self.spinBox_M60_PowerLevel.setValue(self.nkt_s_man.m60.power_level)

    def m60_power_level_set(self):
        self.nkt_s_man.m60.power_level = self.spinBox_M60_PowerLevel.value()
        self.m60_power_level_read()

    def m60_current_level_read(self):
        self.spinBox_M60_CurrentLevel.setValue(self.nkt_s_man.m60.current_level)

    def m60_current_level_set(self):
        self.nkt_s_man.m60.current_level = self.spinBox_M60_CurrentLevel.value()
        self.m60_current_level_read()

    def m60_error_code_read(self):
        self.lineEdit_M60_ErrorCode.setText(f"{hex(self.nkt_s_man.m60.error_code)}")

    def m60_status_read(self):
        status = self.nkt_s_man.m60.status
        lbl_status_bits = {
            0: self.label_M60_StatusBit0,
            1: self.label_M60_StatusBit1,
            2: self.label_M60_StatusBit2,
            3: self.label_M60_StatusBit3,
            4: self.label_M60_StatusBit4,
            5: self.label_M60_StatusBit5,
            6: self.label_M60_StatusBit6,
            7: self.label_M60_StatusBit7,
            13: self.label_M60_StatusBit13,
            14: self.label_M60_StatusBit14,
            15: self.label_M60_StatusBit15
        }

        for bit_index, lbl in lbl_status_bits.items():
            if status & (0x01 << bit_index) != 0:
                lbl.setStyleSheet("background: red")
            else:
                lbl.setStyleSheet("")

    def m60_read_all(self):
        self.m60_system_type_read()
        self.m60_inlet_temp_read()
        self.m60_emission_read()
        self.m60_setup_read()
        self.m60_interlock_read()
        self.m60_pulse_picker_ratio_read()
        self.m60_watchdog_interval_read()
        self.m60_power_level_read()
        self.m60_current_level_read()
        self.m60_error_code_read()
        self.m60_status_read()

    def m66_RF_power_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_RF_power_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_setup_bits_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_setup_bit0(self):
        # self.nkt_s_man.m66
        pass

    def m66_setup_bit1(self):
        # self.nkt_s_man.m66
        pass

    def m66_setup_bit2(self):
        # self.nkt_s_man.m66
        pass

    def m66_setup_bits_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_min_wavelength_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_max_wavelength_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_crystal_temp_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_FSK_mode_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_FSK_mode_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_daughter_board_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_daughter_board_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_conn_crystal_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_conn_crystal_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_ch0_wavelength_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_ch0_wavelength_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_amplitude_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_amplitude_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_modulation_gain_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_modulation_gain_set(self):
        # self.nkt_s_man.m66
        pass

    def m66_status_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_error_code_read(self):
        # self.nkt_s_man.m66
        pass

    def m66_read_all(self):
        # self.nkt_s_man.m66
        pass

    def m67_monitor1_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor2_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor1_gain_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor1_gain_set(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor2_gain_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor2_gain_set(self):
        # self.nkt_s_man.m67
        pass

    def m67_RF_switch_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_RF_switch_set(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor_switch_set(self):
        # self.nkt_s_man.m67
        pass

    def m67_monitor_switch_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_crystal1_min_wavelength_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_crystal1_max_wavelength_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_crystal2_min_wavelength_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_crystal2_max_wavelength_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_status_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_error_code_read(self):
        # self.nkt_s_man.m67
        pass

    def m67_read_all(self):
        # self.nkt_s_man.m67
        pass

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == "__main__":
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])
    eg_man = NKT_SuperKEgMan()
    print(f'Starting...')
    eg_man.show_config_window()
    QApplication.instance().exec_()
    # TODO: standalone test
