from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Hello World !</h1>")

def arct(request, id_arct):
    return HttpResponse("Numer n° {0}".format(id_arct))