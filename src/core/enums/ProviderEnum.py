from django.db.models import TextChoices


class Color(TextChoices):
    RED = "RED",
    BLUE = "BLUE",
    GREEN = "GREEN",
    WHITE = "WHITE",
    BLACK = "BLACK",
    SILVER = "SILVER"
