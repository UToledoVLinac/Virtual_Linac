# -*- coding: utf-8 -*-
"""
Add new beam to beam_dict
"""
__author__ = 'Kanru Xie'

from beam_commissioning.Commissioned_Beams import beam_dict
import globalvar as glv


def add_beam():
    spectrum = glv.get_value('spectrum file')
    angular = glv.get_value('angular file')
    spatial = glv.get_value('spatial file')
    beam_name = glv.get_value('new beam name')
    beam_value = [spectrum, angular, spatial]
    beam_dict.add_beam(beam_name, beam_value)


def delete_beam():
    beam_name = glv.get_value('chosen beam')
    beam_dict.delete_beam(beam_name)


