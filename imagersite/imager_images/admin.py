"""."""
from django.contrib import admin
from imager_images.models import Photo, Album
from imager_profile.models import ImagerProfile

# Register your models here.

admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(ImagerProfile)
