from Service.cardService import CardService
from Service.filmService import FilmService
from Service.rezervareService import RezervareService


class Consola:
    def __init__(self, filmService: FilmService, cardService: CardService,
                 rezervareService: RezervareService):
        self.__filmService = filmService
        self.__cardService = cardService
        self.__rezervareService = rezervareService

    def runMenu(self):
        while True:
            print("1. CRUD film")
            print("2. CRUD card client")
            print("3. CRUD rezervare")
            print("4.Generare random")
            print("5.Cautare full text")
            print("6.Stergere in cascada")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.runCRUDFilmMenu()
            elif optiune == "2":
                self.runCRUDCardClientMenu()
            elif optiune == "3":
                self.runCRUDRezervareMenu()
            elif optiune == "4":
                self.gen_random()
            elif optiune == "5":
                self.uiCautare()
            elif optiune == "6":
                self.uiStergere_in_cascada()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDFilmMenu(self):
        while True:
            print("1.Adauga film")
            print("2.Sterge film")
            print("3.Modifica film")
            print("a.Afiseaza toate filmele")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaFilm()
            elif optiune == "2":
                self.uiStergeFilm()
            elif optiune == "3":
                self.uiModificaFilm()
            elif optiune == "a":
                self.showAllfilm()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def runCRUDCardClientMenu(self):
        while True:
            print("1.Adauga card")
            print("2.Sterge card")
            print("3.Modifica card")
            print("4.Afisare carduri descrescator")
            print("5.Incrementare cu un numar de puncte dat")
            print("a.Afiseaza toate cardurile")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaCard()
            elif optiune == "2":
                self.uiStergeCard()
            elif optiune == "3":
                self.uiModificaCard()
            elif optiune == "4":
                self.uiCard_ord_drescrescator()
            elif optiune == "5":
                self.uiIncrementare()
            elif optiune == "a":
                self.showAllcard()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati:")

    def runCRUDRezervareMenu(self):
        while True:
            print("1.Adauga rezervare")
            print("2.Sterge rezervare")
            print("3.Modifica rezervare")
            print("4.Afisare rezervari interval orar")
            print("5.Stergere rezervari intr-un interval dat")
            print(
                "6.Afișarea filmelor descrescător după numărul de rezervări")
            print("a.Afiseaza toate rezervarile")
            print("x.Iesire")
            optiune = input("Dati optiunea: ")
            if optiune == "1":
                self.uiAdaugaRezervare()
            elif optiune == "2":
                self.uiStergeRezervare()
            elif optiune == "3":
                self.uiModificaRezervare()
            elif optiune == "4":
                self.uiRez_interval()
            elif optiune == "5":
                self.uiRez_stergere_interval()
                self.showAllrezervare()
            elif optiune == "6":
                self.uiOrd_descrescator_dupa_aparitii()
            elif optiune == "a":
                self.showAllrezervare()
            elif optiune == "x":
                break
            else:
                print("Optiune gresita! Reincercati: ")

    def uiAdaugaFilm(self):
        try:
            idFilm = int(input("Dati id-ul filmului: "))
            titluFilm = input("Dati titlul filmului: ")
            anaparitieFilm = input("Dati anul aparitiei filmului: ")
            pretbiletFilm = float(input("Dati pretul biletului: "))
            inprogramFilm = input(
                "Precizati daca filmul este in program(da/nu): ")
            self.__filmService.adauga(idFilm, titluFilm, anaparitieFilm,
                                      pretbiletFilm, inprogramFilm)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeFilm(self):
        try:
            idFilm = input(
                "Dati id-ul filmului pe care vreti sa il stergeti: ")
            self.__filmService.sterge(idFilm)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllfilm(self):
        for film in self.__filmService.getAll():
            print(film)

    def uiModificaFilm(self):
        try:
            idFilm = int(input("Dati id-ul filmului de modificat: "))
            titluFilm = input("Dati noul titlul filmului: ")
            anaparitieFilm = input("Dati noul an al aparitiei filmului: ")
            pretbiletFilm = float(input("Dati noul pret al biletului: "))
            inprogramFilm = input(
                "Precizati daca filmul este in program(da/nu): ")
            self.__filmService.modifica(idFilm, titluFilm, anaparitieFilm,
                                        pretbiletFilm, inprogramFilm)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiAdaugaCard(self):
        try:
            idCard = input("Dati id-ul cardului: ")
            nume = input("Dati numele proprietarului: ")
            prenume = input("Dati prenumele proprietarului: ")
            CNP = input("Dati CNP-ul proprietarului: ")
            datanastere = input("Dati data nasterii proprietarului: ")
            datainregistrare = input("Dati data de inregistrare: ")
            puncteacumulate = float(
                input("Dati numarul de puncte acumulate: "))
            self.__cardService.adauga(idCard, nume, prenume, CNP, datanastere,
                                      datainregistrare, puncteacumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeCard(self):
        try:
            idCard = input(
                "Dati id-ul cardului pe care doriti sa il stergeti: ")
            self.__cardService.stergere(idCard)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaCard(self):
        try:
            idCard = input("Dati id-ul cardului de modificat: ")
            nume = input("Dati noul nume al proprietarului: ")
            prenume = input("Dati noul prenume al proprietarului: ")
            CNP = input("Dati noul CNP al proprietarului: ")
            datanastere = input("Dati noua data de nastere proprietarului: ")
            datainregistrare = input("Dati noua data de inregistrare: ")
            puncteacumulate = float(
                input("Dati noul numar de puncte acumulate: "))
            self.__cardService.modifica(idCard, nume, prenume, CNP,
                                        datanastere, datainregistrare,
                                        puncteacumulate)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiCard_ord_drescrescator(self):
        lista = []
        lista = self.__cardService.card_ord_descrescator()
        for card in lista:
            print(card)

    def showAllcard(self):
        for card in self.__cardService.getAll():
            print(card)

    def uiAdaugaRezervare(self):
        try:
            idRezervare = input("Dati ID-ul rezervarii: ")
            id_film = input(
                "Dati ID-ul filmului pe care doriti sa faceti rezervarea: ")
            id_card_client = input(
                "Dati ID-ul cardului de client (daca nu aveti tastati '0'): ")
            data = input("Dati data rezervarii: ")
            ora = input("Dati ora rezervarii: ")
            var_adaugare = self.__rezervareService.adaugare(idRezervare,
                                                            id_film,
                                                            id_card_client,
                                                            data, ora)
            if var_adaugare is not None:
                print("Numarul total de puncte de pe card este de ",
                      var_adaugare)

        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiStergeRezervare(self):
        try:
            idRezervare = input(
                "Dati id-ul rezervarii pe care doriti sa o stergeti: ")
            self.__rezervareService.stergere(idRezervare)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiModificaRezervare(self):
        try:
            idRezervare = input(
                "Dati ID-ul rezervarii pe care doriti sa o modificati: ")
            id_film = input(
                "Dati noul ID al filmului pe "
                "care doriti sa faceti rezervarea: ")
            id_card_client = input(
                "Dati noul ID al cardului de "
                "client (daca nu aveti tastati '0'): ")
            data = input("Dati noua data a rezervarii: ")
            ora = input("Dati noua ora a rezervarii: ")
            self.__rezervareService.adaugare(idRezervare, id_film,
                                             id_card_client, data, ora)
        except ValueError as ve:
            print(ve)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def showAllrezervare(self):
        for rezervare in self.__rezervareService.getAll():
            print(rezervare)

    def gen_random(self):
        try:
            while True:
                print("1. Genereaza random filme")
                print("2.Genereaza random carduri")
                print("x.Iesire")
                optiune = input("Dati optiunea: ")
                if optiune == "1":
                    n = int(input(
                        "Dati numarul de filme pe care "
                        "doriti sa-l generati: "))
                    self.__filmService.film_random(n)
                    self.showAllfilm()
                elif optiune == "2":
                    n = int(input(
                        "Dati numarul de carduri pe care doriti "
                        "sa-l generati: "))
                    self.__cardService.card_random(n)
                    self.showAllcard()
                elif optiune == "x":
                    break
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiCautare(self):
        try:
            text_input = input("Textul pe care doriti sa il cautati: ")
            filme = self.__filmService.getAll()
            carduri = self.__cardService.getAll()
            lfilm = self.__filmService.cautare_film(text_input, filme)
            lcard = self.__cardService.cautare_card(text_input, carduri)
            for element in lfilm:
                print(element)
            for element in lcard:
                print(element)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiRez_interval(self):
        try:
            orax = input("Dati prima ora a intervalului: ")
            oray = input("Dati a doua ora a intervalului: ")
            rezervari = self.__rezervareService.getAll()
            lista = self.__rezervareService.rez_interval(orax, oray, rezervari)
            for element in lista:
                print(lista)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiRez_stergere_interval(self):
        try:
            ziua1 = input("Dati prima zi a intervalului: ")
            ziua2 = input("Dati a doua zi a intervalului: ")
            rezervari = self.__rezervareService.getAll()
            lista = self.__rezervareService.rez_stergere_interval(ziua1, ziua2,
                                                                  rezervari)
            for rezervare in lista:
                self.__rezervareService.stergere(rezervare.idEntitate)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiIncrementare(self):
        try:
            ziua1 = input("Dati prima zi a intervalului: ")
            ziua2 = input("Dati a doua zi a intervalului: ")
            n = float(
                input(
                    "Dati numarul de puncte pe care doriti sa il adaugati: "))
            carduri = self.__cardService.getAll()
            self.__cardService.incrementare(ziua1, ziua2, n, carduri)
            carduri = self.__cardService.getAll()
            for card in carduri:
                print(card)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)

    def uiOrd_descrescator_dupa_aparitii(self):
        filme = self.__filmService.getAll()
        rez = self.__filmService.getAll()
        rezultat = self.__rezervareService.afisare_filme_descrescator(filme,
                                                                      rez)
        for element in rezultat:
            print(element)

    def uiStergere_in_cascada(self):
        try:
            id_f = input("Dati id-ul filmului: ")
            self.__rezervareService.stergere_in_cascada(id_f)
        except KeyError as ke:
            print(ke)
        except Exception as e:
            print(e)
