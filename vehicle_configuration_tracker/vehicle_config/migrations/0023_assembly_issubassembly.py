# Generated by Django 3.1.7 on 2021-08-15 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0022_auto_20210803_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='assembly',
            name='isSubassembly',
            field=models.BooleanField(default=True),
            preserve_default=False,
        ),
    ]
