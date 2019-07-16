from django.core.management.base import BaseCommand
from ...models import SoilMoistureReadingModel, PlantModel
from ..microcontroller import MicroController
from ..arduino_commands import READ_MOISTURE_1, READ_MOISTURE_2, READ_MOISTURE_3, READ_MOISTURE_4

class Command(BaseCommand):
    def handle(self, **options):
      m = MicroController()
      commands = [READ_MOISTURE_1, READ_MOISTURE_2, READ_MOISTURE_3, READ_MOISTURE_4]
      for command in commands:
        moisture = m.sensorRead(command)
        r = SoilMoistureReadingModel.objects.create(value=moisture)
        p = PlantModel.objects.get(id=int(command))
        p.soilmoisturereadingmodel_set.add(r)