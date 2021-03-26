# -*- coding: utf-8 -*-
"""
Air card module
"""
__author__ = 'Kanru Xie'

import globalvar as glv


def air_card_1():
    # No MLC
    objective = glv.get_value('objective')
    air_card = ''
    if objective != 'd':
        air_card = str('c Air' + '\n' +
                       '  10 2 -0.001293 -999 #1 #2 #3 #11 #12 #21 #22 #31 imp:p,e 1' + '\n')
    elif objective == 'd':
        air_card = str('c Air' + '\n' +
                       '  10 2 -0.001293 -999 #1 #2 #11 #12 #21 #22 #31 imp:p,e 1' + '\n')
    return air_card


def air_card_2():
    # Use MLC
    objective = glv.get_value('objective')
    air_card_mlc = ''
    air_card = ''
    for air_banks in range(1, 3):  # two air banks
        b = ''
        for air_bank_lines in range(0, 5):  # 5 lines in each bank, 12 excludes in each line
            c = ''
            for air_cell_excludes in range(100 * air_banks + 12 * air_bank_lines + 1,
                                           100 * air_banks + 12 * (air_bank_lines + 1) + 1):
                c += '#' + str(air_cell_excludes) + ' '
            b += ' ' * 5 + c + '\n'
        air_card_mlc += b
    if objective != 'd':
        air_card = 'c Air' + '\n' + \
                   '  10 2 -0.001293 -999 #1 #2 #3 #11 #12 #21 #22 #31' + '\n' + \
                   air_card_mlc + \
                   ' ' * 5 + 'imp:p,e 1' + '\n'
    elif objective == 'd':
        air_card = 'c Air' + '\n' + \
                   '  10 2 -0.001293 -999 #1 #2 #11 #12 #21 #22 #31' + '\n' + \
                   air_card_mlc + \
                   ' ' * 5 + 'imp:p,e 1' + '\n'
    return air_card
