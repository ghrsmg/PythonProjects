from Domain import cardclient
from Domain.CardClientError import CardClientError


class CardValidator:
    def valideaza(self, card: cardclient.CardClient):
        erori = []
        if len(card.CNP) < 13:
            erori.append("CNP-ul trebuie sa aiba 13 cifre!")
        if card.datanastere[2] not in [".", "/"] and \
                card.datanastere[5] not in [".", "/"]:
            erori.append(
                "Introduceti corect data de tipul dd/mm/yyyy sau dd.mm.yyyy")
        if card.datainregistrare[2] not in [".", "/"] and \
                card.datainregistrare[5] not in [".", "/"]:
            erori.append(
                "Introduceti corect data de tipul dd/mm/yyyy sau dd.mm.yyyy")
        if int(card.puncteacumulate) < 0:
            erori.append(
                "Punctele acumulate trebuie sa fie mai "
                "mari sau cel putin egale cu 0")
        if len(erori) > 0:
            raise CardClientError(erori)
