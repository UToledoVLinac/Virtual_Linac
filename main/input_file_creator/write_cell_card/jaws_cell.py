# -*- coding: utf-8 -*-
"""
Jaws cell
"""
__author__ = 'Kanru Xie'


from input_file_creator.write_cell_card.trcl import trcl_x, trcl_y
import globalvar as glv


def jaws():
    y1 = glv.convert_float('y1 Jaw')
    y2 = glv.convert_float('y2 Jaw')
    x1 = glv.convert_float('x1 Jaw')
    x2 = glv.convert_float('x2 Jaw')
    # x2 and y2 jaws need a negative sign to indicate it's the opposite direction.
    j_11 = str('  11 3 -18 -11 12 13 -14 15 -16 imp:p,e 1 $Y1' + '\n' +
               '     trcl*=(' + str(trcl_y(y1)) + ')' + '\n')
    j_12 = str('  12 3 -18 -11 12 13 -14 -17 18 imp:p,e 1 $Y2' + '\n' +
               '     trcl*=(' + str(trcl_y(y2)) + ')' + '\n')
    j_21 = str('  21 3 -18 -21 22 23 -24 25 -26 imp:p,e 1 $X1' + '\n' +
               '     trcl*=(' + str(trcl_x(x1)) + ')' + '\n')
    j_22 = str('  22 3 -18 -21 22 23 -24 -27 28 imp:p,e 1 $Y1' + '\n' +
               '     trcl*=(' + str(trcl_x(x2)) + ')')
    jaw_str = j_11 + j_12 + j_21 + j_22
    return jaw_str
