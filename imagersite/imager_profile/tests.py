"""Test file for imagersite."""

from __future__ import unicode_literals
from imager_profile.models import User, ImagerProfile
from django.test import TestCase
import factory
import random
from imagersite import models


class UserFactory(factory.django.DjangoModelFactory):
    """Create fake users for testing."""

    class Meta:
        """."""

        model = User

    username = factory.Sequence(lambda n: '{}'.format(factory.Faker('name'), n))
    email = factory.Faker('email')


class ProfileFactory(factory.django.DjangoModelFactory):
    """Create fake user profiles for testing."""

    class Meta:
        """."""

        model = ImagerProfile

    website = factory.Faker('url')
    location = factory.Faker('address')
    fee = random.uniform(200, 1000)
    camera = factory.Faker('')
    services = factory.Faker('')
    bio = factory.faker('paragraph')
    phone = factory.faker('phone_number')
    photo_style = factory.faker('')


class ProfileTests(TestCase):
    """Test set-up for imagersite module."""

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
