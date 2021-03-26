# -*- coding: utf-8 -*-
"""
Decide the range of leaf numbers need to open based on the input fs
"""
__author__ = 'Kanru Xie'

import globalvar as glv


def mlc_open_leaves():
    mlc_y = glv.convert_float('mlc y')
    global open_l, open_r
    '''
    Had issues of the initial leave numbers. 
    open_l should start from 30 and 46, open_r should start from 31 and 15
    '''
    if 0 <= mlc_y < 8:  # Center quarter leaves cover 8cm in total.
        open_l = 30 + int((mlc_y / 2) // 0.25)  # Leaf number on left side of open field.
        open_r = 31 - int((mlc_y / 2) // 0.25)  # Leaf number on right side of open field.
    elif 8 <= mlc_y < 21:  # Half leaves take from 4cm to 10.5cm on one side.
        open_l = 46 + int(((mlc_y / 2) - 4) // 0.5)
        open_r = 15 - int(((mlc_y / 2) - 4) // 0.5)
    else:  # The rest 0.5cm on each side are outboard leaves.
        open_l = 60
        open_r = 1


def mlc_open_distance(leaf_number):  # either half of x- opening (opened), or 0 (closed).
    mlc_x = glv.convert_float('mlc x')
    x_distance = ''
    mlc_open_leaves()
    if open_r <= (leaf_number % 100) <= open_l:  # 2 banks, leaves numbered as 1xx and 2xx.
        if leaf_number // 100 == 1:  # Bank 1 moves in +x direction
            x_distance = mlc_x / 2
        elif leaf_number // 100 == 2:  # Bank 2 moves in -x direction
            x_distance = - mlc_x / 2
    else:
        x_distance = 0
        # out of field leaves, closed
    return x_distance
