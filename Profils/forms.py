from django import forms
from .models import Utilisateur
from Ecoles.models import Classes
from Ecoles.models import Etudiant
from Ecoles.models import Matieres 
from Ecoles.models import Professeur
from  Relever_NA.models import Notes


class authis( forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class": "inputuser",
        "placeholder": "Nom d'utilisateur"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "inputpassword",
        "placeholder": "  mot de passe "
    }))





class Addutilisateur(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'email', 'role', 'password']



        widgets={
                'username': forms.TextInput(attrs={
                    'placeholder': "Entrez le nom d'utilisateur"
                }),
                'first_name': forms.TextInput(attrs={
                    'placeholder': 'Entrez le prénom'
                }),
                'last_name': forms.TextInput(attrs={
                    'placeholder': 'Entrez le nom'
                }),
                'email': forms.EmailInput(attrs={
                    'placeholder': 'exemple@domaine.com'
                }),
                'role': forms.Select(attrs={
                }),
                'password': forms.PasswordInput(attrs={
                    'placeholder': 'Mot de passe sécurisé'
                }),
            }


class Addutilisateurpasse(forms.ModelForm):
    # password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = Utilisateur
        fields = ['username', 'first_name', 'last_name', 'email', 'role', ]



        widgets={
                'username': forms.TextInput(attrs={
                    'placeholder': "Entrez le nom d'utilisateur"
                }),
                'first_name': forms.TextInput(attrs={
                    'placeholder': 'Entrez le prénom'
                }),
                'last_name': forms.TextInput(attrs={
                    'placeholder': 'Entrez le nom'
                }),
                'email': forms.EmailInput(attrs={
                    'placeholder': 'exemple@domaine.com'
                }),
                'role': forms.Select(attrs={
                }),
            }













class Addetudiant(forms.ModelForm):
    class Meta:
        model=Etudiant
        fields=['nom','prenom', 'age' , 'classe','id_user',]

        widgets={
             'nom': forms.TextInput(attrs={
                                 'placeholder': 'Entrez le nom'
                             }),
            'prenom': forms.TextInput(attrs={
                                             'placeholder': 'Entrez le prenom'
                                         }),
            'age': forms.NumberInput(attrs={
                                             'placeholder': 'Entrez le age'
                                         }),
            'classe': forms.Select(attrs={
                                             'placeholder': 'Entrez le classe'
                                         }),

            'id_user': forms.Select(attrs={
                                             
                                         }),
        }






class Addprofesseur(forms.ModelForm):
    class Meta:
            model=Professeur
            fields=['nom','prenom', 'age' , 'classe', 'matiere', 'id_user',]

            widgets={
                        'nom': forms.TextInput(attrs={
                                            'placeholder': 'Entrez le nom'
                                        }),
                        'prenom': forms.TextInput(attrs={
                                                        'placeholder': 'Entrez le prenom'
                                                    }),
                        'age': forms.NumberInput(attrs={
                                                        'placeholder': 'Entrez le age'
                                                    }),
                        'classe': forms.Select(attrs={
                                                        
                                                    }),
                        'matiere': forms.Select(attrs={
                                                       
                                                    }),
            
                        'id_user': forms.Select(attrs={
                                                        
                                                    }),
                    }




class Addmatiere(forms.ModelForm):
    class Meta:
             model=Matieres
             fields=['nom']
             widgets={
                        'nom': forms.TextInput(attrs={
                                         'placeholder': 'Entrez le nom de la Matieres'
                                     }),
                                     
                     }


class Addclasse(forms.ModelForm):
    class Meta:
             model=Classes
             fields=['nom']
             widgets={
                         'nom': forms.TextInput(attrs={
                            'placeholder': 'Entrez le nom de la classe '
                                             }),
                                                  
                    }









class Notesetudiant(forms.Form):
    class Meta:
         model= Etudiant
         model = Notes
         fields=['matricule', 'notes' ]



         widgets={
                                  'matricule': forms.TextInput(attrs={
                                                     'placeholder': 'ENTRZ LE MATRICULE'
                                                 }),
                                 'notes': forms.TextInput(attrs={
                                                                 'placeholder': 'Entrez le prenom'
                                                             })
                             }