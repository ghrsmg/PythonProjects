from dataclasses import dataclass

from Domain.entitate import Entitate


@dataclass
class Film(Entitate):

    titluFilm: str
    anaparitieFilm: str
    pretbiletFilm: float
    inprogramFilm: str
