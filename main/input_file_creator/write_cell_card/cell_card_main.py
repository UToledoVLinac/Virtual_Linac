# -*- coding: utf-8 -*-
"""
Cell Card main module
"""
__author__ = 'Kanru Xie'

import globalvar as glv
from input_file_creator.write_cell_card import (objective_cell, air_cell, baseplate_cell, jaws_cell, mlc_cell)


def cell_card():
    c_card = ''
    mlc_state = glv.get_value('mlc state')
    if mlc_state == 'no mlc':
        c_card = str('c Cell card' + '\n' +
                     'c Water tank phantom' + '\n' +
                     '  1 1 -1.0 -1 2 imp:p,e 1 $water tank' + '\n' +
                     objective_cell.obj() + '\n' +
                     air_cell.air_card_1() +
                     'c Jaws' + '\n' +
                     jaws_cell.jaws() + '\n' +
                     baseplate_cell.baseplate() + '\n' +
                     'c Void' + '\n' +
                     '  999 0 999 imp:p,e 0' + '\n' + '\n'
                     )
    elif mlc_state == 'standard mlc':
        c_card = str('c Cell card' + '\n' +
                     'c Water tank phantom' + '\n' +
                     '  1 1 -1.0 -1 2 imp:p,e 1 $water tank' + '\n' +
                     objective_cell.obj() + '\n' +
                     air_cell.air_card_2() +
                     'c Jaws' + '\n' +
                     jaws_cell.jaws() + '\n' +
                     baseplate_cell.baseplate() + '\n' +
                     mlc_cell.mlc_card() +
                     'c Void' + '\n' +
                     '  999 0 999 imp:p,e 0' + '\n' + '\n'
                     )

    return c_card
