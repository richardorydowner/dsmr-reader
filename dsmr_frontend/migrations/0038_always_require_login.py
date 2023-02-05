# Generated by Django 3.0.7 on 2020-06-16 16:56

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_frontend", "0037_v3_12_0_release"),
    ]

    operations = [
        migrations.AddField(
            model_name="frontendsettings",
            name="always_require_login",
            field=models.BooleanField(
                default=False,
                help_text="Enable this to enforce login on all pages. Useful to restrict unauthorized access when hosted or reachable on the Internet.",
                verbose_name="Force password login everywhere",
            ),
        ),
    ]
