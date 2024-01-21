from django.shortcuts import render, redirect
from .models import GalleryItem, Events
from .forms import EventsForm


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

    event = Events.objects.order_by('-date')

    return render(request, 'main/main.html', {'items': corr_items, 'event': event})

def about(request):
    return render(request, 'main/about.html')

# def news(request):
#     event = Events.objects.order_by('-date')
#     return render(request, 'main/main.html', {'event': event})


def create_new(request):
    # check data from form
    error = ''
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error('Bad form')
    #
    form = EventsForm()

    data = {
            'form': form,
            'error': error
        }

    return render(request, 'main/create_new.html', data)