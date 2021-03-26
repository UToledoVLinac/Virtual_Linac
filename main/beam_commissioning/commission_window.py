# -*- coding: utf-8 -*-
"""
Beam Commissioning window
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import (QLabel, QPushButton, QVBoxLayout,
                             QHBoxLayout, QWidget, QApplication, QTabWidget)
import globalvar as glv
from beam_commissioning.Commissioned_Beams import beam_dict
from beam_commissioning.commission_tab import Commision_Tab
from beam_commissioning.spatial_tab import Spatial_Tab
from beam_commissioning.angular_tab import Angular_Tab
from beam_commissioning.spectrum_tab import Spectrum_Tab
import sys


class CommissionWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Beam Commissioning')

        self.tabs = QTabWidget()
        self.info = QLabel('Information')
        # self.beam_init_button = QPushButton('Beam Initialization')
        self.tab1 = Commision_Tab()
        self.tab2 = Spectrum_Tab()
        self.tab3 = Angular_Tab()
        self.tab4 = Spatial_Tab()
        self.bottom_widget = QWidget()
        self.save_button = QPushButton('Save')
        self.cancel_button = QPushButton('Cancel')

        self.bottom_layout = QHBoxLayout()
        self.layout = QVBoxLayout()

        self.tabs.addTab(self.tab1, 'Commissioning')
        self.tabs.addTab(self.tab2, 'Spectrum File')
        self.tabs.addTab(self.tab3, 'Angular File')
        self.tabs.addTab(self.tab4, 'Spatial File')

        self.layout_init()
        self.pushbutton_init()
        self.tab1UI()

    def layout_init(self):
        self.bottom_layout.addWidget(self.save_button)
        self.bottom_layout.addWidget(self.cancel_button)
        self.bottom_widget.setLayout(self.bottom_layout)
        self.layout.addWidget(self.info)
        # self.layout.addWidget(self.beam_init_button)
        self.layout.addWidget(self.tabs)
        self.layout.addWidget(self.bottom_widget)
        self.setLayout(self.layout)

    def pushbutton_init(self):
        self.save_button.clicked.connect(self.save_file)

    def tab1UI(self):
        self.tab1.show()

    def tab2UI(self):
        self.tab2.show()

    def tab3UI(self):
        self.tab3.show()

    def tab4UI(self):
        self.tab4.show()

    def save_file(self):
        # Inputwindow().beam_combo_update()
        self.close()


if __name__=='__main__':
    glv._init()
    beam_dict._init()
    app=QApplication(sys.argv)
    demo=CommissionWindow()
    demo.show()
    sys.exit(app.exec_())

