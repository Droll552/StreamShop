from django.test import TestCase
from django.urls import reverse

from users.factories import UserFactory

from datetime import date, time

from livestreams.factories import LivestreamFactory
from livestreams.models import Livestream


class LivestreamTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.date = date(1999, 8, 10)
        self.time = time(10, 10, 10)
        self.stream_name = "SuperStream"
        self.stream_channel = Livestream.StreamChannelChoices.YOUTUBE
        self.tags = ["#beer", "#more_beer"]
        self.status = Livestream.StreamStatusChoices.IN_PROGRESS

        self.livestream = LivestreamFactory(
            user=self.user,
            date=self.date,
            time=self.time,
            stream_name=self.stream_name,
            stream_channel=self.stream_channel,
            tags=self.tags,
            status=self.status,
        )

    # Fields

    def test_it_has_user_field(self):
        self.assertEqual(self.livestream.user, self.user)

    def test_it_has_date_field(self):
        self.assertEqual(self.livestream.date, self.date)
        self.assertEqual(self.livestream._meta.get_field("date").verbose_name, "Date")

    def test_it_has_time_field(self):
        self.assertEqual(self.livestream.time, self.time)
        self.assertEqual(self.livestream._meta.get_field("time").verbose_name, "Time")

    def test_it_has_stream_name_field(self):
        self.assertEqual(self.livestream.stream_name, self.stream_name)
        self.assertEqual(self.livestream._meta.get_field("stream_name").verbose_name, "Live stream name")

    def test_it_has_stream_channel_field(self):
        self.assertEqual(self.livestream.stream_channel, self.stream_channel)
        self.assertEqual(self.livestream._meta.get_field("stream_channel").verbose_name, "Live stream channel")

    def test_it_has_tags_field(self):
        self.assertEqual(self.livestream.tags, self.tags)
        self.assertEqual(self.livestream._meta.get_field("tags").verbose_name, "Tags")

    def test_it_has_status_field(self):
        self.assertEqual(self.livestream.status, self.status)
        self.assertEqual(self.livestream._meta.get_field("status").verbose_name, "Livestream status")

    # model methods

    def test_string_representation(self):
        self.assertEqual(str(self.stream_name), self.livestream.stream_name)

    def test_function_get_public_url(self):
        path = reverse("public_livestream_share", args=[self.livestream.public_id])

        self.assertEqual(
            self.livestream.get_public_url(), f"https://example.com{path}"
        )
