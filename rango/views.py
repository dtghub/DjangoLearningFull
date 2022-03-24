from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Rango says hey there partner! <a href=http://127.0.0.1:8000/rango/about/>About Rango</a>")

def about(request):
    return HttpResponse("Rango says this is the about page <a href=http://127.0.0.1:8000>Go back</a>")
