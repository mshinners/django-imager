from django.shortcuts import render


def home_view(request):
    """."""
    # import pdb; pdb.set_trace()

    return render(request, 'base.html')