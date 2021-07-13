from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractUser

from users.managers import UserManager


class User(AbstractUser):
    username = None
    email = models.EmailField("Email", unique=True)
    objects = UserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["first_name", 'last_name']

    def __str__(self):
        return self.email

    def save(self, *args, **kwargs):
        if not self.first_name or not self.last_name:
            raise ValidationError("You should enter your First name and Last name")

        super().save(*args, **kwargs)


User._meta.get_field('first_name').blank = False
User._meta.get_field('last_name').blank = False

