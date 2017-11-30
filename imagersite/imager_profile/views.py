"""Create Views."""
from django.shortcuts import render


def home_view(request):
    """Create home view callable."""
    return render(request, 'imagersite/home.html')


def login(request):
    """Create login view callable."""
    return render(request, 'imagersite/login.html')

