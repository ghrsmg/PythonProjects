from Domain.artist_validator import ArtistValidator
from Domain.concert_validator import ConcertValidator
from Repository.json_repository import JsonRepository
from Service.artist_service import ArtistService
from Service.concert_service import ConcertService
from Tests.tests import test_all
from UserInterface.console import Console


def main():
    test_all()
    artist_repository = JsonRepository("artisti.json")
    artist_validator = ArtistValidator()
    artist_service = ArtistService(artist_repository, artist_validator)
    concert_repository = JsonRepository("concerte.json")
    concert_validator = ConcertValidator()
    concert_service = ConcertService(concert_repository, concert_validator, artist_repository)
    console = Console(artist_service, concert_service)
    console.run_menu()


if __name__ == '__main__':
    main()
