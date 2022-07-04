from enum import Enum

from django.db.models import TextChoices


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
