# -*- coding: utf-8 -*-
"""
The dialog window to change beam
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QWidget, QLabel, QVBoxLayout, QPushButton, QLineEdit, QGridLayout,
                             QGroupBox, QHBoxLayout, QApplication, QMessageBox)
# from PyQt5.QtCore import QStringListModel
from FindDirectory import Finddir
import sys
import globalvar as glv
from beam_commissioning.beam_check import Beam_Check
from beam_commissioning.Commissioned_Beams import beam_dict


class Beam(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Choose Beam Files')
        self.resize(650, 380)

        # Widedgets
        self.info_label = QLabel('Please choose the spectrum, angular distribution and spatial distribution files '
                                 'of your beam.')
        self.spectrum_button = QPushButton('Choose Spectrum File')
        self.spectrum_line = QLineEdit()
        self.angular_button = QPushButton('Choose Angular File')
        self.angular_line = QLineEdit()
        self.spatial_button = QPushButton('Choose Spatial File')
        self.spatial_line = QLineEdit()
        self.notice_label = QLabel('Attention: This operation will only generate a temporary beam in the input '
                                   'file.' + '\n' +
                                   '                Use Beam Commissioning from Main Window to add new beams.')
        # self.commission_label = QLabel('Commissioned Beams List')
        # self.commission_text = QListWidget()
        # self.commission_widget = QWidget()
        # self.add_button = QPushButton('Add Beam')
        # self.delete_button = QPushButton('Delete Beam')
        # self.delete_button.setDisabled(True)
        # self.new_beam_label = QLabel('New Beam Name')
        # self.new_beam_line = QLineEdit()
        self.confirm_button = QPushButton('Confirm')
        self.cancel_button = QPushButton('Cancel')
        # self.center_widget = QWidget()
        self.bottom_widget = QWidget()

        # Layouts
        self.main_layout = QVBoxLayout()
        self.left_group = QGroupBox('Find Files')
        self.left_layout = QGridLayout()
        # self.right_group = QGroupBox('Change Commissioned Beams')
        # self.right_layout = QHBoxLayout()
        # self.commission_layout = QGridLayout()
        self.bottom_layout = QHBoxLayout()

        self.layout_init()
        self.pushbutton_init()
        # self.listwidget_init()

    #def listwidget_init(self):
        # self.beam_list = beam_dict.list_beams()
        # for i in range(len(self.beam_list)):
        #    QListWidgetItem(self.beam_list[i], self.commission_text)
        # self.commission_text.itemSelectionChanged.connect(self.beam_selected)

    def layout_init(self):
        self.left_layout.addWidget(self.spectrum_button, 0, 0)
        self.left_layout.addWidget(self.spectrum_line, 0, 1)
        self.left_layout.addWidget(self.angular_button, 1, 0)
        self.left_layout.addWidget(self.angular_line, 1, 1)
        self.left_layout.addWidget(self.spatial_button, 2, 0)
        self.left_layout.addWidget(self.spatial_line, 2, 1)
        self.left_group.setLayout(self.left_layout)
        ##self.commission_layout.addWidget(self.add_button, 0, 0)
        #self.commission_layout.addWidget(self.delete_button, 0, 1)
        #self.commission_layout.addWidget(self.new_beam_label, 1, 0)
        #self.commission_layout.addWidget(self.new_beam_line, 1, 1)
        #self.commission_widget.setLayout(self.commission_layout)
        # self.right_layout.addWidget(self.commission_label)
        #self.right_layout.addWidget(self.commission_text)
        #self.right_layout.addWidget(self.commission_widget)
        #self.right_group.setLayout(self.right_layout)
        # self.center_layout.addWidget(self.left_group)
        # self.center_layout.addWidget(self.right_group)
        # self.center_widget.setLayout(self.center_layout)
        self.bottom_layout.addWidget(self.confirm_button)
        self.bottom_layout.addWidget(self.cancel_button)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.main_layout.addWidget(self.info_label)
        self.main_layout.addWidget(self.left_group)
        self.main_layout.addWidget(self.notice_label)
        #self.main_layout.addWidget(self.right_group)
        # self.main_layout.addWidget(self.center_widget)
        self.main_layout.addWidget(self.bottom_widget)
        self.setLayout(self.main_layout)

    def beam_init(self):
        glv.set_value('spectrum file', self.spectrum_line.text())
        glv.set_value('angular file', self.angular_line.text())
        glv.set_value('spatial file', self.spatial_line.text())
        # glv.set_value('new beam name', self.new_beam_line.text())

    def pushbutton_init(self):
        self.spectrum_button.clicked.connect(self.get_spectrum)
        self.angular_button.clicked.connect(self.get_angular)
        self.spatial_button.clicked.connect(self.get_spatial)
        #self.add_button.clicked.connect(self.add_new_beam)
        self.confirm_button.clicked.connect(self.beam_confirmed)
        #self.delete_button.clicked.connect(self.delete_beam)
        self.cancel_button.clicked.connect(self.beam_canceled)

    def get_spectrum(self):
        try:
            f = Finddir().find_filepath()
            self.spectrum_line.setText(str(f))
        except TypeError:
            pass

    def get_angular(self):
        try:
            f = Finddir().find_filepath()
            self.angular_line.setText(str(f))
        except TypeError:
            pass

    def get_spatial(self):
        try:
            f = Finddir().find_filepath()
            self.spatial_line.setText(str(f))
        except TypeError:
            pass

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
        else:
            pass

    def beam_selected(self):
        self.delete_button.setDisabled(False)
        self.selected_index = self.commission_text.currentRow()
        self.beam_delete = self.beam_list[self.selected_index]

    def delete_beam(self):
        self.commission_text.takeItem(self.commission_text.currentRow())
        beam_dict.delete_beam(self.beam_delete)
        beam_dict.update_beam()
       #  self.commission_text.repaint()

    def beam_confirmed(self):
        glv.set_value('spectrum file', self.spectrum_line.text())
        glv.set_value('angular file', self.angular_line.text())
        glv.set_value('spatial file', self.spatial_line.text())
        if Beam_Check().change_beam_check():
            QMessageBox.information(self, 'Done', 'Beam information added.')
            self.close()
        else:
            pass

    def beam_canceled(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Beam()
    w.show()
    app.exec_()
