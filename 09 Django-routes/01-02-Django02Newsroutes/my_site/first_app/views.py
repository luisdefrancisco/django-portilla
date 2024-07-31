from django.shortcuts import render
from django.http.response import HttpResponse
# Create your views here.

#CREAMOS UN DICCIONARIO PARA PODER HACER LAS VISTAS DINÁMICAS
articles = { 
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic): # AÑADIMOS topic que será la KEY del dicionario que utilizamos abajo
    return HttpResponse(articles[topic]) # future TEMPLATE HTML (JINJA)

def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(str(result))


