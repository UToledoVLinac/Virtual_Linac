# -*- coding: utf-8 -*-
"""
Global variables defining module
  --by value type
"""
__author__ = 'Kanru Xie'


def _init():
    global _global_dict
    _global_dict = {}


def set_value(name, value):
    _global_dict[name] = value


def get_value(name, defvalue='') -> object:
    try:
        return _global_dict[name]
    except KeyError:
        return defvalue


def convert_int(name):
    converted = int(_global_dict[name])
    return converted


def convert_float(name):
    converted = float(_global_dict[name])
    return converted


def clear_value():
    _global_dict.clear()


'''
Global variables standard names:
====================================
# Input Window
  'directory'
  'input file name'
  'output file name'
  'e cutoff'
  'p cutoff'
  'nps'
  'randomseed'
  'lattice size'
  'depth'
  'x1 Jaw'
  'x2 Jaw'
  'y1 Jaw'
  'y2 Jaw'
  'mlc x'
  'mlc y'
  'x offaxis'
  'y offaxis'
  'mlc open l'
  'mlc open r'
  'comments'
  'mlc state': no mlc, simplified mlc, standard mlc.
  'objective'
  'beam'
  'spectrum file'
  'spatial file'
'angular file'
'new beam name'
'chosen beam'
====================================
#Output File Analyzer:
  'Output filepath'
  'Output data name'
  'Measured data filepath'
  'Export files path'
  'Output X'
  'Output Y'
  'Output normalized Y'
  'Measured X'
  'Measured Y'
  'Y diff'
'''
