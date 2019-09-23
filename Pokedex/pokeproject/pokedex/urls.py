from django.urls import path
from .views import home, buscar

urlpatterns = [
    path('', home),
    path('buscar/', buscar),
]
