from Domain.artist_validator import ArtistValidator
from Domain.concert_validator import ConcertValidator
from Repository.json_repository import JsonRepository
from Service.artist_service import ArtistService
from Service.concert_service import ConcertService


def test_all():
    test_adauga_artisti()
    test_adauga_concerte()
    test_ordonare()


def clear_file(filename: str):
    with open(filename, "w"):
        pass


def test_adauga_artisti():
    clear_file("test_artist.json")
    artist_repository = JsonRepository("test_artist.json")
    artist_validator = ArtistValidator()
    artist_service = ArtistService(artist_repository, artist_validator)
    artist_service.adauga("1", "ab", "populara", 15.0)
    artist_service.adauga("2", "cd", "pop", 25.0)
    artisi = artist_service.getAll()
    assert len(artisi) == 2
    assert artisi[0].id_entity == "1"
    assert artisi[1].nume == "cd"


def test_adauga_concerte():
    clear_file("test_artist.json")
    artist_repository = JsonRepository("test_artist.json")
    artist_validator = ArtistValidator()
    artist_service = ArtistService(artist_repository, artist_validator)
    artist_service.adauga("1", "ab", "populara", 15.0)
    artist_service.adauga("2", "cd", "pop", 25.0)
    clear_file("test_concert.json")
    concert_repository = JsonRepository("test_concert.json")
    concert_validator = ConcertValidator()
    concert_service = ConcertService(concert_repository, concert_validator, artist_repository)
    concert_service.adauga("1", "abc", "botosani", 1000, "1")
    concert_service.adauga("2", "def", "cluj", 10000, "2")
    concerte = concert_service.getAll()
    assert len(concerte) == 2
    assert concerte[0].id_artist == "1"
    assert concerte[1].locatie == "cluj"


def test_ordonare():
    pass
