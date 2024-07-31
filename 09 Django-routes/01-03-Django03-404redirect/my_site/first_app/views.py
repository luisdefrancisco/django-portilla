from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound
# Create your views here.

#CREAMOS UN DICCIONARIO PARA PODER HACER LAS VISTAS DINÁMICAS
articles = { 
    'sports': 'Sports Page',
    'finance': 'Finance Page',
    'politics': 'Politics Page'
}

def news_view(request, topic): # AÑADIMOS try exept por si no encuentra la pagina en el diccionario
    try:
        result = articles[topic]
        return HttpResponse(articles[topic]) # future TEMPLATE HTML (JINJA)
    except:
        result = 'No page found for that topic'
        #return HttpResponseNotFound(result)
        raise Http404("404 GENERIC ERROR") # 404.html
    
def add_view(request, num1, num2):
    # domain.com/first_app/num1/num2 --> num1+num2
    add_result = num1 + num2
    result = f'{num1} + {num2} = {add_result}'
    return HttpResponse(str(result))


