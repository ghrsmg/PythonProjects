from Domain import rezervare
from Domain.RezervareError import RezervareError


class RezervareValidator:
    def valideaza(self, rezervare: rezervare.Rezervare):
        erori = []
        if int(rezervare.idEntitate) < 1:
            erori.append("ID-ul rezervarii trebuie sa fie valid!")
        if int(rezervare.id_film) < 1:
            erori.append("ID-ul filmului trebuie sa fie valid! ")
        if rezervare.data[2] not in [".", "/"] and rezervare.data[5] \
                not in [".", "/"]:
            erori.append("Introduceti corect data de"
                         " tipul dd/mm/yyyy sau dd.mm.yyyy")
        if rezervare.ora[2] not in [":"]:
            erori.append("Introduceti o ora valida!")
        if len(erori) > 0:
            raise RezervareError(erori)
