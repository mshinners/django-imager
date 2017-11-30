"""Test file for imagersite."""

from __future__ import unicode_literals
from imager_profile.models import User, ImagerProfile
from django.test import TestCase
import factory
import random
# from imagersite import models


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
    bio = factory.Faker('paragraph')
    phone = factory.Faker('phone_number')
    photo_style = factory.Faker('words')


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

        user = UserFactory.create()
        user.set_password(factory.Faker('password'))
        user.save()
        profile = ProfileFactory.create(user=user, is_active=False)
        profile.save()

        for _ in range(10):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()
            profile = ProfileFactory.create(user=user)
            profile.save()

    def test_profile_has_website(self):
        """Test that a profile has a website."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.website, 'www.pics4you.com')

    def test_profile_has_location(self):
        """Test that a profile has a location."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.location, 'Seattle')

    def test_profile_has_fee(self):
        """Test that a profile has a fee."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.fee, 500)

    def test_profile_has_bio(self):
        """Test that a profile has a bio."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.bio, 'I will take picutres for any occasion.')

    def test_profile_has_phone(self):
        """Test that a profile has a phone."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.phone, '206-555-1212')

    def test_profile_has_photo_style(self):
        """Test that a profile has a phone."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertEquals(one_profile.photo_style, 'Matte Finish')

    def test_profile_is_active_by_default(self):
        """Test that a profile is active."""
        active_user = User.objects.get(username='name')
        one_profile = ImagerProfile.objects.get(user=active_user)
        self.assertTrue(one_profile.is_active)
