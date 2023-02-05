# Generated by Django 2.0.7 on 2018-07-10 21:06

from django.db import migrations
from django.utils.translation import gettext_lazy


def migrate_forward(apps, schema_editor):
    """Notify user about the new graphs."""
    import dsmr_frontend.services
    import dsmr_backend.services.backend

    if dsmr_backend.services.backend.is_recent_installation():
        # Skip for new installations.
        return

    Notification = apps.get_model("dsmr_frontend", "Notification")
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=gettext_lazy(
                "The graphs on the Dashboard have been replaced this release and are now scrollable. "
                "The graphs on the Trends page have been updated as well."
            )
        )
    )


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("dsmr_frontend", "0012_frontendsettings_dashboard_graph_width"),
    ]

    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]
