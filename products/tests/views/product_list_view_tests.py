from django.test import TestCase
from django.urls import reverse

from products.factories import ProductFactory
from users.factories import UserFactory


class ProductListViewTests(TestCase):
    def setUp(self):
        self.user = UserFactory(email="test@email.com")
        self.client.force_login(self.user)

        self.products = ProductFactory.create_batch(size=10, user=self.user, asking_price=2000)

        self.url = reverse("product_list")

    def test_product_list_view_status_code(self):
        response = self.client.get(self.url)

        self.assertEqual(200, response.status_code)

    def test_product_list_view_not_shown_without_login(self):
        self.client.logout()
        response = self.client.get(self.url)

        self.assertEqual(302, response.status_code)

    def test_product_list_view_has_products(self):
        response = self.client.get(self.url)

        self.assertContains(response, "2000", 10)

    def test_only_user_who_create_products_see_them(self):
        another_user = UserFactory(email="test1@email.com")

        self.client.force_login(another_user)
        response = self.client.get(self.url)

        self.assertNotContains(response, "2000")
