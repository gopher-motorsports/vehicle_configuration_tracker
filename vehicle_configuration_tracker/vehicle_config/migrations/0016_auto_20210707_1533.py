# Generated by Django 3.1.7 on 2021-07-07 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0015_remove_assembly_test'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='setup',
            name='setup_params',
        ),
        migrations.AddField(
            model_name='setup',
            name='setup_params',
            field=models.ManyToManyField(blank=True, to='vehicle_config.SetupParam'),
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='assemblies',
        ),
        migrations.AddField(
            model_name='vehicle',
            name='assemblies',
            field=models.ManyToManyField(blank=True, null=True, to='vehicle_config.Assembly'),
        ),
    ]
