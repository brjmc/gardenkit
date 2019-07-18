from django.core.management.base import BaseCommand
from django.core.management import call_command


class Command(BaseCommand):
    def handle(self, **options):
      call_command('read_tank', verbosity=0)
      call_command('read_moisture', verbosity=0)
