from Domain.concert import Concert


class ConcertValidator:
    def valideaza(self, concert: Concert):
        erori = []
        if concert.nume is "":
            erori.append("Numele trebuie sa fie un string nenul")
        if len(erori):
            raise ValueError(erori)
