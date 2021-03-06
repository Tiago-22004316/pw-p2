"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from django.shortcuts import render
from . import views

app_name = "website"

urlpatterns = [
    path('', views.home, name='Home'),
    path('Home', views.home, name='Home'),
    path('Recordes', views.recordes, name='recordes'),
    path('Equipas', views.equipas, name='equipas'),
    path('Época', views.epoca, name='epoca'),
    path('Quizz', views.quizz, name='quizz'),
    path('Opinião', views.opiniao, name='opiniao'),
    path('Contacto', views.contacto, name="contacto"),
    path('About', views.about, name='about'),
]