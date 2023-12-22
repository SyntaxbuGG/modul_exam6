import csv
from pathlib import Path

from django.core.management.base import BaseCommand, CommandError

from quizapp.models import UserList


# BASE_DIR = str(Path(__file__).resolve().parent.parent.parent.parent)+'/import_files/'
BASE_DIR = Path(__file__).resolve().parent.parent


class Command(BaseCommand):
    help = 'Add a to user'

    def add_arguments(self, parser):
        parser.add_argument('filename', nargs='+', type=str)

    def handle(self, *args, **options):
        with open('import_files/users.csv') as file:
            content = file.readlines()
            for user in content:
                UserList.objects.create(name=user)

        self.stdout.write(
            self.style.SUCCESS('Successfully')
        )




