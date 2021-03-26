# -*- coding: utf-8 -*-
"""
Material Card Main module
"""
__author__ = 'Kanru Xie'

from input_file_creator.write_material_card import (materials_define, tally, spectrum)
from input_file_creator.write_material_card import angular_distribution, spatial_distribution
import globalvar as glv


def material_card():
    m_card = ''
    nps = glv.get_value('nps')
    randseed = glv.get_value('randomseed')
    p_cutoff = glv.get_value('p cutoff')
    e_cutoff = glv.get_value('e cutoff')
    m_card = 'c Materials' + '\n' + \
             materials_define.materials() + '\n' + \
             'sdef dir=d1 erg Fdir d2 par=2 vec=0 0 -1 X=d19 Y=d20 Z=0 POS=0 0 0' + '\n' + \
             angular_distribution.angles() + '\n' + \
             angular_distribution.prob() + '\n' + \
             spectrum.spectrum_() + \
             spatial_distribution.spatial() + \
             'mode p e' + '\n' + \
             'nps ' + nps + '\n' + \
             'RAND SEED=' + randseed + '\n' + \
             'cut:e j ' + e_cutoff + '\n' + \
             'cut:p j ' + p_cutoff + '\n' + \
             'phys:p 10 0 1 0 1' + '\n' + \
             tally.tally_() + '\n'

    return m_card
