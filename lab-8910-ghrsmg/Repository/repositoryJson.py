import jsonpickle

from Domain.entitate import Entitate
from Repository.repositoryInMemory import RepositoryInMemory


class RepositoryJson(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename

    def __readFile(self):
        try:
            with open(self.filename, "r") as r:
                return jsonpickle.loads(r.read())
        except Exception:
            return {}

    def __writeFile(self):
        with open(self.filename, "w") as r:
            r.write(jsonpickle.dumps(self.entitati, indent=2))

    def read(self, idEntitati=None):
        self.entitati = self.__readFile()
        return super().read(idEntitati)

    def adauga(self, entitate: Entitate):
        self.entitati = self.__readFile()
        super().adauga(entitate)
        self.__writeFile()

    def sterge(self, idEntitate):
        self.entitati = self.__readFile()
        super().sterge(idEntitate)
        self.__writeFile()

    def modifica(self, entitate: Entitate):
        self.entitati = self.__readFile()
        super().modifica(entitate)
        self.__writeFile()
