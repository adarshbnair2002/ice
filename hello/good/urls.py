from django.contrib import admin
from django.urls import path
from good import views


urlpatterns = [
    path("", views.index, name='good'),
    path("register", views.register, name='register'),
    path("contact", views.contact, name='contact'),
    path("home", views.home, name='home'),
    

]
