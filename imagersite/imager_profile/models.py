from django.db import models
from django.contrib.auth.models import User
from multiselectfield import MultiSelectField
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.


class ImagerProfile(models.Model):
    """Set up the user model."""

    website = models.URLField(max_length=50, null=True, blank=True)
    location = models.CharField(max_length=50, null=True, blank=True)
    fee = models.DecimalField(decimal_places=2, max_digits=6, null=True, blank=True)
    camera_choices = [
        ('Nikon', 'Nikon'),
        ('Minolta', 'Minolta'),
        ('Cannon', 'Cannon'),
        ('Polaroid', 'Polariod'),
        ('iPhoneX', 'iPhone X')
    ]
    camera = models.CharField(
        max_length=50,
        choices=camera_choices, null=True, blank=True)

    service_options = [
        ('Wedding', 'Wedding'),
        ('SeniorPhotos', 'Senior Photos'),
        ('FamilyReunions', 'Family Reunions'),
        ('Birthdays', 'Birthdays'),
        ('Boudoir', 'Boudoir')
    ]
    services = MultiSelectField(
        max_length=250,
        choices=service_options, null=True, blank=True)

    bio = models.TextField(max_length=500, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    photo_styles = [
        ('Matte', 'Matte Finish'),
        ('Glossy', 'Glossy Finish'),
        ('Poster', 'Poster Board'),
        ('Frameless', 'Frameless')
    ]
    photo_style = MultiSelectField(
        max_length=100,
        choices=photo_styles, null=True, blank=True)

    user = models.OneToOneField(User, related_name='profile')

    is_active = models.BooleanField(default=True)


@receiver(post_save, sender=User)
def make_new_user_profile(sender, **kwargs):
    """."""
    if kwargs['created']:
        new_profile = ImagerProfile(
            user=kwargs['instance'])
        new_profile.save()
