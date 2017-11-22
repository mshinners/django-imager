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
    camera = factory.Faker('words')
    services = factory.Faker('words')
    bio = factory.faker('paragraph')
    phone = factory.faker('phone_number')
    photo_style = factory.faker('words')


class ProfileTests(TestCase):
    """Test set-up for imagersite module."""

    def setUp(self):
        """Create a user for testing purposes."""
        user = User(username='name', email='name@name.com')
        user.set_password('password')
        user.save()
        profile = ImagerProfile(website='www.pics4you.com',
                                location='Seattle',
                                fee=500,
                                camera='Nikon Pro 3500',
                                services='Weddings',
                                bio='I will take picutres for any occasion.',
                                phone='206-555-1212',
                                photo_style='Matte Finish',
                                user=user
                                )
        profile.save()


    # def test_here(self):
    #     """."""
    #     pass

    # def tearDown(self):
    #     """."""
    #     pass
