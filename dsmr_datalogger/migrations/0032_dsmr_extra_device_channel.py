# Generated by Django 3.2.16 on 2023-01-23 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dsmr_datalogger", "0031_meter_statistics_meta"),
    ]

    operations = [
        migrations.AddField(
            model_name="dataloggersettings",
            name="dsmr_extra_device_channel",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (None, "Automatic (default)"),
                    (1, "Belgium - Fluvius (channel 1)"),
                    (2, "Belgium - Fluvius (channel 2)"),
                    (3, "Belgium - Fluvius (channel 3)"),
                    (4, "Belgium - Fluvius (channel 4)"),
                ],
                default=None,
                help_text="Only use when your extra device is read incorrectly (e.g. gas). Also, only works with specific vendor(s).",
                null=True,
                verbose_name="Extra device channel",
            ),
        ),
        migrations.AlterField(
            model_name="dataloggersettings",
            name="dsmr_version",
            field=models.IntegerField(
                choices=[
                    (4, "Netherlands - DSMR version 4/5 (default)"),
                    (3, "Netherlands - DSMR version 2/3"),
                    (101, "Belgium - Fluvius (gas meter fix)"),
                    (102, "Luxembourg - Smarty (single tariff fix)"),
                ],
                default=4,
                help_text="The DSMR version your meter supports or the vendor related to it. Version should be printed on meter.",
                verbose_name="DSMR version/vendor",
            ),
        ),
    ]
