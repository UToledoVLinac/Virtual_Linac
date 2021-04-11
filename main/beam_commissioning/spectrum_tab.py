# -*- coding: utf-8 -*-
"""
The tab to change spectrum distribution file
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QApplication, QMessageBox, QHBoxLayout, QTableWidget,
                             QHeaderView, QTableWidgetItem, QCheckBox, QComboBox)
from FindDirectory import Finddir
import sys
import os
import numpy as np
import pyqtgraph as pg
import globalvar as glv
from beam_commissioning.new_file_check import New_File_Check


class Spectrum_Tab(QWidget):
    def __init__(self):
        super().__init__()

        self.info_label = QLabel('Information')
        self.load_widget = QWidget()
        self.load_button = QPushButton('Load File')
        self.load_label = QLabel('Loaded Spectrum File: ')
        self.new_file_group = QGroupBox('New Angular Distribution')
        self.data_table = QTableWidget()
        self.plot_widget = QWidget()
        self.old_checkbox = QCheckBox('Show Loaded Spectrum')
        self.new_checkbox = QCheckBox('Show New Spectrum')
        self.angle_label = QLabel('Plot the spectrum at angle:')
        self.angle_combo = QComboBox()
        self.plot_button = QPushButton('Plot')
        self.plot_graph = pg.PlotWidget()
        self.save_group = QGroupBox('Save new angular distribution file')
        self.dir_button = QPushButton('Directory')
        self.dir_line = QLineEdit()
        self.name_lable = QLabel('File Name')
        self.name_line = QLineEdit()
        self.save_button = QPushButton('Save')

        self.load_layout = QHBoxLayout()
        self.new_file_layout = QVBoxLayout()
        self.plot_layout = QGridLayout()
        self.save_layout = QGridLayout()
        self.main_layout = QVBoxLayout()

        self.dir_line.setText(os.getcwd() + '/beam_commissioning/Commissioned_Beams')
        self.old_checkbox.setChecked(True)
        self.new_checkbox.setChecked(True)

        self.layout_init()
        self.table_init()
        self.combo_init()
        self.graph_init()
        self.pushbutton_init()

    def layout_init(self):
        self.load_layout.addWidget(self.load_button)
        self.load_layout.addWidget(self.load_label)
        self.load_widget.setLayout(self.load_layout)
        self.new_file_layout.addWidget(self.data_table)
        self.new_file_group.setLayout(self.new_file_layout)
        self.plot_layout.addWidget(self.old_checkbox, 0, 0)
        self.plot_layout.addWidget(self.new_checkbox, 1, 0)
        self.plot_layout.addWidget(self.angle_label, 0, 1)
        self.plot_layout.addWidget(self.angle_combo, 0, 2)
        self.plot_layout.addWidget(self.plot_button, 1, 2)
        self.plot_widget.setLayout(self.plot_layout)
        self.save_layout.addWidget(self.dir_button, 0, 0)
        self.save_layout.addWidget(self.dir_line, 0, 1)
        self.save_layout.addWidget(self.name_lable, 1, 0)
        self.save_layout.addWidget(self.name_line, 1, 1)
        self.save_layout.addWidget(self.save_button, 2, 0)
        self.save_group.setLayout(self.save_layout)
        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.load_widget)
        self.main_layout.addWidget(self.new_file_group)
        self.main_layout.addWidget(self.plot_widget)
        self.main_layout.addWidget(self.plot_graph)
        self.main_layout.addWidget(self.save_group)
        self.setLayout(self.main_layout)

    def table_init(self):
        self.data_table.setRowCount(15)
        self.data_table.setColumnCount(19)
        self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.data_table.horizontalHeader().hide()
        self.data_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.data_table.setVerticalHeaderLabels(['Energy (MeV)', 'Angle 1', 'Angle 2', 'Angle 3', 'Angle 4',
                                                 'Angle 5', 'Angle 6', 'Angle 7', 'Angle 8', 'Angle 9',
                                                 'Angle 10', 'Angle 11', 'Angle 12', 'Angle 13', 'Angle 14'])

    def combo_init(self):
        self.angle_combo.addItem('All Angles')
        for i in range(1, 15):
            self.angle_combo.addItem('Angle ' + str(i))

    def graph_init(self):
        self.plot_graph.setBackground('w')
        self.plot_graph.setLabel('bottom', text='Energy (MeV)')
        self.plot_graph.setLabel('left', text='Probability')
        self.plot_graph.setXRange(0, 7)
        self.plot_graph.setYRange(0, 1.1)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.addLegend()

    def pushbutton_init(self):
        self.load_button.clicked.connect(self.load_file)
        self.plot_button.clicked.connect(self.show_plot)
        self.dir_button.clicked.connect(self.find_dir)
        self.save_button.clicked.connect(self.save_file)

    def load_file(self):
        try:
            f = Finddir().find_filepath()
            self.load_name = os.path.basename(f)
            self.load_label.setText('Loaded Spectrum File: ' + self.load_name)
            self.loaded_file = np.loadtxt(f, dtype=str)
            self.loaded_array = self.loaded_file[0:15, 1:20]
            if self.loaded_array.shape == (15, 19):
                for i in range(0, 15):
                    for j in range(0, 19):
                        self.data_table.setItem(i, j, QTableWidgetItem(self.loaded_array[i, j]))
            else:
                QMessageBox.warning(self, 'Error', 'This file is not an angular distribution file, please check.')
        except OSError:
            pass
        self.loaded_data()

    def loaded_data(self):
        self.loaded_array = self.loaded_array.astype(float)
        self.x_loaded = self.loaded_array[0, 0:19]
        self.y_loaded = self.loaded_array[1:15, 0:19]

    def new_data(self):
        self.new_array = np.zeros([15, 19])
        try:
            for i in range(0, 15):
                for j in range(0, 19):
                    self.new_array[i, j] = float(self.data_table.item(i, j).text())
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Cells in the table can not be blank. ')
        self.x_new = self.new_array[0, 0:19]
        self.y_new = self.new_array[1:15, 0:19]

    def show_plot(self):
        self.plot_graph.clear()
        self.new_data()
        choice = self.angle_combo.currentIndex()
        loaded_curve_name = 'Loaded Angle ' + str(choice)
        new_curve_name = 'New Angle ' + str(choice)
        r_color = ['b', 'g', 'r', 'c', 'm', 'y', 'k', 'd', 'l', 's', 'b', 'g', 'r', 'c']
        if choice == 0:
            if self.old_checkbox.isChecked():
                for i in range(0, 14):
                    curve_name = 'Loaded Angle ' + str(i + 1)
                    self.plot_graph.plot(self.x_loaded, self.y_loaded[i, 0:19],
                                         pen=pg.mkPen(r_color[i]), name=curve_name)
            if self.new_checkbox.isChecked():
                for i in range(0, 14):
                    curve_name = 'New Angle ' + str(i + 1)
                    self.plot_graph.plot(self.x_new, self.y_new[i, 0:19],
                                         pen=pg.mkPen(r_color[i]), name=curve_name)
        else:
            if self.old_checkbox.isChecked():
                self.plot_graph.plot(self.x_loaded, self.y_loaded[choice - 1, 0:19],
                                     pen=pg.mkPen('r'), name=loaded_curve_name)
            if self.new_checkbox.isChecked():
                self.plot_graph.plot(self.x_new, self.y_new[choice - 1, 0:19],
                                     pen=pg.mkPen('b'), name=new_curve_name)

    def find_dir(self):
        d = Finddir().find_dir()
        if d == '':
            d = self.dir_line.text()
        self.dir_line.setText(d)

    def save_file(self):
        glv.set_value('new beam file directory', self.dir_line.text())
        glv.set_value('new beam file name', self.name_line.text())
        self.new_data()

        text = 'Energy'
        for energy_i in range(0, 19):
            text += ' ' + str(self.new_array[0, energy_i])
        text += '\n'
        for i in range(1, 15):
            text += 'Angle' + str(i)
            for j in range(0, 19):
                text += ' ' + str(self.new_array[i, j])
            text += '\n'

        if New_File_Check().final_check():
            path = os.path.join(self.dir_line.text(), self.name_line.text())
            with open(path, 'w') as f:
                f.write(text)
            QMessageBox.information(self, 'OK', 'New Spectrum distribution file ' +
                                    self.name_line.text() + ' saved.')


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Spectrum_Tab()
    w.show()
    app.exec_()