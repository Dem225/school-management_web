from functools import wraps
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.shortcuts import redirect

def role_required(role_attr, redirect_url='connexion'):
    def decorator(view_func):
        @wraps(view_func)
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_authenticated:
                messages.error(request, "Vous devez être connecté.")
                return redirect('connexion')

            try:
                getattr(request.user, role_attr)
            except (ObjectDoesNotExist, AttributeError):
                messages.error(request, "Accès refusé : vous n'avez pas les droits pour cette page.")
                return redirect(redirect_url)

            return view_func(request, *args, **kwargs)
        return _wrapped_view
    return decorator


# Raccourcis prêts à l'emploi
def professeur_required(view_func):
    return role_required('professeur')(view_func)

def etudiant_required(view_func):
    return role_required('etudiant')(view_func)

def admin_required(view_func):
    return role_required('admin')(view_func)