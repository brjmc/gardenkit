# Generated by Django 2.2.3 on 2019-07-02 02:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Plant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='TankLevelReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TankUltraSonicSensorEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gardenapi.TankLevelReading')),
            ],
        ),
        migrations.CreateModel(
            name='SoilMoistureReading',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('plant', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gardenapi.Plant')),
            ],
        ),
        migrations.CreateModel(
            name='MoistureProbeEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('reading', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='gardenapi.SoilMoistureReading')),
            ],
        ),
    ]
