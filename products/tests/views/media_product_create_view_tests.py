from django.test import TestCase
from django.urls import reverse

from products.models import MediaProduct
from users.factories import UserFactory


class MediaProductCreateViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.client.force_login(self.user)
        self.url = reverse("media_create")

        self.data = {
            "asking_price": 1,
            "artist_name": "Artist",
            "album": "Album",
            "category": "single",
            "condition": "good_good",
            "format": "vinyl",
            "press": "OG",
         }

    def test_media_product_create_view_works(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_media_product_create_view_not_shown_without_login(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_media_product_create_view_creates_media_product(self):
        media_products_count_before = MediaProduct.objects.count()
        response = self.client.post(self.url, self.data)

        self.assertRedirects(response, reverse("product_list"))
        self.assertEqual(media_products_count_before + 1, MediaProduct.objects.count())
        self.assertEqual(1, MediaProduct.objects.first().asking_price)
