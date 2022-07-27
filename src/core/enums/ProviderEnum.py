from enum import Enum


class Color(Enum):
    RED = "RED"
    BLUE = "BLUE"
    GREEN = "GREEN"
    WHITE = "WHITE"
    BLACK = "BLACK"
    SILVER = "SILVER"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
