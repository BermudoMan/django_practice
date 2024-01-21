from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.news, name='news'),
    path('about', views.about, name='about'),
    path('create_new', views.create_new, name='create_new'),
]