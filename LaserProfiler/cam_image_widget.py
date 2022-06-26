#!/usr/bin/env python3

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
import pyqtgraph as pg
import pyqtgraph.exporters
from matplotlib import cm
import numpy as np
import cv2
import math
import warnings

# pg.setConfigOption('background', 'w')
# pg.setConfigOption('foreground', 'k')


# FIT_LINE_COLOR=pg.mkColor(0, 0, 255)
# FRAME_LINE_COLOR=pg.mkColor(0, 0, 0)
# NOTE_COLOR=pg.mkColor(0, 0, 255)
# LINE_LABEL_COLOR=pg.mkColor(0, 0, 255)
# CH_LINE_COLOR=pg.mkColor(0, 255, 0)
# MID_LINE_COLOR=pg.mkColor(255, 0, 255)

FIT_LINE_COLOR=pg.mkColor('y')
FRAME_LINE_COLOR=pg.mkColor('w')
NOTE_COLOR=pg.mkColor(0, 255, 0)
LINE_LABEL_COLOR=pg.mkColor(255, 0, 255)
CH_LINE_COLOR=pg.mkColor(0, 255, 0)
MID_LINE_COLOR=pg.mkColor(255, 0, 255)

class CamImageWidget(pg.GraphicsLayoutWidget):
    image_size_changed = pyqtSignal(int, int, name='image_size_changed')

    def __init__(self, parent=None, **kargs):
        pg.GraphicsLayoutWidget.__init__(self, **kargs)
        self.setParent(parent)
        self.setWindowTitle("Cam Image")
        #self.nextCol()
        self.p_map = self.addPlot()

        self.image_data = np.random.rand(100, 100)
        self.map_img = pg.ImageItem()
        self.map_img.setOpts(axisOrder="row-major")
        self.map_img.setLevels([0, 1])
        self.map_img.setImage(image=self.image_data)
        self.__orig_image_data = self.image_data
        self.__img_rotate_angle = 0
        self.__img_hotspot_x = 0
        self.__img_hotspot_y = 0

        self.p_map.addItem(self.map_img)
        self.p_map.setAspectLocked(lock=True, ratio=1)
        self.p_map.invertY()
        self.p_map.showGrid(x=True, y=True, alpha=0.5)
        self.p_map.enableAutoRange(self.p_map.getViewBox().XYAxes, enable=True)

        self.img_gradient_item = pg.GradientEditorItem()
        self.img_gradient_item.loadPreset('thermal')
        self.img_gradient_item.setOrientation('right')
        self.img_gradient_item.setTickValue(0, 0)
        self.img_gradient_item.setTickValue(-1, 1)
        self.map_img.setLookupTable(self.img_gradient_item.colorMap().getLookupTable(0, 1, 256), update=True)
        self.img_gradient_item.sigGradientChangeFinished.connect(
            lambda: self.map_img.setLookupTable(self.img_gradient_item.colorMap().getLookupTable(0, 1, 256),
                                                update=True))
        self.addItem(self.img_gradient_item)

        self.image_width = self.image_data.shape[1]
        self.image_height = self.image_data.shape[0]

        self.__img_rotate_angle = 0
        self.__rotate_around_hotspot = 0

    @staticmethod
    def get_img_data_hotspot(image_data):
        max_temp = np.max(image_data)
        max_temp_locs = np.where(image_data == max_temp)
        max_temp_center_y, max_temp_center_x = (np.average(max_temp_locs[0]),
                                                np.average(max_temp_locs[1]))
        return max_temp_center_x, max_temp_center_y

    # NOT USED, the moving and clipping operations in this method is useless
    @staticmethod
    def rotate_image(img, around, angle, scale, cords = None):
        # create another image to move to center
        # Works, but not necessary
        height, width = img.shape[:2]
        cx, cy = around
        pad_t = max(height-2*cy, 0)
        pad_b = max(2*cy -height, 0)
        pad_l = max(width-2*cx, 0)
        pad_r = max(2*cy-width, 0)
        img2 = cv2.copyMakeBorder(img, pad_t, pad_b, pad_l, pad_r, cv2.BORDER_CONSTANT,
                                  value=0)
        corners = [[pad_l, pad_t, 1], [width+pad_l, pad_t, 1], [pad_l, height+pad_t, 1], [width+pad_l, height+pad_t, 1]]
        h2, w2 = img2.shape[:2]
        rx, ry = w2/2, h2/2
        rotate_matrix = cv2.getRotationMatrix2D(center=(rx, ry),angle=angle, scale=scale)
        abs_cos = abs(rotate_matrix[0,0])
        abs_sin = abs(rotate_matrix[0,1])
        bound_w = int(h2*abs_sin + w2 * abs_cos)
        bound_h = int(h2*abs_cos + w2 * abs_sin)
        rotate_matrix[0, 2] += bound_w/2 - rx
        rotate_matrix[1, 2] += bound_h/2 - ry
        img_rotated = cv2.warpAffine(src=img2, M=rotate_matrix, dsize=(bound_w, bound_h))
        b_xs = []
        b_ys = []
        for corner in corners:
            corner_n = np.dot(rotate_matrix, corner)
            b_xs.append(corner_n[0])
            b_ys.append(corner_n[1])

        b_t = int(min(b_ys))
        b_b = int(max(b_ys))
        b_l = int(min(b_xs))
        b_r = int(max(b_xs))

        new_cords = []
        if cords is not None:
            for cord in cords:
                cord2 = [cord[0]+pad_l, cord[1]+pad_t, 1]
                cord_n = np.dot(rotate_matrix, cord2)
                new_cords.append([cord_n[0]-b_l, cord_n[0]-b_t])
        img_bound = img_rotated[b_t:b_b, b_l:b_r]
        return img_bound, new_cords

    def update_image_data(self, image_data):
        img_height, img_width = image_data.shape[:2]
        self.__orig_image_data = image_data.copy()
        if img_height != self.image_height or img_width != self.image_width:
            # if origin image size changed then emit
            self.image_size_changed.emit(img_width, img_height)

        if self.__img_rotate_angle != 0:
            rx, ry = img_width/2, img_height/2
            rotate_matrix = cv2.getRotationMatrix2D(center=(rx, ry),angle=self.__img_rotate_angle, scale=1)
            abs_cos = abs(rotate_matrix[0,0])
            abs_sin = abs(rotate_matrix[0,1])
            bound_w = int(img_height*abs_sin + img_width * abs_cos)
            bound_h = int(img_height*abs_cos + img_width * abs_sin)
            rotate_matrix[0, 2] += bound_w/2 - rx
            rotate_matrix[1, 2] += bound_h/2 - ry
            image_data = cv2.warpAffine(src=image_data, M=rotate_matrix, dsize=(bound_w, bound_h))
            
            # Can'g rotate the mpa_h_line and map_v_line's cords every time, auto hotspot will set them below
            # otherwise leave them be
            #cord=[self.map_v_line.value(), self.map_h_line.value(), 1]
            #new_cord=np.dot(rotate_matrix, cord)
            #self.map_v_line.setValue(new_cord[0])
            #self.map_h_line.setValue(new_cord[1])

        self.image_data = image_data
        self.map_img.setImage(image=self.image_data)
        self.image_height, self.image_width = self.image_data.shape[:2]

    def refresh(self):
        self.update_image_data(self.__orig_image_data)


    @staticmethod
    def get_color_map(cmap_name: str):
        colormap = cm.get_cmap(cmap_name)
        colormap._init()
        lut = (colormap._lut * 255).view(np.ndarray)
        return lut

    @property
    def img_rotate_angle(self):
        return self.__img_rotate_angle

    @img_rotate_angle.setter
    def img_rotate_angle(self, a: float):
        if 0 <= a <= 360:
            self.__img_rotate_angle = a
            self.refresh()

    @property
    def rotate_around_hotspot(self):
        return self.__rotate_around_hotspot

    @rotate_around_hotspot.setter
    def rotate_around_hotspot(self, b_hotspot: bool):
        self.__rotate_around_hotspot = b_hotspot
        self.refresh()

    @property
    def hotspot_location(self):
        return self.__img_hotspot_x, self.__img_hotspot_y

    def grab_hotspot(self):
        self.__img_hotspot_x, self.__img_hotspot_y = CamImageWidget.get_img_data_hotspot(self.image_data)
        return self.__img_hotspot_x, self.__img_hotspot_y

    def export_image(self, prefix: str):
        map_exporter = pg.exporters.SVGExporter(self.scene())
        map_exporter.export(prefix+"_profile.svg")
        cv2.imwrite(prefix+"_image.png", self.image_data)
        np.savetxt(prefix+'_img.npraw', self.image_data)

    def load_raw(self, npraw_file: str):
        if npraw_file.endswith(".npraw"):
            image_data = np.loadtxt(npraw_file)
        else:
            # FIXME: add to try .. catch
            image_data = cv2.imread(npraw_file, cv2.IMREAD_GRAYSCALE)
        self.update_image_data(image_data)


def update_image(window, timer):
    import time
    # image = np.random.rand(2160, 2560)
    # t0 = time.time() * 1000
    # window.update_image_data(image)
    # t1 = time.time() * 1000
    # print(f"Update image cost {t1-t0}ms")
    # timer.singleShot(10000, lambda w=window, t=timer: update_image(w, t))
    #window.add_cross_marker()
    win.img_rotate_angle = (win.img_rotate_angle + 10) % 360
    timer.singleShot(2000, lambda w=window, t=timer: update_image(w, t))


if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    win = CamImageWidget()
    win.show()
    #file_path=input("Enter test image path: ")
    file_path="../tests/test.jpg"
    win.img_rotate_angle = 5
    win.update_image_data(cv2.imread(file_path, cv2.IMREAD_GRAYSCALE))
    update_timer = QtCore.QTimer(win)
    update_timer.singleShot(10000, lambda w=win, t=update_timer: update_image(w, t))

    app.exec_()
