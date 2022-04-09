import jsonpickle

from Domain.concert import Concert
from Domain.concert_validator import ConcertValidator
from Repository.json_repository import JsonRepository


class ConcertService:
    def __init__(self, concert_repository: JsonRepository, concert_validator: ConcertValidator,
                 artist_repository: JsonRepository):
        self.concert_repository = concert_repository
        self.concert_validator = concert_validator
        self.artist_repository = artist_repository

    def getAll(self):
        return self.concert_repository.read()

    def adauga(self, id_concert: str, nume: str, locatie: str, capacitate: int, id_artist: str):
        """
        adauga un concert
        :param id_concert: id-ul concertului
        :param nume: numele concertului
        :param locatie: locatia concertului
        :param capacitate: capacitatea concertului
        :param id_artist: id-ul artistului ce sustine concertul
        :return:
        """
        if self.artist_repository.read(id_artist) is None:
            raise KeyError("Nu exista un artist cu id-ul dat!")
        concert = Concert(id_concert, nume, locatie, capacitate, id_artist)
        self.concert_validator.valideaza(concert)
        self.concert_repository.create(concert)

    def nr_concerte_categore(self):
        """
        Arata numarul de concerte la fiecare categorie
        :return: un disctionar
        """
        rezultat = {}
        for artist in self.artist_repository.read():
            rezultat[artist.categorie] = 0
        for concerte in self.concert_repository.read():
            artist_gasit = self.artist_repository.read(concerte.id_artist)
            rezultat[artist_gasit.categorie] += 1
        return rezultat

    def export_json(self, filename: str):
        """
        Exporteaza intr-un fisier json rezultatul
        :param filename: numele fisierului unde vrem sa vedem rezultatul
        :return:
        """
        rezultat = {}
        for artist in self.artist_repository.read():
            rezultat[artist.nume] = []
        for concert in self.concert_repository.read():
            artistul = self.artist_repository.read(concert.id_artist)
            locatie = concert.locatie
            rezultat[artistul.nume].append(locatie)
        with open(filename, 'w') as f:
            f.write(jsonpickle.dumps(rezultat))
