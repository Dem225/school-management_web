from django.db import models
from  Ecoles.models import Matieres
from  Ecoles.models import Etudiant
# Create your models here.


class Notes(models.Model):
    note = models.FloatField(help_text="Note sur 20")
    student_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='notes', null=True)
    matiere_id = models.ForeignKey(Matieres, on_delete=models.CASCADE, related_name='notes', null=True)

    def __str__(self):
        return f"{self.student_id} - {self.matiere_id} : {self.note}/20"


class Absence(models.Model):
    
    STATUT_CHOICES = [
        (0, 'Non justifié'),
        (1, 'Justifié'),
    ]

    student_id = models.ForeignKey(Etudiant, on_delete=models.CASCADE, related_name='absences')
    date = models.DateField()
    status = models.IntegerField(choices=STATUT_CHOICES, default=0)

    def __str__(self):
            return f"{self.student_id} - {self.status}"
    
    