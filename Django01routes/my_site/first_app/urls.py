from django.urls import path
from . import views

# domain.com/first_app/
urlpatterns = [
    path('simple_view', views.simple_view)
]