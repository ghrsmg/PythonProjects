from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Artist(Entity):
    nume: str
    categorie: str
    tarif: float
