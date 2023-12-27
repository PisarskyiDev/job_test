from django.db import models


class SomeModel(models.Model):
    some_name = models.CharField(max_length=255)
    some_value = models.IntegerField()

    def __str__(self):
        return f"{self.some_name}"
