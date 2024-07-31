from django.shortcuts import render
from django.http.response import HttpResponse #Linea importante
# Create your views here.

def simple_view(request):
    return HttpResponse("El contenido de la web") # TEMPLATE HTML (JINJA)

