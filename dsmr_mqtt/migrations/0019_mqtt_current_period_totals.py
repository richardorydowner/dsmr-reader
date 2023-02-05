# Generated by Django 3.1.7 on 2021-03-06 12:14

from django.db import migrations, models
import dsmr_backend.mixins


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_mqtt", "0018_mqtt_always_reconnect"),
    ]

    operations = [
        migrations.CreateModel(
            name="JSONCurrentPeriodTotalsMQTTSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Whether the period totals are sent to the broker, in JSON format.",
                        verbose_name="Enabled",
                    ),
                ),
                (
                    "topic",
                    models.CharField(
                        default="dsmr/current-period",
                        help_text="The topic to send the JSON formatted message to.",
                        max_length=256,
                        verbose_name="Topic path",
                    ),
                ),
                (
                    "formatting",
                    models.TextField(
                        default="\n[mapping]\n### SOURCE DATA = JSON FIELD\n### Only alter fields on the RIGHT HAND SIDE below. Remove lines to omit them from the JSON structure sent.\n\n### Current month\ncurrent_month_electricity1 = current_month_electricity1\ncurrent_month_electricity2 = current_month_electricity2\ncurrent_month_electricity1_returned = current_month_electricity1_returned\ncurrent_month_electricity2_returned = current_month_electricity2_returned\ncurrent_month_electricity_merged = current_month_electricity_merged\ncurrent_month_electricity_returned_merged = current_month_electricity_returned_merged\ncurrent_month_electricity1_cost = current_month_electricity1_cost\ncurrent_month_electricity2_cost = current_month_electricity2_cost\ncurrent_month_electricity_cost_merged = current_month_electricity_cost_merged\ncurrent_month_gas = current_month_gas\ncurrent_month_gas_cost = current_month_gas_cost\ncurrent_month_fixed_cost = current_month_fixed_cost\ncurrent_month_total_cost = current_month_total_cost\n\n### Current year\ncurrent_year_electricity1 = current_year_electricity1\ncurrent_year_electricity2 = current_year_electricity2\ncurrent_year_electricity1_returned = current_year_electricity1_returned\ncurrent_year_electricity2_returned = current_year_electricity2_returned\ncurrent_year_electricity_merged = current_year_electricity_merged\ncurrent_year_electricity_returned_merged = current_year_electricity_returned_merged\ncurrent_year_electricity1_cost = current_year_electricity1_cost\ncurrent_year_electricity2_cost = current_year_electricity2_cost\ncurrent_year_electricity_cost_merged = current_year_electricity_cost_merged\ncurrent_year_gas = current_year_gas\ncurrent_year_gas_cost = current_year_gas_cost\ncurrent_year_fixed_cost = current_year_fixed_cost\ncurrent_year_total_cost = current_year_total_cost\n",
                        help_text="Maps the field names used in the JSON message sent to the broker.",
                        verbose_name="Formatting",
                    ),
                ),
            ],
            options={
                "verbose_name": "(Data source) Current month/year totals: JSON",
                "default_permissions": (),
            },
            bases=(dsmr_backend.mixins.ModelUpdateMixin, models.Model),
        ),
        migrations.CreateModel(
            name="SplitTopicCurrentPeriodTotalsMQTTSettings",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "enabled",
                    models.BooleanField(
                        default=False,
                        help_text="Whether period totals are sent to the broker, having each field sent to a different topic.",
                        verbose_name="Enabled",
                    ),
                ),
                (
                    "formatting",
                    models.TextField(
                        default="\n[mapping]\n### SOURCE DATA = TOPIC PATH\n### Only alter the topic paths on the RIGHT HAND SIDE below. Remove lines to prevent them from being sent at all.\n\n### Current month\ncurrent_month_electricity1 = dsmr/current-month/electricity1\ncurrent_month_electricity2 = dsmr/current-month/electricity2\ncurrent_month_electricity1_returned = dsmr/current-month/electricity1_returned\ncurrent_month_electricity2_returned = dsmr/current-month/electricity2_returned\ncurrent_month_electricity_merged = dsmr/current-month/electricity_merged\ncurrent_month_electricity_returned_merged = dsmr/current-month/electricity_returned_merged\ncurrent_month_electricity1_cost = dsmr/current-month/electricity1_cost\ncurrent_month_electricity2_cost = dsmr/current-month/electricity2_cost\ncurrent_month_electricity_cost_merged = dsmr/current-month/electricity_cost_merged\ncurrent_month_gas = dsmr/current-month/gas\ncurrent_month_gas_cost = dsmr/current-month/gas_cost\ncurrent_month_fixed_cost = dsmr/current-month/fixed_cost\ncurrent_month_total_cost = dsmr/current-month/total_cost\n\n### Current year\ncurrent_year_electricity1 = dsmr/current-year/electricity1\ncurrent_year_electricity2 = dsmr/current-year/electricity2\ncurrent_year_electricity1_returned = dsmr/current-year/electricity1_returned\ncurrent_year_electricity2_returned = dsmr/current-year/electricity2_returned\ncurrent_year_electricity_merged = dsmr/current-year/electricity_merged\ncurrent_year_electricity_returned_merged = dsmr/current-year/electricity_returned_merged\ncurrent_year_electricity1_cost = dsmr/current-year/electricity1_cost\ncurrent_year_electricity2_cost = dsmr/current-year/electricity2_cost\ncurrent_year_electricity_cost_merged = dsmr/current-year/electricity_cost_merged\ncurrent_year_gas = dsmr/current-year/gas\ncurrent_year_gas_cost = dsmr/current-year/gas_cost\ncurrent_year_fixed_cost = dsmr/current-year/fixed_cost\ncurrent_year_total_cost = dsmr/current-year/total_cost\n",
                        help_text="Maps the field names to separate topics sent to the broker.",
                        verbose_name="Formatting",
                    ),
                ),
            ],
            options={
                "verbose_name": "(Data source) Current month/year totals: Split topic",
                "default_permissions": (),
            },
            bases=(dsmr_backend.mixins.ModelUpdateMixin, models.Model),
        ),
    ]
