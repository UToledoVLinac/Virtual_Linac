# -*- coding: utf-8 -*-
"""
Input file content checking
--MAKE ME ROBUST!!!

Change some global variables type from str to float or int
(But this is not achievable. Don't know why.
 Will have Type error: 'Tuple' object is not callable
 in Mainwindow.py)
"""
__author__ = 'Kanru Xie'

import globalvar as glv
import os
from PyQt5.QtWidgets import QMessageBox


class ContentCheck(QMessageBox):
    def __init__(self):
        super().__init__()

        self.check_dict = dict.fromkeys(['path', 'lattice', 'depth', 'jaws', 'randomseed',
                                         'nps', 'cutoff', 'x off axis', 'y off axis', 'mlc'], False)
        self.directory = glv.get_value('directory')
        self.input_name = glv.get_value('input file name')
        self.output_name = glv.get_value('output file name')
        self.x1_jaw = glv.get_value('x1 Jaw')
        self.x2_jaw = glv.get_value('x2 Jaw')
        self.y1_jaw = glv.get_value('y1 Jaw')
        self.y2_jaw = glv.get_value('y2 Jaw')
        self.lattice_size = glv.get_value('lattice size')
        self.depth = glv.get_value('depth')
        self.x_offaxis = glv.get_value('x offaxis')
        self.y_offaxis = glv.get_value('y offaxis')
        self.randomseeds = glv.get_value('randomseed')
        self.nps = glv.get_value('nps')
        self.e_cutoff = glv.get_value('e cutoff')
        self.p_cutoff = glv.get_value('p cutoff')
        self.mlc_x = glv.get_value('mlc x')
        self.mlc_y = glv.get_value('mlc y')
        self.objective = glv.get_value('objective')
        self.mlc_state = glv.get_value('mlc state')
        self.lattice = 0

    def filepath_check(self):
        if self.directory == '':
            QMessageBox.critical(self, 'Error', 'Please enter Directory')
        elif self.input_name == '':
            QMessageBox.critical(self, 'Error', 'Please enter Input file name')
        elif self.output_name == '':
            QMessageBox.critical(self, 'Error', 'Please enter Output file name')
        else:
            os.chdir(self.directory)
            if not os.path.isfile('./' + self.input_name):
                self.check_dict['path'] = True
            else:
                warnings = str(self.input_name + ' already exists. Do you want to overwrite?')
                file_choice = QMessageBox.question(self, 'Caution', warnings,
                                                   QMessageBox.Yes | QMessageBox.No)
                if file_choice == QMessageBox.Yes:
                    self.check_dict['path'] = True
                elif file_choice == QMessageBox.No:
                    pass

    def jaws_check(self):
        if self.x1_jaw == '' or self.x2_jaw == '' or self.y1_jaw == '' or self.y2_jaw == '':
            QMessageBox.critical(self, 'Error', 'Please enter all Jaws positions')
        else:
            x1 = float(self.x1_jaw)
            x2 = float(self.x2_jaw)
            y1 = float(self.y1_jaw)
            y2 = float(self.y2_jaw)
            # glv.set_value('x1 Jaw', x1)
            # glv.set_value('x2 Jaw', x2)
            # glv.set_value('y1 Jaw', y1)
            # glv.set_value('y2 Jaw', y2)
            if x1 > 20 or x1 < -20:
                QMessageBox.warning(self, 'Warning', 'X1 position out of range, please try again [-20 cm, 20 cm]')
            elif x2 > 20 or x2 < -20:
                QMessageBox.warning(self, 'Warning', 'X2 position out of range, please try again [-20 cm, 20 cm]')
            elif y1 > 20 or y1 < -20:
                QMessageBox.warning(self, 'Warning', 'Y1 position out of range, please try again [-20 cm, 20 cm]')
            elif y1 > 20 or y2 < -20:
                QMessageBox.warning(self, 'Warning', 'Y2 position out of range, please try again [-20 cm, 20 cm]')
            elif x1 - x2 < 0:
                QMessageBox.critical(self, 'Warning', 'X Jaws have collision, please try again')
            elif y1 - y2 < 0:
                QMessageBox.critical(self, 'Warning', 'Y Jaws have collision, please try again')
            else:
                self.check_dict['jaws'] = True

    def lattice_check(self):
        if self.objective == 'd':
            # glv.set_value = ('lattice size', 0.15)
            self.lattice = 0.15
            self.check_dict['lattice'] = True
        else:
            if self.lattice_size == '':
                QMessageBox.critical(self, 'Error', 'Please enter lattice size')
            else:
                self.lattice = float(self.lattice_size)
                # glv.set_value = ('lattice size', self.lattice)
                if self.lattice <= 0 or self.lattice > 40:
                    QMessageBox.warning(self, 'Warning', 'Lattice size out of range, please try again (0cm, 40cm]')
                else:
                    self.check_dict['lattice'] = True

    def depth_check(self):
        if self.objective == 'z':
            self.check_dict['depth'] = True
        else:
            if self.depth == '':
                QMessageBox.critical(self, 'Error', 'Please enter depth')
            else:
                depth = float(self.depth)
                # glv.set_value = ('depth', depth)
                if (depth - self.lattice / 2) < 0 or (depth + self.lattice / 2) > 40:
                    QMessageBox.warning(self, 'Warning', 'Depth out of range, ' +
                                        'please make sure the lattice is inside the water tank. ' + '\n' + '\n' +
                                        '(depth - lattice size / 2 >= 0 and ' + '\n' +
                                        'depth + lattice size / 2 <= 40)'
                                        )
                else:
                    self.check_dict['depth'] = True

    def x_offaxis_check(self):
        if self.objective == 'x':
            self.check_dict['x off axis'] = True
        else:
            if self.x_offaxis == '':
                QMessageBox.critical(self, 'Error', 'Please enter x- offaxis value.')
            else:
                x_off = float(self.x_offaxis)
                # glv.set_value('x offaxis', x_off)
                if (x_off - self.lattice / 2) < -20 or (x_off + self.lattice / 2) > 20:
                    QMessageBox.warning(self, 'Warning', 'x-off axis value out of range, ' +
                                        'please make sure the lattice is inside the water tank. ' + '\n' + '\n' +
                                        '(x-off axis - lattice size / 2 >= -20 and ' + '\n' +
                                        'x-off axis + lattice size / 2 <= 20)'
                                        )
                else:
                    self.check_dict['x off axis'] = True

    def y_offaxis_check(self):
        if self.objective == 'y':
            self.check_dict['y off axis'] = True
        else:
            if self.y_offaxis == '':
                QMessageBox.critical(self, 'Error', 'Please enter y- offaxis value.')
            else:
                y_off = float(self.y_offaxis)
                # glv.set_value('y offaxis', y_off)
                if (y_off - self.lattice / 2) < -20 or (y_off + self.lattice / 2) > 20:
                    QMessageBox.warning(self, 'Warning', 'y-off axis value out of range, ' +
                                        'please make sure the lattice is inside the water tank. ' + '\n' + '\n' +
                                        '(y-off axis - lattice size / 2 >= -20 and ' + '\n' +
                                        'y-off axis + lattice size / 2 <= 20)'
                                        )
                else:
                    self.check_dict['y off axis'] = True

    def randomseed_check(self):
        if self.randomseeds == '':
            QMessageBox.critical(self, 'Error', 'Please enter Randomseed.')
        else:
            randseed = int(self.randomseeds)
            # glv.set_value('randomseed', randseed)
            # TypeError: 'tuple' object is not callable
            if randseed % 2 == 1:
                self.check_dict['randomseed'] = True
            else:
                QMessageBox.warning(self, 'Warning', 'Randomseed should be an odd number.')

    def nps_check(self):
        if self.nps == '':
            QMessageBox.warning(self, 'Error', 'Please enter nps.')
        else:
            nps = int(self.nps)
            # glv.set_value('nps', nps)
            if nps <= 0:
                QMessageBox.warning(self, 'Warning', 'nps should by a positive integer.')
            else:
                self.check_dict['nps'] = True

    def cutoff_check(self):
        if self.e_cutoff == '' or self.p_cutoff == '':
            QMessageBox.warning(self, 'Error', 'Please enter cutoff energies.')
        else:
            e_cut = float(self.e_cutoff)
            p_cut = float(self.p_cutoff)
            # glv.set_value('e cutoff', e_cut)
            # glv.set_value('p cutoff', p_cut)
            if e_cut < 0.001 or e_cut > 1 or p_cut < 0.001 or p_cut > 1:
                cutoff_choice = QMessageBox.question(self, 'Attention',
                                                     'Your cutoff energies are very big or very small,' + '\n' +
                                                     'are you sure to proceed?',
                                                     QMessageBox.Yes | QMessageBox.No)
                if cutoff_choice == QMessageBox.Yes:
                    self.check_dict['cutoff'] = True
                else:
                    pass
            else:
                self.check_dict['cutoff'] = True

    def mlc_check(self):
        if self.mlc_state == 'no mlc':
            self.check_dict['mlc'] = True
        else:
            if self.mlc_x == '' or self.mlc_y == '':
                QMessageBox.critical(self, 'Error', 'Please enter MLC opening field values')
            else:
                mlc_x = float(self.mlc_x)
                mlc_y = float(self.mlc_y)
                if mlc_x < 0 or mlc_x > 30:
                    QMessageBox.warning(self, 'Warning', 'MLC x opening out of range, ' +
                                        'please try again [0, 30] cm.')
                elif mlc_y < 0 or mlc_y > 22:
                    QMessageBox.warning(self, 'Error', 'MLC y opening out of range, ' +
                                        'please try again [0, 22] cm')
                else:
                    self.check_dict['mlc'] = True

    def final_check(self):
        self.filepath_check()
        self.jaws_check()
        self.lattice_check()
        self.depth_check()
        self.x_offaxis_check()
        self.y_offaxis_check()
        self.randomseed_check()
        self.nps_check()
        self.cutoff_check()
        self.mlc_check()

        if all(value for value in self.check_dict.values()):
            QMessageBox.information(self, 'Good Job', self.input_name + ' printed.')
            return True
        else:
            return False
            # QMessageBox.information(self, 'something wrong', self.input_name + ' not printed.')

    def length_check(self):
        if self.directory == '':
            QMessageBox.critical(self, 'Error', 'Please enter Directory')
        elif self.input_name == '':
            QMessageBox.critical(self, 'Error', 'Please enter Input file name')
        else:
            dir = glv.get_value('directory')
            file = glv.get_value('input file name')
            filepath = os.path.join(dir, file)
            os.chdir(dir)
            if not os.path.isfile('./' + file):
                QMessageBox.critical(self, 'Error', 'File does not exists.')
            else:
                with open(filepath) as checkfile:
                    counter = 0  # counter for the number of lines longer than 80.
                    lines_list = []
                    long_lines_list = []
                    long_lines_str = ''

                    for line in checkfile:
                        lines_list += [line]  # make each line in the file as an element in lines_list
                    for i in range(len(lines_list)):
                        if len(lines_list[i]) >= 80:
                            counter += 1
                            long_lines_list += ['  line#:' + str(i) + ', length= ' + str(len(lines_list[i])) +
                                                ', ' + str([lines_list[i]])]
                    for j in range(len(long_lines_list)):
                        long_lines_str += str(long_lines_list[j] + '\n' * 2)

                    if counter == 0 or counter == 1:  # For grammar correctness
                        line_plural = ' line'
                    else:
                        line_plural = ' lines'

                    len_check_info = str(len(lines_list)) + ' lines checked, ' + str(counter) + str(line_plural) + \
                                     ' exceeding 80 characters:' + '\n' * 2
                    QMessageBox.information(self, 'Length Check', filepath + ':' + '\n' * 2 +
                                      len_check_info + long_lines_str)



