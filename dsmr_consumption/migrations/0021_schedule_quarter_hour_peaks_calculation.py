# Generated by Django 3.2.12 on 2022-05-04 18:41

from django.db import migrations
from django.conf import settings


def migrate_forward(apps, schema_editor):
    ScheduledProcess = apps.get_model('dsmr_backend', 'ScheduledProcess')
    ScheduledProcess.objects.create(
        name='Calculate quarter hour electricity peaks',
        module=settings.DSMRREADER_MODULE_CALCULATE_QUARTER_HOUR_PEAKS,
    )


def migrate_backward(apps, schema_editor):
    ScheduledProcess = apps.get_model('dsmr_backend', 'ScheduledProcess')
    ScheduledProcess.objects.filter(module=settings.DSMRREADER_MODULE_CALCULATE_QUARTER_HOUR_PEAKS).delete()


class Migration(migrations.Migration):

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ('dsmr_consumption', '0020_quarter_hour_peaks'),
    ]
