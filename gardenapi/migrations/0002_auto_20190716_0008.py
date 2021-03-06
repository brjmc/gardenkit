# Generated by Django 2.2.3 on 2019-07-16 00:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gardenapi', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Plant',
            new_name='PlantModel',
        ),
        migrations.RenameModel(
            old_name='TankUltraSonicSensorEvent',
            new_name='SoilMoistureReadingModel',
        ),
        migrations.RenameModel(
            old_name='TankLevelReading',
            new_name='TankLevelReadingModel',
        ),
        migrations.RemoveField(
            model_name='soilmoisturereading',
            name='plant',
        ),
        migrations.RemoveField(
            model_name='soilmoisturereadingmodel',
            name='reading',
        ),
        migrations.AddField(
            model_name='soilmoisturereadingmodel',
            name='plant',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gardenapi.PlantModel'),
        ),
        migrations.DeleteModel(
            name='MoistureProbeEvent',
        ),
        migrations.DeleteModel(
            name='SoilMoistureReading',
        ),
    ]
