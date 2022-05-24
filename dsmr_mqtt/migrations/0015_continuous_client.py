# Generated by Django 3.0.7 on 2020-07-14 19:47


from django.db import migrations, models


class Migration(migrations.Migration):

    def migrate_forward(apps, schema_editor):
        MQTTBrokerSettings = apps.get_model('dsmr_mqtt', 'MQTTBrokerSettings')

        mqtt_settings, _ = MQTTBrokerSettings.objects.get_or_create()

        if not mqtt_settings.hostname:
            return

        # Enable MQTT for all installations with a hostname set.
        MQTTBrokerSettings.objects.all().update(
            enabled=True
        )

    def migrate_backward(apps, schema_editor):
        pass  # Nothing to do, but allow going backwards.

    dependencies = [
        ('dsmr_mqtt', '0014_mqtt_telegram_defaults'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mqttbrokersettings',
            name='process_sleep',
        ),
        migrations.AddField(
            model_name='mqttbrokersettings',
            name='enabled',
            field=models.BooleanField(default=False, help_text='Whether the MQTT integration is enabled.', verbose_name='Enabled'),
        ),
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
