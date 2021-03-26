# -*- coding: utf-8 -*-
"""
TRCL module
functions to calculate trcl card of jaws and mlc
"""
__author__ = 'Kanru Xie'

from math import atan, tan, sin, cos
from itertools import chain
from input_file_creator.write_cell_card.mlc_open import mlc_open_distance


def trcl_y(fs):
    t = [0, 0, 0, 0, 90, 90, 90, 0, -90, 90, 90, 0]
    rotation = float(atan(fs / 100) * 360 / 6.282)
    t[1] = 0.001
    # MCNP issue, dy of Y-Jaws can't be 0, have to give them a small value, don't know why...
    t[7] = ("%0.4f" % rotation)
    t[8] = ("%0.4f" % (rotation - 90))
    t[10] = ("%0.4f" % (rotation + 90))
    t[11] = ("%0.4f" % rotation)
    tr = ''
    for i in range(len(t)):
        tr += str(t[i]) + ' '
    return tr


def trcl_x(fs):
    t = [0, 0, 0, 0, 90, 90, 90, 0, -90, 90, 90, 0]
    rotation = float(atan(fs / 100) * 360 / 6.282)
    rotation_rad = float(atan(fs / 200))
    t[0] = ("%.4f" % (36.61 * (tan(rotation_rad) - sin(rotation_rad))))
    t[2] = ("%.4f" % (36.61 * (cos(rotation_rad) - 1)))
    t[3] = ("%.4f" % rotation)
    t[5] = ("%.4f" % (rotation - 90))
    t[9] = ("%.4f" % (rotation + 90))
    t[11] = ("%.4f" % rotation)
    tr = ''
    for i in range(len(t)):
        tr += str(t[i]) + ' '
    return tr


def trcl_mlc(mlc_type):
    t = [0, 0, 0, 0, 90, 90, 90, 0, -90, 90, 90, 0]
    leaf_bank = ''  # Will be the string for this whole group of leaves.
    basic_leaf = ''  # The leaf number with surfaces described.
    leaf_range = ''  # The leaves numbers in this group.
    center_z = ''  # Center z- value of this leaf, Isocenter and Target leaves are different.
    leaf_shift = ''  # The value for half-leaves to shift from center over the quarter leaves.
    leaf_width = ''  # 3 different width by quarter, half and outboard leaves.
    # There may be a better way to describe all these different basic leaves.
    if mlc_type == 'qi1':
        basic_leaf = 130
        leaf_range = chain(range(116, 130, 2), range(132, 148, 2))
        center_z = 50.98
        leaf_shift = 0
        leaf_width = 0.285
    elif mlc_type == 'qi2':
        basic_leaf = 230
        leaf_range = chain(range(216, 230, 2), range(232, 248, 2))
        center_z = 50.98
        leaf_shift = 0
        leaf_width = 0.285
    elif mlc_type == 'qt1':
        basic_leaf = 131
        leaf_range = chain(range(115, 131, 2), range(133, 147, 2))
        center_z = 50.88
        leaf_shift = 0
        leaf_width = 0.285
    elif mlc_type == 'qt2':
        basic_leaf = 231
        leaf_range = chain(range(215, 231, 2), range(233, 247, 2))
        center_z = 50.88
        leaf_shift = 0
        leaf_width = 0.285
    elif mlc_type == 'hi1r':  # right half group
        basic_leaf = 114
        leaf_range = range(102, 114, 2)
        center_z = 50.98
        leaf_shift = 2.28
        leaf_width = 0.574
    elif mlc_type == 'hi1l':  # left half group
        basic_leaf = 114
        leaf_range = range(148, 160, 2)
        center_z = 50.98
        leaf_shift = 6.904
        leaf_width = 0.574
    elif mlc_type == 'hi2r':  # right half group
        basic_leaf = 214
        leaf_range = range(202, 214, 2)
        center_z = 50.98
        leaf_shift = 2.28
        leaf_width = 0.574
    elif mlc_type == 'hi2l':  # left half group
        basic_leaf = 214
        leaf_range = range(248, 260, 2)
        center_z = 50.98
        leaf_shift = 6.904
        leaf_width = 0.574
    elif mlc_type == 'ht1r':  # right half group
        basic_leaf = 113
        leaf_range = range(103, 113, 2)
        center_z = 50.88
        leaf_shift = 2.854
        leaf_width = 0.574
    elif mlc_type == 'ht1l':  # left half group
        basic_leaf = 113
        leaf_range = range(147, 160, 2)
        center_z = 50.88
        leaf_shift = 7.478
        leaf_width = 0.574
    elif mlc_type == 'ht2r':  # right half group
        basic_leaf = 213
        leaf_range = range(203, 213, 2)
        center_z = 50.88
        leaf_shift = 2.854
        leaf_width = 0.574
    elif mlc_type == 'ht2l':  # left half group
        basic_leaf = 213
        leaf_range = range(247, 260, 2)
        center_z = 50.88
        leaf_shift = 7.478
        leaf_width = 0.574
    # For calculation methods see the structure document.
    # There are 3 layers of loop: t_i for elements in the trcl of one single leaf.
    # j and k are to put the elements and words of one leaf into a string of MCNP input card.
    # leaf_bank is to put strings of all those similar leaves together.
    for leaf_i in leaf_range:
        t_i = t
        leaf_space = (basic_leaf - leaf_i) / 2  # Calculate how many leaves is this away from basic.
        rotation = leaf_width * leaf_space + leaf_shift
        rotation_rad = rotation * 6.28 / 360
        t_i[0] = mlc_open_distance(leaf_i)  # Only moves in x- direction, dx decide by function.
        t_i[1] = ("%0.4f" % (center_z * (tan(rotation_rad) - sin(rotation_rad))))
        t_i[2] = ("%0.4f" % (center_z * (cos(rotation_rad) - 1)))
        t_i[7] = ("%0.4f" % rotation)
        t_i[8] = ("%0.4f" % (rotation - 90))
        t_i[10] = ("%0.4f" % (rotation + 90))
        t_i[11] = ("%0.4f" % rotation)
        tr_displacement = ''
        tr_rotation = ''
        for j in range(3):  # Need 2 lines for the trcl card otherwise it will be too long.
            tr_displacement += str(t_i[j]) + ' '
        for k in range(3, 12):
            tr_rotation += str(t_i[k]) + ' '
        leaf_bank += '  ' + str(leaf_i) + ' like ' + str(basic_leaf) + \
                     ' but trcl*=(' + tr_displacement + '\n' + \
                     ' ' * 26 + tr_rotation + ')' + '\n'  # 26 spaces is to make it look neatly.
    return leaf_bank
