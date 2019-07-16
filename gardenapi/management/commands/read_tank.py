from django.core.management.base import BaseCommand
from ...models import TankLevelReadingModel
from ..microcontroller import MicroController
from ..arduino_commands import READ_TANK

class Command(BaseCommand):
    def handle(self, **options):
      m = MicroController()
      waterHeight = m.sensorRead(READ_TANK)
      print(waterHeight)
      result = TankLevelReadingModel.objects.create(sensorReading=waterHeight)