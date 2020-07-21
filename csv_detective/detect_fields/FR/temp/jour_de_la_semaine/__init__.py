from os.path import dirname, join
from process_text import _process_text
import re

PROPORTION = 1

def _is(val):
    '''Renvoie True si les champs peuvent être des jours de la semaine'''
    val = val.lower()
    jours = ['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche','lun','mar','mer','jeu','ven','sam','dim']
    return val in jours
