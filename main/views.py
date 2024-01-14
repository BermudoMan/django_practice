from django.shortcuts import render
from .models import GalleryItem

def index(request):
    items = GalleryItem.objects.values_list('way')
    return render(request, 'main/main.html', {'items': items})

def about(request):
    return render(request, 'main/about.html')

