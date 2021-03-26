# -*- coding: utf-8 -*-
"""
Read beam commisioning file and write in material card
"""
__author__ = 'Kanru Xie'

import numpy as np
import globalvar as glv


def angular_init():
    global a
    filepath = glv.get_value('angular file')
    a = np.loadtxt(filepath, dtype=str)


def angles():
    angular_init()
    angle_ = 'c Source divergence (cosine of the angle)' + '\n' + \
             '  si1 A ' + a[1, 1] + ' ' + a[1, 2] + ' ' + a[1, 3] + ' ' + a[1, 4] + ' ' + a[1, 5] + '\n' + \
             ' ' * 8 + a[1, 6] + ' ' + a[1, 7] + ' ' + a[1, 8] + ' ' + a[1, 9] + ' ' + a[1, 10] + '\n' + \
             ' ' * 8 + a[1, 11] + ' ' + a[1, 12] + ' ' + a[1, 13] + ' ' + a[1, 14] + ' ' + a[1, 15]
    return angle_


def prob():
    angular_init()
    prob_ = 'c Source divergence distribution values' + '\n' + \
            '  sp1 ' + a[2, 1] + ' ' + a[2, 2] + ' ' + a[2, 3] + ' ' + a[2, 4] + ' ' + a[2, 5] + '\n' + \
            ' ' * 8 + a[2, 6] + ' ' + a[2, 7] + ' ' + a[2, 8] + ' ' + a[2, 9] + ' ' + a[2, 10] + '\n' + \
            ' ' * 8 + a[2, 11] + ' ' + a[2, 12] + ' ' + a[2, 13] + ' ' + a[2, 14] + ' ' + a[2, 15]
    return prob_

