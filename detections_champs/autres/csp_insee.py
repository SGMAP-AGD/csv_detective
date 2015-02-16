# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:54:46 2015

@author: leo_cdo_intern
"""

from os.path import dirname, join
from process_text.process_text import _process_text
import re

rel_path = '../../fichiers_de_reference/autres'
path = join(dirname(__file__), rel_path)

def _csp_insee(val):
    '''Repère les csp telles que définies par l'INSEE'''
    val = _process_text(val)
    f = open(join(path, 'csp_insee.txt'), 'r')
    liste = f.read().split('\n')
    f.close()
    return val in liste
