# -*- coding: utf-8 -*-
"""
Find directory
"""
__author__ = 'Kanru Xie'

from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtCore import QFileInfo
import globalvar as glv
import os


class Finddir(QFileDialog):
    def __init__(self):
        super().__init__()

    def find_dir(self):
        dir = QFileDialog.getExistingDirectory(self, 'Directory', os.getcwd())
        if dir == '':
            pass
        else:
            return dir

    def find_filepath(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        filepath = QFileInfo(file).filePath()
        return filepath

    def find_filename(self):
        file, _ = QFileDialog.getOpenFileName(self, 'Open file', os.getcwd())
        filename = QFileInfo(file).fileName()
        return filename

    def find_measured_data(self):
        measured_path = os.getcwd() + '/output_file_analyzer/Measured Data'
        file, _ = QFileDialog.getOpenFileName(self, 'Open file', measured_path)
        filepath = QFileInfo(file).filePath()
        return filepath
