from Domain.artist import Artist
from Domain.artist_validator import ArtistValidator
from Repository.json_repository import JsonRepository


class ArtistService:
    def __init__(self, artist_repository: JsonRepository,
                 artist_validator: ArtistValidator):
        self.artist_repository = artist_repository
        self.artist_validator = artist_validator

    def getAll(self):
        """

        :return: toti artistii inregistrati
        """
        return self.artist_repository.read()

    def adauga(self, id_artist: str, nume: str, categorie: str, tarif: float):
        """
        adauga un artist
        :param id_artist: id-ul acestuia
        :param nume: numele artistului
        :param categorie: categoria din care face parte
        :param tarif: tariful pe care acesta il cere
        :return:
        """
        artist = Artist(id_artist, nume, categorie, tarif)
        self.artist_validator.valideaza(artist)
        self.artist_repository.create(artist)

    def afisare_artisti_descrescator(self):
        """
        afisarea artistilor descrescator dupa pret
        :return: o lista de dictionare
        """
        rezultat = []
        for artist in self.artist_repository.read():
            rezultat.append({
                "artist": artist.nume,
                "tarif": artist.tarif
            })
        return sorted(rezultat, key=lambda x: x["tarif"], reverse=True)
