# -*- coding: utf-8 -*-
"""
Print module
"""
__author__ = 'Kanru Xie'

from input_file_creator.write_cell_card.cell_card_main import cell_card
from input_file_creator.write_surface_card.surface_card_main import surface_card
from input_file_creator.write_material_card.material_card_main import material_card
import globalvar as glv
import os


def file_print():
    directory = glv.get_value('directory')
    input_name = glv.get_value('input file name')
    output_name = glv.get_value('output file name')
    comments = glv.get_value('comments')
    filepath = os.path.join(directory, input_name)
    c_card = cell_card()
    s_card = surface_card()
    m_card = material_card()

    f = open(filepath, 'w')
    f.write('message: r=r%s o=o%s' % (output_name, output_name) + '\n')
    f.write(comments)
    f.write(c_card)
    f.write(s_card)
    f.write(m_card)
    f.close()
