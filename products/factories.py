import factory.django
from faker import Faker

from .models import Product, MediaProduct
from users.factories import UserFactory

fake = Faker(locale="en")


class ProductFactory(factory.django.DjangoModelFactory):

    user = factory.SubFactory(UserFactory)
    asking_price = fake.pydecimal(left_digits=4, right_digits=2, positive=True)
    product_type = fake.random_element(elements=Product.PressTypeChoices.choices)[0]

    class Meta:
        model = Product


class MediaProductFactory(ProductFactory):

    product_type = "Media"
    artist_name = fake.text(max_nb_chars=24)
    album = fake.text(max_nb_chars=24)
    category = fake.random_element(elements=MediaProduct.CategoryChoices.choices)[0]
    condition = fake.random_element(elements=MediaProduct.ConditionChoices.choices)[0]
    format = fake.random_element(elements=MediaProduct.FormatChoices.choices)[0]

    class Meta:
        model = MediaProduct
