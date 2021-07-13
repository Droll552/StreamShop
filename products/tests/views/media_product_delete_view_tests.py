from django.test import TestCase
from django.urls import reverse

from products.factories import MediaProductFactory
from products.models import MediaProduct
from users.factories import UserFactory


class MediaProductDeleteViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory(email="test@email.com")
        self.client.force_login(self.user)
        self.media_product = MediaProductFactory(user=self.user)
        self.url = reverse("media_delete", args=[self.media_product.pk])

    def test_media_product_delete_view_works(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_media_product_delete_view_not_shown_without_login(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_media_product_delete_view_shown_only_for_creator(self):
        another_user = UserFactory(email="test1@email.com")
        self.client.force_login(another_user)
        response = self.client.get(self.url)

        self.assertEqual(403, response.status_code)

    def test_media_product_update_view_deletes_media_product(self):
        response = self.client.post(self.url)

        self.assertRedirects(response, reverse("product_list"))
        self.assertEqual(0, MediaProduct.objects.count())
