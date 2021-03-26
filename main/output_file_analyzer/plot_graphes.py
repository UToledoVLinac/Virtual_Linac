# -*- coding: utf-8 -*-
"""
Plot the graphes
"""
__author__ = 'Kanru Xie'


import globalvar as glv
import pyqtgraph as pg


def graph_init():
    pg.setBackground('w')
    pg.showGrid(x=True, y=True)
    pg.setYRange(0, 1.1)
    pg.plot_graph.addLegend()


def plot_output_pdd():
    x = glv.get_value('Output PDD depth')
    y = glv.get_value('Output PDD normalized dose')
    name = glv.get_value('Output data name')
    pg.plot(x, y, pen=pg.mkPen('r'), name=name)
