# Generated by Django 3.1.2 on 2020-10-18 10:54

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_datalogger", "0028_drop_legacy_telegram_logging"),
    ]

    operations = [
        migrations.AlterField(
            model_name="retentionsettings",
            name="data_retention_in_hours",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (
                        None,
                        "Disabled (WARNING: Will eventually lead to performance issues!)",
                    ),
                    (168, "Clean up most source data after one week (RECOMMENDED)"),
                    (672, "Clean up most source data after one month (RECOMMENDED)"),
                    (2016, "Clean up most source data after three months"),
                    (4032, "Clean up most source data after six months"),
                    (8064, "Clean up most source data after one year"),
                ],
                default=672,
                help_text="The lifetime of source readings and consumption records. Day and hour statistics will always be preserved indefinitely.",
                null=True,
                verbose_name="Data retention policy",
            ),
        ),
    ]
