from Domain import film
from Domain.FilmError import FilmError


class FilmValidator:
    def valideaza(self, film: film.Film):
        erori = []
        if int(film.pretbiletFilm) < 0:
            erori.append("Pretul biletului trebuie "
                         "sa fie pozitiv")
        if film.inprogramFilm not in ["da", "nu"]:
            erori.append("In campul 'in program' se "
                         "poate completa doar cu 'da' sau 'nu")
        if int(film.anaparitieFilm) < 1900:
            erori.append("Anul aparitiei filmului trebuie"
                         " sa fie mai mare de 1900")
        if len(erori) > 0:
            raise FilmError(erori)
