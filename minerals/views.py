from django.shortcuts import render, get_object_or_404

from .models import Mineral


def home_page(request):
    """View displays list of mineral names with links"""
    minerals = Mineral.objects.all()
    return render(request, 'index.html', {'minerals': minerals})


def detail(request, pk):
    """View displays individual mineral details"""
    mineral = get_object_or_404(Mineral, pk=pk)
    return render(request, 'detail.html', {'mineral': mineral})
