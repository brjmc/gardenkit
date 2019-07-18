from django.core.management.base import BaseCommand
from django.core.management import call_command
from ...models import TankLevelReadingModel, ValveOpenEvent
from ..arduino_commands import OPEN_VALVE_30s, OPEN_VALVE_5s
from ..microcontroller import MicroController
import time

class Command(BaseCommand):
    def handle(self, **options):
      level_before = TankLevelReadingModel.objects.last()
      m = MicroController()
      result = m.execute_command(OPEN_VALVE_5s)
      print(str(result))
      time.sleep(30)
      call_command('read_tank', verbosity=0)
      level_after = TankLevelReadingModel.objects.last()
      delta = level_before.level() - level_after.level()
      print('DELTA: {}'.format(delta))
      v = ValveOpenEvent.objects.create(
        tankLevelBefore=level_before,
        tankLevelAfter=level_after,
        durationSeconds=30
        )