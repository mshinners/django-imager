"""Views for site."""
from imager_profile.models import ImagerProfile
from imager_images.models import Album, Photo
from django.views.generic import DetailView, TemplateView, ListView
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy
from random import choice


class HomeView(TemplateView):
    """Set up view for home page."""

    template_name = 'imagersite/home.html'
    model = Photo

    def get_context_data(self, **kwargs):
        """."""
        context = super(HomeView, self).get_context_data(**kwargs)
        photos = Photo.objects.filter(published='Public').all()
        if len(photos) > 0:
            context['photo'] = choice(photos)
        else:
            context['photo'] = None
        return context


class ProfileView(DetailView):
    """Private profile page view."""

    template_name = 'imagersite/profile.html'
    model = ImagerProfile
    context_object_name = 'profile'

    def get_object(self):
        """Get current user profile."""
        import pdb; pdb.set_trace()
        self.object = super(ProfileView, self).get_object()
        profile = self.request.user.profile
        photos = self.request.user.photos.all()
        ph_public = len(photos.filter(published="Public"))
        ph_private = len(photos.filter(published="Private"))
        albums = self.request.user.albums.all()
        al_public = len(albums.filter(published="Public"))
        al_private = len(albums.filter(published="Private"))
        # return {'user': user, 'ph_public': ph_public, 'ph_private': ph_private,
        #         'al_public': al_public, 'al_private': al_private}
        return profile


class OtherProfileView(DetailView):
    """Set up profile view for other users."""

    template_name = 'imagersite/profile.html'
    model = ImagerProfile
    slug_field = 'user__username'
    context_object_name = 'profile'

    def get_context_data(self, **kwargs):
        context = super(OtherProfileView, self).get_context_data(**kwargs)
        context['user'] = context['profile'].user
        return context



class ProfileEditView(UpdateView):
    """View for editing the users profile."""

    template_name = 'imagersite/edit.html'
    model = ImagerProfile
    success_url = reverse_lazy('profile')
    fields = ['website', 'location', 'fee', 'camera', 'services', 'bio', 'phone_number', 'photo_style']

    def get_object(self):
        """Return the user."""
        return self.request.user.profile
