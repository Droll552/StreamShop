from django.test import TestCase
from django.urls import reverse

from users.factories import UserFactory
from livestreams.factories import LivestreamFactory
from livestreams.models import Livestream


class LivestreamCompleteListViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.another_user = UserFactory.create()
        self.user_without_complete_streams = UserFactory.create()

        self.url = reverse('livestream_complete_list')

        LivestreamFactory.create_batch(
            2,
            stream_name="Completed",
            user=self.user,
            status=Livestream.StreamStatusChoices.COMPLETE_LIVESTREAMS
        )

        LivestreamFactory.create_batch(
            3,
            stream_name="Beer",
            user=self.another_user,
            status=Livestream.StreamStatusChoices.COMPLETE_LIVESTREAMS
        )

        LivestreamFactory.create_batch(
            4,
            stream_name="Upcoming",
            user=self.user,
            status=Livestream.StreamStatusChoices.UPCOMING
        )

        LivestreamFactory.create_batch(
            5,
            stream_name="In Progress",
            user=self.another_user,
            status=Livestream.StreamStatusChoices.IN_PROGRESS
        )

        LivestreamFactory.create_batch(6, user=self.user_without_complete_streams)

    def test_complete_livestreams_statistics(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Number of complete livestreams: 2')

    def test_complete_livestream_list_view_has_streams(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Completed', count=2)
        self.assertNotContains(response, 'Beer')

    def test_another_user_complete_livestreams(self):
        self.client.force_login(self.another_user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Beer', count=3)
        self.assertNotContains(response, 'Completed')

    def test_message_if_no_complete_livestream(self):
        self.client.force_login(self.user_without_complete_streams)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'You have not any completed livestreams')
        self.assertNotContains(response, 'Beer')
        self.assertNotContains(response, 'Completed')

    def test_complete_listview_not_shown_without_login(self):
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)
