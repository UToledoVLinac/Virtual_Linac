# -*- coding: utf-8 -*-
"""
Input file creator window
"""
__author__ = 'Kanru Xie'

import os
import sys
from random import randint
from PyQt5.QtGui import QIntValidator, QDoubleValidator
from PyQt5.QtWidgets import (QCheckBox, QRadioButton, QTextEdit, QLabel, QLineEdit, QPushButton, QVBoxLayout,
                             QHBoxLayout, QGroupBox, QGridLayout, QWidget, QApplication, QComboBox)
import globalvar as glv
from FindDirectory import Finddir
from beam_commissioning.Commissioned_Beams import beam_dict
from input_file_creator.change_beam_window import Beam
from input_file_creator.inputfile_check import ContentCheck
from input_file_creator.print_input import file_print


class Inputwindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Input File Creator')
        self.directory_label = QLabel('Directory:')
        self.directory_line = QLineEdit()
        self.browse_button = QPushButton('Browse')
        self.input_label = QLabel('Input file name: ')
        self.input_line = QLineEdit()
        self.output_label = QLabel('Output file name: ')
        self.output_line = QLineEdit()
        self.x_profile_check = QRadioButton('x- profile')
        self.y_profile_check = QRadioButton('y- profile')
        self.xy_profiles_check = QRadioButton('x- and y- profiles')
        self.dose_map_check = QRadioButton('xy 2D dose map')
        self.z_PDD_check = QRadioButton('z- PDD')
        self.detector_check = QRadioButton('W-1 detector')
        self.lattice_size_label = QLabel('Lattice size (cm):')
        self.lattice_size_line = QLineEdit()
        self.depth_label = QLabel('Depth (cm):')
        self.depth_line = QLineEdit()
        self.x_offaxis_label = QLabel('x- off axis (cm)')
        self.x_offaxis_line = QLineEdit()
        self.y_offaxis_label = QLabel('y- off axis (cm)')
        self.y_offaxis_line = QLineEdit()
        self.x1_label = QLabel('X1:')
        self.x1_line = QLineEdit()
        self.x2_label = QLabel('X2:')
        self.x2_line = QLineEdit()
        self.y1_label = QLabel('Y1:')
        self.y1_line = QLineEdit()
        self.y2_label = QLabel('Y2:')
        self.y2_line = QLineEdit()
        self.mlc_checkbox_1 = QRadioButton('No MLC')
        self.mlc_checkbox_2 = QRadioButton('Standard MLC')
        self.mlc_checkbox_3 = QRadioButton('Simplified MLC')
        self.mlc_x_label = QLabel('MLC x opening:')
        self.mlc_x_line = QLineEdit()
        self.mlc_y_label = QLabel('MLC y opening:')
        self.mlc_y_line = QLineEdit()
        self.mlc_customize_button = QPushButton('Customize field')
        self.machine_label = QLabel('Machine')
        self.machine_combo = QComboBox()
        self.beam_lable = QLabel('Beam')
        self.beam_combo = QComboBox()
        self.beam_button = QPushButton('Choose File')
        self.tally_label = QLabel('Tally:')
        self.tally_combo = QComboBox()
        self.nps_label = QLabel('nps:')
        self.nps_line = QLineEdit()
        self.randseed_label = QLabel('Random Seed:')
        self.randseed_line = QLineEdit()
        self.randseed_button = QPushButton('Random')
        self.cutoff_p_label = QLabel('cutoff:p (MeV)')
        self.cutoff_p_line = QLineEdit()
        self.cutoff_e_label = QLabel('cutoff:e (MeV)')
        self.cutoff_e_line = QLineEdit()
        self.comment_box = QTextEdit()
        self.print_button = QPushButton('Print', self)
        self.check_length_button = QPushButton('Check Lines Length', self)
        self.beam_window = Beam()

        # default values as validators
        self.directory_line.setText(os.getcwd())
        self.lattice_size_line.setValidator(QDoubleValidator(self))
        self.lattice_size_line.setText('0.2')
        self.depth_line.setValidator(QDoubleValidator(self))
        self.depth_line.setText('10')
        self.x_offaxis_line.setValidator((QDoubleValidator(self)))
        self.x_offaxis_line.setText('0')
        self.y_offaxis_line.setValidator(QDoubleValidator(self))
        self.y_offaxis_line.setText('0')
        self.x1_line.setValidator(QDoubleValidator(self))
        self.x2_line.setValidator(QDoubleValidator(self))
        self.y1_line.setValidator(QDoubleValidator(self))
        self.y2_line.setValidator(QDoubleValidator(self))
        self.mlc_x_line.setText('0')
        self.mlc_x_line.setValidator(QDoubleValidator(self))
        self.mlc_y_line.setText('0')
        self.mlc_y_line.setValidator(QDoubleValidator(self))
        self.nps_line.setValidator(QIntValidator(self))
        self.randseed_line.setValidator(QIntValidator(self))
        self.randseed_line.setText(str(randint(10 ** 12, 10 ** 13) * 2 + 1))
        self.cutoff_p_line.setValidator(QDoubleValidator(self))
        self.cutoff_p_line.setText('0.01')
        self.cutoff_e_line.setValidator(QDoubleValidator(self))
        self.cutoff_e_line.setText('0.20')
        self.x1_line.setText('5')
        self.x2_line.setText('-5')
        self.y1_line.setText('5')
        self.y2_line.setText('-5')
        self.nps_line.setText('13000000000')
        self.comments_text = ''

        # layouts
        self.main_layout = QVBoxLayout()
        self.file_group = QGroupBox('File information')
        self.file_layout = QGridLayout()
        self.objective_group = QGroupBox('Objective')
        self.objective_layout = QGridLayout()
        self.jaws_group = QGroupBox('Jaws positions (cm)')
        self.jaws_layout = QGridLayout()
        self.mlc_group = QGroupBox('MLC opening field (cm), only symmetrical in current version.')
        self.mlc_layout = QGridLayout()
        self.simulation_group = QGroupBox('Simulation information')
        self.simulation_layout = QGridLayout()
        self.center_widget = QWidget()
        self.center_layout = QHBoxLayout()
        self.left_widget = QWidget()
        self.left_layout = QVBoxLayout()
        self.right_widget = QWidget()
        self.right_layout = QVBoxLayout()
        self.comments_group = QGroupBox('Comments (Please add \'c \' at the beginning of each line)')
        self.comments_layout = QVBoxLayout()

        self.cc = ContentCheck()

        self.layout_init()
        self.pushbutton_init()
        self.combobox_init()

    def layout_init(self):
        self.file_layout.addWidget(self.directory_label, 0, 0)
        self.file_layout.addWidget(self.directory_line, 0, 1)
        self.file_layout.addWidget(self.browse_button, 0, 2)
        self.file_layout.addWidget(self.input_label, 1, 0)
        self.file_layout.addWidget(self.input_line, 1, 1)
        self.file_layout.addWidget(self.output_label, 2, 0)
        self.file_layout.addWidget(self.output_line, 2, 1)
        self.file_group.setLayout(self.file_layout)
        self.objective_layout.addWidget(self.z_PDD_check, 0, 0)
        self.objective_layout.addWidget(self.xy_profiles_check, 1, 0)
        self.objective_layout.addWidget(self.x_profile_check, 2, 0)
        self.objective_layout.addWidget(self.y_profile_check, 3, 0)
        self.objective_layout.addWidget(self.detector_check, 4, 0)
        self.objective_layout.addWidget(self.dose_map_check, 5, 0)
        self.objective_layout.addWidget(self.lattice_size_label, 0, 1)
        self.objective_layout.addWidget(self.lattice_size_line, 0, 2)
        self.objective_layout.addWidget(self.depth_label, 1, 1)
        self.objective_layout.addWidget(self.depth_line, 1, 2)
        self.objective_layout.addWidget(self.x_offaxis_label, 2, 1)
        self.objective_layout.addWidget(self.x_offaxis_line, 2, 2)
        self.objective_layout.addWidget(self.y_offaxis_label, 3, 1)
        self.objective_layout.addWidget(self.y_offaxis_line, 3, 2)
        self.objective_group.setLayout(self.objective_layout)
        self.jaws_layout.addWidget(self.x1_label, 0, 0)
        self.jaws_layout.addWidget(self.x1_line, 0, 1)
        self.jaws_layout.addWidget(self.x2_label, 0, 2)
        self.jaws_layout.addWidget(self.x2_line, 0, 3)
        self.jaws_layout.addWidget(self.y1_label, 1, 0)
        self.jaws_layout.addWidget(self.y1_line, 1, 1)
        self.jaws_layout.addWidget(self.y2_label, 1, 2)
        self.jaws_layout.addWidget(self.y2_line, 1, 3)
        self.jaws_group.setLayout(self.jaws_layout)
        self.mlc_layout.addWidget(self.mlc_checkbox_1, 0, 0)
        self.mlc_layout.addWidget(self.mlc_checkbox_2, 0, 1)
        self.mlc_layout.addWidget(self.mlc_checkbox_3, 0, 2)
        self.mlc_layout.addWidget(self.mlc_x_label, 1, 0)
        self.mlc_layout.addWidget(self.mlc_x_line, 1, 1)
        self.mlc_layout.addWidget(self.mlc_y_label, 2, 0)
        self.mlc_layout.addWidget(self.mlc_y_line, 2, 1)
        self.mlc_layout.addWidget(self.mlc_customize_button, 3, 0)
        self.mlc_group.setLayout(self.mlc_layout)
        self.simulation_layout.addWidget(self.machine_label, 0, 0)
        self.simulation_layout.addWidget(self.machine_combo, 0, 1)
        self.simulation_layout.addWidget(self.beam_lable, 1, 0)
        self.simulation_layout.addWidget(self.beam_combo, 1, 1)
        self.simulation_layout.addWidget(self.beam_button, 1, 2)
        self.simulation_layout.addWidget(self.tally_label, 2, 0)
        self.simulation_layout.addWidget(self.tally_combo, 2, 1)
        self.simulation_layout.addWidget(self.nps_label, 3, 0)
        self.simulation_layout.addWidget(self.nps_line, 3, 1)
        self.simulation_layout.addWidget(self.randseed_label, 4, 0)
        self.simulation_layout.addWidget(self.randseed_line, 4, 1)
        self.simulation_layout.addWidget(self.randseed_button, 4, 2)
        self.simulation_layout.addWidget(self.cutoff_p_label, 5, 0)
        self.simulation_layout.addWidget(self.cutoff_p_line, 5, 1)
        self.simulation_layout.addWidget(self.cutoff_e_label, 6, 0)
        self.simulation_layout.addWidget(self.cutoff_e_line, 6, 1)
        self.simulation_group.setLayout(self.simulation_layout)
        self.center_layout.addWidget(self.left_widget)
        self.center_layout.addWidget(self.right_widget)
        self.center_widget.setLayout(self.center_layout)
        self.left_layout.addWidget(self.file_group)
        self.left_layout.addWidget(self.simulation_group)
        self.left_widget.setLayout(self.left_layout)
        self.right_layout.addWidget(self.objective_group)
        self.right_layout.addWidget(self.jaws_group)
        self.right_layout.addWidget(self.mlc_group)
        self.right_widget.setLayout(self.right_layout)
        self.comments_layout.addWidget(self.comment_box)
        self.comments_group.setLayout(self.comments_layout)
        self.main_layout.addWidget(self.center_widget)
        self.main_layout.addStretch(1)
        self.main_layout.addWidget(self.comments_group)
        self.main_layout.addWidget(self.print_button)
        self.main_layout.addWidget(self.check_length_button)
        self.setLayout(self.main_layout)

    def pushbutton_init(self):
        self.browse_button.clicked.connect(self.findd)
        self.mlc_checkbox_1.toggled.connect(self.mlc_x_line.setDisabled)
        self.mlc_checkbox_1.toggled.connect(self.mlc_y_line.setDisabled)
        self.mlc_checkbox_1.toggled.connect(self.mlc_x_label.setDisabled)
        self.mlc_checkbox_1.toggled.connect(self.mlc_y_label.setDisabled)
        self.mlc_checkbox_1.toggled.connect(self.mlc_state)
        self.mlc_checkbox_2.toggled.connect(self.mlc_state)
        self.mlc_checkbox_3.setDisabled(True)
        self.mlc_checkbox_1.setChecked(True)
        self.mlc_customize_button.setDisabled(True)
        self.x_profile_check.toggled.connect(self.objective_choice)
        self.x_profile_check.toggled.connect(self.x_offaxis_label.setDisabled)
        self.x_profile_check.toggled.connect(self.x_offaxis_line.setDisabled)
        self.y_profile_check.toggled.connect(self.objective_choice)
        self.y_profile_check.toggled.connect(self.y_offaxis_label.setDisabled)
        self.y_profile_check.toggled.connect(self.y_offaxis_line.setDisabled)
        self.z_PDD_check.toggled.connect(self.depth_line.setDisabled)
        self.z_PDD_check.toggled.connect(self.depth_label.setDisabled)
        self.z_PDD_check.toggled.connect(self.objective_choice)
        self.detector_check.toggled.connect(self.lattice_size_label.setDisabled)
        self.detector_check.toggled.connect(self.lattice_size_line.setDisabled)
        self.detector_check.toggled.connect(self.objective_choice)
        self.dose_map_check.setDisabled(True)
        self.randseed_button.clicked.connect(self.generate_randseed)
        self.print_button.clicked.connect(self.content_check)
        self.z_PDD_check.setChecked(True)  # This setChecked statement has to be here.
        self.beam_button.setDisabled(False)
        self.beam_button.clicked.connect(self.change_beam)
        self.check_length_button.clicked.connect(self.input_length_check)

    def beam_combobox_init(self):
        self.beam_combo.clear()
        beam_list = beam_dict.list_beams()
        if len(beam_list) == 0:
            self.beam_combo.addItem('No commissioned beam')
        else:
            for i in range(len(beam_list)):
                self.beam_combo.addItem(beam_list[i])
                glv.set_value('beam', beam_list[0])
        self.beam_combo.addItem('Other (please choose files)')

    def combobox_init(self):
        # machine combo box
        self.machine_combo.addItem('Edge(HDMLC-120)')
        self.machine_combo.addItem('TrueBeam(MLC-120)-NOT COMMISSIONED')

        # tally combo box
        self.tally_combo.addItem('F8*')

    def beam_init(self):
        try:
            beam = glv.get_value('beam')
            beam_info = beam_dict.get_beam(beam)
            glv.set_value('spectrum file', beam_info[0])
            glv.set_value('angular file', beam_info[1])
            glv.set_value('spatial file', beam_info[2])
        except KeyError:
            pass

    def variables_init(self):
        glv.set_value('directory', self.directory_line.text())
        glv.set_value('input file name', self.input_line.text())
        glv.set_value('output file name', self.output_line.text())
        glv.set_value('e cutoff', self.cutoff_e_line.text())
        glv.set_value('p cutoff', self.cutoff_p_line.text())
        glv.set_value('nps', self.nps_line.text())
        glv.set_value('randomseed', self.randseed_line.text())
        glv.set_value('lattice size', self.lattice_size_line.text())
        glv.set_value('depth', self.depth_line.text())
        glv.set_value('x1 Jaw', self.x1_line.text())
        glv.set_value('x2 Jaw', self.x2_line.text())
        glv.set_value('y1 Jaw', self.y1_line.text())
        glv.set_value('y2 Jaw', self.y2_line.text())
        glv.set_value('mlc x', self.mlc_x_line.text())
        glv.set_value('mlc y', self.mlc_y_line.text())
        glv.set_value('x offaxis', self.x_offaxis_line.text())
        glv.set_value('y offaxis', self.y_offaxis_line.text())
        glv.set_value('mlc state', '')
        glv.set_value('objective', '')
        if self.comment_box.toPlainText() != '':
            self.comments_text = str('\n' + self.comment_box.toPlainText() + '\n')
        else:
            self.comments_text = '\n'
        glv.set_value('comments', self.comments_text)

    def findd(self):
        d = Finddir().find_dir()
        if d == '':
            pass
        else:
            self.directory_line.setText(d)

    def beam_choice(self):
        beam = self.beam_combo.currentText()
        if beam == 'Other (please choose files)':
            self.beam_button.setDisabled(False)
        else:
            glv.set_value('beam', beam)
            self.beam_init()

    def mlc_state(self):
        if self.mlc_checkbox_1.isChecked():
            glv.set_value('mlc state', 'no mlc')
        elif self.mlc_checkbox_3.isChecked():
            glv.set_value('mlc state', 'simplified mlc')
        elif self.mlc_checkbox_2.isChecked():
            glv.set_value('mlc state', 'standard mlc')

    def objective_choice(self):
        if self.x_profile_check.isChecked():
            glv.set_value('objective', 'x')
        elif self.y_profile_check.isChecked():
            glv.set_value('objective', 'y')
        elif self.xy_profiles_check.isChecked():
            glv.set_value('objective', 'xy')
        elif self.dose_map_check.isChecked():
            glv.set_value('objective', 'dose map')
        elif self.z_PDD_check.isChecked():
            glv.set_value('objective', 'z')
        elif self.detector_check.isChecked():
            glv.set_value('objective', 'd')

    def change_beam(self):
        self.beam_window.show()

    def generate_randseed(self):
        random_number = str(randint(10 ** 12, 10 ** 13) * 2 + 1)
        self.randseed_line.setText(random_number)

    def content_check(self):
        self.variables_init()
        self.mlc_state()
        self.objective_choice()
        self.beam_choice()
        if ContentCheck().final_check():
            file_print()
        else:
            pass
        # glv.clear_value()

    def input_length_check(self):
        self.variables_init()
        ContentCheck().length_check()


if __name__ == '__main__':
    glv._init()
    app = QApplication(sys.argv)
    w = Inputwindow()
    w.show()
    app.exec_()
