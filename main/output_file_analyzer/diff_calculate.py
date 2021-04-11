# -*- coding: utf-8 -*-
"""
Load measured data and calculate percent different
"""
__author__ = 'Kanru Xie'

import numpy as np
import globalvar as glv
from scipy import interpolate

'''
def pdd_calc():
    measured_data = glv.get_value('Measured data filepath')
    measured_data_array = np.loadtxt(measured_data, delimiter=',')
    x_measured = measured_data_array[:, 0]
    y_measured = measured_data_array[:, 1]
    x_output = glv.get_value('Output X')
    y_output = glv.get_value('Output normalized Y')
    for i in range(1, len(x_output)):
        if x_measured[i - 1] <= x_output[0] < x_measured[i]:
            index_min = i - 1
        if x_output[i - 1] <= x_measured[-1] < x_output[i]:
            index_max = i - 1
    x_new = x_output[:index_max]
    y_interp = interpolate.interp1d(x_measured[index_min:], y_measured[index_min:], kind='linear')
    y_measured_new = y_interp(x_new)
    y_measured_normalize = y_measured_new / max(y_measured_new)
    y_diff = (y_measured_new - y_output[:index_max]) / y_measured_new

    glv.set_value('Measured X', x_new)
    glv.set_value('Measured Y', y_measured_normalize)
    glv.set_value('Y diff', y_diff)
'''


def pdd_calc():
    measured_data = glv.get_value('Measured data filepath')
    measured_data_array = np.loadtxt(measured_data, delimiter=',')
    x_measured = measured_data_array[:, 0]
    y_measured = measured_data_array[:, 1]
    index_max = len(x_measured)
    x_output = glv.get_value('Output X')
    y_output = glv.get_value('Output normalized Y')
    y_diff = (y_measured - y_output[:index_max]) / y_measured
    glv.set_value('Measured X', x_measured)
    glv.set_value('Measured Y', y_measured)
    glv.set_value('Y diff', y_diff)


def profile_calc():
    measured_data = glv.get_value('Measured data filepath')
    measured_data_array = np.loadtxt(measured_data)
    x_measured = measured_data_array[:, 0]
    y_measured = measured_data_array[:, 1]
    x_output = glv.get_value('Output X')
    y_output = glv.get_value('Output normalized Y')
    index_min = 0
    index_max = 0

    if x_measured[0] < -200 or x_measured[0] > 200:
        for i in range(0, len(x_measured) - 1):
            if x_measured[i] < -200 <= x_measured[i + 1]:
                index_min = i
            if x_measured[i] <= 200 < x_measured[i + 1]:
                index_max = i + 1
        x_new = x_output
        y_interp = interpolate.interp1d(x_measured[index_min:index_max],
                                        y_measured[index_min:index_max], kind='linear')
        y_measured_new = y_interp(x_new)
        y_measured_normalize = y_measured_new / max(y_measured_new)
        y_diff = (y_measured_normalize - y_output) / y_measured_normalize
    if -200 <= x_measured[0] <= 200:
        for i in range(0, len(x_output) - 1):
            if x_output[i] <= x_measured[0] < x_output[i + 1]:
                index_min = i
            if x_output[i] < x_measured[-1] <= x_output[i + 1]:
                index_max = i + 1
        x_new = x_output[index_min:index_max]
        y_interp = interpolate.interp1d(x_measured, y_measured, kind='linear')
        y_measured_new = y_interp(x_new)
        y_measured_normalize = y_measured_new / max(y_measured_new)
        y_diff = (y_measured_normalize - y_output[index_min:index_max]) / y_measured_normalize

    glv.set_value('Measured X', x_new)
    glv.set_value('Measured Y', y_measured_normalize)
    glv.set_value('Y diff', y_diff)


''' X and Y profiles are the same
def yprofile_calc():
    measured_data = glv.get_value('Measured data filepath')
    measured_data_array = np.loadtxt(measured_data)
    x_measured = measured_data_array[:, 0]
    y_measured = measured_data_array[:, 1]
    x_output = glv.get_value('Output X')
    y_output = glv.get_value('Output normalized Y')
    index_min = 0
    index_max = 0

    if x_measured[0] < -200 or x_measured[0] > 200:
        for i in range(0, len(x_measured) - 1):
            if x_measured[i] < -200 <= x_measured[i + 1]:
                index_min = i
            if x_measured[i] <= 200 < x_measured[i + 1]:
                index_max = i + 1
        x_new = x_output
        y_interp = interpolate.interp1d(x_measured[index_min:index_max],
                                        y_measured[index_min:index_max], kind='linear')
        y_measured_new = y_interp(x_new)
        y_measured_normalize = y_measured_new / max(y_measured_new)
        y_diff = (y_measured_normalize - y_output) / y_measured_normalize
    if -200 <= x_measured[0] <= 200:
        for i in range(0, len(x_output) - 1):
            if x_output[i] <= x_measured[0] < x_output[i + 1]:
                index_min = i
            if x_output[i] < x_measured[-1] <= x_output[i + 1]:
                index_max = i + 1
        x_new = x_output[index_min:index_max]
        y_interp = interpolate.interp1d(x_measured, y_measured, kind='linear')
        y_measured_new = y_interp(x_new)
        y_measured_normalize = y_measured_new / max(y_measured_new)
        y_diff = (y_measured_normalize - y_output[index_min:index_max]) / y_measured_normalize

    glv.set_value('Measured X', x_new)
    glv.set_value('Measured Y', y_measured_normalize)
    glv.set_value('Y diff', y_diff)
'''
