# -*- coding: utf-8 -*-
"""
Beam spatial distribution
"""
__author__ = 'Kanru Xie'

import numpy as np
import globalvar as glv


def spatial_init():
    filepath = glv.get_value('spatial file')
    global a
    a = np.loadtxt(filepath, dtype=str)


def spatial():
    spatial_init()
    source_spatial = ''
    if a[0, 0] == 'gaussian':
        source_spatial = str('c Source spacial distribution' + '\n' +
                             '  sp19 -41 ' + a[1, 1] + ' 0' + '\n' +
                             '  sp20 -41 ' + a[2, 1] + ' 0' + '\n'
                             )
    elif a[0, 0] == 'uniform':
        x = '%.3f' % (float(a[1, 1]) / 2)
        y = '%.3f' % (float(a[2, 1]) / 2)
        source_spatial = str('c Source spacial distribution' + '\n' +
                             '  si19 -' + x + ' ' + x + '\n' +
                             '  sp19 0 1' + '\n' +
                             '  si20 -' + y + ' ' + y + '\n' +
                             '  sp20 0 1' + '\n'
                             )
    return source_spatial

