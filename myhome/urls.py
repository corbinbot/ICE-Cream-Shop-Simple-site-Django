
from django.contrib import admin
from django.urls import path
from myhome import views


urlpatterns = [
    path("", views.index, name='myhome'),
    path("about", views.about, name='aboutpage'),
    path("services", views.services, name='servicepage'),
    path("contacts", views.contacts, name='contactepage') 
]