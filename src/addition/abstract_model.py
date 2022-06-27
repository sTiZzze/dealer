from django.db import models


class UpdatedAt(models.Model):
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Delete(models.Model):
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True



