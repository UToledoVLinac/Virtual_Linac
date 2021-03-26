# -*- coding: utf-8 -*-
"""
The module to write and read json file for beam dictionary
"""
__author__ = 'Kanru Xie'


import json
import os


def _init():
    dir = os.getcwd()
    filepath = dir + '/beam_commissioning/Commissioned_Beams/commissioned_beams.json'
    # be careful about the file path
    global _beam_dict
    with open(filepath, 'r') as f:
        _beam_dict = json.load(f)


def add_beam(name, value):
    _beam_dict[name] = value


def delete_beam(name):
    del _beam_dict[name]


def get_beam(name):
    beam_info = _beam_dict[name]
    return beam_info


def update_beam():
    dir = os.getcwd()
    filepath1 = dir + '/beam_commissioning/Commissioned_Beams/commissioned_beams.json'
    updated_beam_dict = _beam_dict
    with open(filepath1, 'w') as f:
        json.dump(updated_beam_dict, f)


def update_list():
    dir = os.getcwd()
    filepath1 = dir + '/beam_commissioning/Commissioned_Beams/commissioned_list.json'
    list = []
    for key in _beam_dict.keys():
        list.append(key)
        # why I need to use append but not +=
    with open(filepath1, 'w') as f:
        json.dump(list, f)


def list_beams():
    dir = os.getcwd()
    filepath2 = dir + '/beam_commissioning/Commissioned_Beams/commissioned_list.json'
    with open(filepath2, 'r') as f:
        list = json.load(f)
    return list
