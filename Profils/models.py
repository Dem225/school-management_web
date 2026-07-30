from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Utilisateur(AbstractUser):
    ROLES = [
        ('admin', 'administrateur'),
        ('professeur', 'professeur'),
        ('etudiant', 'etudiant'),
    ]
    
    role = models.CharField(max_length=40, choices=ROLES, default='etudiant')
    

    email = models.EmailField(unique=True)

    
    REQUIRED_FIELDS = ['email', 'role', 'first_name', 'last_name']

    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.get_role_display()} ({self.username})"