from os.path import dirname, join
from process_text import _process_text
import re

PROPORTION = 1


with open(join(dirname(__file__), 'iso_country_code.txt'), 'r') as iofile:
    liste_pays = iofile.read().split('\n')

def _is(val):
    '''Renvoie True si val peut etre un code iso pays, False sinon'''
    regex = r'[A-Z]{2,3}$'
    if not bool(re.match(regex, val)):
        return False
    return val in liste_pays



