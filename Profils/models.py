from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class Utilisateur (AbstractUser):
    ROLES=[
        ('admin','administrateur'),
        ('professeur', 'professeur'),
        ('etudiant','etudiant')
        ]
    role=models.CharField(max_length=40, choices=ROLES)


    REQUIRED_FIELDS=  ['email' , 'role' ]
    
    def __str__(self):
         return f"{self.first_name} {self.last_name} ({self.username})"