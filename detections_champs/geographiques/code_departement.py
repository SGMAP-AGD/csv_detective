# -*- coding: utf-8 -*-
"""
Created on Thu Feb 12 11:51:29 2015

@author: leo_cdo_intern
"""

from os.path import dirname, join
from process_text.process_text import _process_text
import re

rel_path = '../../fichiers_de_reference/geographiques'
path = join(dirname(__file__), rel_path)

def _code_departement(val):
    '''Renvoie True si val peut être un code_département, False sinon'''
    val = val.zfill(3)
    liste_des_dep = [str(x).zfill(3) for x in range(1,96)] + \
                    ['02A', '02B'] + [str(x).zfill(3) for x in range(971,976)]
    # TODO: Enregistrer la liste des départements dans un fichier texte séparé
    return val in liste_des_dep




