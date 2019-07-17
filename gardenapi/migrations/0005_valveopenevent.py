# Generated by Django 2.2.3 on 2019-07-17 02:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gardenapi', '0004_auto_20190716_2010'),
    ]

    operations = [
        migrations.CreateModel(
            name='ValveOpenEvent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('durationSeconds', models.SmallIntegerField()),
                ('tankLevelAfter', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='gardenapi.TankLevelReadingModel')),
                ('tankLevelBefore', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='gardenapi.TankLevelReadingModel')),
            ],
        ),
    ]
