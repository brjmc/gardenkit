from django.core.management.base import BaseCommand
from ...models import SoilMoistureReadingModel
from ..microcontroller import MicroController
from ..arduino_commands import READ_MOISTURE_1, READ_MOISTURE_2

class Command(BaseCommand):
    def handle(self, **options):
      m = MicroController()
      commands = [READ_MOISTURE_1, READ_MOISTURE_2]
      for command in commands:
        moisture = m.sensorRead(command)
        print(moisture)