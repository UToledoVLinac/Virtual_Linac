# -*- coding: utf-8 -*-
"""
Check beam information
"""
__author__ = 'Kanru Xie'

import globalvar as glv
from PyQt5.QtWidgets import QMessageBox
from beam_commissioning.Commissioned_Beams import beam_dict
import os
import numpy as np


class Beam_Check(QMessageBox):
    def __init__(self):
        super().__init__()

        self.check_dict = dict.fromkeys(['spectrum', 'angular', 'spatial', 'beam name'], False)
        self.spectrum = glv.get_value('spectrum file')
        self.angular = glv.get_value('angular file')
        self.spatial = glv.get_value('spatial file')
        self.new_beam_name = glv.get_value('new beam name')
        self.beam_list = beam_dict.list_beams()

    def beam_name_check(self):
        if self.new_beam_name == '':
            QMessageBox.critical(self, 'Error', 'Please enter new beam name')
        else:
            if len(self.beam_list) == 0:
                self.check_dict['beam name'] = True
            else:
                for i in range(len(self.beam_list)):
                    if self.new_beam_name == self.beam_list[i]:
                        QMessageBox.critical(self, 'Error', 'This beam name already exists. Please try another.')
                        self.check_dict['beam name'] = False
                    else:
                        self.check_dict['beam name'] = True

    def spectrum_check(self):
        if self.spectrum == '':
            QMessageBox.critical(self, 'Error', 'Please choose spectrum file.')
        else:
            if not os.path.isfile(self.spectrum):
                QMessageBox.critical(self, 'Error', 'Spectrum file does not exist, please check filepath.')
            else:
                file = np.loadtxt(self.spectrum, dtype=str)
                if file.shape != (0, 0):  # file.shape == (15, 20):
                    self.check_dict['spectrum'] = True
                else:
                    QMessageBox.warning(self, 'warning', 'The spectrum file looks not right, please check.')

    def angular_check(self):
        if self.angular == '':
            QMessageBox.critical(self, 'Error', 'Please choose angular file.')
        else:
            if not os.path.isfile(self.angular):
                QMessageBox.critical(self, 'Error', 'Angular file does not exist, please check filepath.')
            else:
                file = np.loadtxt(self.angular, dtype=str)
                if file.shape != (0, 0):  # file.shape == (16, 2):
                    self.check_dict['angular'] = True
                else:
                    QMessageBox.warning(self, 'warning', 'The angular file looks not right, please check.')

    def spatial_check(self):
        if self.spatial == '':
            QMessageBox.critical(self, 'Error', 'Please choose spatial file.')
        else:
            if not os.path.isfile(self.angular):
                QMessageBox.critical(self, 'Error', 'Spatial file does not exist, please check filepath.')
            else:
                file = np.loadtxt(self.spatial, dtype=str)
                if file.shape != (0, 0):  # file.shape == (16, 2):
                    self.check_dict['spatial'] = True
                else:
                    QMessageBox.warning(self, 'warning', 'The spatial file looks not right, please check.')

    def add_new_check(self):
        self.beam_name_check()
        self.spectrum_check()
        self.angular_check()
        self.spatial_check()
        if all(value for value in self.check_dict.values()):
            QMessageBox.information(self, 'Good Job,', self.new_beam_name + ' added.')
            return True
        else:
            # QMessageBox.information(self, 'something wrong', self.new_beam_name + ' not printed.')
            return False

    def change_beam_check(self):
        self.check_dict['beam name'] = True
        self.spectrum_check()
        self.angular_check()
        self.spatial_check()
        if all(value for value in self.check_dict.values()):
            # QMessageBox.information(self, 'Good Job,', self.new_beam_name + ' added.')
            return True
        else:
            return False
            # QMessageBox.information(self, 'something wrong', self.input_name + ' not printed.')

