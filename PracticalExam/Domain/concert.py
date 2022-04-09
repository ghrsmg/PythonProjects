from dataclasses import dataclass

from Domain.entity import Entity


@dataclass
class Concert(Entity):
    nume: str
    locatie: str
    capacitate: int
    id_artist: str
