from os.path import dirname, join
from process_text import _process_text
import re

PROPORTION = 1

def _is(val):
    '''Repère le sexe'''
    val =_process_text(val)
    return val in ['homme', 'femme', 'h', 'f', 'm', 'masculin', 'feminin']

