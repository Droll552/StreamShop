from users.factories import UserFactory
from .models import Livestream

import factory.django
from faker import Faker

fake = Faker(locale="en")


class LivestreamFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(UserFactory)
    date = fake.date()
    time = fake.time()
    stream_name = fake.text(max_nb_chars=40)
    tags = fake.text(max_nb_chars=40)

    class Meta:
        model = Livestream
