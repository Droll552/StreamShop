from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from users.factories import UserFactory
from livestreams.models import Livestream


class LivestreamCreateViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_login(self.user)
        self.url = reverse("livestream_create")

        self.data_for_create = {
            'stream_name': "Blue Oyster",
            'date': date(1999, 8, 10),
            'time': time(10, 10, 10),
            'stream_channel': Livestream.StreamChannelChoices.YOUTUBE,
            'status': Livestream.StreamStatusChoices.UPCOMING,
        }

    def test_livestream_create_view_works(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_livestream_create_view_not_shown_without_login(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_livestream_creates(self):
        livestreams_number = Livestream.objects.count()
        response = self.client.post(self.url, self.data_for_create)

        self.assertRedirects(response, reverse("livestream_list"))
        self.assertEqual(livestreams_number + 1, Livestream.objects.count())
        self.assertEqual("Blue Oyster", Livestream.objects.first().stream_name)

