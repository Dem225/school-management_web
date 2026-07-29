from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate ,login
from Profils.models import Utilisateur

from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def Authantification (request):
    if request.method== 'POST':
        
        username= request.POST.get("username")
        password= request.POST.get("password")
        utilisateur=authenticate(request, username=username,password=password )
        if utilisateur is None:
            return render (request , "registration/login.html")
        
        if utilisateur.role=='admin':
            return redirect ('Tableau_de_bord_admin')

        elif utilisateur.role=='professeur':
            return  redirect ('Tableau_de_bord_professeur')

        elif utilisateur.role=='etudiant':
            return redirect ('Tableau_de_bord_etudiant')
    else:
        return render (request ,"registration/login.html", )

def Home(request):
    return render(request,"Profils/home.html" )


def ConnexionView(resquest):
    return render(resquest , "registration/login.html")

# page d'accueil pour les utilisateur

def  Tableau_de_bord_Admin(resquest):
    return render(resquest,"Profils/ADMIN/Tableau_de_bord.html" )

def  Tableau_de_bord_ETUDIANT(resquest):
    return render(resquest,"Profils/ETUDIANT/Tableau_de_bord.html" )

def  Tableau_de_bord_PROFESSEUR(resquest):
    return render(resquest,"Profils/PROFESSEUR/Tableau_de_bord.html" )


# Gestion des  utilisateurs de L'ADMIN

def  Gestions_utilisateur(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_utilisateurs.html" )



def  Gestion_Etudiant(resquest):
    return render(resquest,"Profils/ADMIN/Gestion_Etudiant.html" )

        
def  Gestions_professeur(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_professeur.html" )

        
def  Gestions_matiere(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_matiere.html" )


def  Gestion_notes(resquest):
    return render(resquest,"Profils/ADMIN/Gestion_notes.html" )



def  Gestions_absence(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_absence.html" )



def  Gestions_matiere(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_matiere.html" )

    