from urllib.parse import urlparse

from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site
import uuid

from django.urls import reverse
from livestreams.managers import LivestreamManager

from taggit.managers import TaggableManager


class Livestream(models.Model):
    class StreamChannelChoices(models.TextChoices):
        YOUTUBE = "Youtube"
        TWITCH = "Twitch"
        FACEBOOK = "Facebook"

    class StreamStatusChoices(models.TextChoices):
        UPCOMING = "Upcoming"
        IN_PROGRESS = "In Progress"
        IN_PAYMENT_REQUEST = "In Payment Request"
        COMPLETE_LIVESTREAMS = "Complete Livestreams"

    user = models.ForeignKey(
        get_user_model(),
        on_delete=models.CASCADE,
        related_name="livestreams",
        verbose_name="User"
    )
    date = models.DateField("Date")
    time = models.TimeField("Time")
    stream_name = models.CharField("Live stream name", max_length=150)
    stream_link = models.URLField(
        "Live stream link",
        max_length=150,
        default='',
        null=True,
        blank=True
    )
    stream_channel = models.CharField(
        "Live stream channel",
        max_length=8,
        choices=StreamChannelChoices.choices,
    )
    tags = TaggableManager("Tags", blank=True)
    public_id = models.UUIDField(
        "Public link",
        default=uuid.uuid4,
        editable=False,
        unique=True
    )
    status = models.CharField(
        "Livestream status",
        max_length=20,
        choices=StreamStatusChoices.choices,
        default=StreamStatusChoices.UPCOMING,
    )
    objects = LivestreamManager()

    def __str__(self):
        return self.stream_name

    def get_public_url(self):
        domain = Site.objects.get_current(self).domain
        path = reverse(
            "public_livestream_share",
            args=[
                str(self.public_id),
            ],
        )
        return f"https://{domain}{path}"


