"""
Django settings for school_management_web project.
Version adaptée pour déploiement sur PythonAnywhere.
"""

import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()



BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/6.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-xn^aczsrm#_p_h)m+l-+mgjp!ma*)u*2kgec1@%wwq%p)s4$a0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ["Schoolmanage.pythonanywhere.com", "localhost", "127.0.0.1"]

# --- SÉCURITÉ ---
# La clé secrète et DEBUG sont définis via variables d'environnement,
# elles-mêmes définies dans le fichier WSGI de PythonAnywhere (voir plus bas).
# SECRET_KEY = os.environ.get('SECRET_KEY')
# DEBUG = os.environ.get('DEBUG', 'False') == 'True'
# DEBUG=True
# SECRET_KEY = os.environ.get('SECRET_KEY', 'django-insecure-cle-locale-par-defaut')



_allowed_hosts = os.environ.get('ALLOWED_HOSTS', '')
ALLOWED_HOSTS = [h.strip() for h in _allowed_hosts.split(',') if h.strip()]


# --- APPLICATIONS ---
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'Profils',
    'Relever_NA',
    'Ecoles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'school_management_web.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'school_management_web.wsgi.application'


# --- BASE DE DONNÉES ---
DATABASES = {
    "default": {
        "ENGINE": "django_libsql",
        "NAME": os.getenv("TURSO_DATABASE_URL"),
        "AUTH_TOKEN": os.getenv("TURSO_AUTH_TOKEN"),
    }
}


# --- UTILISATEUR PERSONNALISÉ ---
AUTH_USER_MODEL = 'Profils.Utilisateur'


# --- VALIDATION MOTS DE PASSE ---
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]


# --- INTERNATIONALISATION ---
LANGUAGE_CODE = 'fr-fr'
TIME_ZONE = 'Africa/Abidjan'
USE_I18N = True
USE_TZ = True


# --- FICHIERS STATIQUES ---
STATIC_URL = 'static/'
STATICFILES_DIRS = [BASE_DIR / 'static']
STATIC_ROOT = BASE_DIR / 'staticfiles'

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# --- AUTHENTIFICATION ---
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'login'






# {% if user.is_authenticated %}

#             <form method="post" action="{% url 'logout' %}">
#                 {% csrf_token %}
#                 <button type="submit">DÉCONNEXION</button>
#             </form>
#         {% else %}

#             <a href="{% url 'login' %}">CONNEXION</a>
#         {% endif %}
#  {% endcomment %}

STATIC_ROOT = BASE_DIR / "staticfiles"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

