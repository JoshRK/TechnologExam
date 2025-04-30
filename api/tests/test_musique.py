import unittest
from ModeleMusique.Musique import Musique

class TestMusique(unittest.TestCase):

    # 🔲 BOÎTE NOIRE : cas entièrement valide
    def test_immatriculation_valide(self):
        m = Musique("Beat Street", "Bob Marley", "BM/180/POP/1234")
        self.assertTrue(m.immatriculation_valide())

    # 🔲 BOÎTE NOIRE : genre non autorisé
    def test_genre_invalide(self):
        m = Musique("Genre Test", "Bob Marley", "BM/180/JAZ/1234")
        self.assertFalse(m.immatriculation_valide())

    # 🔲 BOÎTE NOIRE : identifiant contenant un 6
    def test_identifiant_avec_6(self):
        m = Musique("Bad ID", "Bob Marley", "BM/180/POP/1264")
        self.assertFalse(m.immatriculation_valide())

    # 🔲 BOÎTE NOIRE : durée trop courte
    def test_duree_trop_courte(self):
        m = Musique("Too Short", "Bob Marley", "BM/050/POP/1234")
        self.assertFalse(m.immatriculation_valide())

    # 🔲 BOÎTE NOIRE : durée trop longue
    def test_duree_trop_longue(self):
        m = Musique("Too Long", "Bob Marley", "BM/999/POP/1234")
        self.assertFalse(m.immatriculation_valide())

    # 🔳 BOÎTE BLANCHE : initiales incorrectes (alors que tout le reste est bon)
    def test_initiales_invalides(self):
        m = Musique("Fake Artist", "Alice Cooper", "ZZ/180/POP/1234")  # ZZ ≠ AC
        self.assertFalse(m.immatriculation_valide())

    # 🔳 BOÎTE BLANCHE : initiales correctes avec nom/prénom
    def test_initiales_valides_avec_deux_noms(self):
        m = Musique("Valid Artist", "Alicia Keys", "AK/180/RNB/1234")
        self.assertTrue(m.immatriculation_valide())

    # 🔳 BOÎTE BLANCHE : nom composé (plus de 2 mots)
    def test_initiales_trois_noms(self):
        m = Musique("Long Name", "Jean Claude Van", "JC/180/RAP/1234")
        self.assertTrue(m.immatriculation_valide())  # prend les 2 premiers mots

    # 🔳 BOÎTE BLANCHE : format général invalide (tiret au lieu de slash)
    def test_format_general_invalide(self):
        m = Musique("Format", "Bob Marley", "BM-180-POP-1234")
        self.assertFalse(m.immatriculation_valide())

if __name__ == '__main__':
    unittest.main()
