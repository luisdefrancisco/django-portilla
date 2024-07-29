from django.urls import path
from . import views

# domain.com/first_app/
urlpatterns = [
    path('<topic>/', views.news_view)
]