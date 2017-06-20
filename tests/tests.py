from csv_detective.detect_fields.FR.other import code_csp_insee, csp_insee, sexe, siren, tel_fr
from csv_detective.detect_fields.other import email, url

from csv_detective.detect_fields.FR.geo import adresse, code_commune_insee, code_postal, commune, departement, pays, region
from csv_detective.detect_fields.geo import iso_country_code

from csv_detective.detect_fields.FR.temp import jour_de_la_semaine
from csv_detective.detect_fields.temp import year, date


# csp_insee
def test_match_csp_insee():
    val = 'employes de la poste'
    assert csp_insee._is(val)


def test_do_not_match_csp_insee():
    val = 'super-heros'
    assert not csp_insee._is(val)


# code_csp_insee
def test_match_code_csp_insee():
    val = '121f'
    assert code_csp_insee._is(val)


def test_do_not_match_code_csp_insee():
    val = '121x'
    assert not code_csp_insee._is(val)


# sexe
def test_match_sexe():
    val = 'homme'
    assert sexe._is(val)


def test_do_not_match_sexe():
    val = 'hermaphrodite'
    assert not sexe._is(val)

# tel_fr
def test_match_tel_fr():
    val = '0134643467'
    assert tel_fr._is(val)


def test_do_not_match_tel_fr():
    val = '3345689715'
    assert not tel_fr._is(val)


# email
def test_match_email():
    val = 'cdo_intern@data.gouv.fr'
    assert email._is(val)


def test_do_not_match_email():
    val = 'cdo@@gouv.sfd'
    assert not email._is(val)

# url
def test_match_url():
    val = 'www.etalab.data.gouv.fr'
    assert url._is(val)


def test_do_not_match_url():
    val = 'c est une phrase'
    assert not url._is(val)


# adresse
def test_match_adresse():
    val = 'rue du martyr'
    assert adresse._is(val)


def test_do_not_match_adresse():
    val = 'bonjour les amis'
    assert not adresse._is(val)


# code_commune_insee
def test_match_code_commune_insee():
    val = '91471'
    assert code_commune_insee._is(val)


def test_do_not_match_code_commune_insee():
    val = '914712'
    assert not code_commune_insee._is(val)

# commune
def test_match_commune():
    val = 'saint denis'
    assert commune._is(val)

def test_do_not_match_commune():
    val = 'new york'
    assert not commune._is(val)

# departement
def test_match_departement():
    val = 'essonne'
    assert departement._is(val)

def test_do_not_match_departement():
    val = 'new york'
    assert not departement._is(val)

# pays
def test_match_pays():
    val = 'france'
    assert pays._is(val)


def test_do_not_match_pays():
    val = 'new york'
    assert not pays._is(val)

# region
def test_match_region():
    val = 'bretagne'
    assert region._is(val)


def test_do_not_match_region():
    val = 'jambon beurre'
    assert not region._is(val)

# iso_country_code
def test_match_iso_country_code():
    val = 'FR'
    assert iso_country_code._is(val)


def test_do_not_match_iso_country_code():
    val = 'XX'
    assert not iso_country_code._is(val)

# jour de la semaine
def test_match_jour_de_la_semaine():
    val = 'lundi'
    assert jour_de_la_semaine._is(val)


def test_do_not_match_jour_de_la_semaine():
    val = 'jour de la biere'
    assert not jour_de_la_semaine._is(val)

# year
def test_match_year():
    val = '2015'
    assert year._is(val)


def test_do_not_match_year():
    val = '20166'
    assert not year._is(val)

# date
def test_match_date():
    val = '1960-08-07'
    assert date._is(val)


def test_do_not_match_date():
    val = '1993-1993-1993'
    assert not date._is(val)


# siren
def test_match_siren():
    val = '552 100 554'
    assert siren._is(val)


def test_do_not_match_siren():
    val = '42'
    assert not siren._is(val)
