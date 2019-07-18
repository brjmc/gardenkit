from django.core.management.base import BaseCommand
from ...models import TankLevelReadingModel
from django.utils import timezone
import pytz

class Command(BaseCommand):
    def handle(self, **options):
      items = TankLevelReadingModel.objects.all()
      return items