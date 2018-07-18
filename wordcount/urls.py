from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='home'), #tutaj odnosimy sie do funkcji zawartej w zaimportowanym pliku views
    path('count/', views.count, name='count'),  
    path('about/', views.about, name='about')
]
