# script_exemple.py

from ModeleMagasin.Magasin import Magasin
from ModeleMusique.Musique import Musique

# Création de quelques Musique
m1 = Musique(titre="Imagine", artiste="John Lennon", immatriculation="JL/001/POP/1971")
m2 = Musique(titre="Billie Jean", artiste="Michael Jackson", immatriculation="MJ/002/POP/1982")

# Création du Magasin
store = Magasin(genre="Pop")

# Ajouts
store.ajouter_vinyle(m1)
store.ajouter_dvd(m2)

print("Vinyles :", store.lister_vinyles())
print("DVDs   :", store.lister_dvds())
