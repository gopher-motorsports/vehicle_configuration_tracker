# Generated by Django 3.1.7 on 2021-07-08 23:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0019_assembly_deleted'),
    ]

    operations = [
        migrations.AddField(
            model_name='setup',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='setupparam',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='deleted',
            field=models.DateTimeField(editable=False, null=True),
        ),
    ]
