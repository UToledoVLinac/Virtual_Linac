# -*- coding: utf-8 -*-
"""
The tab to change angular distribution file
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QHBoxLayout, QApplication, QMessageBox, QTableWidget, QCheckBox,
                             QHeaderView, QTableWidgetItem)
from FindDirectory import Finddir
import sys
import os
import numpy as np
import pyqtgraph as pg
import globalvar as glv
import math
from beam_commissioning.new_file_check import New_File_Check


class Angular_Tab(QWidget):
    def __init__(self):
        super().__init__()

        self.info_label = QLabel('Information')
        self.load_widget = QWidget()
        self.load_button = QPushButton('Load File')
        self.load_label = QLabel('Loaded Angular File: ')
        self.new_file_group = QGroupBox('New Angular Distribution')
        self.data_table = QTableWidget()
        self.plot_widget = QWidget()
        self.old_checkbox = QCheckBox('Show Loaded Angular Distribution')
        self.new_checkbox = QCheckBox('Show New Angular Distribution')
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
        self.plot_layout = QHBoxLayout()
        self.save_layout = QGridLayout()
        self.main_layout = QVBoxLayout()

        self.dir_line.setText(os.getcwd())
        self.old_checkbox.setChecked(True)
        self.new_checkbox.setChecked(True)

        self.layout_init()
        self.table_init()
        self.graph_init()
        self.pushbutton_init()

    def layout_init(self):
        self.load_layout.addWidget(self.load_button)
        self.load_layout.addWidget(self.load_label)
        self.load_widget.setLayout(self.load_layout)
        self.new_file_layout.addWidget(self.data_table)
        self.new_file_group.setLayout(self.new_file_layout)
        self.plot_layout.addWidget(self.old_checkbox)
        self.plot_layout.addWidget(self.new_checkbox)
        self.plot_layout.addWidget(self.plot_button)
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
        self.data_table.setRowCount(2)
        self.data_table.setColumnCount(15)
        self.data_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.data_table.horizontalHeader().hide()
        self.data_table.verticalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.data_table.setVerticalHeaderLabels(['Angle', 'Probability'])
        # self.data_table.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        '''
        How to limit the table content to be float only?
        How to set the first row not editable?
        '''

    def graph_init(self):
        # self.plot_graph.setConfigOptions(leftButtonPan=True)
        pg.setConfigOption('leftButtonPan', False)
        self.plot_graph.setBackground('w')
        self.plot_graph.setLabel('bottom', text='Angle (degree)')
        self.plot_graph.setLabel('left', text='Probability')
        self.plot_graph.setXRange(0, 15)
        self.plot_graph.setYRange(0, 1.1)
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.addLegend()

    def pushbutton_init(self):
        self.load_button.clicked.connect(self.load_file)
        self.plot_button.clicked.connect(self.show_plot)
        self.save_button.clicked.connect(self.save_file)
        self.dir_button.clicked.connect(self.find_dir)

    def load_file(self):
        try:
            f = Finddir().find_filepath()
            self.load_name = os.path.basename(f)
            self.load_label.setText('Loaded Angular File: ' + self.load_name)
            self.a = np.loadtxt(f, dtype=str)
            self.loaded_data = []
            if self.a.shape == (3, 16):
                for i in range(0, 15):
                    self.data_table.setItem(0, i, QTableWidgetItem(self.a[0, 15 - i]))
                    self.data_table.setItem(1, i, QTableWidgetItem(self.a[2, 15 - i]))
                for col in range(0, 15):
                    self.loaded_data.append(float(self.data_table.item(1, col).text()))
            else:
                QMessageBox.warning(self, 'Error', 'This file is not an angular distribution file, please check.')
        except OSError:
            pass

    def show_plot(self):
        self.plot_graph.clear()
        x_1 = np.linspace(0, 14, 15)
        y_1 = np.array(self.loaded_data)
        self.new_data_x = []
        self.new_data_y = []
        try:
            for i in range(0, 15):
                self.new_data_x.append(float(self.data_table.item(0, i).text()))
                self.new_data_y.append(float(self.data_table.item(1, i).text()))
            x_2 = np.array(self.new_data_x)
            y_2 = np.array(self.new_data_y)
        except ValueError:
            QMessageBox.critical(self, 'Error', 'Cells in the table can not be blank. ')

        if self.old_checkbox.isChecked():
            self.plot_graph.plot(x_1, y_1, pen=pg.mkPen('r'), name=self.load_name)
        if self.new_checkbox.isChecked():
            self.plot_graph.plot(x_2, y_2, pen=pg.mkPen('b'), name='New Angular Distribution')
        self.plot_graph.addLegend()

    def find_dir(self):
        d = Finddir().find_dir()
        if d == '':
            d = self.dir_line.text()
        self.dir_line.setText(d)

    def save_file(self):
        glv.set_value('new beam file directory', self.dir_line.text())
        glv.set_value('new beam file name', self.name_line.text())
        angles = ''
        cosines = ''
        probability = ''
        for i in range(14, -1, -1):
            angles += str(self.new_data_x[i]) + ' '
            cosines += str(round(math.cos((self.new_data_x[i] * 6.282 / 360)), 4)) + ' '
            probability += str(self.new_data_y[i]) + ' '

        if New_File_Check().final_check():
            path = os.path.join(self.dir_line.text(), self.name_line.text())
            with open(path, 'w') as f:
                f.write('Angle ' + angles + '\n' +
                        'cos ' + cosines + '\n' +
                        'Probability ' + probability)
            QMessageBox.information(self, 'OK', 'New angular distribution file ' +
                                    self.name_line.text() + ' saved.')


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Angular_Tab()
    w.show()
    app.exec_()
        


