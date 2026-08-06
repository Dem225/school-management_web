from .views import *
from django.urls import path

urlpatterns = [
    path('',Home, name='home' ),
    path('connexion/',Authantification , name='connexion'),
    path('deconnexion/',Deconnexion , name='deconnexion'),
    path('Tableau_de_bord_admin/',Tableau_de_bord_Admin , name='Tableau_de_bord_admin'),
    path('Tableau_de_bord_professeur/',Tableau_de_bord_PROFESSEUR , name='Tableau_de_bord_professeur'),


    
    path('Tableau_de_bord_etudiant/',Tableau_de_bord_ETUDIANT , name='Tableau_de_bord_etudiant'),
    path('Voirnote_etd/',Voirnote_etd , name='Voirnote_etd'),
    path('Voir_absences_etd/',Voir_absences_etd , name='Voir_absences_etd'),
    path('Voirprofil_etd/',Voirprofil_etd , name='Voirprofil_etd'),

    
    path('Gestions_utilisateur_ADMIN/',Gestions_utilisateur , name='Gestions_utilisateur_ADMIN'),
    path('ajouterutilisateur/',add_utilisateur_view , name='ajouterutilisateur'),

    path('ajoutetudiant/',add_etudiant_view , name='ajoutetudiant'),
    path('addprofesseur/',add_professeur_view , name='addprofesseur'),
    path('addmatiere/',addmatiere , name='addmatiere'),   

    path('addclasse/',addclasse , name='addclasse'),



    
    path('Gestion_Etudiant/',Gestion_Etudiant , name='Gestion_Etudiant'),
    path('Gestions_professeur/',Gestions_professeur , name='Gestions_professeur'),
    path('Gestions_matiere/',Gestions_matiere , name='Gestions_matiere'),
    path('Gestion_notes/',Gestion_notes , name='Gestion_notes'),

    path('Gestions_absence/',Gestions_absence , name='Gestions_absence'),
    path('Gestion_statistique/',Gestion_statistique , name='Gestion_statistique'), 
    path('Gestion_classe/',Gestion_classe , name='Gestion_classe'),
    
    path('modifier_etudiant/<int:id>/', UpdateEtudiant, name='modifier_etudiant'),
    path('UpdateUtilisateur/<int:id>/', UpdateUtilisateur, name='UpdateUtilisateur'),
    path('Updateprofe/<int:id>/', Updateprofe, name='Updateprofe'),
    path('Updatematier/<int:id>/', Updatematier, name='Updatematier'),

    path('Deltutilisateur/<int:id>/', Deltutilisateur, name='Deltutilisateur'),
    path('Deltettudiant/<int:id>/', Deltettudiant, name='Deltettudiant'),
    path('Deltprofe/<int:id>/', Deltprofe, name='Deltprofe'),
    path('Deltmatiere/<int:id>/', Deltmatiere, name='Deltmatiere'),
    path('UpdateClasse/<int:id>/', UpdateClasse, name='UpdateClasse'),
    path('Deltclasse/<int:id>/', Deltclasse, name='Deltclasse'),
    path('profil_veiw/',profil_veiw , name='profil_veiw'),
    path('notes_veiw/',notes_veiw , name='notes_veiw'),
    path('mes_etudiant_veiw/',mes_etudiant_veiw , name='mes_etudiant_veiw'),
    path('absence_veiw/',absence_veiw , name='absence_veiw'),

    path('addnotes/', addnotes, name='addnotes_general'),
    path('addnotes/<int:id>/',addnotes , name='addnotes'),


    

    
]


