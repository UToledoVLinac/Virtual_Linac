# -*- coding: utf-8 -*-
"""
Beam commission, add and delete tab under commission beam window
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QHBoxLayout, QApplication, QMessageBox, QListWidget, QListWidgetItem)
from FindDirectory import Finddir
import sys
import globalvar as glv
from beam_commissioning.beam_check import Beam_Check
from beam_commissioning.Commissioned_Beams import beam_dict


class Commision_Tab(QWidget):
    def __init__(self):
        super().__init__()

        # Widedgets
        self.info_label = QLabel('Please choose the spectrum, angular distribution and spatial distribution files '
                                 'of your beam.')
        self.files_group = QGroupBox('Browse Files')
        self.spectrum_button = QPushButton('Choose Spectrum File')
        self.spectrum_line = QLineEdit()
        self.angular_button = QPushButton('Choose Angular File')
        self.angular_line = QLineEdit()
        self.spatial_button = QPushButton('Choose Spatial File')
        self.spatial_line = QLineEdit()
        self.notice_label = QLabel('Attention: This operation will only generate a temporary beam in the input')
        self.commission_group = QGroupBox('Change Commissioned Beams')
        self.commission_text = QListWidget()
        self.organize_widget = QWidget()
        self.load_button = QPushButton('Load Beam')
        self.load_button.setDisabled(True)
        self.add_button = QPushButton('Add Beam')
        self.delete_button = QPushButton('Delete Beam')
        self.delete_button.setDisabled(True)
        self.new_beam_label = QLabel('New Beam Name')
        self.new_beam_line = QLineEdit()

        # Layouts
        self.main_layout = QVBoxLayout()
        self.files_layout = QGridLayout()
        self.organize_layout = QGridLayout()
        self.commission_layout = QHBoxLayout()

        self.layout_init()
        self.pushbutton_init()
        self.listwidget_init()

    def layout_init(self):
        self.files_layout.addWidget(self.spectrum_button, 0, 0)
        self.files_layout.addWidget(self.spectrum_line, 0, 1)
        self.files_layout.addWidget(self.angular_button, 1, 0)
        self.files_layout.addWidget(self.angular_line, 1, 1)
        self.files_layout.addWidget(self.spatial_button, 2, 0)
        self.files_layout.addWidget(self.spatial_line, 2, 1)
        self.files_group.setLayout(self.files_layout)
        self.commission_layout.addWidget(self.commission_text)
        self.commission_layout.addWidget(self.organize_widget)
        self.commission_group.setLayout(self.commission_layout)
        self.organize_layout.addWidget(self.load_button, 0, 0)
        self.organize_layout.addWidget(self.delete_button, 0, 1)
        self.organize_layout.addWidget(self.add_button, 2, 0)
        self.organize_layout.addWidget(self.new_beam_label, 1, 0)
        self.organize_layout.addWidget(self.new_beam_line, 1, 1)
        self.organize_widget.setLayout(self.organize_layout)
        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.files_group)
        self.main_layout.addWidget(self.notice_label)
        self.main_layout.addWidget(self.commission_group)
        self.setLayout(self.main_layout)

    def pushbutton_init(self):
        self.spectrum_button.clicked.connect(self.get_spectrum)
        self.angular_button.clicked.connect(self.get_angular)
        self.spatial_button.clicked.connect(self.get_spatial)
        self.add_button.clicked.connect(self.add_new_beam)
        self.delete_button.clicked.connect(self.delete_beam)
        self.load_button.clicked.connect(self.load_beam)

    def listwidget_init(self):
        self.beam_list = beam_dict.list_beams()
        for i in range(len(self.beam_list)):
            QListWidgetItem(self.beam_list[i], self.commission_text)
        self.commission_text.itemSelectionChanged.connect(self.beam_selected)

    def beam_init(self):
        glv.set_value('spectrum file', self.spectrum_line.text())
        glv.set_value('angular file', self.angular_line.text())
        glv.set_value('spatial file', self.spatial_line.text())
        glv.set_value('new beam name', self.new_beam_line.text())

    def get_spectrum(self):
        try:
            f = Finddir().find_filepath()
            if f == '':
                pass
            else:
                self.spectrum_line.setText(str(f))
        except TypeError:
            pass

    def get_angular(self):
        try:
            f = Finddir().find_filepath()
            if f == '':
                pass
            else:
                self.angular_line.setText(str(f))
        except TypeError:
            pass

    def get_spatial(self):
        try:
            f = Finddir().find_filepath()
            if f == '':
                pass
            else:
                self.spatial_line.setText(str(f))
        except TypeError:
            pass

    def beam_selected(self):
        self.delete_button.setDisabled(False)
        self.load_button.setDisabled(False)

    def load_beam(self):
        beam_list = beam_dict.list_beams()
        selected_index = self.commission_text.currentRow()
        beam_load = beam_list[selected_index]
        beam_feature = beam_dict.get_beam(beam_load)
        self.spectrum_line.setText(beam_feature[0])
        self.angular_line.setText(beam_feature[1])
        self.spatial_line.setText(beam_feature[2])

    def delete_beam(self):
        # need to reload the beam list, otherwise the list index can be used only once
        beam_list = beam_dict.list_beams()
        selected_index = self.commission_text.currentRow()
        beam_delete = beam_list[selected_index]
        beam_dict.delete_beam(beam_delete)
        beam_dict.update_beam()
        beam_dict.update_list()
        self.commission_text.takeItem(self.commission_text.currentRow())

    def add_new_beam(self):
        self.beam_init()
        if Beam_Check().add_new_check():
            name = glv.get_value('new beam name')
            spectrum = glv.get_value('spectrum file')
            angular = glv.get_value('angular file')
            spatial = glv.get_value('spatial file')
            beam_features = [spectrum, angular, spatial]
            beam_dict.add_beam(name, beam_features)
            self.commission_text.addItem(name)
            beam_dict.update_beam()
            beam_dict.update_list()
        else:
            pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Commision_Tab()
    w.show()
    app.exec_()


