# -*- coding: utf-8 -*-
"""
Check dir and file name for new beam files
"""
__author__ = 'Kanru Xie'


import globalvar as glv
import os
from PyQt5.QtWidgets import QMessageBox


class New_File_Check(QMessageBox):
    def __init__(self):
        super().__init__()

        self.check_dict = dict.fromkeys(['dir', 'name'], False)
        self.directory = glv.get_value('new beam file directory')
        self.name = glv.get_value('new beam file name')

    def directory_check(self):
        if self.directory == '':
            QMessageBox.critical(self, 'Error', 'Please enter directory.')
        elif not os.path.isdir(self.directory):
            QMessageBox.critical(self, 'Error', 'Directory does not exist.')
        else:
            self.check_dict['dir'] = True

    def name_check(self):
        if self.name == '':
            QMessageBox.critical(self, 'Error', 'Please enter new file name.')
        else:
            filepath = os.path.join(self.directory, self.name)
            if not os.path.isfile(filepath):
                self.check_dict['name'] = True
            else:
                warnings = str(self.name + ' already exists. Do you want to overwrite?')
                file_choice = QMessageBox.question(self, 'Caution', warnings,
                                                   QMessageBox.Yes | QMessageBox.No)
                if file_choice == QMessageBox.Yes:
                    self.check_dict['name'] = True
                elif file_choice == QMessageBox.No:
                    pass

    def final_check(self):
        self.directory_check()
        self.name_check()

        if all(value for value in self.check_dict.values()):
            return True
        else:
            return False
