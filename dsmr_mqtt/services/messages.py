import logging
from typing import NoReturn

from django.conf import settings
from django.core.cache import caches

from dsmr_mqtt.models import queue


logger = logging.getLogger('dsmrreader')


def queue_message(topic: str, payload: str) -> NoReturn:
    """
    Queues a new message, but only if it doesn't exist yet and is no cached.

    - Maximum message queue size will be maintained.
    - Duplicate, unsent messages will be ignored.
    - Each message sent will be cached, as it'll be dispatched with the retain flag.
    """

    if queue.Message.objects.all().count() >= settings.DSMRREADER_MQTT_MAX_MESSAGES_IN_QUEUE:
        return logger.warning(
            'MQTT: Rejecting message for topic due to maximum queue size (%d): %s',
            settings.DSMRREADER_MQTT_MAX_MESSAGES_IN_QUEUE,
            topic
        )

    cache_storage = caches['mqtt']
    cache_key = topic
    cached_data = cache_storage.get(cache_key)

    # We could have cached the topic, but with different data. Only ignore exactly the same topic + data.
    if cached_data is not None and cached_data == payload:
        # This is by design, since we publish all messages with the "retain" flag for the broker.
        return logger.debug(
            'MQTT: Rejecting message as it exactly matches the previous message sent for this topic: %s', topic
        )

    _, created = queue.Message.objects.get_or_create(topic=topic, payload=payload)
    cache_storage.set(cache_key, payload)

    if not created:
        return logger.debug('MQTT: Rejecting message due to similar message already queued for this topic: %s', topic)

    logger.debug('MQTT: Queued message for %s: %s', topic, payload)
