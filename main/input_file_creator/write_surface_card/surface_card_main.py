# -*- coding: utf-8 -*-
"""
Surface Card Main module
"""
__author__ = 'Kanru Xie'


import globalvar as glv
from input_file_creator.write_surface_card import (objective_surface)
from input_file_creator.write_surface_card import mlc_surface, baseplate_surface, jaws_surface


def surface_card():
    s_card = ''
    mlc_state = glv.get_value('mlc state')
    if mlc_state == 'no mlc':
        s_card = str('c surface card' + '\n' +
                     '  1  box 20 20 -100 -40 0 0 0 -40 0 0 0 -40 $water tank' + '\n' +
                     objective_surface.obj() +
                     '  999 rpp -35 35 -35 35 -145 5 $Void' + '\n' +
                     jaws_surface.x_jaw() +
                     jaws_surface.y_jaw() +
                     baseplate_surface.baseplate() + '\n'
                     )
    elif mlc_state == 'standard mlc':
        s_card = str('c surface card' + '\n' +
                     '  1  box 20 20 -100 -40 0 0 0 -40 0 0 0 -40 $water tank' + '\n' +
                     objective_surface.obj() +
                     '  999 rpp -35 35 -35 35 -145 5 $Void' + '\n' +
                     jaws_surface.x_jaw() +
                     jaws_surface.y_jaw() +
                     baseplate_surface.baseplate() +
                     mlc_surface.mlc() + '\n'
                     )

    return s_card
