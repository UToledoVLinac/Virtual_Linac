# -*- coding: utf-8 -*-
"""
Read beam commisioning file and write in material card
"""
__author__ = 'Kanru Xie'

import numpy as np
import globalvar as glv
import os


def spectrum_init():
    filepath = glv.get_value('spectrum file')
    global a
    a = np.loadtxt(filepath, dtype=str)


def energy(interval):
    spectrum_init()
    ds_number = str(interval + 2)
    # ds is the MCNP source dependent card
    energy_str = '  si' + ds_number + ' A ' + a[0, 1] + ' ' + a[0, 2] + ' ' + a[0, 3] + ' ' + a[0, 4] + ' ' + \
                 a[0, 5] + ' ' + a[0, 6] + ' ' + a[0, 7] + ' ' + a[0, 8] + ' ' + a[0, 9] + ' ' + \
                 a[0, 10] + ' ' + a[0, 11] + ' ' + a[0, 12] + ' ' + a[0, 13] + ' ' + a[0, 14] + ' ' + '\n' + \
                 ' ' * 8 + a[0, 15] + ' ' + a[0, 16] + ' ' + a[0, 17] + ' ' + a[0, 18] + ' ' + a[0, 19] + '\n'
    return energy_str


def prob(interval):
    spectrum_init()
    ds_number = str(interval + 2)
    c = 15 - interval
    prob_str = '  sp' + ds_number + ' ' + a[c, 1] + ' ' + a[c, 2] + ' ' + a[c, 3] + ' ' + a[c, 4] + ' ' + \
               a[c, 5] + ' ' + a[c, 6] + ' ' + a[c, 7] + ' ' + a[c, 8] + ' ' + a[c, 9] + ' ' + \
               a[c, 10] + ' ' + a[c, 11] + ' ' + a[c, 12] + ' ' + '\n' + \
               ' ' * 8 + a[c, 13] + ' ' + a[c, 14] + ' ' + a[c, 15] + ' ' + a[c, 16] + ' ' + \
               a[c, 17] + ' ' + a[c, 18] + ' ' + a[c, 19] + '\n'
    return prob_str


def spectrum_():
    spectrum_angles = ''
    for i in range(1, 15):
        spectrum_angles += energy(i) + prob(i)
    spectrum_card = 'c Source spectrum by angles' + '\n' + \
                    '  ds2 s 3 4 5 6 7 8 9 10 11 12 13 14 15 16' + '\n' + \
                    spectrum_angles
    return spectrum_card
