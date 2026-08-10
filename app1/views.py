from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def hello_world(request):
    return render(request, "app1/hello_world.html")

def home(request):
    return render(request, "app1/home.html")

def acerca_de_mi(request):
    return render(request, "app1/acerca_de_mi.html")