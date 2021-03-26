# -*- coding: utf-8 -*-
"""
Objectives Surfaces
"""
__author__ = 'Kanru Xie'

import globalvar as glv


def obj():
    objective = glv.get_value('objective')
    lat_size = glv.convert_float('lattice size')
    depth = glv.convert_float('depth')
    x_offaxis = glv.convert_float('x offaxis')
    y_offaxis = glv.convert_float('y offaxis')
    obj_surface = ''
    if objective == 'x':
        obj_surface = str('  2  box ' + str(20 - lat_size / 2) + ' ' + str(y_offaxis + lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' + str(-40 + lat_size) +
                          ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + '\n' +
                          '  3  box ' + str(20 - lat_size / 2) + ' ' + str(y_offaxis + lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' +
                          str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 ' +
                          str(-lat_size) + '\n'
                          )
    elif objective == 'y':
        obj_surface = str('  2  box ' + str(x_offaxis + lat_size / 2) + ' ' + str(20 - lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' + str(-lat_size) +
                          ' 0 0 0 ' + str(-40 + lat_size) + ' 0 0 0 ' + str(-lat_size) + '\n' +
                          '  3  box ' + str(x_offaxis + lat_size / 2) + ' ' + str(20 - lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' + str(-lat_size) +
                          ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + '\n'
                          )
    elif objective == 'z':
        obj_surface = str('  2  box ' + str(x_offaxis + lat_size / 2) + ' ' +
                          str(y_offaxis + lat_size / 2) + ' -100 ' +
                          str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 -40' + '\n' +
                          '  3  box ' + str(x_offaxis + lat_size / 2) + ' ' +
                          str(y_offaxis + lat_size / 2) + ' -100 ' +
                          str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 ' +
                          str(-lat_size) + '\n'
                          )
    elif objective == 'xy' or objective == 'dose map':
        obj_surface = str('  2  box ' + str(20 - lat_size / 2) + ' ' + str(20 - lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' + str(-40 + lat_size) +
                          ' 0 0 0 ' + str(-40 + lat_size) + ' 0 0 0 ' + str(-lat_size) + '\n' +
                          '  3  box ' + str(20 - lat_size / 2) + ' ' + str(20 - lat_size / 2) + ' ' +
                          str(-100 - depth + lat_size / 2) + ' ' +
                          str(-lat_size) + ' 0 0 0 ' + str(-lat_size) + ' 0 0 0 ' +
                          str(-lat_size) + '\n'
                          )
    elif objective == 'd':
        obj_surface = str('  2  rcc 0 0.15 ' + str(-100 - depth) + ' 0 -0.3 0 0.05' + '\n')
    return obj_surface
