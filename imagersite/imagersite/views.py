"""Master view file for entire app."""
from django.views.generic import TemplateView
from imager_images.models import Photo


class HomeView(TemplateView):
    """."""
    template_name = 'imagersite/home.html'
    def get_context_data(self):
        import pdb; pdb.set_trace()
        context = super(HomeView, self).get_context_data()  # get_context_data is built in method of Template View.
        photos = Photo.objects.all()
        context['photos'] = photos
        return context

# 3 options for 
# get context data
# get querry set
# get object