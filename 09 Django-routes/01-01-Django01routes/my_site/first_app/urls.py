from django.urls import path
from . import views  #Importamos el archivo views de la misma carpeta

# domain.com/first_app/
urlpatterns = [
    path('simple_view', views.simple_view) #Para el domain.com/first_app/simple_view
    # carga la funcion simple_view de views, por eso lo hemos importado
    # Si queremos que el path solo sea first_app ponemos entre comillas nada 
]