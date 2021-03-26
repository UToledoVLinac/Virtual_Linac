# -*- coding: utf-8 -*-
"""
The main window
"""
__author__ = 'Kanru Xie'

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget, QHBoxLayout)
from PyQt5.QtGui import QPixmap
import sys
import os
import globalvar as glv
from input_file_creator.input_window import Inputwindow
from beam_commissioning.commission_window import CommissionWindow
from output_file_analyzer.output_window import Output_Window
from collimator_designing.collimator_window import CollimatorsWindow
from beam_commissioning.Commissioned_Beams import beam_dict
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MCNP-Linac')
        self.main_widget = QWidget()
        self.statement = QLabel('FOR UNIVERSITY OF TOLEDO MEDICAL PHYSICS RESEARCH ONLY')
        self.version = QLabel('Author: Kanru Xie' + '\n' +
                              'Version: 1.0.0 Beta')
        self.picture = QPixmap('../dcc_sunset.png')
        self.piclabel = QLabel()
        self.piclabel.setPixmap(self.picture)
        # self.piclabel.resize(640, 640)
        self.piclabel.setScaledContents(True)
        self.bottom_widget = QWidget()
        self.button_widget = QWidget()

        self.window1 = Inputwindow()
        self.window2 = Output_Window()
        self.window3 = CommissionWindow()
        self.window4 = CollimatorsWindow()

        self.btn1 = QPushButton('Input File Creator')
        self.btn2 = QPushButton('Output File Analyzer')
        self.btn3 = QPushButton('Beam Commissioning')
        self.btn4 = QPushButton('Collimator Designing')
        self.btn5 = QPushButton('Help')

        self.main_layout = QVBoxLayout()
        self.bottom_layout = QHBoxLayout()
        self.button_layout = QVBoxLayout()

        self.layout_init()
        self.pushbutton_init()

    def layout_init(self):
        self.main_layout.addWidget(self.statement)
        self.main_layout.addWidget(self.version)
        self.main_layout.addWidget(self.bottom_widget)
        self.bottom_layout.addWidget(self.piclabel)
        self.bottom_layout.addWidget(self.button_widget)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.button_layout.addWidget(self.btn1)
        self.button_layout.addWidget(self.btn2)
        self.button_layout.addWidget(self.btn3)
        self.button_layout.addWidget(self.btn4)
        self.button_layout.addWidget(self.btn5)
        self.button_widget.setLayout(self.button_layout)
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(self.main_widget)

    def pushbutton_init(self):
        self.btn1.clicked.connect(self.click_btn1)
        self.btn2.clicked.connect(self.click_btn2)
        self.btn3.clicked.connect(self.click_btn3)
        self.btn4.clicked.connect(self.click_btn4)
        self.btn5.clicked.connect(self.click_btn5)

    def click_btn1(self):
        self.window1.beam_combobox_init()
        self.window1.show()

    def click_btn2(self):
        self.window2.show()

    def click_btn3(self):
        self.window3.show()

    def click_btn4(self):
        self.window4.show()

    def click_btn5(self):
        filepath = str(os.getcwd() + '/Instruction_Manual.pdf')
        webbrowser.open_new(r'file:' + filepath)


if __name__ == '__main__':
    glv._init()
    beam_dict._init()
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()

