# -*- coding: utf-8 -*-
"""
Write objective cells 2 and 3
"""
__author__ = 'Kanru Xie'

import globalvar as glv


def obj():
    obj_cell = ''
    objective = glv.get_value('objective')

    if objective != 'd':
        obj_cell = str('  2 1 -1.0 -2 fill=1 imp:p,e 1 $lattice body' + '\n' +
                       '  3 1 -1.0 -3 lat=1 u=1 imp:p,e 1 $lattice cell')
    elif objective == 'd':
        obj_cell = str('  2 1 -1.0 -2 imp:p,e 1 $detector')
    else:
        print('no objective')

    return obj_cell
