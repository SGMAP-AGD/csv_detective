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


def _siren(val):
    '''Repere les codes SIREN'''
    val = val.replace(' ', '')
    regex = r'^[0-9]{9}$'
    if not bool(re.match(regex, val)):
        return False
    # Vérification par clé propre aux codes siren
    cle = 0
    pair = False
    for x in val:
        y = int(x) * (1 + pair)
        cle += y // 10 + y % 10
        pair = not pair
    return cle % 10 == 0
