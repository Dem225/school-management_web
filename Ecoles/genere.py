from datetime import datetime
import random

from  .models import Etudiant

from  .models import Classes


def GrMatricule():
    date = datetime.now().year
    nombre = str(random.randint(1000, 9999))
    matricule = f"ET-{date}-{nombre}"
    
    
    while Etudiant.objects.filter(matricule=matricule).exists():
        nombre = str(random.randint(1000, 9999))  
        matricule = f"ET-{date}-{nombre}"
        
    return matricule




def CodeClasse():
    date=datetime.now().year
    nombre=str(random.randint(50, 400))
    matricule=f"CD-{date}-{nombre}"

    while Classes.objects.filter(code_classe=matricule).exists():

        nombre=str(random.randint(50, 400))
        matricule=f"CD-{date}-{nombre}"


    return matricule