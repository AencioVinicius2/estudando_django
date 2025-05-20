from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
print('Acessar site em http://127.0.0.1:8000/contato/')

def home(request):
    return render(request,'recipes/home.html')

def contato(request):
    return render(request,'temp/temp.html')

def sobre(request):
    return HttpResponse('VOCÊ ESTÁ EM SOBRE')
