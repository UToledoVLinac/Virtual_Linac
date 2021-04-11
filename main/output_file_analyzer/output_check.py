# -*- coding: utf-8 -*-
"""
Check output file and measured date before plot
"""
__author__ = 'Kanru Xie'

import globalvar as glv
from PyQt5.QtWidgets import QMessageBox
import numpy as np
import re
import os


class Output_Check(QMessageBox):
    def __init__(self):
        super().__init__()

        self.output_file = glv.get_value('Output filepath')
        self.measured_data = glv.get_value('Measured data filepath')
        self.data_name = glv.get_value('Output data name')
        self.export_path = glv.get_value('Export files path')
        self.check_dict = dict.fromkeys(['output', 'measured', 'name'], False)
        self.data_analyzed = False

    def data_name_check(self):
        if self.data_name == '':
            QMessageBox.critical(self, 'Error', 'Please define data name')
        else:
            self.check_dict['name'] = True

    def measured_check(self):
        if self.measured_data == '':
            self.check_dict['measured'] = True
        else:
            try:
                a = np.loadtxt(self.measured_data, delimiter=',')
                if len(a[0]) == 2:
                    self.check_dict['measured'] = True
                else:
                    QMessageBox.critical(self, 'Error', 'The measured data file has problem, please check.')
            except FileNotFoundError:
                QMessageBox.critical(self, 'Error', 'Can not find measured data file.')

    def pdd_check(self):
        self.data_name_check()
        self.measured_check()
        # self.check_dict['measured'] = True

        if self.output_file == '':
            QMessageBox.critical(self, 'Error', 'Please choose output file.')
        else:
            try:
                with open(self.output_file, 'r') as f:
                    lines = f.read()
                    pattern = re.compile(' cell \(3<3\[0 0 .*')
                    if not re.search(pattern, lines):
                        QMessageBox.critical(self, 'Error', 'The output file is not a PDD file, please check.')
                    else:
                        self.check_dict['output'] = True
            except FileNotFoundError:
                QMessageBox.critical(self, 'Error', 'Can not find output file.')

        if all(value for value in self.check_dict.values()):
            glv.set_value('Data analyzed', True)
            return True
        else:
            return False

    def profile_check(self):
        self.data_name_check()
        self.measured_check()

        if self.output_file == '':
            QMessageBox.critical(self, 'Error', 'Please choose output file.')
        else:
            try:
                with open(self.output_file, 'r') as f:
                    lines = f.read()
                    pattern = re.compile(' cell \(3<3\[.* .* 0')
                    if not re.search(pattern, lines):
                        QMessageBox.critical(self, 'Error', 'The output file is not a profile file, please check.')
                    else:
                        self.check_dict['output'] = True
            except FileNotFoundError:
                QMessageBox.critical(self, 'Error', 'Can not find output file.')

        if all(value for value in self.check_dict.values()):
            glv.set_value('Data analyzed', True)
            return True
        else:
            return False

    def export_check(self):
        data_analyzed = glv.get_value('Data analyzed')
        if self.export_path == '':
            QMessageBox.critical(self, 'Error', 'Please choose directory.')
        if not data_analyzed:
            QMessageBox.critical(self, 'Error', 'Please analyze and plot data first.')
        else:
            txt_name = str(self.data_name) + '.txt'
            txt_path = os.path.join(self.export_path, txt_name)
            csv_name = str(self.data_name) + '.csv'
            csv_path = os.path.join(self.export_path, csv_name)
            png_name = str(self.data_name) + '.png'
            png_path = os.path.join(self.export_path, png_name)
            if os.path.isfile(txt_path) or \
                    os.path.isfile(csv_path) or \
                    os.path.isfile(png_path):
                choice = QMessageBox.question(self, 'Question', 'Files already exist, do you want to overwrite?',
                                              QMessageBox.Yes | QMessageBox.No)
                if choice == QMessageBox.Yes:
                    return True
                elif choice == QMessageBox.No:
                    return False
            else:
                return True

