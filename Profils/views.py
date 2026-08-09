from django.contrib.auth.decorators import login_required
from django.shortcuts import render , redirect , get_object_or_404
from django.views.generic import ListView
from django.contrib.auth import authenticate ,login
from Profils.models import Utilisateur
from Profils.forms import authis
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from  Profils.forms  import Addutilisateur 
from  Profils.forms  import Addutilisateurpasse
from Ecoles.genere import GrMatricule 
from Ecoles.genere import  CodeClasse
from  Profils.forms  import Addetudiant
from  Profils.forms  import Addprofesseur
from  Profils.forms  import Addmatiere
from  Profils.forms  import Addclasse
from Relever_NA.models import Notes
from Ecoles.models import Etudiant
from Ecoles.models import Professeur
from Ecoles.models import Matieres
from Ecoles.models import Classes

from  Profils.forms  import Notesetudiant

from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def Authantification (request):
    form= authis()
    if request.method== 'POST':
        
        form=authis(request.POST)
        
        if form.is_valid():
            username= form.cleaned_data["username"]
            password= form.cleaned_data["password"]
            
            user=authenticate(request, username=username,password=password )
            print(user)
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
                messages.add_error('username', "ce username existe déja !")
            elif Utilisateur.objects.filter(email=email).exists():
                   messages.add_error('email', "ce email existe déja !")
            else:
                Utilisateur.objects.create_user(

                    username=username,
                    first_name=first_name,
                    last_name=last_name,
                    email=email,
                    role=role,
                    password=password
                )
                form=Addutilisateur()
                messages.success(resquest , "UTILISATEUR AJOUTER AVEC SUCCES")
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
                messages.error(resquest, "Erreur de génération du matricule, veuillez réessayer. svp")

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

def addclasse(resquest):
    form=Addclasse()
    if resquest.method=='POST':
        form=Addclasse(resquest.POST)
        if form.is_valid():
            nom = form.cleaned_data.get("nom")
            code_classe =CodeClasse()
            if Classes.objects.filter(nom=nom).exists():
                messages.error(resquest, "Cette classe existe déjà")
            else:
               
                Classes.objects.create(nom=nom, code_classe=code_classe)
                form = Addclasse()
                messages.success(resquest, "Classe ajoutée avec succès")
    context={
        "form" :form
    }
    return  render (resquest , "Profils/ADMIN/addclasse.html", context)




def  Gestion_Etudiant(resquest):
    etudiant= Etudiant.objects.all()
    conte_Users= Etudiant.objects.count()
    
    return render(resquest,"Profils/ADMIN/Gestion_Etudiant.html" ,{"etudiant":etudiant, "conte_Users" :conte_Users}  )

        
def  Gestions_professeur(resquest):
    professeurs= Professeur.objects.all()
    conte_Users= Professeur.objects.count()
    return render(resquest,"Profils/ADMIN/Gestions_professeur.html"  ,{"professeurs":professeurs, "conte_Users" :conte_Users} )


def Gestion_classe(resquest):
    classe=Classes.objects.all()
    conte_calssse=Classes.objects.count()
    return render(resquest , "Profils/ADMIN/Gestionsclasse.html", {"classe":classe, "conte_calssse" :conte_calssse})
        
def  Gestions_matiere(resquest ):
    gsmath= Matieres.objects.all()
    conte_Users= Matieres.objects.count()
    return render(resquest,"Profils/ADMIN/Gestions_matiere.html"  ,{"gsmath":gsmath, "conte_Users" :conte_Users} )




def  Gestion_notes(resquest):
    return render(resquest,"Profils/ADMIN/Gestion_notes.html" )

def  Gestion_statistique(resquest):
    return render(resquest,"Profils/ADMIN/Gestionstatistique.html" )


def  Gestions_absence(resquest):
    return render(resquest,"Profils/ADMIN/Gestions_absence.html" )

def Voirnote_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mes_notes.html")
def Voir_absences_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mes_absences.html")
def Voirprofil_etd(resquest):
    return render (resquest,"Profils/ETUDIANT/Mon_profil.html")



#information des untilisateur admin 

#modifier et supprimer pour admin


def UpdateEtudiant(resquest,id):

    etudiants=get_object_or_404(Etudiant, id=id)
    form=Addetudiant(instance=etudiants)
    if resquest.method=="POST":
        form=Addetudiant(resquest.POST, instance=etudiants)
        if form.is_valid():
            form.save()
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
            return redirect('Gestion_Etudiant')
        else:
            form=Addetudiant(instance=etudiants)
            messages.success(resquest, "MODIFICATIONs EFFECTUÉE AVEC SUCCÈS")
    context = {
        'form': form,
        'etudiants': etudiants 
    }
  
    return render(resquest, "Profils/ADMIN/modifierEtudiant.html", context)


def UpdateClasse(resquest,id):

    classe=get_object_or_404(Classes, id=id)
    form=Addclasse(instance=classe)
    if resquest.method=="POST":
        form=Addclasse(resquest.POST, instance=classe)
        if form.is_valid():
            form.save()
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
            return redirect('Gestion_classe')
        else:
            form=Addclasse(instance=classe)
            messages.success(resquest, "MODIFICATIONs EFFECTUÉE AVEC SUCCÈS")
    context = {
        'form': form,
        'classe': classe 
    }
  
    return render(resquest, "Profils/ADMIN/modifierclasse.html", context)



def UpdateUtilisateur(resquest,id):

    Utils=get_object_or_404(Utilisateur, id=id)
    form=Addutilisateurpasse(instance=Utils)
    if resquest.method=="POST":
        form=Addutilisateurpasse(resquest.POST, instance=Utils)
        if form.is_valid():
            form.save()
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
            return redirect('Gestions_utilisateur_ADMIN')
        else:
            form=Addutilisateurpasse(instance=Utils)
            messages.success(resquest, "MODIFICATIONs EFFECTUÉE AVEC SUCCÈS")
    context = {
        'form': form,
        'Utils': Utils 
    }
  
    return render(resquest, "Profils/ADMIN/modifierutilisateur.html", context)





def Updateprofe(resquest,id):

    profe=get_object_or_404(Professeur, id=id)
    form=Addprofesseur(instance=profe)
    if resquest.method=="POST":
        form=Addprofesseur(resquest.POST, instance=profe)
        if form.is_valid():
            form.save()
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
            return redirect('Gestions_professeur')
        else:
            form=Addprofesseur(instance=profe)
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
    context = {
        'form': form,
        'profe': profe 
    }
  
    return render(resquest, "Profils/ADMIN/modifierprofe.html", context)





def Updatematier(resquest,id):

    Mathiere=get_object_or_404(Matieres, id=id)
    form=Addmatiere(instance=Mathiere)
    if resquest.method=="POST":
        form=Addmatiere(resquest.POST, instance=Mathiere)
        if form.is_valid():
            form.save()
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
            return redirect('Gestions_matiere')
        else:
            form=Addmatiere(instance=Mathiere)
            messages.success(resquest, "MODIFICATION EFFECTUÉE AVEC SUCCÈS")
    context = {
        'form': form,
        'Mathiere': Mathiere 
    }
  
    return render(resquest, "Profils/ADMIN/modifiermatiere.html", context)




#SUPPRIMER

def Deltutilisateur(resquest, id):
    if resquest.method=="POST":
        recipe=get_object_or_404(Utilisateur, id=id)
        recipe.delete()
        messages.success(resquest, "Utilisateur supprimer avce success")
        return redirect("Gestions_utilisateur_ADMIN")
    messages.success(resquest , "Envoyer uniqueent en post ")
    return redirect("Gestions_utilisateur_ADMIN")



def Deltettudiant(resquest, id):
    if resquest.method=="POST":
        recipe=get_object_or_404(Etudiant, id=id)
        recipe.delete()
        messages.success(resquest, "Utilisateur supprimer avce success")
        return redirect("Gestions_utilisateur_ADMIN")
    messages.success(resquest , "Envoyer uniqueent en post ")
    return redirect("Gestions_utilisateur_ADMIN")


def Deltprofe(resquest, id):
    if resquest.method=="POST":
        recipe=get_object_or_404(Professeur, id=id)
        recipe.delete()
        messages.success(resquest, "Utilisateur supprimer avce success")
        return redirect("Gestions_utilisateur_ADMIN")
    messages.success(resquest , "Envoyer uniqueent en post ")
    return redirect("Gestions_utilisateur_ADMIN")



def Deltmatiere(resquest, id):
    if resquest.method=="POST":
        recipe=get_object_or_404(Matieres, id=id)
        recipe.delete()
        messages.success(resquest, "MATIERE SUPPRIMER supprimer avce success")
        return redirect("Gestions_matiere")
    messages.success(resquest , "Envoyer uniqueent en post ")
    return redirect("Gestions_matiere")


def Deltclasse(resquest, id):
    if resquest.method=="POST":
        recipe=get_object_or_404(Classes, id=id)
        recipe.delete()
        messages.success(resquest, "MATIERE SUPPRIMER supprimer avce success")
        return redirect("Gestion_classe")
    messages.success(resquest , "Envoyer uniqueent en post ")
    return redirect("Gestion_classe")




#  GESTIONS DE ETUDIANT


def profil_veiw(resquest):
    try:
            professeur = resquest.user.professeur
    except ObjectDoesNotExist:
            professeur = None 
    context = {
            'professeur': professeur,
        }
    
    return render(resquest , "Profils/PROFESSEUR/profil.html" , context)
@login_required
def notes_veiw(resquest):

    professeur = getattr(resquest.user, 'professeur', None)
    
    if professeur and professeur.matiere:
        notes = Notes.objects.filter(matiere=professeur.matiere)
    else:
        notes = Notes.objects.none()
  
    context = {
        'notes': notes,
        'professeur': professeur,
    }
    return render(resquest , "Profils/PROFESSEUR/notes.html" , context)


def mes_etudiant_veiw(resquest):
    try:
        professeur = resquest.user.professeur
    except ObjectDoesNotExist:
        professeur = None

    if professeur and professeur.classe:
        etudiants=Etudiant.objects.filter(classe=professeur.classe)
    else:
        etudiants=Etudiant.objects.none()


    context={
        'etudiants':etudiants,
        'matieres':professeur.matiere if professeur else None,
        'classe': professeur.classe if professeur else None
    }

    return render(resquest , "Profils/PROFESSEUR/mes_etudiant.html", context )
def absence_veiw(resquest):
    return render(resquest , "Profils/PROFESSEUR/absence.html" )



#AJOUTEZ DES NOTES A UN ETUDIANT POUR LE PROFFESSEUR
def addnotes(request, id=None):
    try:
        professeur = request.user.professeur
    except ObjectDoesNotExist:
        professeur = None

    etudiant = get_object_or_404(Etudiant, id=id) if id else None
    matiere = professeur.matiere if professeur else None

    if request.method == 'POST':
        form = Notesetudiant(request.POST)
        if form.is_valid():
            note_obj = form.save(commit=False)
            note_obj.etudiant = etudiant
            note_obj.matiere = matiere
            note_obj.save()
            messages.success(request, "Note ajoutée avec succès !")
            return redirect('mes_etudiant_veiw')  
        else:
            messages.error(request, "Erreur : vérifiez la note saisie.")
            return redirect('mes_etudiant_veiw')
    else:
        form = Notesetudiant()

    context = {'form': form, 'etudiant': etudiant, 'matiere': matiere}
    return render(request, "Profils/PROFESSEUR/addnotes.html", context)