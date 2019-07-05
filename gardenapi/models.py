from django.db import models

class PlantModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  description = models.CharField(max_length=200)
  def __str__(self):
    return self.description

class SoilMoistureReadingModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  plant = models.ForeignKey(PlantModel, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value

class MoistureProbeEventModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  reading = models.ForeignKey(SoilMoistureReadingModel, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value

class TankLevelReadingModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  level = models.FloatField
  def __str__(self):
    return self.value

class TankUltraSonicSensorEventModel(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  reading = models.ForeignKey(TankLevelReadingModel, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value