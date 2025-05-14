from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
print('Acessar site em http://127.0.0.1:8000/contato/')

def home(request):
    return HttpResponse('VOCÊ ESTÁ EM HOME')

def contato(request):
    return HttpResponse('VOCÊ ESTÁ EM CONTATO')

def sobre(request):
    return HttpResponse('VOCÊ ESTÁ EM SOBRE')
