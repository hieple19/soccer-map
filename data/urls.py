from django.urls import path

from . import views

urlpatterns = [
    path('', views.soccer, name='soccer'),
    path('search/', views.search, name='search'),
    path('map/', views.map, name='map'),
]