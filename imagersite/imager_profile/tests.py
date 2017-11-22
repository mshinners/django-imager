"""Test file for imagersite."""

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.test import TestCase
import factory

from imagersite import models


class UserFactory(factory.django.DjangoModelFactory):
    """."""

    class Meta:
        """."""

        model = User

    first_name = factory.Sequence(lambda n: "user{}".format(n))
    last_name = factory.Sequence(lambda n: "user{}".format(n))
    email = factory.Sequence(lambda n: "user{}@example.com".format(n))


class ProfileTestCase(TestCase):
    """."""

    def setUp(self):
        """."""
        self.users = []
        for i in range(10):
            user = UserFactory.create()
            user.save()
            self.users.append(user)

    def test_here(self):
        """."""
        pass

    def tearDown(self):
        """."""
        pass


"""
factory(faker)......


    website = factory.Faker('website')
    location = factory.Faker('location')
    fee = factory.Faker('fee')
    camera = factory.Faker('camera_choices')
    services = factory.Faker('service_options')
    website = factory.Faker('website')
    website = factory.Faker('website')
    website = factory.Faker('website')
    website = factory.Faker('website')
    website = factory.Faker('website')
"""
