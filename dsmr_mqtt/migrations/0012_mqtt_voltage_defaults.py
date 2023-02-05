# Generated by Django 2.2.6 on 2019-10-14 19:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_mqtt", "0011_mqtt_meta_description"),
    ]

    operations = [
        migrations.AlterField(
            model_name="jsontelegrammqttsettings",
            name="formatting",
            field=models.TextField(
                default="\n[mapping]\n# READING FIELD = JSON FIELD\nid = id\ntimestamp = timestamp\nelectricity_delivered_1 = electricity_delivered_1\nelectricity_returned_1 = electricity_returned_1\nelectricity_delivered_2 = electricity_delivered_2\nelectricity_returned_2 = electricity_returned_2\nelectricity_currently_delivered = electricity_currently_delivered\nelectricity_currently_returned = electricity_currently_returned\nphase_currently_delivered_l1 = phase_currently_delivered_l1\nphase_currently_delivered_l2 = phase_currently_delivered_l2\nphase_currently_delivered_l3 = phase_currently_delivered_l3\nphase_currently_returned_l1 = phase_currently_returned_l1\nphase_currently_returned_l2 = phase_currently_returned_l2\nphase_currently_returned_l3 = phase_currently_returned_l3\nextra_device_timestamp = extra_device_timestamp\nextra_device_delivered = extra_device_delivered\nphase_voltage_l1 = dsmr/reading/phase_voltage_l1\nphase_voltage_l2 = dsmr/reading/phase_voltage_l2\nphase_voltage_l3 = dsmr/reading/phase_voltage_l3\n",
                help_text="Maps the field names used in the JSON message sent to the broker.",
                verbose_name="Formatting",
            ),
        ),
        migrations.AlterField(
            model_name="splittopictelegrammqttsettings",
            name="formatting",
            field=models.TextField(
                default="\n[mapping]\n# READING FIELD = TOPIC PATH\nid = dsmr/reading/id\ntimestamp = dsmr/reading/timestamp\nelectricity_delivered_1 = dsmr/reading/electricity_delivered_1\nelectricity_returned_1 = dsmr/reading/electricity_returned_1\nelectricity_delivered_2 = dsmr/reading/electricity_delivered_2\nelectricity_returned_2 = dsmr/reading/electricity_returned_2\nelectricity_currently_delivered = dsmr/reading/electricity_currently_delivered\nelectricity_currently_returned = dsmr/reading/electricity_currently_returned\nphase_currently_delivered_l1 = dsmr/reading/phase_currently_delivered_l1\nphase_currently_delivered_l2 = dsmr/reading/phase_currently_delivered_l2\nphase_currently_delivered_l3 = dsmr/reading/phase_currently_delivered_l3\nphase_currently_returned_l1 = dsmr/reading/phase_currently_returned_l1\nphase_currently_returned_l2 = dsmr/reading/phase_currently_returned_l2\nphase_currently_returned_l3 = dsmr/reading/phase_currently_returned_l3\nextra_device_timestamp = dsmr/reading/extra_device_timestamp\nextra_device_delivered = dsmr/reading/extra_device_delivered\nphase_voltage_l1 = dsmr/reading/phase_voltage_l1\nphase_voltage_l2 = dsmr/reading/phase_voltage_l2\nphase_voltage_l3 = dsmr/reading/phase_voltage_l3\n",
                help_text="Maps the field names to separate topics sent to the broker.",
                verbose_name="Formatting",
            ),
        ),
    ]
