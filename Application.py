from ImageProcessing_main import Ui_Dialog
from Indices_dialog import Ui_Dialog as Inui
from ImageClassification import Ui_Dialog as cui
import sys
import os
from PyQt5.QtWidgets import QApplication, QDialog, QMessageBox
from PyQt5 import QtCore, QtGui
from PyQt5 import QtWidgets
import rasterio
from rasterio.merge import merge
from rasterio.plot import show
import glob
import fnmatch
import numpy as np
import threading

ui = Ui_Dialog()
app = QApplication(sys.argv)
window = QDialog()
in_ui = Inui()
inapp = QApplication(sys.argv)
inwindow = QDialog()
icui = cui()
capp = QApplication(sys.argv)
cwindow = QDialog()
icon = QtGui.QIcon()
icon.addPixmap(QtGui.QPixmap(":/pwclogo/pwclogo.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
inp_dir_path = ""
out_dir_path = ""
ind_path = ""
c_inp_path = ""


class PercentageWorker(QtCore.QObject):
    started = QtCore.pyqtSignal()
    finished = QtCore.pyqtSignal()
    percentageChanged = QtCore.pyqtSignal(int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._percentage = 0

    @property
    def percentage(self):
        return self._percentage

    @percentage.setter
    def percentage(self, value):
        if self._percentage == value:
            return
        self._percentage = value
        self.percentageChanged.emit(self.percentage)

    def start(self):
        self.started.emit()

    def finish(self):
        self.finished.emit()


class FakeWorker:
    def start(self):
        pass

    def finish(self):
        pass

    @property
    def percentage(self):
        return 0

    @percentage.setter
    def percentage(self, value):
        pass


def message_box(msg_str):
    msg = QMessageBox()
    msg.setText(msg_str)
    msg.setWindowIcon(icon)
    msg.setWindowTitle("Alert")
    msg.setStandardButtons(QMessageBox.Ok)
    msg.exec_()
    return True


def browseClicked():
    try:
        dialog = QtWidgets.QFileDialog(None, "Select the Input Directory")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.DirectoryOnly)
        global inp_dir_path
        inp_dir_path = ""
        if dialog.exec_():
            inp_dir_path = str(dialog.selectedFiles()[0])
            ui.plainTextEdit.setPlainText(inp_dir_path)
        else:
            message_box("Please select a valid directory")
            ui.plainTextEdit.setPlainText("Directory not selected")
    except Exception as N:
        message_box("File Exception")
        ui.plainTextEdit.setPlainText(str(N))
    return True


def browseClickedClassification():
    try:
        dialog = QtWidgets.QFileDialog(None, "Select the Input Directory")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.DirectoryOnly)
        global inp_dir_path
        c_inp_path = ""
        if dialog.exec_():
            c_inp_path = str(dialog.selectedFiles()[0])
            icui.plainTextEdit.setPlainText(c_inp_path)
        else:
            message_box("Please select a valid directory")
            icui.plainTextEdit.setPlainText("Directory not selected")
    except Exception as N:
        message_box("File Exception")
        icui.plainTextEdit.setPlainText(str(N))
    return True


def browseClickedOut():
    try:
        dialog = QtWidgets.QFileDialog(None, "Select the Output Directory")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.DirectoryOnly)
        global out_dir_path
        out_dir_path = ""
        if dialog.exec_():
            out_dir_path = str(dialog.selectedFiles()[0])
            ui.plainTextEdit_2.setPlainText(out_dir_path)
        else:
            message_box("Please select a valid directory")
            ui.plainTextEdit_2.setPlainText("Directory not selected")
    except Exception as N:
        message_box("File Exception")
        ui.plainTextEdit_2.setPlainText(str(N))
    return True


def browseClickedIndices():
    try:
        dialog = QtWidgets.QFileDialog(None, "Select Input Bands")
        dialog.setFileMode(QtWidgets.QFileDialog.FileMode.ExistingFiles)
        global ind_path
        ind_path = ""
        if dialog.exec_() and len(dialog.selectedFiles()) == 2:
            ind_path = str(dialog.selectedFiles()[0]) + '\n' + str(dialog.selectedFiles()[1])
            in_ui.plainTextEdit.setPlainText(ind_path)
        else:
            message_box(" Select 2 Bands")
            in_ui.plainTextEdit.setPlainText("")
            ind_path = ""
    except Exception as N:
        message_box("File Exception")
        in_ui.plainTextEdit.setPlainText(str(N))
        ind_path = ""
    return True


def imageMosaic(worker=None):
    # print("imageMosaic")
    basedirpath = inp_dir_path
    bandsearch = ['B02', 'B03', 'B04', 'B08']
    bandcount = 0
    if worker is None:
        worker = FakeWorker()
    worker.start()
    while worker.percentage < 100:
        # print(foo, baz)
        # time.sleep(1)
        # worker.finish()

        def find(pattern, path):
            result = []
            for root, dirs, files in os.walk(path):
                for name in files:
                    if fnmatch.fnmatch(name, pattern):
                        result.append(os.path.join(root, name))
            return result

        # for searchtext in bandsearch:
        searchstring = '*_' + bandsearch[bandcount] + '_10m.JP2'
        files_tif = find(searchstring, basedirpath)
        print(files_tif)
        with rasterio.open(files_tif[0]) as src:
            meta = src.meta.copy()

        # The merge function returns a single array and the affine transform info
        arr, out_trans = merge(files_tif)

        meta.update({
            "driver": "GTiff",
            "height": arr.shape[1],
            "width": arr.shape[2],
            "transform": out_trans
        })

        # Write the mosaic raster to disk
        with rasterio.open(os.path.join(out_dir_path, bandsearch[bandcount] + '_s2.tif'), "w", **meta) as dest:
            dest.write(arr)
        # time.sleep(1)
        bandcount += 1
        worker.percentage += int(100 / len(bandsearch))
        worker.finish()
    return True


def bandStacking(worker=None):
    # global read_band
    bands = []
    if worker is None:
        worker = FakeWorker()
    worker.start()
    while worker.percentage < 100:
        for filenames in glob.glob(os.path.join(out_dir_path, "*.tif")):
            read_band = rasterio.open(filenames)
            bands.append(read_band.read(1, masked=True))
        out_meta = read_band.meta.copy()
        out_meta.update({"count": 4})
        print(out_meta)
        out_img = os.path.join(out_dir_path, "stacked_image.tif")
        with rasterio.open(out_img, 'w', **out_meta) as dest:
            for band_nr, src in enumerate(bands, start=1):
                dest.write(src, band_nr)
                worker.percentage += int(100 / len(bands))
        worker.finish()

    return True


def indicesCalculation(worker=None):
    bands = ind_path.split('\n')
    # print(bands)
    if worker is None:
        worker = FakeWorker()
    worker.start()
    selectedIndex = in_ui.comboBox.currentText()
    while worker.percentage < 100:
        with rasterio.open(bands[0]) as src:
            band_red = src.read(1)
            out_meta = src.meta.copy()
            worker.percentage += int(100 / 10)
        with rasterio.open(bands[1]) as src:
            band_nir = src.read(1)
            worker.percentage += int(100 / 10)
        band_red = band_red / 10000
        band_nir = band_nir / 10000
        worker.percentage += int(100 / 10)

        if selectedIndex == "NDVI":
            # Allow division by zero
            np.seterr(divide='ignore', invalid='ignore')

            # Calculate NDVI
            ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
            worker.percentage += int(100 / 10)
            # out_meta = band_red.meta.copy()
            out_meta.update({"dtype": 'float32', "count": 1})
            # print(out_meta)
            worker.percentage += int(100 / 10)
            with rasterio.open(os.path.join(out_dir_path, 'ndvi.tif'), 'w', **out_meta) as dst:
                worker.percentage += int(100 / 10)
                dst.write_band(1, ndvi.astype(rasterio.float32))
            worker.percentage += 40
        elif selectedIndex == "TNDVI":
            np.seterr(divide='ignore', invalid='ignore')

            # Calculate TNDVI
            ndvi = (band_nir.astype(float) - band_red.astype(float)) / (band_nir + band_red)
            tndvi = (ndvi + 0.5) ** 0.5
            worker.percentage += int(100 / 10)
            # out_meta = band_red.meta.copy()
            out_meta.update({"dtype": 'float32', "count": 1})
            # print(out_meta)
            worker.percentage += int(100 / 10)
            with rasterio.open(os.path.join(out_dir_path, 'tndvi.tif'), 'w', **out_meta) as dst:
                worker.percentage += int(100 / 10)
                dst.write_band(1, tndvi.astype(rasterio.float32))
            worker.percentage += 40
        elif selectedIndex == "SAVI":
            np.seterr(divide='ignore', invalid='ignore')

            # Calculate TNDVI
            savi = (band_nir.astype(float) - band_red.astype(float)) * (1.5) / (band_nir + band_red + 0.5)
            worker.percentage += int(100 / 10)
            # out_meta = band_red.meta.copy()
            out_meta.update({"dtype": 'float32', "count": 1})
            # print(out_meta)
            worker.percentage += int(100 / 10)
            with rasterio.open(os.path.join(out_dir_path, 'savi.tif'), 'w', **out_meta) as dst:
                worker.percentage += int(100 / 10)
                dst.write_band(1, savi.astype(rasterio.float32))
            worker.percentage += 40
        else:
            np.seterr(divide='ignore', invalid='ignore')

            # Calculate TNDVI
            msavi2 = (2 * band_nir.astype(float) + 1 - ((2 * band_nir.astype(float) + 1) ** 2 - 8 * (
                    band_nir.astype(float) - band_red.astype(float))) ** 0.5) / 2
            worker.percentage += int(100 / 10)
            # out_meta = band_red.meta.copy()
            out_meta.update({"dtype": 'float32', "count": 1})
            # print(out_meta)
            worker.percentage += int(100 / 10)
            with rasterio.open(os.path.join(out_dir_path, 'msavi2.tif'), 'w', **out_meta) as dst:
                worker.percentage += int(100 / 10)
                dst.write_band(1, msavi2.astype(rasterio.float32))
            worker.percentage += 40
        worker.finish()
    return True


def launch():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=imageMosaic,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def launch2():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=bandStacking,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def launch3():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=indicesCalculation,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def launchModelTraining():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=indicesCalculation,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def launchClassification():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=indicesCalculation,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def launchAccuracyAssessment():
    # print("inside launch")
    worker = PercentageWorker()
    worker.percentageChanged.connect(ui.progressBar.setValue)
    threading.Thread(
        target=indicesCalculation,
        kwargs=dict(worker=worker),
        daemon=True,
    ).start()


def indices_pressed():
    in_ui.setupUi(inwindow)
    in_ui.pushButton.clicked.connect(browseClickedIndices)
    in_ui.pushButton_2.clicked.connect(launch3)
    inwindow.show()
    inapp.exec_()
    return True


def mlClassification():
    icui.setupUi(cwindow)
    icui.pushButton.clicked.connect(browseClickedClassification)
    icui.pushButton_2.clicked.connect(launchModelTraining)
    icui.pushButton_3.clicked.connect(launchClassification)
    icui.pushButton_4.clicked.connect(launchAccuracyAssessment)
    cwindow.show()
    capp.exec_()
    return True


ui.setupUi(window)
ui.pushButton.clicked.connect(browseClicked)
ui.pushButton_2.clicked.connect(launch)
ui.pushButton_3.clicked.connect(launch2)
ui.pushButton_4.clicked.connect(indices_pressed)
ui.pushButton_5.clicked.connect(browseClickedOut)
ui.pushButton_6.clicked.connect(mlClassification)
window.show()
app.exec_()
