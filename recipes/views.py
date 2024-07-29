from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('HOME')

def contato(request):  
    return HttpResponse("CONTATO") 

def sobre(request):  
    return HttpResponse("SOBRE") 
