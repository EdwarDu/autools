#!/usr/bin/env python3

import serial
import serial.tools.list_ports
import logging
from .piezo_config_ui import Ui_Piezo_Config_Window
from PyQt5.QtWidgets import QWidget
import traceback
import time

_SPLIT_LOG = False

if _SPLIT_LOG:
    piezo_logger = logging.getLogger("piezo")

    piezo_logger.setLevel(logging.INFO)
    piezo_fh = logging.FileHandler("piezo.log")
    piezo_formatter = logging.Formatter('%(asctime)s [%(component)s] - %(levelname)s - %(message)s')
    piezo_fh.setFormatter(piezo_formatter)
    piezo_logger.addHandler(piezo_fh)

    piezo_ch = logging.StreamHandler()
    piezo_ch.setFormatter(piezo_formatter)
    piezo_logger.addHandler(piezo_ch)
else:
    piezo_logger = logging.getLogger("autools_setup_main")

from .PiezoGCSCom import PiezoGCSCom


class PiezoMan(PiezoGCSCom):
    def __init__(self, serial_name=None, baudrate=115200, parity=serial.PARITY_NONE, stopbits=serial.STOPBITS_ONE,
                 uart_lock=None):
        PiezoGCSCom.__init__(self, serial_name, baudrate, parity, stopbits, uart_lock)
        self.config_window = None
        self.b_online = False
        self.b_closedloop = False
        self.x_em = 0.07
        self.y_em = 0.07
        self.z_em = 0.07

    def goto_xy(self, x, y, wait_10ms=300):
        self.set_target_pos(["A", x], ["B", y])
        i = 0
        while i < wait_10ms:
            pos = self.get_real_position("A", "B")
            pos_x, pos_y = pos["A"], pos["B"]
            if abs(pos_x - x) <= 0.01 and abs(pos_y - y) <= 0.01:
                return
            else:
                time.sleep(0.01)
                i += 1
        raise TimeoutError(f"PZT Unable to go to {x},{y} in {wait_10ms} x 10ms")

    def goto_xy_ont(self, x: float, y: float, wait_10ms=300):
        self.set_target_pos(["A", x], ["B", y])
        time.sleep(0.01)
        i = 0
        while i < wait_10ms:
            ont = self.get_on_target_status("A", "B")
            if ont["A"] and ont["B"]:
                pos = self.get_real_position("A", "B")
                pos_x, pos_y = pos["A"], pos["B"]
                piezo_logger.info(f"Target: {x}, {y}; Real Pos:{pos_x}, {pos_y}",
                                  extra={"component": "Piezo"})
                return
            else:
                time.sleep(0.01)
                i += 1
        raise TimeoutError(f"PZT Unable to go to {x},{y} in {wait_10ms} x 10ms")

    # TODO: merge functions
    def goto_xyz_combined(self, x: float or None = None, y: float or None = None, z: float or None = None,
                          wait_10ms=300):
        args = []
        if x is not None:
            args.append(["A", x])
        if y is not None:
            args.append(["B", y])
        if z is not None:
            args.append(["C", z])

        if len(args) == 0:
            return

        self.set_target_pos(*args)
        time.sleep(0.01)
        i = 0
        ont = {"A": False, "B": False, "C": False}
        while i < wait_10ms / 2:
            ont = self.get_on_target_status("A", "B", "C")
            if ont["A"] and ont["B"] and ont["C"]:
                pos = self.get_real_position("A", "B", "C")
                pos_x, pos_y, pos_z = pos["A"], pos["B"], pos["C"]
                piezo_logger.info(f"Target: {x}, {y}, {z}; Real Pos:{pos_x}, {pos_y}, {pos_z}",
                                  extra={"component": "Piezo"})
                return
            else:
                time.sleep(0.01)
                i += 1
        piezo_logger.info(f"On target status not working, switch to margin checking {x_em}, {y_em}, {z_em}",
                          extra={"component": "Piezo"})
        i = 0
        while i < wait_10ms / 2:
            moving_x, moving_y, moving_z = self.is_axes_moving()
            if moving_x or moving_y or moving_z:
                time.sleep(0.01)
                i += 1
                continue

            pos = self.get_real_position("A", "B", "C")
            pos_x, pos_y, pos_z = pos["A"], pos["B"], pos["C"]
            if (x is None or abs(pos_x - x) <= self.x_em or ont["A"]) and \
                    (y is None or abs(pos_y - y) <= self.y_em or ont["B"]) and \
                    (z is None or abs(pos_z - z) <= self.z_em or ont["C"]):
                return
            else:
                time.sleep(0.01)
                i += 1

        raise TimeoutError(f"PZT Unable to go to {x},{y} in {wait_10ms} x 10ms")

    def show_config_window(self):
        if self.config_window is None:
            self.config_window = PiezoConfigWindow(self)

        self.config_window.show()


# noinspection PyPep8Naming
def get_available_COMs():
    com_port_list = serial.tools.list_ports.comports()
    return {com.device: f'{com.manufacturer} {com.description}' for com in com_port_list}


class PiezoConfigWindow(Ui_Piezo_Config_Window):
    def __init__(self, piezoman: PiezoMan):
        self.piezo_man = piezoman
        self.window = QWidget()
        Ui_Piezo_Config_Window.__init__(self)
        self.setupUi(self.window)

        self.pushButton_COM_Refresh.clicked.connect(self.refresh_comlist)
        self.comboBox_COM.currentTextChanged.connect(self.com_changed)
        self.comboBox_COM_Baudrate.currentTextChanged.connect(self.baudrate_changed)
        self.comboBox_COM_Parity.currentTextChanged.connect(self.parity_changed)
        self.comboBox_COM_Stopbits.currentTextChanged.connect(self.stopbits_changed)

        self.pushButton_COM_Open.clicked.connect(self.open_conn_clicked)

        self.doubleSpinBox_XTarget_C.valueChanged.connect(lambda value: self.piezo_man.set_target_pos(["A", value]))
        self.doubleSpinBox_YTarget_C.valueChanged.connect(lambda value: self.piezo_man.set_target_pos(["B", value]))
        self.doubleSpinBox_ZTarget_C.valueChanged.connect(lambda value: self.piezo_man.set_target_pos(["C", value]))

        # self.doubleSpinBox_XTarget_C.editingFinished.connect(
        #     lambda: self.piezo_man.set_target_pos(["A", self.doubleSpinBox_XTarget_C.value()]))
        # self.doubleSpinBox_YTarget_C.editingFinished.connect(
        #     lambda: self.piezo_man.set_target_pos(["B", self.doubleSpinBox_YTarget_C.value()]))
        # self.doubleSpinBox_ZTarget_C.editingFinished.connect(
        #     lambda: self.piezo_man.set_target_pos(["C", self.doubleSpinBox_ZTarget_C.value()]))

        self.doubleSpinBox_XTarget_O.valueChanged.connect(
            lambda value: self.piezo_man.set_openloop_axis_value(["1", value]))
        self.doubleSpinBox_YTarget_O.valueChanged.connect(
            lambda value: self.piezo_man.set_openloop_axis_value(["2", value]))
        self.doubleSpinBox_ZTarget_O.valueChanged.connect(
            lambda value: self.piezo_man.set_openloop_axis_value(["3", value]))

        # self.doubleSpinBox_XTarget_O.editingFinished.connect(
        #     lambda: self.piezo_man.set_openloop_axis_value(["1", self.doubleSpinBox_XTarget_O.value()]))
        # self.doubleSpinBox_YTarget_O.editingFinished.connect(
        #     lambda: self.piezo_man.set_openloop_axis_value(["2", self.doubleSpinBox_YTarget_O.value()]))
        # self.doubleSpinBox_ZTarget_O.editingFinished.connect(
        #     lambda: self.piezo_man.set_openloop_axis_value(["3", self.doubleSpinBox_ZTarget_O.value()]))

        self.radioButton_OpenLoop.toggled.connect(self.switch_loop_mode)
        self.radioButton_ClosedLoop.toggled.connect(self.switch_loop_mode)

        self.radioButton_Online.toggled.connect(self.switch_online_mode)
        self.radioButton_Offline.toggled.connect(self.switch_online_mode)

        self.pushButton_Sync.clicked.connect(self.sync_current_axis_status)
        self.pushButton_GetVel.clicked.connect(self.sync_current_axis_velctrl)
        self.pushButton_SetVel.clicked.connect(self.set_current_axis_velctrl)

        self.doubleSpinBox_Xem.valueChanged.connect(self.axis_em_changed)
        self.doubleSpinBox_Yem.valueChanged.connect(self.axis_em_changed)
        self.doubleSpinBox_Zem.valueChanged.connect(self.axis_em_changed)
        self.doubleSpinBox_Xem.setValue(self.piezo_man.x_em)
        self.doubleSpinBox_Yem.setValue(self.piezo_man.y_em)
        self.doubleSpinBox_Zem.setValue(self.piezo_man.z_em)

        self.refresh_comlist()

    def axis_em_changed(self):
        self.piezo_man.x_em = self.doubleSpinBox_Xem.value()
        self.piezo_man.y_em = self.doubleSpinBox_Yem.value()
        self.piezo_man.z_em = self.doubleSpinBox_Zem.value()

    def switch_loop_mode(self):
        if self.radioButton_ClosedLoop.isChecked() and not self.piezo_man.b_closedloop:
            self.groupBox_Control_ClosedLoop.setEnabled(True)
            self.groupBox_Control_OpenLoop.setEnabled(False)
            self.piezo_man.set_servo_state(["A", 1], ["B", 1], ["C", 1])
            self.piezo_man.b_closedloop = True
        elif not self.radioButton_ClosedLoop.isChecked() and self.piezo_man.b_closedloop:
            self.groupBox_Control_ClosedLoop.setEnabled(False)
            self.groupBox_Control_OpenLoop.setEnabled(True)
            self.piezo_man.set_servo_state(["A", 0], ["B", 0], ["C", 0])
            self.piezo_man.b_closedloop = False

        if self.piezo_man.b_closedloop:
            self.piezo_man.set_drift_compensation_mode(['A', 1], ['B', 1], ['C', 1])
            # self.piezo_man.set_velocity_control_mode(["A", 1], ["B", 1], ["C", 1])
            self.label_VelUnit.setText("um/s")
        else:
            self.label_VelUnit.setText("V/s")

        self.sync_current_axis_status()
        self.sync_current_axis_velctrl()

    def switch_online_mode(self):
        if self.radioButton_Online.isChecked() and not self.piezo_man.b_online:
            self.groupBox_Control_Online.setEnabled(True)
            self.piezo_man.set_control_mode(["1", 1], ["2", 1], ["3", 1])
            self.piezo_man.b_online = True
        elif not self.radioButton_Online.isChecked() and self.piezo_man.b_online:
            self.groupBox_Control_Online.setEnabled(False)
            self.piezo_man.set_control_mode(["1", 0], ["2", 0], ["3", 0])
            self.piezo_man.b_online = False

    def refresh_comlist(self):
        self.comboBox_COM.clear()
        com_dict = get_available_COMs()
        for com_dev in com_dict.keys():
            self.comboBox_COM.addItem(com_dev + ':' + com_dict[com_dev], com_dev)

    def com_changed(self):
        self.piezo_man.com_dev = self.comboBox_COM.currentData()

    def parity_changed(self, p: str):
        if p == 'None':
            self.piezo_man.ser_parity = serial.PARITY_NONE
        elif p == 'ODD':
            self.piezo_man.ser_parity = serial.PARITY_ODD
        elif p == 'EVEN':
            self.piezo_man.ser_parity = serial.PARITY_EVEN
        else:
            raise ValueError(f"Unknown parity {p}")

    def baudrate_changed(self, b: int or str):
        if type(b) is str:
            b = int(b)
        self.piezo_man.ser_baudrate = b

    def stopbits_changed(self, b: int or str):
        if type(b) is str:
            b = float(b)

        if b == 1:
            self.piezo_man.ser_stopbits = serial.STOPBITS_ONE
        elif b == 1.5:
            self.piezo_man.ser_stopbits = serial.STOPBITS_ONE_POINT_FIVE
        elif b == 2:
            self.piezo_man.ser_stopbits = serial.STOPBITS_TWO
        else:
            raise ValueError(f"Unknown Stopbits {b}")

    def sync_current_control_status(self):
        online_status = self.piezo_man.get_control_mode("1", "2", "3")
        if online_status["1"] == online_status["2"] == online_status["3"]:
            self.radioButton_Online.setChecked(online_status["1"])
            self.radioButton_Offline.setChecked(not online_status["1"])
            self.piezo_man.b_online = online_status["1"]
        else:
            # Force to online mode
            self.radioButton_Online.setChecked(True)
            self.radioButton_Offline.setChecked(False)
            self.piezo_man.b_online = True

            self.piezo_man.set_control_mode(["1", 1, "2", 1, "3", 1])
        self.groupBox_Control_Online.setEnabled(self.piezo_man.b_online)

        loop_mode = self.piezo_man.get_servo_state("A", "B", "C")
        if loop_mode["A"] == loop_mode["B"] == loop_mode["C"]:
            self.radioButton_ClosedLoop.setChecked(loop_mode["A"])
            self.radioButton_OpenLoop.setChecked(not loop_mode["B"])
            self.piezo_man.b_closedloop = loop_mode["C"]
        else:
            # Force to closed loop mode
            self.radioButton_ClosedLoop.setChecked(True)
            self.radioButton_OpenLoop.setChecked(False)
            self.piezo_man.b_closedloop = True
            self.piezo_man.set_servo_state(["A", 1], ["B", 1], ["C", 1])
        self.groupBox_Control_ClosedLoop.setEnabled(self.piezo_man.b_closedloop)
        self.groupBox_Control_OpenLoop.setEnabled(not self.piezo_man.b_closedloop)

    def sync_current_axis_status(self):
        if self.piezo_man.b_online and self.piezo_man.b_closedloop:
            min_positions = self.piezo_man.get_min_commandable_position("A", "B", "C")
            self.doubleSpinBox_XTarget_C.setMinimum(min_positions["A"])
            self.doubleSpinBox_YTarget_C.setMinimum(min_positions["B"])
            self.doubleSpinBox_ZTarget_C.setMinimum(min_positions["C"])
            self.label_XMIN_C.setText(f"{min_positions['A']:.6f}")
            self.label_YMIN_C.setText(f"{min_positions['B']:.6f}")
            self.label_ZMIN_C.setText(f"{min_positions['C']:.6f}")

            max_positions = self.piezo_man.get_max_commandable_position("A", "B", "C")
            self.doubleSpinBox_XTarget_C.setMaximum(max_positions["A"])
            self.doubleSpinBox_YTarget_C.setMaximum(max_positions["B"])
            self.doubleSpinBox_ZTarget_C.setMaximum(max_positions["C"])
            self.label_XMAX_C.setText(f"{max_positions['A']:.6f}")
            self.label_YMAX_C.setText(f"{max_positions['B']:.6f}")
            self.label_ZMAX_C.setText(f"{max_positions['C']:.6f}")

        elif self.piezo_man.b_online and not self.piezo_man.b_closedloop:
            min_positions = self.piezo_man.get_out_voltage_low_limit("1", "2", "3")
            self.doubleSpinBox_XTarget_O.setMinimum(min_positions["1"])
            self.doubleSpinBox_YTarget_O.setMinimum(min_positions["2"])
            self.doubleSpinBox_ZTarget_O.setMinimum(min_positions["3"])
            self.label_XMIN_O.setText(f"{min_positions['1']:.6f}")
            self.label_YMIN_O.setText(f"{min_positions['2']:.6f}")
            self.label_ZMIN_O.setText(f"{min_positions['3']:.6f}")

            max_positions = self.piezo_man.get_out_voltage_high_limit("1", "2", "3")
            self.doubleSpinBox_XTarget_O.setMaximum(max_positions["1"])
            self.doubleSpinBox_YTarget_O.setMaximum(max_positions["2"])
            self.doubleSpinBox_ZTarget_O.setMaximum(max_positions["3"])
            self.label_XMAX_O.setText(f"{max_positions['1']:.6f}")
            self.label_YMAX_O.setText(f"{max_positions['2']:.6f}")
            self.label_ZMAX_O.setText(f"{max_positions['3']:.6f}")

            current_pos = self.piezo_man.get_out_voltage("1", "2", "3")
            self.label_XCurrentPos_O.setText(f"{current_pos['1']:.6f}")
            self.label_YCurrentPos_O.setText(f"{current_pos['2']:.6f}")
            self.label_ZCurrentPos_O.setText(f"{current_pos['3']:.6f}")

        # Current XYZ position
        current_pos = self.piezo_man.get_real_position("A", "B", "C")
        self.label_XCurrentPos_C.setText(f"{current_pos['A']:.6f}")
        self.label_YCurrentPos_C.setText(f"{current_pos['B']:.6f}")
        self.label_ZCurrentPos_C.setText(f"{current_pos['C']:.6f}")

    def sync_current_axis_velctrl(self):
        velctrls = self.piezo_man.get_velocity_control_mode("A", "B", "C")
        self.checkBox_VelCtrlX.setChecked(velctrls['A'] == 1)
        self.checkBox_VelCtrlY.setChecked(velctrls['B'] == 1)
        self.checkBox_VelCtrlZ.setChecked(velctrls['C'] == 1)

        vels = self.piezo_man.get_closedloop_velocity("A", "B", "C")
        self.doubleSpinBox_XVel.setValue(vels['A'])
        self.doubleSpinBox_YVel.setValue(vels['B'])
        self.doubleSpinBox_ZVel.setValue(vels['C'])

    def set_current_axis_velctrl(self):
        self.piezo_man.set_velocity_control_mode(["A", 1 if self.checkBox_VelCtrlX.isChecked() else 0],
                                                 ["B", 1 if self.checkBox_VelCtrlY.isChecked() else 0],
                                                 ["C", 1 if self.checkBox_VelCtrlZ.isChecked() else 0])
        self.piezo_man.set_closedloop_velocity(["A", self.doubleSpinBox_XVel.value()],
                                               ["B", self.doubleSpinBox_XVel.value()],
                                               ["C", self.doubleSpinBox_XVel.value()])
        self.sync_current_axis_velctrl()

    def open_conn_clicked(self, state):
        if not state:  # post event state
            self.close_ser_conn()
        else:
            # FIXME: Actually open connection
            self.open_ser_conn()

    def open_ser_conn(self):
        try:
            self.piezo_man.open()
            self.pushButton_COM_Open.setText("Close")
            self.pushButton_COM_Open.setChecked(True)
            # Disable the COM configuration input
            self.comboBox_COM.setDisabled(True)
            self.comboBox_COM_Baudrate.setDisabled(True)
            self.comboBox_COM_Parity.setDisabled(True)
            self.pushButton_COM_Refresh.setDisabled(True)
            self.comboBox_COM_Stopbits.setDisabled(True)
            # Enable the settings input
            self.groupBox_Control.setDisabled(False)
            self.label_COM_Status.setStyleSheet("background: green")

            # update current settings
            self.sync_current_control_status()
            self.sync_current_axis_status()
            piezo_logger.info(f"Piezo COM connection opened", extra={"component": "PIEZO"})
            piezo_logger.debug(f"Piezo COM: {self.piezo_man.com_dev} "
                               f"B:{self.piezo_man.ser_baudrate} "
                               f"P:{self.piezo_man.ser_parity} "
                               f"S:{self.piezo_man.ser_stopbits}", extra={"component": "PIEZO"})
        except Exception as e:
            traceback.print_tb(e.__traceback__)
            piezo_logger.error(f"Failed to open Piezo COM connection, {e}", extra={"component": "PIEZO"})
            self.close_ser_conn()

    def close_ser_conn(self):
        global piezo_logger
        self.piezo_man.close()
        self.pushButton_COM_Open.setText("Open")
        self.pushButton_COM_Open.setChecked(False)
        # Enable the COM configuration input
        self.comboBox_COM.setDisabled(False)
        self.comboBox_COM_Baudrate.setDisabled(False)
        self.comboBox_COM_Parity.setDisabled(False)
        self.pushButton_COM_Refresh.setDisabled(False)
        self.comboBox_COM_Stopbits.setDisabled(False)
        # Disable the settings input
        self.groupBox_Control.setDisabled(True)
        self.label_COM_Status.setStyleSheet("background: red")
        piezo_logger.info(f"Piezo COM connection closed", extra={"component": "PIEZO"})

    def show(self):
        self.window.show()

    def close(self):
        self.window.hide()


if __name__ == '__main__':
    from PyQt5.QtWidgets import QApplication

    app = QApplication([])

    piezo_man = PiezoMan()
    print(f'Starting...')
    piezo_man.show_config_window()
    QApplication.instance().exec_()
