# -*- coding: utf-8 -*-
"""
Tally
"""
__author__ = 'Kanru Xie'

import globalvar as glv


def tally_():
    obj = glv.get_value('objective')
    lat_size = glv.convert_float('lattice size')
    t_card = ''
    max_lat = int(40 / lat_size - 2)
    center_lat = int(max_lat / 2)
    if obj == 'x':
        t_card = str('*F8:p (3<3[0:' + str(max_lat) + ' 0:0 0:0])')
    elif obj == 'y':
        t_card = str('*F8:p (3<3[0:0 0:' + str(max_lat) + ' 0:0])')
    elif obj == 'z':
        t_card = str('*F8:p (3<3[0:0 0:0 0:' + str(int(40 / lat_size - 1)) + '])')
    elif obj == 'xy':
        t_card = str('*F8:p (3<3[0:' + str(max_lat) + ' ' +
                     str(center_lat) + ':' + str(center_lat) + ' 0:0])' + '\n' +
                     '*F18:p (3<3[' + str(center_lat) + ':' + str(center_lat) +
                     ' 0:' + str(int(40 / lat_size - 1)) + ' 0:0])'
                     )
    elif obj == 'detector':
        t_card = str('*F8:p 2')
    return t_card
