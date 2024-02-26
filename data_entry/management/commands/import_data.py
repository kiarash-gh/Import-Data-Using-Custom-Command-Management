from django.core.management.base import BaseCommand
from data_entry.models import Student


class Command(BaseCommand):
    help = 'used to import data'

    def handle(self, *args, **kwargs):
        Student.objects.create(roll_no = '1001', name = 'kiarash', age = 36)
        self.stdout.write(self.style.SUCCESS('Data Imported Successfuly.'))