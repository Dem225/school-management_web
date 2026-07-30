from datetime import datetime
import random

from  .models import Etudiant




def GrMatricule():
    date = datetime.now().year
    nombre = str(random.randint(1000, 9999))
    matricule = f"ET-{date}-{nombre}"
    
    
    while Etudiant.objects.filter(matricule=matricule).exists():
        nombre = str(random.randint(1000, 9999))  
        matricule = f"ET-{date}-{nombre}"
        
    return matricule