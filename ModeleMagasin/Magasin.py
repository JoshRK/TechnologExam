from dataclasses import dataclass, field
from typing import List
from ModeleMusique.Musique import Musique

@dataclass
class Magasin:
    genre: str
    vinyles: List[Musique] = field(default_factory=list)
    dvds: List[Musique] = field(default_factory=list)

    def lister_vinyles(self) -> List[Musique]:
        return list(self.vinyles)

    def lister_dvds(self) -> List[Musique]:
        return list(self.dvds)

    def ajouter_vinyle(self, musique: Musique) -> bool:
        if not musique.immatriculation_valide():
            return False
        if self.genre not in musique.immatriculation:
            return False
        if musique in self.vinyles:
            return False
        self.vinyles.append(musique)
        return True

    def retirer_vinyle(self, immatriculation: str) -> bool:
        before = len(self.vinyles)
        self.vinyles = [
            m for m in self.vinyles if m.immatriculation != immatriculation
        ]
        return len(self.vinyles) < before

    def ajouter_dvd(self, musique: Musique) -> bool:
        if not musique.immatriculation_valide():
            return False
        if self.genre not in musique.immatriculation:
            return False
        if musique in self.dvds:
            return False
        self.dvds.append(musique)
        return True

    def retirer_dvd(self, immatriculation: str) -> bool:
        before = len(self.dvds)
        self.dvds = [
            m for m in self.dvds if m.immatriculation != immatriculation
        ]
        return len(self.dvds) < before
