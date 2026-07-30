from django.shortcuts import render , redirect
from django.views.generic import ListView
from django.contrib.auth import authenticate ,login
from Profils.models import Utilisateur
from Profils.forms import authis
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  Profils.forms  import Addutilisateur
from Ecoles.genere import GrMatricule
from  Profils.forms  import Addetudiant
from  Profils.forms  import Addprofesseur
from  Profils.forms  import Addmatiere
from  Profils.forms  import Addclasse

from Ecoles.models import Etudiant
from Ecoles.models import Professeur
from Ecoles.models import Matieres
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
    Utilisateurs= Utilisateur.objects.all()
    conte_Users= Utilisateur.objects.count()
    return render(resquest,"Profils/ADMIN/Gestions_utilisateurs.html", {"Utilisateurs":Utilisateurs, "conte_Users" :conte_Users}  )


def add_utilisateur_view(resquest):
    form = Addutilisateur()
    if resquest.method=='POST':
        form=Addutilisateur(resquest.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            first_name = form.cleaned_data.get('first_name')
            last_name = form.cleaned_data.get('last_name')
            email = form.cleaned_data.get('email')
            role = form.cleaned_data.get('role')
            password = form.cleaned_data.get('password')
            if Utilisateur.objects.filter(username=username).exists():
                form.add_error('username', "ce username existe déja !")
            elif Utilisateur.objects.filter(email=email).exists():
                   form.add_error('email', "ce email existe déja !")
            else:
                Utilisateur.objects.create_user(

                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role=role,
                    password=password,
                )
                form=Addutilisateur()

    context={
        'form' : form
    }
    
    return render (resquest, "Profils/ADMIN/addutilisateur.html", context)

def add_etudiant_view(resquest):
    form=Addetudiant()
    if resquest.method=='POST':
        form=Addetudiant(resquest.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            age = form.cleaned_data.get('age')
            classe = form.cleaned_data.get('classe')
            id_user = form.cleaned_data.get('id_user')
            matricule = GrMatricule()
            if Etudiant.objects.filter(matricule=matricule).exists():
                messages.error(resquest, "Erreur de génération du matricule, veuillez réessayer.")

            elif Etudiant.objects.filter(id_user=id_user).exists():
               form.add_error('id_user', "ce id_user existe déjà !")
            else:
                Etudiant.objects.create(

                    nom=nom,
                    prenom=prenom,
                    age=age,
                    classe=classe,
                    id_user=id_user,
                    matricule=matricule,

                     )
                form=Addetudiant()
                messages.success(resquest , "ÉTUDIANT AJOUTER AVEC SUCCES")
    context={
        'form' : form
    }

    return render (resquest, "Profils/ADMIN/addetudiant.html", context)

def add_professeur_view(resquest):
    form = Addprofesseur()
    if resquest.method == 'POST':
        form = Addprofesseur(resquest.POST)
        if form.is_valid():
            nom = form.cleaned_data.get('nom')
            prenom = form.cleaned_data.get('prenom')
            age = form.cleaned_data.get('age')
            classe = form.cleaned_data.get('classe')
            matiere = form.cleaned_data.get('matiere')
            id_user = form.cleaned_data.get('id_user')
            
            if Professeur.objects.filter(id_user=id_user).exists():
                form.add_error('id_user', "Ce id_user est déjà assigné à un professeur !")
            else:
                Professeur.objects.create(
                    nom=nom,
                    prenom=prenom,
                    age=age,
                    classe=classe,
                    matiere=matiere,
                    id_user=id_user,
                )
                form = Addprofesseur()
                messages.success(resquest, "PROFESSEUR AJOUTÉ AVEC SUCCÈS")
                
    context = {
        'form': form
    }

    return render(resquest, "Profils/ADMIN/addprofesseur.html", context)

def addmatiere(resquest):
    form = Addmatiere()
    if resquest.method == 'POST':
        form = Addmatiere(resquest.POST)
        if form.is_valid():
            nom = form.cleaned_data.get("nom")
            
            if Matieres.objects.filter(nom=nom).exists():
                messages.error(resquest, "CE NOM DE MATIÈRE EXISTE DÉJÀ, UTILISEZ UN AUTRE NOM")
            else:
                Matieres.objects.create(nom=nom)
                form = Addmatiere() 
                messages.success(resquest, "VOTRE MATIÈRE A BIEN ÉTÉ CRÉÉE")

    context = {
        'form': form
    }
    return render(resquest, "Profils/ADMIN/addmatiere.html", context)


          
def  Gestion_Etudiant(resquest):
    etudiant= Etudiant.objects.all()
    conte_Users= Etudiant.objects.count()
    
    return render(resquest,"Profils/ADMIN/Gestion_Etudiant.html" ,{"etudiant":etudiant, "conte_Users" :conte_Users}  )

        
def  Gestions_professeur(resquest):
    professeurs= Professeur.objects.all()
    conte_Users= Professeur.objects.count()
    return render(resquest,"Profils/ADMIN/Gestions_professeur.html"  ,{"professeurs":professeurs, "conte_Users" :conte_Users} )

        
def  Gestions_matiere(resquest):
    gsmath= Matieres.objects.all()
    conte_Users= Matieres.objects.count()
    return render(resquest,"Profils/ADMIN/Gestions_matiere.html"  ,{"gsmath":gsmath, "conte_Users" :conte_Users} )


def  Gestion_notes(resquest):
    return render(resquest,"Profils/ADMIN/Gestion_notes.html" )



def  Gestions_absence(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_absence.html" )

def Voirnote_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mes_notes.html")
def Voir_absences_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mes_absences.html")
def Voirprofil_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mon_profil.html")



#information des untilisateur admin 

