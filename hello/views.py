from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, "hello/index.html")

def labib(reques):
    return HttpResponse("Hello Labib")

def joty(reques):
    return HttpResponse("Hello joty i am from the fun joty")

def randf(request,name):
    return render(request, "hello/RandomName.html",{
        "name":name.capitalize()
    } )
