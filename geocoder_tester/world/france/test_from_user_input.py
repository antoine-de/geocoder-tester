from geocoder_tester.base import assert_search
import pytest


@pytest.mark.qwant_non_regression
def test_ajaccio():
    assert_search("ajaccio", {'name': 'Ajaccio', 'coordinate': '41.9263991, 8.7376029,5000'})

@pytest.mark.qwant_non_regression
def test_chateauroux():
    assert_search("chateauroux", {'name': 'Châteauroux', 'postcode': '36000'})

@pytest.mark.qwant_non_regression
def test_indre_et_loire():
    assert_search("indre et loire", {'name': 'Indre-et-Loire', 'coordinate': '47.2232046,0.6866702523286876,50000'})

@pytest.mark.qwant_non_regression
def test_28_Rue_de_la_Belle_Marie_Barbizon():
    assert_search("28 Rue de la Belle Marie Barbizon", {'street': 'Rue de la Belle Marie', 'postcode': '77630'})

@pytest.mark.qwant_non_regression
def test_6_Rue_Romy_Schneider_Chevry_Cossigny():
    assert_search("6 Rue Romy Schneider Chevry-Cossigny", {'name': '6 Rue Romy Schneider', 'postcode': '77173'})

@pytest.mark.qwant_non_regression
def test_25_Promenade_des_Golfeurs_77600():
    assert_search("25 Promenade des Golfeurs 77600", {'housenumber': '25', 'street': 'Promenade des Golfeurs', 'city': 'Bussy-Saint-Georges'})

@pytest.mark.qwant_non_regression
def test_14_Ruelle_du_Moulin_Brûlé_77320():
    assert_search("14 Ruelle du Moulin Brûlé 77320", {'name': '14 Ruelle du Moulin Brûlé', 'city': 'Jouy-sur-Morin'})

@pytest.mark.qwant_non_regression
def test_Rue_Beaubourg__PARIS():
    assert_search("Rue Beaubourg  PARIS", {'city': 'Paris', 'coordinate': '48.8627324,2.3542832,500'})

@pytest.mark.qwant_non_regression
def test_Rue_Messidor_Vauréal():
    assert_search("Rue Messidor Vauréal", {'name': 'Rue Messidor', 'postcode': '95490'})

@pytest.mark.qwant_non_regression
def test_3_Rue_de_la_République_Montmorency():
    assert_search("3 Rue de la République Montmorency", {'street': 'Rue de la République', 'postcode': '95160'})

@pytest.mark.qwant_non_regression
def test_Sentier_des_Briandais_22100():
    assert_search("Sentier des Briandais 22100", {'street': 'Sentier des Briandais', 'postcode': '22100'})

@pytest.mark.qwant_non_regression
def test_Rue_Frégate_la_Belle_Poule_29200():
    assert_search("Rue Frégate la Belle-Poule 29200", {'street': 'Rue Frégate la Belle-Poule', 'postcode': '29200'})

@pytest.mark.qwant_non_regression
def test_Chemin_des_Amers_29830():
    assert_search("Chemin des Amers 29830", {'street': 'Chemin des Amers', 'postcode': '29830'})

@pytest.mark.qwant_non_regression
def test_ECOLE_DU_LOUVRE_PARIS():
    assert_search("ECOLE DU LOUVRE PARIS", {'name': 'École du Louvre', 'city': 'Paris', 'coordinate': '48.861519,2.3345495,500'})

@pytest.mark.qwant_non_regression
def test_AccorHotels_Arena():
    assert_search("AccorHotels Arena", {'city': 'Paris', 'coordinate': '48.83870845,2.3787666192264645,100'})

@pytest.mark.qwant_non_regression
def test_collège_yvonne_le_tac():
    assert_search("collège yvonne le tac", {'name': 'Collège Yvonne Le Tac', 'city': 'Paris'})

@pytest.mark.qwant_non_regression
def test_6_Rue_Ane_Rubaud_94230():
    assert_search("6 Rue Ane Rubaud 94230", {'street': 'Rue Ange Rubaud', 'postcode': '94230'})

@pytest.mark.qwant_non_regression
def test_11_Rue_de_la_Grenuillère_Brie_Comte_Robert():
    assert_search("11 Rue de la Grenuillère Brie-Comte-Robert", {'housenumber': '11', 'street': 'Rue de la Grenouillère', 'postcode': '77170'})

@pytest.mark.qwant_non_regression
def test_9_Allée_des_Doits_de_lHomme():
    assert_search("9 Allée des Doits de l'Homme", {'housenumber': '9', 'street': "Allée des Droits de l'Homme", 'postcode': '78114'})

@pytest.mark.qwant_non_regression
def test_bd_bercy_paris():
    assert_search("bd bercy paris", {'street': 'boulevard de Bercy', 'city': 'Paris'})

@pytest.mark.qwant_non_regression
def test_la_ferté_ss_jouarre():
    assert_search("la ferté ss jouarre", {'name': 'La Ferté-sous-Jouarre', 'postcode': '77260'})

@pytest.mark.qwant_non_regression
def test_st_marcellin():
    assert_search("st marcellin", {'name': 'Saint-Marcellin', 'postcode': '38160'})

@pytest.mark.qwant_non_regression
def test_12_rue_mlle_bourgeois():
    assert_search("12 rue mlle bourgeois", {'housenumber': '12', 'street': 'Rue Mademoiselle Bourgeois'})

@pytest.mark.qwant_non_regression
def test_1_place_du_cc_Lomprez():
    assert_search("1 place du cc Lomprez", {'housenumber': '1', 'street': 'Place du Centre Commercial Lomprez'})
