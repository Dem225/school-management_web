from .views import *
from django.urls import path

urlpatterns = [
    path('',Home, name='home' ),
    path('connexion/',Authantification , name='connexion'),
    path('deconnexion/',Deconnexion , name='deconnexion'),
    path('Tableau_de_bord_admin/',Tableau_de_bord_Admin , name='Tableau_de_bord_admin'),
    path('Tableau_de_bord_professeur/',Tableau_de_bord_PROFESSEUR , name='Tableau_de_bord_professeur'),
    path('Tableau_de_bord_etudiant/',Tableau_de_bord_ETUDIANT , name='Tableau_de_bord_etudiant'),
    path('Gestions_utilisateur_ADMIN/',Gestions_utilisateur , name='Gestions_utilisateur_ADMIN'),
    path('Gestion_Etudiant/',Gestion_Etudiant , name='Gestion_Etudiant'),
    path('Gestions_professeur/',Gestions_professeur , name='Gestions_professeur'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
    path('Gestion_notes/',Gestion_notes , name='Gestion_notes'),
    path('Gestions_absence/',Gestions_absence , name='Gestions_absence'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
]


