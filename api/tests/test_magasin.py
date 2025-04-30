import unittest
from ModeleMagasin.Magasin import Magasin
from ModeleMusique.Musique import Musique

class TestMagasin(unittest.TestCase):

    # 🔲 BOÎTE NOIRE : ajout valide
    def test_ajouter_vinyle_valide(self):
        m = Musique("Hit", "Bob Marley", "BM/180/POP/1234")
        magasin = Magasin("POP")
        result = magasin.ajouter_vinyle(m)
        self.assertTrue(result)
        self.assertIn(m, magasin.vinyles)

    # 🔲 BOÎTE NOIRE : ajout vinyle avec mauvais genre
    def test_ajout_mauvais_genre(self):
        m = Musique("Flow", "Bob Marley", "BM/180/RAP/1234")
        magasin = Magasin("POP")
        result = magasin.ajouter_vinyle(m)
        self.assertFalse(result)
        self.assertNotIn(m, magasin.vinyles)

    # 🔲 BOÎTE NOIRE : ajout vinyle avec immatriculation invalide
    def test_ajout_immatriculation_invalide(self):
        m = Musique("Fake", "Bob Marley", "BM/50/POP/1234")  # durée trop courte
        magasin = Magasin("POP")
        result = magasin.ajouter_vinyle(m)
        self.assertFalse(result)

    # 🔲 BOÎTE NOIRE : retirer un vinyle existant
    def test_retirer_vinyle(self):
        m = Musique("Track", "Bob Marley", "BM/180/POP/1234")
        magasin = Magasin("POP")
        magasin.ajouter_vinyle(m)
        result = magasin.retirer_vinyle(m.immatriculation)
        self.assertTrue(result)
        self.assertNotIn(m, magasin.vinyles)

    # 🔳 BOÎTE BLANCHE : éviter les doublons
    def test_ajout_doublon(self):
        m = Musique("Repeat", "Bob Marley", "BM/180/POP/1234")
        magasin = Magasin("POP")
        magasin.ajouter_vinyle(m)
        result = magasin.ajouter_vinyle(m)
        self.assertFalse(result)  # déjà présent

    # 🔳 BOÎTE BLANCHE : retirer un vinyle inexistant
    def test_retirer_inexistant(self):
        magasin = Magasin("POP")
        result = magasin.retirer_vinyle("ZZ/200/POP/9999")
        self.assertFalse(result)

    # 🔳 BOÎTE BLANCHE : ajouter un DVD au bon genre
    def test_ajouter_dvd_valide(self):
        m = Musique("Smooth", "Alicia Keys", "AK/200/RNB/1234")
        magasin = Magasin("RNB")
        result = magasin.ajouter_dvd(m)
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
