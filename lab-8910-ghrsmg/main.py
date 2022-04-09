import Domain.FilmValidator
import Domain.CardValidator
import Domain.RezervareValidator
from Repository.repositoryJson import RepositoryJson
from Service.filmService import FilmService
from Service.cardService import CardService
from Service.rezervareService import RezervareService
from Tests.tests import runAllTests
from UI.consola import Consola


def main():
    runAllTests()
    filmRepositoryJson = RepositoryJson("filme.json")
    cardRepositoryJson = RepositoryJson("carduri.json")
    rezervareRepositoryJson = RepositoryJson("rezervari.json")
    filmValidator = Domain.FilmValidator.FilmValidator()
    cardValidator = Domain.CardValidator.CardValidator()
    rezervareValidator = Domain.RezervareValidator.RezervareValidator()
    filmService = FilmService(filmRepositoryJson, filmValidator)
    cardService = CardService(cardRepositoryJson, cardValidator)
    rezervareService = RezervareService(rezervareRepositoryJson,
                                        rezervareValidator, filmRepositoryJson,
                                        cardRepositoryJson)
    consola = Consola(filmService, cardService, rezervareService)
    consola.runMenu()


main()
