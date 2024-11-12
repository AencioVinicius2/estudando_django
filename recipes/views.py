from django.shortcuts import render

# Create your views here.

def home(request):
    return render(request, 'recipes/home.html')

def contato(request):  
    return render("CONTATO") 

def sobre(request):  
    return render("SOBRE") 
