from django.db import models
from math import sqrt

class PlantModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  description = models.CharField(max_length=200)
  def __str__(self):
    return self.description

class SoilMoistureReadingModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField()
  plant = models.ForeignKey(PlantModel, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value

class TankLevelReadingModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  sensorReading = models.FloatField(default=0)
  def __str__(self):
    return str(self.sensorReading)

  def level(self):
    tankHeight = 33
    tankSliceAreaSlope = 15.7
    tankBaseArea = 1462

    waterDepth = tankHeight - self.sensorReading
    areaAtWaterSurface = (waterDepth * tankSliceAreaSlope) + tankBaseArea
    volume = (waterDepth/3) * (tankBaseArea + areaAtWaterSurface + sqrt(tankBaseArea * areaAtWaterSurface))

    return volume * 1000

class ValveOpenEvent(models.Models):
  created = models.DateTimeField(auto_now_add=True)
  durationSeconds = models.SmallIntegerField()
  tankLevelBefore = models.ForeignKey(TankLevelReadingModel, on_delete=models.SET_NULL, null=True)
  tankLevelAfter = models.ForeignKey(TankLevelReadingModel, on_delete=models.SET_NULL, null=True)