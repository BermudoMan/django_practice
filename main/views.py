from django.shortcuts import render
from .models import GalleryItem

def index(request):
    items = GalleryItem.objects.values('title')
    list_items = list(items)
    corr_items = []
    for i in list_items:
        j = i.values()
        j = str(j)
        j = j.replace("dict_values(['", "static/main/img/")
        j = j.replace("'])", '.jpg')
        corr_items.append(j)
    return render(request, 'main/main.html', {'items': corr_items})

def about(request):
    return render(request, 'main/about.html')

