from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Rango says hey there partner! <a href='/webapp/about/'>About</a>")

def about(request):
    return HttpResponse("This is the about page <a href='/webapp/'>Index</a>")
