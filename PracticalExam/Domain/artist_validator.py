from Domain.artist import Artist


class ArtistValidator:
    def valideaza(self, artist: Artist):
        erori = []
        if artist.nume == "":
            erori.append("Numele trebuie sa fie un string nenul!")
        if len(erori):
            raise ValueError(erori)
