from Domain.RezervareValidator import RezervareValidator
from Domain.rezervare import Rezervare
from Repository.repository import Repository


class RezervareService:
    def __init__(self, rezervareRepository: Repository,
                 rezervareValidator: RezervareValidator,
                 film_repository: Repository,
                 card_repository: Repository):
        self.__rezervareValidator = rezervareValidator
        self.__rezervareRepository = rezervareRepository
        self.__film_repository = film_repository
        self.__card_repository = card_repository

    def getAll(self):
        return self.__rezervareRepository.read()

    def adaugare(self, idRezervare, id_film, id_card_client, data, ora):

        rezervare = Rezervare(idRezervare, id_film, id_card_client, data, ora)
        film = self.__film_repository.read(id_film)
        card = self.__card_repository.read(id_card_client)
        if film is not None:
            if film.inprogramFilm == "da":
                self.__rezervareValidator.valideaza(rezervare)
                self.__rezervareRepository.adauga(rezervare)
                if card is not None:
                    puncte = 1 / 10 * film.pretbiletFilm
                    card.puncteacumulate += puncte
                    total = card.puncteacumulate
                    self.__card_repository.modifica(card)
                    return total

            else:
                raise KeyError("Filmul nu este in program!")
        else:
            raise KeyError("Nu exista un film cu id-ul dat")

    def stergere(self, idRezervare):
        self.__rezervareRepository.sterge(idRezervare)

    def modifica(self, idRezervare, id_film, id_card_client, data, ora):
        rezervare = Rezervare(idRezervare, id_film, id_card_client, data, ora)
        self.__rezervareValidator.valideaza(rezervare)
        self.__rezervareRepository.modifica(rezervare)

    def rez_interval(self, ora_x: str, ora_y: str, rezervari):
        lista = []
        if ora_x[2] not in [":"]:
            raise KeyError("Introduceti o ora valida!")
        if ora_x[2] not in [":"]:
            raise KeyError("Introduceti o ora valida!")
        if len(ora_x) > 5:
            raise KeyError("Introduceti o ora valida!")
        if len(ora_y) > 5:
            raise KeyError("Introduceti o ora valida!")
        oraxint = int(ora_x[0]) * 10 + int(ora_x[1])
        orayint = int(ora_y[0]) * 10 + int(ora_y[1])
        if oraxint > orayint:
            raise KeyError("Intervalul orar nu este valid!")

        for rezervare in rezervari:
            ora = int(rezervare.ora[0]) * 10 + int(rezervare.ora[1])
            if ora >= oraxint and ora <= orayint:
                lista.append(rezervare)
        return lista

    def rez_stergere_interval(self, data1: str, data2: str, rezervari):
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
        lista = []
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

        for rezervare in rezervari:
            ziua_rezervarii = int(rezervare.data[0]) * 10 + int(
                rezervare.data[1])
            luna_rezervarii = int(rezervare.data[3]) * 10 + int(
                rezervare.data[4])
            anul_rezervarii = int(rezervare.data[6]) * 1000 + int(
                rezervare.data[7]) * 100 + int(
                rezervare.data[8]) * 10 + int(rezervare.data[9])
            if anul_rezervarii > anul1int and anul2int > anul_rezervarii:
                lista.append(rezervare)
            if anul1int == anul2int and anul2int == anul_rezervarii:
                if luna_rezervarii > luna1int and luna2int > luna_rezervarii:
                    lista.append(rezervare)
            if anul1int == anul2int and anul2int == anul_rezervarii:
                if luna1int == luna2int and luna1int == luna_rezervarii:
                    if ziua_rezervarii >= ziua1int:
                        if ziua2int >= ziua_rezervarii:
                            lista.append(rezervare)

        return lista

    def afisare_filme_descrescator(self, filme, rezervari):
        rezultat = []
        index_film = []

        filme = self.__film_repository.read()
        rezervari = self.__rezervareRepository.read()

        for film in filme:
            index_film.append(film.idEntitate)

        nr_rezervari = [0] * len(index_film)

        for i in range(len(index_film)):
            for rezervare in rezervari:
                if rezervare.id_film == index_film[i]:
                    nr_rezervari[int(i)] += 1

        for i in range(len(nr_rezervari)):
            rezultat.append({
                "film": self.__film_repository.read(index_film[i]),
                "numar aparitii": nr_rezervari[i]

            })
        return sorted(rezultat, key=lambda x: x["numar aparitii"],
                      reverse=True)

    def stergere_in_cascada(self, id_f: str):
        self.__film_repository.sterge(id_f)
        for rezervare in self.__rezervareRepository.read():
            if rezervare.id_film == id_f:
                self.__rezervareRepository.sterge(rezervare.idEntitate)
