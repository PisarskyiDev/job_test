from django.core.management.base import BaseCommand

from main import models


class Command(BaseCommand):
    help = "Displays all SomeModel objects"

    def handle(self, *args, **kwargs):
        data = models.SomeModel.objects.all()
        for obj in data:
            self.stdout.write(f"{obj.pk} - {obj.some_name} - {obj.some_value}")
