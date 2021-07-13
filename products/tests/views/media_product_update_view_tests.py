from django.test import TestCase
from django.urls import reverse

from products.factories import MediaProductFactory
from users.factories import UserFactory


class MediaProductUpdateViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory(email="test@email.com")
        self.client.force_login(self.user)
        self.media_product = MediaProductFactory(user=self.user, asking_price=1)
        self.url = reverse("media_update", args=[self.media_product.pk])
        self.data = {
            "asking_price": 2,
            "artist_name": self.media_product.artist_name,
            "album": self.media_product.album,
            "category": self.media_product.category,
            "condition": self.media_product.condition,
            "format": self.media_product.format,
            "press": self.media_product.press,
        }

    def test_media_product_update_view_works(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_media_product_update_view_not_shown_without_login(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_media_product_update_view_shown_only_for_creator(self):
        another_user = UserFactory(email="test1@email.com")
        self.client.force_login(another_user)
        response = self.client.get(self.url)

        self.assertEqual(403, response.status_code)

    def test_media_product_update_view_updates_media_product(self):
        response = self.client.post(self.url, self.data)
        self.media_product.refresh_from_db()
        self.assertRedirects(response, reverse("media_detail", args=[self.media_product.pk]))
        self.assertEqual(2, self.media_product.asking_price)
