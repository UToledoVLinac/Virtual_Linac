# -*- coding: utf-8 -*-
"""
Read output file with RE
"""
__author__ = 'Kanru Xie'

import numpy as np
import re
import globalvar as glv


def read_file():
    global filepath, lattice_1, lattice_2
    filepath = glv.get_value('Output filepath')
    with open(filepath, 'r') as f:
        read = f.read()
        tally_1 = re.findall(r' *\d*- {7}\*F8:p \(3<3\[\d+:\d+ \d+:\d+ \d+:\d+', read)
        tally_2 = re.findall(r' *\d*- {7}\*F18:p \(3<3\[\d+:\d+ \d+:\d+ \d+:\d+', read)
        lattice_1 = re.findall(r'\d+', str(tally_1))
        lattice_2 = re.findall(r'\d+', str(tally_2))


def read_pdd():
    read_file()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        text = ' cell \(3<3\[' + str(lattice_1[4]) + ' ' + str(lattice_1[6]) + ' ' + '.*'
        pattern = re.compile(text)
        dose_list = []
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                t = lines[i + 1]
                b = float(t[17:28])
                dose_list += [b]

    step = 400 / len(dose_list)
    start = step / 2
    end = start + 400
    max = int(14 / step - 1)  # which lattice is max dose, not depth

    dose_array = np.array(dose_list)
    max_dose = dose_array[max]
    dose_normalized_array = dose_array / max_dose

    depth_array = np.arange(start, end, step)
    glv.set_value('Output X', depth_array)
    glv.set_value('Output Y', dose_array)
    glv.set_value('Output normalized Y', dose_normalized_array)


def read_xprofile():
    read_file()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        text = ' cell \(3<3\[.* ' + str(lattice_1[6]) + ' ' + str(lattice_1[8]) + '\]\)'
        pattern = re.compile(text)
        numbers_list = []
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                t = lines[i + 1]
                b = float(t[17:28])
                numbers_list += [b]

    if not lattice_2:
        dose_list = numbers_list
    else:
        dose_list = numbers_list[:-1]

    step = 400 / (len(dose_list) + 1)  # we are having one lattice in the center, so the len is an odd number
    start = -200 + step
    end = 200
    max = int(lattice_1[6])

    dose_array = np.array(dose_list)
    max_dose = dose_array[max]
    dose_normalized_array = dose_array / max_dose

    distance_array = np.arange(start, end, step)
    glv.set_value('Output X', distance_array)
    glv.set_value('Output Y', dose_array)
    glv.set_value('Output normalized Y', dose_normalized_array)


def read_yprofile():
    read_file()
    with open(filepath, 'r') as f:
        lines = f.readlines()
        text = ' cell \(3<3\[' + str(lattice_2[4]) + ' .* ' + str(lattice_2[8]) + '\]\)'
        pattern = re.compile(text)
        numbers_list = []
        for i, line in enumerate(lines):
            if re.search(pattern, line):
                t = lines[i + 1]
                b = float(t[17:28])
                numbers_list += [b]

    if not lattice_2:
        dose_list = numbers_list
        max = int(lattice_1[4])
    else:
        dose_list = numbers_list[1:]
        max = int(lattice_2[4])

    step = 400 / (len(dose_list) + 1)  # we are having one lattice in the center, so the len is an odd number
    start = -200 + step
    end = 200

    dose_array = np.array(dose_list)
    max_dose = dose_array[max]
    dose_normalized_array = dose_array / max_dose

    depth_array = np.arange(start, end, step)
    glv.set_value('Output X', depth_array)
    glv.set_value('Output Y', dose_array)
    glv.set_value('Output normalized Y', dose_normalized_array)
