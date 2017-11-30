from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField

# Create your models here.


class ImagerProfile(models.Model):
    """Set up the user model."""

    website = models.URLField(max_length=50)
    location = models.CharField(max_length=50)
    fee = models.DecimalField(decimal_places=2, max_digits=6)
    camera_choices = [
        ('Nikon', 'Nikon'),
        ('Minolta', 'Minolta'),
        ('Cannon', 'Cannon'),
        ('Polaroid', 'Polariod'),
        ('iPhoneX', 'iPhone X')
    ]
    camera = models.CharField(
        max_length=10,
        choices=camera_choices)

    service_options = [
        ('Wedding', 'Wedding'),
        ('SeniorPhotos', 'Senior Photos'),
        ('FamilyReunions', 'Family Reunions'),
        ('Birthdays', 'Birthdays'),
        ('Boudoir', 'Boudior')
    ]
    services = MultiSelectField(
        max_length=20,
        choices=service_options)

    bio = models.CharField(max_length=500)
    phone = models.CharField(max_length=10)
    photo_styles = [
        ('Matte', 'Matte Finish'),
        ('Glossy', 'Glossy Finish'),
        ('Poster', 'Poster Board'),
        ('Frameless', 'Frameless')
    ]
    photo_style = MultiSelectField(
        max_length=10,
        choices=photo_styles)

    user = models.OneToOneField(User, related_name='profile')

    is_active = models.BooleanField(default=True)
