from django.urls import path
from . import views

# domain.com/first_app/
# LO FUNDAMENTAL ES <topic>
urlpatterns = [
    path('<str:topic>/', views.news_view), #<str:topic> nos asegura que pase una cadena de texto
    path('<int:num1>/<int:num2>', views.add_view)
]