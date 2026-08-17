from django.db import models
from  Ecoles.models import Matieres
from  Ecoles.models import Etudiant
from django.utils import timezone
# Create your models here.




class Notes(models.Model):
    note = models.FloatField(help_text="Note sur 20")
    matricule = models.ForeignKey(to=Etudiant, on_delete=models.CASCADE, related_name='etudiant', null=True)
    matiere_id = models.ForeignKey(to=Matieres, on_delete=models.CASCADE, related_name='notes', null=True)
    date = models.DateField(default=timezone.now)



class Absence(models.Model):
    STATUT_CHOICES = [
        (0, 'Non justifié'),
        (1, 'Justifié'),
    ]
    student = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    heure = models.DateTimeField(default=timezone.now)
    matiere = models.ForeignKey(Matieres, on_delete=models.CASCADE, related_name='etudiant', null=True)
    status = models.IntegerField(choices=STATUT_CHOICES, default=0)

    def __str__(self):
        return f"{self.student} - Statut : {self.get_status_display()}"