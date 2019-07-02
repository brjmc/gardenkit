from django.db import models

class Plant(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  modified = models.DateTimeField(auto_now=True)
  description = models.CharField(max_length=200)
  def __str__(self):
    return self.description

class SoilMoistureReading(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  plant = models.ForeignKey(Plant, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value

class MoistureProbeEvent(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  reading = models.ForeignKey(SoilMoistureReading, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value

class TankLevelReading(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  level = models.FloatField
  def __str__(self):
    return self.value

class TankUltraSonicSensorEvent(models.Model):
  created = models.DateTimeField(auto_now_add=True)
  value = models.FloatField
  reading = models.ForeignKey(TankLevelReading, on_delete=models.SET_NULL, null=True)
  def __str__(self):
    return self.value