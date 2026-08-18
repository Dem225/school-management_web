from django.db import models
from Profils.models import Utilisateur


# Create your models here.


class Matieres (models.Model):
    nom=models.CharField(max_length=50)

    def __str__(self):
        return self.nom
    


class Classes (models.Model):
    code_classe = models.CharField(max_length=40, unique=True)
    nom=models.CharField(max_length=40)
   
    def __str__(self):
        return f"{self.nom} - {self.code_classe}"
    


class Etudiant (models.Model):
    nom=models.CharField(max_length=100)
    prenom =models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL,null=True)
    matricule =models.CharField(max_length=50, unique=True)
    id_user =models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='etudiant' , null=True)

    def __str__(self):
        return f"{self.nom} - {self.prenom} - {self.classe} - {self.matricule}"



 
class Professeur (models.Model):
    nom=models.CharField(max_length=100)
    prenom =models.CharField(max_length=100)
    age=models.IntegerField(default=0)
    classe = models.ForeignKey(Classes, on_delete=models.SET_NULL,null=True,blank=True)
    matiere = models.ForeignKey(Matieres, on_delete=models.CASCADE, null=True, blank=True)
    id_user =models.OneToOneField(Utilisateur, on_delete=models.CASCADE, related_name='professeur' , null=True )

    def __str__(self):  
        return f"{self.nom} - {self.matiere} - {self.classe}"


  