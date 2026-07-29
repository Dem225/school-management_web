from django import forms


class authis( forms.Form):

    username=forms.CharField(widget=forms.TextInput(attrs={
        "class": "inputuser",
        "placeholder": "Nom d'utilisateur"
    }))
    password=forms.CharField(widget=forms.PasswordInput(attrs={
        "class": "inputpassword",
        "placeholder": "  mot de passe "
    }))








































