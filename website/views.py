#  hello/views.py
import datetime
from django.shortcuts import render

def home(request):
	context = {'time' : datetime.datetime.now()}
	return render(request, 'website/Home.html', context)

def epoca(request):
    return render(request, 'website/epoca.html')

def recordes(request):
    return render(request, 'website/recordes.html')

def equipas(request):
    return render(request, 'website/equipas.html')

def opiniao(request):
    return render(request, 'website/opiniao.html')

def about(request):
    return render(request, 'website/about.html')

def contacto(request):
    return render(request, 'website/contacto.html')

def quizz(request):
    return render(request, 'website/quizz.html')