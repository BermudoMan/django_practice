from django.shortcuts import render, redirect
from .models import GalleryItem, Events
from .forms import EventsForm, UploadFileForm


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

def load_img2(request):
    error_img = ''
    if request.method == "POST":
        form_img = LoadImageForm(request.POST)
        if form_img.is_valid():
            form_img.save()
            return redirect('home')
        else:
            error_img('Bad form')


    form_img = LoadImageForm()

    data_img = {
        'form_img': form_img,
        'error_img': error_img
    }

    return render(request, 'main/load_img.html', data_img)


def handle_uploaded_file(f):
    with open(f"main/static/main/img/{f.name}", "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)

def load_img(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            fp = GalleryItem(file=form.cleaned_data['file'])
            fp.save()
#             handle_uploaded_file(form.cleaned_data['file'])
    else:
        form = UploadFileForm(request.POST, request.FILES)
    return render(request, 'main/load_img.html', {'form': form})
