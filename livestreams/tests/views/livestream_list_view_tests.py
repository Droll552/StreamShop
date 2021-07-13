from django.test import TestCase
from django.urls import reverse

from users.factories import UserFactory
from livestreams.factories import LivestreamFactory
from livestreams.models import Livestream


class LivestreamListViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory.create()
        self.another_user = UserFactory.create()
        self.user_without_streams = UserFactory.create()

        self.url = reverse('livestream_list')

        LivestreamFactory.create_batch(
            2,
            stream_name='UpcomingStreamName',
            user=self.user,
            status=Livestream.StreamStatusChoices.UPCOMING
        )
        LivestreamFactory.create_batch(
            3,
            stream_name='InProgressStreamName',
            user=self.user,
            status=Livestream.StreamStatusChoices.IN_PROGRESS,
        )
        LivestreamFactory.create_batch(
            4,
            stream_name='InPaymentRequestStreamName',
            user=self.user,
            status=Livestream.StreamStatusChoices.IN_PAYMENT_REQUEST,
        )
        LivestreamFactory.create_batch(
            10,
            stream_name='AnotherUsersStreamName',
            user=self.another_user,
        )

    def test_livestreams_statistics(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'Number of Upcoming livestreams: 2')
        self.assertContains(response, 'Number of In progress livestreams: 3')
        self.assertContains(response, 'Number of In payment streams: 4')

    def test_livestream_list_view_has_streams(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'UpcomingStreamName', count=2)
        self.assertContains(response, 'InProgressStreamName', count=3)
        self.assertContains(response, 'InPaymentRequestStreamName', count=4)

    def test_livestreams_user_quantity_and_privacy(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertNotContains(response, 'AnotherUsersStreamName')

    def test_livestreams_another_user_quantity_and_privacy(self):
        self.client.force_login(self.another_user)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'AnotherUsersStreamName', count=10)
        self.assertNotContains(response, 'InPaymentRequestStreamName')

    def test_livestreams_user_without_streams_message_if_no_livestreams(self):
        self.client.force_login(self.user_without_streams)
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)
        self.assertContains(response, 'You don\'t have any upcoming livestreams')
        self.assertContains(response, 'You don\'t have any "In Progress" Livestreams')
        self.assertContains(response, 'You don\'t have any "In Payment" Livestreams')

        self.assertNotContains(response, 'InPaymentRequestStreamName')
        self.assertNotContains(response, 'AnotherUsersStreamName')

    def test_listview_not_shown_without_login(self):
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)
