# Generated by Django 3.1.7 on 2021-03-28 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0003_auto_20210327_2239'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='setup_params',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
