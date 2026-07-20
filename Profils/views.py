from django.shortcuts import render
from django.views.generic import ListView

# Create your views here.



def Home(request):
    return render(request,"Profils/home.html" )


def ConnexionView(resquest):
    return render(resquest , "Profils/connexion.html")



