from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate ,login
from Profils.models import Utilisateur
from Profils.forms import authis
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.

def Authantification (request):
    form= authis()
    if request.method== 'POST':
        
        form=authis(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            
            user=authenticate(request, username=username,password=password )
            
            if user is not None:
                login(request,user)
                role = user.role
                if role=='admin':
                    return redirect ('Tableau_de_bord_admin')

                elif role=='professeur':
                    return  redirect ('Tableau_de_bord_professeur')

                elif role =='etudiant':
                    return redirect ('Tableau_de_bord_etudiant')

            messages.error(request,"votre Nom d 'utilisateur ou mot de passe incorrest ")
        

            
    return render (request ,"Profils/connexion.html", {'forms':form})




def Home(request):
    return render(request,"Profils/home.html" )


def ConnexionView(resquest):
    return render(resquest , "Profils/connexion.html")

def Deconnexion(request):
    return redirect('connexion')



    
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



    