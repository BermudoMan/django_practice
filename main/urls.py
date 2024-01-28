from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('', views.news, name='news'),
    path('about', views.about, name='about'),
    path('load_img', views.load_img, name='load_img'),
    path('create_new', views.create_new, name='create_new'),
]