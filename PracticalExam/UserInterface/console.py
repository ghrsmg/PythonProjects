from Service.artist_service import ArtistService
from Service.concert_service import ConcertService


class Console:
    def __init__(self, artist_service: ArtistService, concert_service: ConcertService):
        self.artist_service = artist_service
        self.concert_service = concert_service

    def run_menu(self):
        while True:
            print("1.Adauga artist")
            print("2.Adauga concert")
            print("3.Afisare artisti descrescator dupa tarif")
            print("4.Numarul concertelor per categorie")
            print("5.Export json")
            print("a2.Afisare concerte")
            print("a1. Afisare artisti")
            print("x.Iesire")

            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.ui_adauga_artist()
            if optiune == "2":
                self.ui_adauga_concert()
            if optiune == "3":
                self.ui_afisare(self.artist_service.afisare_artisti_descrescator())
            elif optiune == "4":
                self.ui_afisare(self.concert_service.nr_concerte_categore())
            elif optiune == "5":
                self.ui_export_json()
            elif optiune == "a1":
                self.ui_afisare(self.artist_service.getAll())
            elif optiune == "a2":
                self.ui_afisare(self.concert_service.getAll())

            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def ui_afisare(self, entitati):
        for entitate in entitati:
            print(entitate)

    def ui_adauga_artist(self):
        try:
            id_artist = input("Dati id-ul artistului: ")
            nume = input("Dati numele artistului: ")
            categorie = input("Dati categoria artistului: ")
            tarif = float(input("Dati tariful artistului: "))
            self.artist_service.adauga(id_artist, nume, categorie, tarif)
        except Exception as e:
            print(e)

    def ui_adauga_concert(self):
        try:
            id_concert = input("Dati id-ul concertului: ")
            nume = input("Dati numele concertului: ")
            locatie = input("Dati locatia concertului: ")
            capacitate = int(input("Dati capacitatea concertului: "))
            id_artist = input("Dati id-ul artistului: ")
            self.concert_service.adauga(id_concert, nume, locatie, capacitate, id_artist)
        except Exception as e:
            print(e)

    def ui_export_json(self):
        try:
            filename = input("Dati numele fisierului in care sa se faca exportul")
            self.concert_service.export_json(filename)
        except Exception as e:
            print(e)
