# -*- coding: utf-8 -*-
"""
Load beam files module
"""
__author__ = 'Kanru Xie'


from beam_commissioning.Commissioned_Beams import beam_dict


def find_beam(name):
    beam_list = beam_dict.list_beams()
    selected_index = self.commission_text.currentRow()
    beam_load = beam_list[selected_index]
    beam_feature = beam_dict.get_beam(beam_load)
    self.spectrum_line.setText(beam_feature[0])
    self.angular_line.setText(beam_feature[1])
    self.spatial_line.setText(beam_feature[2])