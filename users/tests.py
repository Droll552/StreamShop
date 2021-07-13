from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.test import TestCase

from .factories import UserFactory


class UserTests(TestCase):

    def setUp(self):
        self.first_name = "John"
        self.last_name = "Jones"
        self.email = "testuser@email.com"

        self.user = UserFactory(
            first_name=self.first_name,
            last_name=self.last_name,
            email=self.email,
        )

    # fields

    def test_it_has_first_name_field(self):
        self.assertEqual(self.user.first_name, self.first_name)
        self.assertEqual(
            self.user._meta.get_field("first_name").verbose_name, "first name"
        )

    def test_first_name_is_required(self):
        self.assertFalse(self.user._meta.get_field("first_name").blank)

    def test_last_name_is_required(self):
        self.assertFalse(self.user._meta.get_field("last_name").blank)

    def test_it_has_last_name_field(self):
        self.assertEqual(self.user.last_name, self.last_name)
        self.assertEqual(
            self.user._meta.get_field("last_name").verbose_name, "last name"
        )

    def test_it_has_email_field(self):
        self.assertEqual(self.user.email, self.email)
        self.assertEqual(self.user._meta.get_field("email").verbose_name, "Email")



    # methods

    def test_create_user(self):

        User = get_user_model()
        user = User.objects.create_user(
            first_name="John",
            last_name="Jones",
            email="test@email.com",
            password="test1234",
        )

        self.assertEqual(user.first_name, "John")
        self.assertEqual(user.last_name, "Jones")
        self.assertEqual(user.email, "test@email.com")
        self.assertTrue(user.is_active)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)

    def test_create_user_without_name(self):

        User = get_user_model()
        with self.assertRaises(ValidationError):
            User.objects.create(
                last_name="Jones",
                email="test@email.com",
                password="test1234",)

    def test_create_superuser(self):

        User = get_user_model()
        admin_user = User.objects.create_superuser(
            first_name='Admin',
            last_name='Adminov',
            email="admin@email.com",
            password="admin1234",
        )
        self.assertEqual(admin_user.first_name, "Admin")
        self.assertEqual(admin_user.last_name, "Adminov")
        self.assertEqual(admin_user.email, "admin@email.com")
        self.assertTrue(admin_user.is_active)
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_string_representation(self):
        self.assertEqual(str(self.user), self.user.email)
