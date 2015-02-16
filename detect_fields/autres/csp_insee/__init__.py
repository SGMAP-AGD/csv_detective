# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:54:46 2015

@author: leo_cdo_intern
"""

from os.path import dirname, join
from process_text.process_text import _process_text
import re

PROPORTION = 1

def _is(val):
    '''Repère les csp telles que définies par l'INSEE'''
    val = _process_text(val)
    f = open(join(dirname(__file__), 'csp_insee.txt'), 'r')
    liste = f.read().split('\n')
    f.close()
    return val in liste