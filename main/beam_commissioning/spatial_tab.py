# -*- coding: utf-8 -*-
"""
The tab to change spatial distribution file
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QApplication, QMessageBox, QHBoxLayout, QRadioButton)
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
        self.distribution_widget = QWidget()
        self.gaussian_button = QRadioButton('Gaussian distribution (FWHM)')
        self.uniform_button = QRadioButton('Uniform distribution')
        self.distance_widget = QWidget()
        self.x_label = QLabel('X (cm) =')
        self.x_line = QLineEdit()
        self.y_label = QLabel('Y (cm) =')
        self.y_line = QLineEdit()
        self.plot_button = QPushButton('Plot')
        self.plot_graph = pg.PlotWidget()
        # self.calc_button = QPushButton('Calculate')
        self.file_group = QGroupBox('Save new spatial distribution file')
        self.dir_button = QPushButton('Directory')
        self.dir_line = QLineEdit()
        self.name_lable = QLabel('File Name')
        self.name_line = QLineEdit()
        self.save_button = QPushButton('Save')
        
        # Layouts
        self.main_layout = QVBoxLayout()
        self.load_layout = QHBoxLayout()
        self.input_layout = QVBoxLayout()
        self.distribution_layout = QHBoxLayout()
        self.distance_layout = QHBoxLayout()
        self.file_layout = QGridLayout()

        self.dir_line.setText(os.getcwd() + '/beam_commissioning/Commissioned_Beams')
        self.x_line.setValidator(QDoubleValidator(self))
        self.y_line.setValidator(QDoubleValidator(self))
        
        self.layout_init()
        self.pushbutton_init()
        self.graph_init()
        
    def layout_init(self):
        self.load_layout.addWidget(self.load_button)
        self.load_layout.addWidget(self.load_label)
        self.load_widget.setLayout(self.load_layout)

        self.distribution_layout.addWidget(self.gaussian_button)
        self.distribution_layout.addWidget(self.uniform_button)
        self.distribution_widget.setLayout(self.distribution_layout)
        self.distance_layout.addWidget(self.x_label)
        self.distance_layout.addWidget(self.x_line)
        self.distance_layout.addWidget(self.y_label)
        self.distance_layout.addWidget(self.y_line)
        self.distance_widget.setLayout(self.distance_layout)
        self.input_layout.addWidget(self.distribution_widget)
        self.input_layout.addWidget(self.distance_widget)
        self.input_layout.addWidget(self.plot_button)
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
        self.plot_button.clicked.connect(self.show_plot)
        self.save_button.clicked.connect(self.save_file)
        self.gaussian_button.toggled.connect(self.distribution_type)
        self.uniform_button.toggled.connect(self.distribution_type)
        self.gaussian_button.setChecked(True)

    def graph_init(self):
        # self.plot_graph.setConfigureOptions(leftButtonPan=True)
        self.plot_graph.setBackground('w')
        self.plot_graph.setLabel('bottom', text='Distance (cm)')
        self.plot_graph.setLabel('left', text='Normalized Probability')
        self.plot_graph.setXRange(-0.5, 0.5)
        self.plot_graph.setYRange(0, 1.1)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.addLegend()

    def distribution_type(self):
        if self.gaussian_button.isChecked():
            glv.set_value('spatial distribution', 'gaussian')
        elif self.uniform_button.isChecked():
            glv.set_value('spatial distribution', 'uniform')

    def load_file(self):
        try:
            f = Finddir().find_beam_file()
            self.load_name = os.path.basename(f)
            self.load_label.setText('Loaded Spatial File: ' + self.load_name)
            a = np.loadtxt(f, dtype=str)
            if a.shape == (3, 2):
                self.x_line.setText(a[1, 1])
                self.y_line.setText(a[2, 1])
                if a[0, 0] == 'gaussian':
                    self.gaussian_button.setChecked(True)
                else:
                    self.uniform_button.setChecked(True)
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

    def show_plot(self):
        self.graph_init()
        self.plot_graph.clear()
        if self.gaussian_button.isChecked():
            x_sd = (float(self.x_line.text()) / 2.3548)
            y_sd = (float(self.y_line.text()) / 2.3548)
            x = np.linspace(-0.5, 0.5, 1000)
            y_y = (stats.norm.pdf(x, 0, y_sd)) * 2.51 * y_sd
            y_x = (stats.norm.pdf(x, 0, x_sd)) * 2.51 * x_sd
            self.plot_graph.plot(x, y_x, pen=pg.mkPen('r'), name='Spatial Distribution in X')
            self.plot_graph.plot(x, y_y, pen=pg.mkPen('b'), name='Spatial Distribution in Y')
        elif self.uniform_button.isChecked():
            x_uniform = float(self.x_line.text()) / 2
            y_uniform = float(self.y_line.text()) / 2
            x = np.linspace(-0.5, 0.5, 1000)
            y_x = np.where(abs(x) <= x_uniform, 1, 0)
            y_y = np.where(abs(x) <= y_uniform, 1, 0)
            self.plot_graph.plot(x, y_x, pen=pg.mkPen('r'), name='Spatial Distribution in X')
            self.plot_graph.plot(x, y_y, pen=pg.mkPen('b'), name='Spatial Distribution in Y')
        self.plot_graph.addLegend()

    def save_file(self):
        glv.set_value('new beam file directory', self.dir_line.text())
        glv.set_value('new beam file name', self.name_line.text())
        spatial = glv.get_value('spatial distribution')

        if New_File_Check().final_check():
            path = os.path.join(self.dir_line.text(), self.name_line.text())
            with open(path, 'w') as f:
                f.write(spatial + ' distribution' + '\n' +
                        'x ' + self.x_line.text() + '\n' +
                        'y ' + self.y_line.text())
            QMessageBox.information(self, 'OK', 'New spatial distribution file ' +
                                    self.name_line.text() + ' saved.')


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Spatial_Tab()
    w.show()
    app.exec_()
        


