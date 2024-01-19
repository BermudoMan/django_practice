from django.shortcuts import render
from .models import GalleryItem
from news.models import Events

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

def news_on_page(request):
    event = Events.objects.all()
    return render(request, 'main/layout.html', {'event': event})


