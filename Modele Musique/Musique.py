# musique.py

from dataclasses import dataclass, field
import re

@dataclass
class Musique:
    titre: str
    artiste: str
    immatriculation: str = field(repr=False)

    def __post_init__(self) -> None:
        """
        Valide que l'immatriculation est au format XX/123/ABC/1234
        (2 lettres, 3 chiffres, 3 lettres, 4 chiffres).
        """
        pattern = r"^[A-Z]{2}/\d{3}/[A-Z]{3}/\d{4}$"
        if not re.fullmatch(pattern, self.immatriculation):
            raise ValueError(
                f"Immatriculation invalide « {self.immatriculation} » ; "
                "doit être au format XX/123/ABC/1234"
            )
