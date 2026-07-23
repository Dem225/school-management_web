from .views import *
from django.urls import path

urlpatterns = [
    path('',Home, name='home' ),
    path('connexion/',ConnexionView , name='connexion'),
]


