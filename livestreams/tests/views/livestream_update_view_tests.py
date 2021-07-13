from datetime import date, time

from django.test import TestCase
from django.urls import reverse

from users.factories import UserFactory
from livestreams.factories import LivestreamFactory
from livestreams.models import Livestream


def _post_url(pk):
    return reverse('livestream_update', kwargs={'pk': pk})


class LivestreamUpdateViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory.create()

        self.upcoming_livestream = LivestreamFactory(
            user=self.user,
            status=Livestream.StreamStatusChoices.UPCOMING
        )
        self.in_progress_livestream = LivestreamFactory(
            user=self.user,
            status=Livestream.StreamStatusChoices.IN_PROGRESS
        )
        self.in_payment_livestream = LivestreamFactory(
            user=self.user,
            status=Livestream.StreamStatusChoices.IN_PAYMENT_REQUEST
        )
        self.complete_livestream = LivestreamFactory(
            user=self.user,
            status=Livestream.StreamStatusChoices.COMPLETE_LIVESTREAMS
        )

        self.new_stream_name = 'CowboyParty'

        self.data_for_update = {
            'stream_name': self.new_stream_name,
            'user': self.user,
            'date': date(1999, 8, 10),
            'time': time(10, 10, 10),
            'stream_channel': Livestream.StreamChannelChoices.YOUTUBE,
            'status': Livestream.StreamStatusChoices.UPCOMING,
        }

    def test_update_upcoming_livestream(self):
        self.client.force_login(self.user)
        response = self.client.post(
            _post_url(self.upcoming_livestream.id), self.data_for_update
        )
        self.upcoming_livestream.refresh_from_db()

        self.assertRedirects(response, reverse('livestream_list'))
        self.assertEqual(self.upcoming_livestream.stream_name, self.new_stream_name)

    def test_in_progress_livestream(self):
        self.client.force_login(self.user)
        response = self.client.post(
            _post_url(self.in_progress_livestream.id), self.data_for_update
        )
        self.in_progress_livestream.refresh_from_db()

        self.assertRedirects(response, reverse('livestream_list'))
        self.assertEqual(self.in_progress_livestream.stream_name, self.new_stream_name)

    def test_update_in_payment_livestream(self):
        self.client.force_login(self.user)
        response = self.client.post(
            _post_url(self.in_payment_livestream.id), self.data_for_update
        )

        self.assertEqual(404, response.status_code)

    def test_complete_livestream(self):
        self.client.force_login(self.user)
        response = self.client.post(_post_url(
            self.complete_livestream.id), self.data_for_update
        )
        self.assertEqual(404, response.status_code)

    def test_user_can_update_only_his_own_livestream(self):
        another_user = UserFactory.create(email="bla@bla.com")

        self.client.force_login(another_user)
        response = self.client.post(_post_url(
            self.upcoming_livestream.id), self.data_for_update
        )

        self.assertEqual(404, response.status_code)

    def test_user_must_be_logged_in_to_update_livestream(self):
        response = self.client.post(_post_url(
            self.upcoming_livestream.id), self.data_for_update
        )

        self.assertEqual(302, response.status_code)
