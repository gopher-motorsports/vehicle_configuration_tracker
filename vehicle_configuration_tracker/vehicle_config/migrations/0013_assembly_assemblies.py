# Generated by Django 3.1.7 on 2021-06-07 01:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0012_auto_20210605_1751'),
    ]

    operations = [
        migrations.AddField(
            model_name='assembly',
            name='assemblies',
            field=models.ManyToManyField(blank=True, to='vehicle_config.Assembly'),
        ),
    ]
