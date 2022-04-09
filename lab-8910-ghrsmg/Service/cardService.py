from random import randint, choice

from Domain.CardValidator import CardValidator
from Domain.cardclient import CardClient
from Repository.repository import Repository


class CardService:
    def __init__(self, cardRepository: Repository,
                 cardValidator: CardValidator):
        self.__cardValidator = cardValidator
        self.__cardRepository = cardRepository

    def getAll(self):
        return self.__cardRepository.read()

    def adauga(self, idCard, nume, prenume, CNP, datanastere, datainregistrare,
               puncteacumulate):
        card = CardClient(idCard, nume, prenume, CNP, datanastere,
                          datainregistrare, puncteacumulate)
        self.__cardValidator.valideaza(card)
        self.__cardRepository.adauga(card)

    def stergere(self, idCard):
        self.__cardRepository.sterge(idCard)

    def modifica(self, idCard, nume, prenume, CNP, datanastere,
                 datainregistrare, puncteacumulate):
        card = CardClient(idCard, nume, prenume, CNP, datanastere,
                          datainregistrare, puncteacumulate)
        self.__cardValidator.valideaza(card)
        self.__cardRepository.modifica(card)

    def card_random(self, n: int):
        nr_carduri = 0
        while True:
            idCard = str(randint(1, 1000))
            Nume = ["Albulescu", "Bazon", "Cantemir", "Dumitrescu", "Golescu",
                    "Popa", "Cazacu", "Alexe", "Mihalcea",
                    "Dumbrava", "Chirica", "Negru", "Dogaru"]
            nume = choice(Nume)
            Prenume = ["Ada", "Beatrice", "Carol", "Dan", "Elena", "Fabiana",
                       "Gabriel", "Ioan", "Lorena", "Jana",
                       "Marian"]
            prenume = choice(Prenume)
            CNP = str(
                randint(1, 9) * 1000000000000 + randint(0,
                                                        9) * 1000000000000 +
                randint(0, 9) * 100000000000 +
                randint(0, 9) * 10000000000 +
                randint(0, 9) * 1000000000 + randint(
                    0, 9) * 100000000 +
                randint(0, 9) * 10000000 + randint(0, 9) * 1000000
                + randint(0, 9) * 100000 + randint(
                    0, 9) * 10000 +
                randint(0, 9) * 1000 + randint(0, 9) * 100 + randint(0, 9)
                * 10 + randint(
                    0, 9))
            DataNastere = ["01.01.2001", "02.10.2002", "08.06.1994",
                           "03.02.2000", "13.04.1999", "30.09.2002",
                           "12.12.2004", "07.07.2004", "07.01.2003",
                           "28.02.2003"]
            datanastere = choice(DataNastere)
            DataInregistrare = ["01.01.2010", "02.10.2017", "08.06.2020",
                                "03.02.2008", "13.04.2013", "30.09.2015",
                                "12.12.2014", "07.07.2018", "07.01.2009",
                                "28.02.20011"]
            datainregistrare = choice(DataInregistrare)
            puncteacumulate = float(randint(0, 1000))
            card = CardClient(idCard, nume, prenume, CNP, datanastere,
                              datainregistrare, puncteacumulate)
            if self.__cardRepository.read(idCard) is None:
                nr_carduri += 1
                self.__cardRepository.adauga(card)
            if nr_carduri == n:
                break

    def card_ord_descrescator(self):
        rezultat = []
        for card in self.__cardRepository.read():
            rezultat.append(card)
        rezultat = sorted(rezultat, key=lambda x: x.puncteacumulate,
                          reverse=True)
        return rezultat

    def cautare_card(self, text_input: str, carduri):
        lista_card = []
        for card in carduri:
            while True:
                text = str(card.idEntitate)
                if text_input in text:
                    lista_card.append(card)
                    break
                text = str(card.nume)
                if text_input in text:
                    lista_card.append(card)
                    break
                text = str(card.prenume)
                if text_input in text:
                    lista_card.append(card)
                    break
                text = str(card.CNP)
                if text_input in text:
                    lista_card.append(card)
                    break
                text = str(card.datanastere)
                if text_input in text:
                    lista_card.append(card)
                    break
                text = str(card.datainregistrare)
                if text_input in text:
                    lista_card.append(card)
                    break
                break
        return lista_card

    def incrementare(self, data1: str, data2: str, n: float, carduri):
        if data1[2] not in ["."]:
            raise KeyError("Introduceti o data valida!")
        if data2[2] not in ["."]:
            raise KeyError("Introduceti o data valida!")
        if data1[5] not in ["."]:
            raise KeyError("Introduceti o data valida!")
        if data2[5] not in ["."]:
            raise KeyError("Introduceti o data valida!")
        if len(data1) > 10:
            raise KeyError("Introduceti o data valida!")
        if len(data2) > 10:
            raise KeyError("Introduceti o data valida!")
        ziua1int = int(data1[0]) * 10 + int(data1[1])
        ziua2int = int(data2[0]) * 10 + int(data2[1])
        luna1int = int(data1[3]) * 10 + int(data1[4])
        luna2int = int(data2[3]) * 10 + int(data2[4])
        anul1int = int(data1[6]) * 1000 + int(data1[7]) * 100 + int(
            data1[8]) * 10 + int(data1[9])
        anul2int = int(data2[6]) * 1000 + int(data2[7]) * 100 + int(
            data2[8]) * 10 + int(data2[9])

        if anul1int > anul2int:
            raise KeyError("Intervalul orar nu este valid!")
        if anul1int == anul2int:
            if luna1int > luna2int:
                raise KeyError("Intervalul orar nu este valid!")
        if anul1int == anul2int:
            if luna1int == luna2int:
                if ziua1int > ziua2int:
                    raise KeyError("Intervalul orar nu este valid!")

        for card in carduri:
            ziua_nasterii = int(card.datanastere[0]) * 10 + int(
                card.datanastere[1])
            luna_nasterii = int(card.datanastere[3]) * 10 + int(
                card.datanastere[4])
            anul_nasterii = int(card.datanastere[6]) * 1000 + int(
                card.datanastere[7]) * 100 + int(
                card.datanastere[8]) * 10 + int(
                card.datanastere[9])
            if anul_nasterii > anul1int and anul2int > anul_nasterii:
                card.puncteacumulate = card.puncteacumulate + n
                self.modifica(card.idEntitate, card.nume, card.prenume,
                              card.CNP, card.datanastere,
                              card.datainregistrare,
                              card.puncteacumulate)
            if anul1int == anul2int and anul2int == anul_nasterii:
                if luna_nasterii > luna1int and luna2int > luna_nasterii:
                    card.puncteacumulate = card.puncteacumulate + n
                    self.modifica(card.idEntitate, card.nume, card.prenume,
                                  card.CNP, card.datanastere,
                                  card.datainregistrare,
                                  card.puncteacumulate)
            if anul1int == anul2int and anul2int == anul_nasterii:
                if luna1int == luna2int and luna1int == luna_nasterii:
                    if ziua_nasterii >= ziua1int:
                        if ziua2int >= ziua_nasterii:
                            card.puncteacumulate = card.puncteacumulate + n
                            self.modifica(card.idEntitate, card.nume,
                                          card.prenume,
                                          card.CNP, card.datanastere,
                                          card.datainregistrare,
                                          card.puncteacumulate)
