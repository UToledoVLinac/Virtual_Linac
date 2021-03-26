# -*- coding: utf-8 -*-
"""
Collimators designing window
"""
__author__ = 'Kanru Xie'


from PyQt5.QtWidgets import QLabel, QWidget, QVBoxLayout, QApplication
import sys


class CollimatorsWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Collimators Designing')
        self.setFixedSize(400, 300)
        self.info_label = QLabel('UNDER CONSTRUCTION')
        self.main_layout = QVBoxLayout()
        self.main_layout.addWidget(self.info_label)
        self.setLayout(self.main_layout)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = CollimatorsWindow()
    w.show()
    app.exec_()
