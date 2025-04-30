from dataclasses import dataclass, field
import re

@dataclass
class Musique:
    titre: str
    artiste: str
    immatriculation: str = field(repr=False)

    def immatriculation_valide(self) -> bool:
        match = re.fullmatch(r"^([A-Z]{2})/(\d{3})/([A-Z]{3})/(\d{4})$", self.immatriculation)
        if not match:
            return False

        initiales, duree_str, genre, identifiant = match.groups()

        attendues = ''.join([mot[0].upper() for mot in self.artiste.split()[:2]])
        if initiales != attendues:
            return False

        duree = int(duree_str)
        if not (60 < duree < 300):
            return False

        if genre not in ["POP", "RAP", "RNB"]:
            return False

        if "6" in identifiant:
            return False

        return True
