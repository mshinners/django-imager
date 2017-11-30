"""Create Views."""
from django.shortcuts import render


def home_view(request):
    """Create Home View."""
    # import pdb; pdb.set_trace()

    return render(request, 'imagersite/home.html')

