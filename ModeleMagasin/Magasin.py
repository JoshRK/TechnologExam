# magasin.py

from dataclasses import dataclass, field
from typing import List
from Modele Musique.musique import Musique   # import relatif si votre package est un module

@dataclass
class Magasin:
    genre: str
    vinyles: List[Musique] = field(default_factory=list)
    dvds:    List[Musique] = field(default_factory=list)

    def lister_vinyles(self) -> List[Musique]:
        return list(self.vinyles)

    def lister_dvds(self) -> List[Musique]:
        return list(self.dvds)

    def ajouter_vinyle(self, musique: Musique) -> None:
        if musique in self.vinyles:
            raise ValueError(f"« {musique.titre} » est déjà en vinyle.")
        self.vinyles.append(musique)

    def retirer_vinyle(self, immatriculation: str) -> None:
        before = len(self.vinyles)
        self.vinyles = [
            m for m in self.vinyles if m.immatriculation != immatriculation
        ]
        if len(self.vinyles) == before:
            raise LookupError(f"Aucun vinyle trouvé pour « {immatriculation} ».")

    def ajouter_dvd(self, musique: Musique) -> None:
        if musique in self.dvds:
            raise ValueError(f"« {musique.titre} » est déjà en DVD.")
        self.dvds.append(musique)

    def retirer_dvd(self, immatriculation: str) -> None:
        before = len(self.dvds)
        self.dvds = [
            m for m in self.dvds if m.immatriculation != immatriculation
        ]
        if len(self.dvds) == before:
            raise LookupError(f"Aucun DVD trouvé pour « {immatriculation} ».")
