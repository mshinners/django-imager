from django.db import models
from django.contib.auth.models import User

# Create your models here.


class ImagerProfile(models.Model):
    """Set up the user model."""

    Nikon = 'Nikon'
    Minolta = 'Minolta'
    Cannon = 'Cannon'
    Polaroid = 'Polaroid'
    iPhoneX = 'iPhoneX'
    Wedding = 'Wedding'
    SeniorPhotos = 'Senior Photos'
    FamilyReunions = 'Family Reunions'
    Birthdays = 'Birthdays'
    Boudoir = 'Boudoir'
    Matte = 'Matte Finish'
    Glossy = 'Glossy Finish'
    Poster = 'Poster Board'
    Frameless = 'Frameless'

    website = models.URLField(max_length=50)
    location = models.CharField(max_length=50)
    fee = models.DeciamlField(max_length=2)
    camera_choices = [
        (Nikon, 'Nikon'),
        (Minolta, 'Minolta'),
        (Cannon, 'Cannon'),
        (Polaroid, 'Polariod'),
        (iPhoneX, 'iPhone X')
    ]
    camera = models.CharField(
        max_length=10,
        choices=camera_choices)

    service_options = [
        (Wedding, 'Wedding'),
        (SeniorPhotos, 'Senior Photos'),
        (FamilyReunions, 'Family Reunions'),
        (Birthdays, 'Birthdays'),
        (Boudoir, 'Boudior')
    ]
    services = models.Charfield(
        max_length=20,
        choices=service_options)

    bio = models.Charfield(max_length=500)
    phone = models.Charfiels(max_length=10)
    photo_styles = [
        (Matte, 'Matte Finish'),
        (Glossy, 'Glossy Finish'),
        (Poster, 'Poster Board'),
        (Frameless, 'Frameless')
    ]
    photo = models.CharField(
        max_length=10,
        choices=photo_styles)

    is_active = models.BooleanField(
        _('active'),
        default=True,

    user = models.OneToOneField(User, related_name='profile')
