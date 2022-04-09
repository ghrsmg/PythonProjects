import jsonpickle
from typing import Dict, Union, Optional, List, Type

from Domain.entity import Entity
from Repository.repository import Repository


class JsonRepository(Repository):
    """
    Repository cu fisiere Json
    """

    def __init__(self, filename):
        self.filename = filename

    def __read_file(self):
        """
        Metoda de citire a fisierelor
        :return:
        """
        try:
            with open(self.filename, 'r') as f:
                return jsonpickle.loads(f.read())
        except Exception:
            return {}

    def __write_file(self, objects: Dict[str, Entity]):
        """
        Metoda de scriere in fisier
        :param objects: obiecte
        :return:
        """
        with open(self.filename, 'w') as f:
            f.write(jsonpickle.dumps(objects))

    def create(self, entity: Entity) -> None:
        """
        Metoda de a adauga o entitate
        :param entity:
        :return:
        """

        entities = self.__read_file()
        if self.read(entity.id_entity) is not None:
            raise KeyError(f'Exista deja o '
                           f'entitate cu id-ul {entity.id_entity}.')

        entities[entity.id_entity] = entity
        self.__write_file(entities)

    def read(self, id_entity: object = None) \
            -> Type[Union[Optional[Entity], List[Entity]]]:
        """
        Metoda ce indica entitati
        :param id_entity: id entitate
        :return: toate enttitatile daca nu este specificat un id anume;
        entitatea cu id-ul dat sau None, daca nu exista
        """

        entities = self.__read_file()
        if id_entity:
            if id_entity in entities:
                return entities[id_entity]
            else:
                return None

        return list(entities.values())

    def update(self, entity: Entity) -> None:
        """
        Metoda ce modifica o entitate
        :param entity: o entitate
        :return:
        """
        entities = self.__read_file()
        if self.read(entity.id_entity) is None:
            msg = f'Nu exista o entitate cu id-ul ' \
                  f'{entity.id_entity} de actualizat.'
            raise KeyError(msg)

        entities[entity.id_entity] = entity
        self.__write_file(entities)

    def delete(self, id_entity: str) -> None:
        """
        Metoda de stergere a entitatii
        :param id_entity: id-ul entitatii
        :return:
        """
        entities = self.__read_file()
        if self.read(id_entity) is None:
            raise KeyError(
                f'Nu exista o entitate cu id-ul '
                f'{id_entity} pe care sa o stergem.')

        del entities[id_entity]
        self.__write_file(entities)
