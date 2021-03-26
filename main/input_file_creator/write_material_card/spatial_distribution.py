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
    source_spatial = str('c Source spacial distribution' + '\n' +
                         '  sp19 -41 ' + a[0, 1] + ' 0' + '\n' +
                         '  sp20 -41 ' + a[1, 1] + ' 0' + '\n'
                         )
    return source_spatial
