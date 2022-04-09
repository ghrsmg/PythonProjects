from Domain.CardValidator import CardValidator
from Domain.FilmValidator import FilmValidator
from Domain.RezervareValidator import RezervareValidator
from Repository.repositoryJson import RepositoryJson
from Service.cardService import CardService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService


def runAllTests():
    testAdaugaFilm()
    testAdaugaCard()
    testAdaugaRezervare()
    test_rez_interval()
    test_rez_stergere_interval()
    test_incrementare()
    test_card_ord_descrescator()
    test_cautare_full_text()
    test_afsare_filme_descrescator()


def clearfile(filename):
    with open(filename, "w") as f:
        pass


def testAdaugaFilm():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    filme = filmService.getAll()
    assert len(filme) == 1
    assert filme[0].idEntitate == 1
    assert filme[0].titluFilm == "Titanic"


def testAdaugaCard():
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    carduri = cardService.getAll()
    assert len(carduri) == 1
    assert carduri[0].nume == "Mihai"
    assert carduri[0].CNP == "5981126040016"
    assert carduri[0].puncteacumulate == 50.0


def testAdaugaRezervare():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    clearfile("test-rezervari.json")
    rezervareRepository = RepositoryJson("test-rezervari.json")
    rezervareValidator = RezervareValidator()
    rezervareService = RezervareService(rezervareRepository,
                                        rezervareValidator, filmRepository,
                                        cardRepository)
    rezervareService.adaugare("1", "1", "1", "11.12.2021", "22:00")
    rezervari = rezervareService.getAll()
    assert len(rezervari) == 1
    assert rezervari[0].idEntitate == "1"
    assert rezervari[0].data == "11.12.2021"
    assert rezervari[0].ora == "22:00"


def test_rez_interval():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    clearfile("test-rezervari.json")
    rezervareRepository = RepositoryJson("test-rezervari.json")
    rezervareValidator = RezervareValidator()
    rezervareService = RezervareService(rezervareRepository,
                                        rezervareValidator, filmRepository,
                                        cardRepository)
    rezervareService.adaugare("1", "1", "1", "11.12.2021", "22:00")
    rezervari = rezervareService.getAll()
    lista = rezervareService.rez_interval("21:00", "23:00", rezervari)
    assert len(lista) == 1
    assert lista[0].idEntitate == "1"
    assert lista[0].data == "11.12.2021"


def test_rez_stergere_interval():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    clearfile("test-rezervari.json")
    rezervareRepository = RepositoryJson("test-rezervari.json")
    rezervareValidator = RezervareValidator()
    rezervareService = RezervareService(rezervareRepository,
                                        rezervareValidator, filmRepository,
                                        cardRepository)
    rezervareService.adaugare("1", "1", "1", "11.12.2021", "22:00")
    rezervari = rezervareService.getAll()
    lista = rezervareService.rez_stergere_interval("10.11.2019", "13.12.2022",
                                                   rezervari)
    assert len(lista) == 1
    assert lista[0].idEntitate == "1"
    for element in lista:
        rezervareService.stergere(element.idEntitate)
    rezervari_aux = rezervareService.getAll()
    assert len(rezervari_aux) == 0


def test_incrementare():
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    carduri = cardService.getAll()
    cardService.incrementare("23.10.1990", "30.09.2000", 155.3, carduri)
    assert carduri[0].puncteacumulate == 205.3
    cardService.incrementare("23.10.1990", "30.09.2000", 30, carduri)
    assert carduri[0].puncteacumulate == 235.3
    cardService.incrementare("23.10.1990", "30.09.2000", 14.7, carduri)
    assert carduri[0].puncteacumulate == 250


def test_card_ord_descrescator():
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    cardService.adauga("2", "Gherasim", "Gabbriel", "5020930070049",
                       "30.09.2002", "17.04.2019", 120.0)
    rezultat = cardService.card_ord_descrescator()
    assert len(rezultat) == 2
    assert rezultat[0].idEntitate == "2"
    assert rezultat[1].nume == "Mihai"
    assert rezultat[1].puncteacumulate == 50.0


def test_cautare_full_text():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    textinput = "Titanic"
    filme = filmRepository.read()
    carduri = cardRepository.read()
    lfilm_test = filmService.cautare_film(textinput, filme)
    lcard_text = cardService.cautare_card(textinput, carduri)
    assert len(lfilm_test) == 1
    assert lfilm_test[0].pretbiletFilm == 20.0
    assert lfilm_test[0].inprogramFilm == "da"
    assert len(lcard_text) == 0
    textinput = "Mihai"
    lfilm_test = filmService.cautare_film(textinput, filme)
    lcard_text = cardService.cautare_card(textinput, carduri)
    assert len(lcard_text) == 1


def test_afsare_filme_descrescator():
    clearfile("test-filme.json")
    filmRepository = RepositoryJson("test-filme.json")
    filmValidator = FilmValidator()
    filmService = FilmService(filmRepository, filmValidator)

    filmService.adauga(1, "Titanic", "2000", 20.0, "da")
    filmService.adauga(2, "Home alone", "2002", 10.0, "da")
    clearfile("test-carduri.json")
    cardRepository = RepositoryJson("test-carduri.json")
    cardValidator = CardValidator()
    cardService = CardService(cardRepository, cardValidator)
    cardService.adauga("1", "Mihai", "Andrei", "5981126040016", "26.11.1998",
                       "10.06.2020", 50.0)
    clearfile("test-rezervari.json")
    rezervareRepository = RepositoryJson("test-rezervari.json")
    rezervareValidator = RezervareValidator()
    rezervareService = RezervareService(rezervareRepository,
                                        rezervareValidator, filmRepository,
                                        cardRepository)
    rezervareService.adaugare("1", "1", "1", "11.12.2021", "22:00")
    rezervareService.adaugare("2", "2", "1", "11.12.2021", "23:30")
    rezervareService.adaugare("3", "1", "1", "12.12.2021", "22:00")
    filme = filmService.getAll()
    rezervari = rezervareService.getAll()
    lista = rezervareService.afisare_filme_descrescator(filme, rezervari)
    assert len(lista) == 2
