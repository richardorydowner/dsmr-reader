# Generated by Django 2.2.9 on 2020-01-05 21:16

from django.db import migrations
from django.utils.translation import ugettext_lazy


def migrate_forward(apps, schema_editor):
    import dsmr_frontend.services
    import dsmr_backend.services.backend

    if dsmr_backend.services.backend.is_recent_installation():
        # Skip for new installations.
        return

    Notification = apps.get_model("dsmr_frontend", "Notification")
    Notification.objects.create(
        message=dsmr_frontend.services.get_translated_string(
            text=ugettext_lazy(
                "DSMR-reader v2.14.0: Some configuration options in setting.py were relocated or removed. This only "
                "affects you if you are using custom settings in setting.py. See the changelog for more information."
            )
        ),
        redirect_to="frontend:changelog-redirect",
    )


def migrate_backward(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    operations = [
        migrations.RunPython(migrate_forward, migrate_backward),
    ]

    dependencies = [
        ("dsmr_frontend", "0025_increase_max_dashboard_graph_width"),
    ]
