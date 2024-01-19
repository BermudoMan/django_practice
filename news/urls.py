from django.urls import path
from . import views

urlpatterns = [
    path('', views.news, name='news'),
    path('create_new', views.create_new, name='create_new'),
    # path('', views.news_on_page, name='news_on_page'),
]
