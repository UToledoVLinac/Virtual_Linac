# -*- coding: utf-8 -*-
"""
The main window
"""
__author__ = 'Kanru Xie'

from PyQt5.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton, QVBoxLayout, QWidget)
from PyQt5.QtGui import QPixmap
import sys
from input_file_creator.input_window import Inputwindow
from beam_commissioning.commission_window import CommissionWindow
from output_file_analyzer.output_window import Output_Window
import globalvar as glv
from beam_commissioning.Commissioned_Beams import beam_dict
import webbrowser


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle('MCNP-Linac')
        self.statement = QLabel('FOR UNIVERSITY OF TOLEDO MEDICAL PHYSICS RESEARCH ONLY')
        self.version = QLabel('Author: Kanru Xie.' + '\n' +
                              'Version: 1.0.1 Beta')
        self.picture = QPixmap('dcc_sunset.png')
        self.piclabel = QLabel()
        self.piclabel.setPixmap(self.picture)
        self.piclabel.resize(640, 640)
        self.piclabel.setScaledContents(True)

        self.window1 = Inputwindow()
        self.window2 = Output_Window()
        self.window3 = CommissionWindow()

        self.btn1 = QPushButton('Input File Creator')
        self.btn2 = QPushButton('Output File Analyzer')
        self.btn3 = QPushButton('Beam Commissioning')
        self.btn4 = QPushButton('Collimator Designing')
        self.btn5 = QPushButton('Help')

        self.layout_init()
        self.pushbutton_init()

    def layout_init(self):
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.statement)
        main_layout.addWidget(self.version)
        main_layout.addWidget(self.btn1)
        main_layout.addWidget(self.btn2)
        main_layout.addWidget(self.btn3)
        main_layout.addWidget(self.btn4)
        main_layout.addWidget(self.piclabel)
        main_layout.addWidget(self.btn5)

        main_widget = QWidget()
        main_widget.setLayout(main_layout)
        self.setCentralWidget(main_widget)

    def pushbutton_init(self):
        self.btn1.clicked.connect(self.click_btn1)
        self.btn2.clicked.connect(self.click_btn2)
        self.btn3.clicked.connect(self.click_btn3)
        self.btn5.clicked.connect(self.click_btn5)

    def click_btn1(self):
        self.window1.beam_combobox_init()
        self.window1.show()

    def click_btn2(self):
        self.window2.show()

    def click_btn3(self):
        self.window3.show()

    def click_btn5(self):
        # filepath = str(os.getcwd() + 'main/Instruction_Manual.pdf')
        # now go to Github
        webbrowser.open(r'https://github.com/KanruXie/Virtual_Linac')


if __name__ == '__main__':
    glv._init()
    beam_dict._init()
    app = QApplication(sys.argv)
    w = MainWindow()
    w.show()
    app.exec_()
