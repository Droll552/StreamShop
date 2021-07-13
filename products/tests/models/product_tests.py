from django.test import TestCase

from products.factories import ProductFactory, UserFactory
from products.models import Product


class ProductTests(TestCase):
    def setUp(self):
        self.user = UserFactory()
        self.product_type = Product.ProductTypeChoices.MEDIA
        self.asking_price = 1234.56
        self.opening_price = 9999.99
        self.press_year = 2000
        self.notes = "Notes"
        self.press = Product.PressTypeChoices.ORIGINAL

        self.product = ProductFactory(
            user=self.user,
            product_type=self.product_type,
            asking_price=self.asking_price,
            opening_price=self.opening_price,
            press_year=self.press_year,
            notes=self.notes,
            press=self.press,
        )

    # fields

    def test_it_has_user_field(self):
        self.assertEqual(self.user, self.product.user)

    def test_it_has_product_type_field(self):
        self.assertEqual(self.product_type, self.product.product_type)
        self.assertEqual("Product Type", self.product._meta.get_field("product_type").verbose_name)

    def test_it_has_asking_price_field(self):
        self.assertEqual(self.asking_price, self.product.asking_price)
        self.assertEqual("Asking Price", self.product._meta.get_field("asking_price").verbose_name)

    def test_it_has_opening_price_field(self):
        self.assertEqual(self.opening_price, self.product.opening_price)
        self.assertEqual("Opening Price", self.product._meta.get_field("opening_price").verbose_name)

    def test_it_has_press_year_field(self):
        self.assertEqual(self.press_year, self.product.press_year)
        self.assertEqual("Press Year", self.product._meta.get_field("press_year").verbose_name)

    def test_it_has_notes_field(self):
        self.assertEqual(self.notes, self.product.notes)
        self.assertEqual("Notes", self.product._meta.get_field("notes").verbose_name)

    def test_it_has_press_field(self):
        self.assertEqual(self.press, self.product.press)
        self.assertEqual("Press", self.product._meta.get_field("press").verbose_name)

    # methods

    def test_product_name_method(self):
        with self.assertRaises(NotImplementedError):
            self.product.product_name()

    def test_description_method(self):
        with self.assertRaises(NotImplementedError):
            self.product.description()

    def test_details_method(self):
        with self.assertRaises(NotImplementedError):
            self.product.details()
