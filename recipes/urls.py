from django.http import HttpResponse
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('recipes.urls')), # / 
    path('recipes', include('recipes.urls')), # / dominio.com/recipes/ 
]
