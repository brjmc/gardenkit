from .tankservice import TankService
from datetime import datetime, timedelta

s = TankService()
s.createNewReading()
range = s.getReadingsInRange(dateRange=[datetime.now() - timedelta(hours = 1), datetime.now()])
print(range)