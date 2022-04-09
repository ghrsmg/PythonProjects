from Domain.FilmValidator import FilmValidator
from Domain.film import Film
from random import choice, randint

from Repository.repository import Repository


class FilmService:
    def __init__(self, filmRepository: Repository,
                 filmValidator: FilmValidator):
        self.__filmValidator = filmValidator
        self.__filmRepository = filmRepository

    def getAll(self):
        return self.__filmRepository.read()

    def adauga(self, idFilm, titluFilm, anaparitieFilm, pretbiletFilm,
               inprogramFilm):
        film = Film(idFilm, titluFilm, anaparitieFilm, pretbiletFilm,
                    inprogramFilm)
        self.__filmValidator.valideaza(film)
        self.__filmRepository.adauga(film)

    def sterge(self, idFilm):
        self.__filmRepository.sterge(idFilm)

    def modifica(self, idFilm, titluFilm, anaparitieFilm, pretbiletFilm,
                 inprogramFilm):
        film = Film(idFilm, titluFilm, anaparitieFilm, pretbiletFilm,
                    inprogramFilm)
        self.__filmValidator.valideaza(film)
        self.__filmRepository.modifica(film)

    def film_random(self, n: int):
        nr_filme = 0
        while True:
            idFilm = str(randint(1, 1000))
            titluri = ["Army of dead", "Red Notice", "The Do Over",
                       "Ride Along 2 ", "Spoiled Brats", "Titanic",
                       "Murder Mystery", "White Chicks", "Just Go With It",
                       "Journey 2", "A Boy Called Christmas",
                       "Sonic The Hedhehog", "Klaus", "Shrek", "IT",
                       "Bird Box"]
            titlu = choice(titluri)
            anaparitie = str(randint(1990, 2021))
            pretbilet = float(randint(10, 40))
            inprogram = ["da", "nu"]
            InProgram = choice(inprogram)
            film = Film(idFilm, titlu, anaparitie, pretbilet, InProgram)
            if self.__filmRepository.read(idFilm) is None:
                nr_filme += 1
                self.__filmRepository.adauga(film)
            if nr_filme == n:
                break

    def cautare_film(self, text_input: str, filme):
        lista_film = []
        for film in filme:
            while True:
                text = str(film.idEntitate)
                if text_input in text:
                    lista_film.append(film)
                    break
                text = str(film.titluFilm)
                if text_input in text:
                    lista_film.append(film)
                    break
                text = str(film.anaparitieFilm)
                if text_input in text:
                    lista_film.append(film)
                    break
                text = str(film.pretbiletFilm)
                if text_input in text:
                    lista_film.append(film)
                    break
                break
        return lista_film
