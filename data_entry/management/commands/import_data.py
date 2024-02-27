from django.core.management.base import BaseCommand, CommandError
from django.apps import apps
import csv



class Command(BaseCommand):
    help = 'Use To Import CSV Dataset.'


    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='Path To The CSV File.')
        parser.add_argument('model_name', type=str, help='Name Of The Model To Import Data To.')
        

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        model_name = kwargs['model_name'].capitalize()


        # Search for the model across all installed apps
        model = None
        for app_config in apps.get_app_configs():
            # try to search for the model
            try:
                model = apps.get_model(app_label=app_config.label, model_name=model_name)
                break
            except LookupError:
                continue


        if not model:
            raise CommandError(f'Model "{model_name}" Not Found In Any App!')

        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                model.objects.create(**row)

        self.stdout.write(self.style.SUCCESS('Data Imported From CSV Successfully'))

        