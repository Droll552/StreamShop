from django.db import models
from django.contrib.auth import get_user_model


class Product(models.Model):

    class PressTypeChoices(models.TextChoices):
        ORIGINAL = "OG", "OG"
        REPUBLISHED = "RE", "RE"
        UNDEFINED = "UN", "UN"

    class ProductTypeChoices(models.TextChoices):
        MEDIA = "media", "Media"
        CARDS = "cards", "Cards"
        GAMING = "gaming", "Gaming"
        COMICS = "comics", "Comics"
        SHOES = "shoes", "Shoes"

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="products")
    product_type = models.CharField("Product Type", max_length=6, choices=ProductTypeChoices.choices)
    asking_price = models.DecimalField("Asking Price", max_digits=6, decimal_places=2)
    opening_price = models.DecimalField("Opening Price", max_digits=6, decimal_places=2, blank=True, null=True)
    created_at = models.DateField("Created at", auto_now_add=True)
    press_year = models.IntegerField("Press Year", blank=True, null=True)
    notes = models.TextField("Notes", blank=True, null=True)
    press = models.CharField("Press", max_length=2, choices=PressTypeChoices.choices,
                             default=PressTypeChoices.UNDEFINED)

    @property
    def product_name(self):
        raise NotImplementedError("Should be implemented in child class!")

    @property
    def description(self):
        raise NotImplementedError("Should be implemented in child class!")

    @property
    def details(self):
        raise NotImplementedError("Should be implemented in child class!")

    def __str__(self):
        return self.product_name
