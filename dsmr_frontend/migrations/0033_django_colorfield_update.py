# Generated by Django 3.0.3 on 2020-02-18 22:37

import colorfield.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_frontend", "0032_v3_4_0_release"),
    ]

    operations = [
        migrations.AlterField(
            model_name="frontendsettings",
            name="electricity_delivered_alternate_color",
            field=colorfield.fields.ColorField(
                default="#7D311A",
                help_text="Graph color for electricity delivered (Dutch users: low tariff)",
                max_length=18,
                verbose_name="Electricity delivered color (alternative)",
            ),
        ),
        migrations.AlterField(
            model_name="frontendsettings",
            name="electricity_delivered_color",
            field=colorfield.fields.ColorField(
                default="#F05050",
                help_text="Graph color for electricity delivered (default + high tariff)",
                max_length=18,
                verbose_name="Electricity delivered color",
            ),
        ),
        migrations.AlterField(
            model_name="frontendsettings",
            name="electricity_returned_alternate_color",
            field=colorfield.fields.ColorField(
                default="#C8C864",
                help_text="Graph color for electricity returned (Dutch users: low tariff)",
                max_length=18,
                verbose_name="Electricity returned color (alternative)",
            ),
        ),
        migrations.AlterField(
            model_name="frontendsettings",
            name="electricity_returned_color",
            field=colorfield.fields.ColorField(
                default="#27C24C",
                help_text="Graph color for electricity returned (default + high tariff)",
                max_length=18,
                verbose_name="Electricity returned color",
            ),
        ),
        migrations.AlterField(
            model_name="frontendsettings",
            name="gas_delivered_color",
            field=colorfield.fields.ColorField(
                default="#FF851B",
                help_text="Graph color for gas delivered",
                max_length=18,
                verbose_name="Gas delivered color",
            ),
        ),
        migrations.AlterField(
            model_name="frontendsettings",
            name="temperature_color",
            field=colorfield.fields.ColorField(
                default="#0073B7",
                help_text="Graph color for temperatures read",
                max_length=18,
                verbose_name="Temperature color",
            ),
        ),
    ]
