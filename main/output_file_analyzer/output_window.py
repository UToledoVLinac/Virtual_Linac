# -*- coding: utf-8 -*-
"""
The Output analyzer window
"""
__author__ = 'Kanru Xie'

from PyQt5.QtWidgets import (QCheckBox, QRadioButton, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QGridLayout, QWidget, QApplication)
import os
import sys
from output_file_analyzer import read_output_file, diff_calculate
from FindDirectory import Finddir
import pyqtgraph as pg
import pyqtgraph.exporters
import globalvar as glv
from output_file_analyzer.output_check import Output_Check
import numpy as np


class Output_Window(QWidget):
    def __init__(self):
        super().__init__()

        self.info_label = QLabel('Information')
        self.upper_widget = QWidget()
        self.file_group = QGroupBox('File information')
        self.file_1_widget = QWidget()
        self.file_2_widget = QWidget()
        self.output_file_label = QLabel('Choose Output File:')
        self.output_file_line = QLineEdit()
        self.browse_button_1 = QPushButton('Browse')
        self.measured_label = QLabel('Choose Measured Data:')
        self.measured_line = QLineEdit()
        self.browse_button_2 = QPushButton('Browse')
        self.data_name_label = QLabel('Data Name:')
        self.data_name_line = QLineEdit()
        self.data_type_label = QLabel('Data Type:')
        self.data_pdd_button = QRadioButton('PDD')
        self.data_xprofile_button = QRadioButton('X profile')
        self.data_yprofile_button = QRadioButton('Y profile')
        self.plot_group = QGroupBox('Plot graph')
        self.output_checkbox = QCheckBox('Plot output data')
        self.measured_checkbox = QCheckBox('Plot measured data')
        self.diff_checkbox = QCheckBox('Plot %difference')
        self.plot_button = QPushButton('Plot')
        self.plot_clear_button = QPushButton('Clear Graph')
        self.plot_graph = pg.PlotWidget()
        self.save_group = QGroupBox('Save files')
        self.save_txt_checkbox = QCheckBox('Save original data as .txt file')
        self.save_csv_checkbox = QCheckBox('Save analyzed data as .csv file')
        self.save_img_checkbox = QCheckBox('Save graph as image file')
        self.save_dir_widget = QWidget()
        self.save_dir_label = QLabel('Directory')
        self.save_dir_line = QLineEdit()
        self.browse_button_3 = QPushButton('Browse')
        self.save_button = QPushButton('Save')

        self.main_layout = QVBoxLayout()
        self.upper_layout = QHBoxLayout()
        self.file_layout = QVBoxLayout()
        self.file_1_layout = QGridLayout()
        self.file_2_layout = QHBoxLayout()
        self.plot_layout = QVBoxLayout()
        self.save_layout = QVBoxLayout()
        self.save_dir_layout = QGridLayout()

        self.output_checkbox.setChecked(True)
        self.measured_checkbox.setChecked(True)
        self.diff_checkbox.setChecked(True)
        self.save_txt_checkbox.setChecked(True)
        self.save_csv_checkbox.setChecked(True)
        self.save_img_checkbox.setChecked(True)
        self.data_pdd_button.setChecked(True)
        self.save_dir_line.setText(os.getcwd())

        self.layout_init()
        self.graph_init()
        self.pushbutton_init()

    def layout_init(self):
        self.upper_layout.addWidget(self.file_group)
        # self.upper_layout.addWidget(self.plot_group)
        self.upper_widget.setLayout(self.upper_layout)
        self.file_1_layout.addWidget(self.output_file_label, 0, 0)
        self.file_1_layout.addWidget(self.output_file_line, 0, 1)
        self.file_1_layout.addWidget(self.browse_button_1, 0, 2)
        self.file_1_layout.addWidget(self.measured_label, 1, 0)
        self.file_1_layout.addWidget(self.measured_line, 1, 1)
        self.file_1_layout.addWidget(self.browse_button_2, 1, 2)
        self.file_1_layout.addWidget(self.data_name_label, 2, 0)
        self.file_1_layout.addWidget(self.data_name_line, 2, 1)
        self.file_1_widget.setLayout(self.file_1_layout)
        self.file_2_layout.addWidget(self.data_type_label)
        self.file_2_layout.addWidget(self.data_pdd_button)
        self.file_2_layout.addWidget(self.data_xprofile_button)
        self.file_2_layout.addWidget(self.data_yprofile_button)
        self.file_2_layout.addWidget(self.plot_button)
        self.file_2_layout.addWidget(self.plot_clear_button)
        self.file_2_widget.setLayout(self.file_2_layout)
        self.file_layout.addWidget(self.file_1_widget)
        self.file_layout.addWidget(self.file_2_widget)
        self.file_group.setLayout(self.file_layout)
        #self.plot_layout.addWidget(self.output_checkbox)
        #self.plot_layout.addWidget(self.measured_checkbox)
        # self.plot_layout.addWidget(self.diff_checkbox)
        #self.plot_layout.addWidget(self.plot_button)
        #self.plot_layout.addWidget(self.plot_clear_button)
        self.plot_group.setLayout(self.plot_layout)
        self.save_dir_layout.addWidget(self.save_dir_label, 0, 0)
        self.save_dir_layout.addWidget(self.save_dir_line, 0, 1)
        self.save_dir_layout.addWidget(self.browse_button_3, 0, 2)
        self.save_dir_layout.addWidget(self.save_button, 1, 0)
        self.save_dir_widget.setLayout(self.save_dir_layout)
        self.save_layout.addWidget(self.save_txt_checkbox)
        self.save_layout.addWidget(self.save_csv_checkbox)
        self.save_layout.addWidget(self.save_img_checkbox)
        self.save_layout.addWidget(self.save_dir_widget)
        self.save_group.setLayout(self.save_layout)

        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.upper_widget)
        self.main_layout.addWidget(self.plot_graph)
        self.main_layout.addWidget(self.save_group)
        self.setLayout(self.main_layout)

    def graph_init(self):
        self.plot_graph.setBackground('w')
        self.plot_graph.showGrid(x=True, y=True)
        self.plot_graph.setYRange(0, 1.1)
        self.plot_graph.addLegend()
        pg.setConfigOptions(antialias=True)

    def pushbutton_init(self):
        self.browse_button_1.clicked.connect(self.choose_output_file)
        self.browse_button_2.clicked.connect(self.choose_measured_file)
        self.browse_button_3.clicked.connect(self.choose_save_dir)
        self.plot_button.clicked.connect(self.show_plot)
        self.plot_clear_button.clicked.connect(lambda: self.plot_graph.clear())
        self.save_button.clicked.connect(self.save_files)

    def choose_output_file(self):
        filepath = Finddir().find_filepath()
        if filepath == '':
            pass
        else:
            self.output_file_line.setText(filepath)

    def choose_measured_file(self):
        filepath = Finddir().find_filepath()
        if filepath == '':
            pass
        else:
            self.measured_line.setText(filepath)

    def show_plot(self):
        glv.set_value('Output filepath', self.output_file_line.text())
        glv.set_value('Output data name', self.data_name_line.text())
        glv.set_value('Measured data filepath', self.measured_line.text())

        if self.data_pdd_button.isChecked():
            if Output_Check().pdd_check():
                read_output_file.read_pdd()
                self.x_output = glv.get_value('Output X')
                self.y_output = glv.get_value('Output normalized Y')
                self.plot_graph.plot(self.x_output, self.y_output, pen=pg.mkPen('r'), name=self.data_name_line.text())
                self.plot_graph.setLabel('bottom', text='Depth(mm)')
                self.plot_graph.setLabel('left', text='Percent Dose')
                if self.measured_line.text() != '':
                    diff_calculate.pdd_calc()
                    self.x_measured = glv.get_value('Measured X')
                    self.y_measured = glv.get_value('Measured Y')
                    self.y_diff = glv.get_value('Y diff')
                    self.plot_graph.plot(self.x_measured, self.y_measured, pen=pg.mkPen('b'), name='measured')
                    self.plot_graph.plot(self.x_measured, self.y_diff, pen=pg.mkPen('g'), name='%diff')

        if self.data_xprofile_button.isChecked():
            if Output_Check().profile_check():
                read_output_file.read_xprofile()
                self.x_output = glv.get_value('Output X')
                self.y_output = glv.get_value('Output normalized Y')
                self.plot_graph.plot(self.x_output, self.y_output, pen=pg.mkPen('r'), name=self.data_name_line.text())
                self.plot_graph.setLabel('bottom', text='X distance (mm)')
                self.plot_graph.setLabel('left', text='Percent Dose')
                if self.measured_line.text() != '':
                    diff_calculate.profile_calc()
                    self.x_measured = glv.get_value('Measured X')
                    self.y_measured = glv.get_value('Measured Y')
                    self.y_diff = glv.get_value('Y diff')
                    self.plot_graph.plot(self.x_measured, self.y_measured, pen=pg.mkPen('b'), name='measured')
                    self.plot_graph.plot(self.x_measured, self.y_diff, pen=pg.mkPen('g'), name='%diff')

        if self.data_yprofile_button.isChecked():
            if Output_Check().profile_check():
                read_output_file.read_yprofile()
                self.x_output = glv.get_value('Output X')
                self.y_output = glv.get_value('Output normalized Y')
                self.plot_graph.plot(self.x_output, self.y_output, pen=pg.mkPen('r'), name=self.data_name_line.text())
                self.plot_graph.setLabel('bottom', text='Y distance (mm)')
                self.plot_graph.setLabel('left', text='Percent Dose')
                if self.measured_line.text() != '':
                    diff_calculate.profile_calc()
                    self.x_measured = glv.get_value('Measured X')
                    self.y_measured = glv.get_value('Measured Y')
                    self.y_diff = glv.get_value('Y diff')
                    self.plot_graph.plot(self.x_measured, self.y_measured, pen=pg.mkPen('b'), name='measured')
                    self.plot_graph.plot(self.x_measured, self.y_diff, pen=pg.mkPen('g'), name='%diff')

    def choose_save_dir(self):
        filepath = Finddir().find_dir()
        if filepath == '':
            pass
        else:
            self.save_dir_line.setText(filepath)

    def save_files(self):
        glv.set_value('Export files path', self.save_dir_line.text())
        if Output_Check().export_check():
            if self.save_txt_checkbox.isChecked():
                data = glv.get_value('Output Y')
                txt_name = self.data_name_line.text() + '_original.txt'
                txt_path = os.path.join(self.save_dir_line.text(), txt_name)
                np.savetxt(txt_path, data, fmt='%.5e')
            if self.save_csv_checkbox.isChecked():
                csv_name = self.data_name_line.text() + '_analyzed.csv'
                csv_path = os.path.join(self.save_dir_line.text(), csv_name)
                exporter = pg.exporters.CSVExporter(self.plot_graph.plotItem)
                exporter.parameters()['columnMode'] = '(x,y,y,y) for all plots'
                exporter.export(csv_path)
            if self.save_img_checkbox.isChecked():
                png_name = self.data_name_line.text() + '.png'
                png_path = os.path.join(self.save_dir_line.text(), png_name)
                exporter = pg.exporters.ImageExporter(self.plot_graph.plotItem)
                exporter.export(png_path)


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Output_Window()
    w.show()
    app.exec_()
