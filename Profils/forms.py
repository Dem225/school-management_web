from django import forms
from .models import Utilisateur
from Ecoles.models import Classes
from Ecoles.models import Etudiant
from Ecoles.models import Matieres 
from Ecoles.models import Professeur
from  Relever_NA.models import Notes
from  Relever_NA.models import Absence

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







class Notesetudiant(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ['note' , 'date'] # Ou ['matricule', 'note'] selon les champs de ton modèle Notes
        
        widgets = {
            'note': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Entrez la note'
            }), 
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }
    def clean_note(self):
        note = self.cleaned_data.get('note')
        if note is not None and (note < 0 or note > 20):
            raise forms.ValidationError("La note doit être comprise entre 0 et 20.")
        return note

class AbsenceForm(forms.ModelForm):
    class Meta:
        model = Absence
        fields = ['date', 'status', 'heure' , 'matiere']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
            'heure': forms.DateTimeInput(attrs={'type': 'datetime-local', 'class': 'form-control'}),
            'matiere': forms.Select(attrs={'class': 'form-control'}),
        }