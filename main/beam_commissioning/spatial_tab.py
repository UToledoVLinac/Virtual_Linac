# -*- coding: utf-8 -*-
"""
The tab to change spatial distribution file
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QApplication, QMessageBox, QHBoxLayout)
from FindDirectory import Finddir
import sys
import os
import numpy as np
import pyqtgraph as pg
import scipy.stats as stats
import globalvar as glv
from beam_commissioning.new_file_check import New_File_Check
from PyQt5.QtGui import QDoubleValidator


class Spatial_Tab(QWidget):
    def __init__(self):
        super().__init__()
        
        self.info_label = QLabel('The virtual photon source is located at (0, 0) and is 2-D Gaussian spatial '
                                 'distribution.')
        self.load_widget = QWidget()
        self.load_button = QPushButton('Load File')
        self.load_label = QLabel('Loaded Spatial File:')
        self.input_group = QGroupBox('Spatial Distributions')
        self.x_label = QLabel('X:')
        self.x_FWHM_label = QLabel('FWHM (cm) = ')
        self.x_FWHM_line = QLineEdit()
        self.x_SD_label = QLabel(', or SD (cm) = ')
        self.x_SD_line = QLineEdit()
        self.y_label = QLabel('Y:')
        self.y_FWHM_label = QLabel('FWHM (cm) = ')
        self.y_FWHM_line = QLineEdit()
        self.y_SD_label = QLabel(', or SD (cm) = ')
        self.y_SD_line = QLineEdit()
        self.plot_button = QPushButton('Plot')
        self.plot_graph = pg.PlotWidget()
        self.calc_button = QPushButton('Calculate')
        self.file_group = QGroupBox('Save new spatial distribution file')
        self.dir_button = QPushButton('Directory')
        self.dir_line = QLineEdit()
        self.name_lable = QLabel('File Name')
        self.name_line = QLineEdit()
        self.save_button = QPushButton('Save')
        
        # Layouts
        self.main_layout = QVBoxLayout()
        self.load_layout = QHBoxLayout()
        self.input_layout = QGridLayout()
        self.file_layout = QGridLayout()

        self.dir_line.setText(os.getcwd())
        self.x_FWHM_line.setValidator(QDoubleValidator(self))
        self.y_FWHM_line.setValidator(QDoubleValidator(self))
        self.x_SD_line.setValidator(QDoubleValidator(self))
        self.y_SD_line.setValidator(QDoubleValidator(self))
        
        self.layout_init()
        self.pushbutton_init()
        self.graph_init()
        
    def layout_init(self):
        self.load_layout.addWidget(self.load_button)
        self.load_layout.addWidget(self.load_label)
        self.load_widget.setLayout(self.load_layout)
        self.input_layout.addWidget(self.x_label, 0, 0)
        self.input_layout.addWidget(self.x_FWHM_label, 0, 1)
        self.input_layout.addWidget(self.x_FWHM_line, 0, 2)
        self.input_layout.addWidget(self.x_SD_label, 0, 3)
        self.input_layout.addWidget(self.x_SD_line, 0, 4)
        self.input_layout.addWidget(self.y_label, 1, 0)
        self.input_layout.addWidget(self.y_FWHM_label, 1, 1)
        self.input_layout.addWidget(self.y_FWHM_line, 1, 2)
        self.input_layout.addWidget(self.y_SD_label, 1, 3)
        self.input_layout.addWidget(self.y_SD_line, 1, 4)
        self.input_layout.addWidget(self.plot_button, 0, 5)
        self.input_layout.addWidget(self.calc_button, 1, 5)
        self.input_group.setLayout(self.input_layout)
        self.file_layout.addWidget(self.dir_button, 0, 0)
        self.file_layout.addWidget(self.dir_line, 0, 1)
        self.file_layout.addWidget(self.name_lable, 1, 0)
        self.file_layout.addWidget(self.name_line, 1, 1)
        self.file_layout.addWidget(self.save_button, 2, 0)
        self.file_group.setLayout(self.file_layout)
        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.load_widget)
        self.main_layout.addWidget(self.input_group)
        self.main_layout.addWidget(self.plot_graph)
        self.main_layout.addWidget(self.file_group)
        self.setLayout(self.main_layout)

    def pushbutton_init(self):
        self.load_button.clicked.connect(self.load_file)
        self.dir_button.clicked.connect(self.find_dir)
        self.calc_button.clicked.connect(self.calculate)
        self.plot_button.clicked.connect(self.show_plot)
        self.save_button.clicked.connect(self.save_file)

    def graph_init(self):
        # self.plot_graph.setConfigureOptions(leftButtonPan=True)
        self.plot_graph.setBackground('w')
        self.plot_graph.setLabel('bottom', text='Distance (cm)')
        self.plot_graph.setLabel('left', text='Normalized Probability')
        self.plot_graph.setXRange(-0.5, 0.5)
        self.plot_graph.setYRange(0, 1.1)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.addLegend()

    def load_file(self):
        try:
            f = Finddir().find_filepath()
            self.load_name = os.path.basename(f)
            self.load_label.setText('Loaded Spatial File: ' + self.load_name)
            a = np.loadtxt(f, dtype=str)
            if a.shape == (2, 2):
                self.x_FWHM_line.setText(a[0, 1])
                self.y_FWHM_line.setText(a[1, 1])
            else:
                QMessageBox.warning(self, 'Error', 'This file is not a spatial distribution file, please check.')
        except OSError:
            pass

    def find_dir(self):
        d = Finddir().find_dir()
        if d == '':
            pass
        else:
            self.dir_line.setText(d)

    def calculate(self):
        x_1 = self.x_FWHM_line.text()
        x_2 = self.x_SD_line.text()
        y_1 = self.y_FWHM_line.text()
        y_2 = self.y_SD_line.text()

        if x_1 == '' and x_2 != '':
            self.x_FWHM_line.setText(str("%.2f" % (2.3548 * float(x_2))))
        elif x_1 != '' and x_2 == '':
            self.x_SD_line.setText(str("%.2f" % (float(x_1) / 2.3548)))
        else:
            pass
        
        if y_1 == '' and y_2 != '':
            self.y_FWHM_line.setText(str("%.2f" % (2.3548 * float(y_2))))
        elif y_1 != '' and y_2 == '':
            self.y_SD_line.setText(str("%.2f" % (float(y_1) / 2.3548)))
        else:
            pass

    def show_plot(self):
        self.graph_init()
        self.plot_graph.clear()
        self.calculate()
        x_sd = float(self.x_SD_line.text())
        y_sd = float(self.y_SD_line.text())
        x = np.linspace(-0.5, 0.5, 1000)
        y_y = (stats.norm.pdf(x, 0, y_sd)) * 2.51 * y_sd
        y_x = (stats.norm.pdf(x, 0, x_sd)) * 2.51 * x_sd
        self.plot_graph.plot(x, y_x, pen=pg.mkPen('r'), name='Spatial Distribution in X')
        self.plot_graph.plot(x, y_y, pen=pg.mkPen('b'), name='Spatial Distribution in Y')
        self.plot_graph.addLegend()

    def save_file(self):
        glv.set_value('new beam file directory', self.dir_line.text())
        glv.set_value('new beam file name', self.name_line.text())

        if New_File_Check().final_check():
            path = os.path.join(self.dir_line.text(), self.name_line.text())
            with open(path, 'w') as f:
                f.write('x_FWHM ' + self.x_FWHM_line.text() + '\n' +
                        'y_FWHM ' + self.y_FWHM_line.text())
            QMessageBox.information(self, 'OK', 'New spatial distribution file ' +
                                    self.name_line.text() + ' saved.')


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Spatial_Tab()
    w.show()
    app.exec_()
        


