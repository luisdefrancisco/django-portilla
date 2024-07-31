from django.urls import path
from . import views

# domain.com/first_app/
# LO FUNDAMENTAL ES <topic>
urlpatterns = [
    path('<int:num_page>', views.num_page_view),
    path('<str:topic>', views.news_view, name='topic-page'), #<str:topic> nos asegura que pase una cadena de texto
]