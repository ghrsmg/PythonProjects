from dataclasses import dataclass


@dataclass
class CardClientError(Exception):
    mesaj: str

    def __str__(self):
        return f'CardClientError:{self.mesaj}'
