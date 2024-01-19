from django.shortcuts import render, redirect
from .models import Events
from .forms import EventsForm

def news(request):
    event = Events.objects.order_by('-date')
    return render(request, 'news/news.html', {'event': event})

def create_new(request):
    # check data from form
    error = ''
    if request.method == "POST":
        form = EventsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  #redirecting
        else:
            error('Bad form')
    #
    form = EventsForm()

    data = {
            'form': form,
            'error': error
        }

    return render(request, 'news/create_new.html', data)

# def news_on_page(request):
#     news = EventsForm.objects.order_by('-date')
#     return render(request, 'main/main.html', {'news_': news_})