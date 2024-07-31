from django.shortcuts import render
from django.http.response import Http404, HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse
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
        #result = 'No page found for that topic'
        #return HttpResponseNotFound(result)
        raise Http404("404 GENERIC ERROR") # 404.html

# domain.com/first_app/0 -----> domain.com/first_app/sports     
def num_page_view(request, num_page):
    topics_list = list(articles.keys()) #['sports', 'finace', 'politics']
    topic = topics_list[num_page]

    #webpage = reverse('topic-page', args=[topic])
    #return HttpResponseRedirect(webpage)
    return HttpResponseRedirect(reverse('topic-page', args=[topic]))

