#Day 66: New views.py file-I acknowledge that this might be a bit redundant. Refactoring is coming soon. 

from django.shortcuts import render

def index(request):
    """Home Page"""
    return render(request, 'forest/index.html')

def menu_1(request):
    context = {'menu_1': menu_1}
    return render(request, 'forest/menu_1.html')

def menu_2(request):
    context = {'menu_2': menu_2}
    return render(request, 'forest/menu_2.html')
    
def menu_3(request):
    context = {'menu_3': menu_3}
    return render(request, 'forest/menu_3.html')

def menu_4(request):
    context = {'menu_4': menu_4}
    return render(request, 'forest/menu_4.html')

def menu_5(request):
    context = {'menu_5': menu_5}
    return render(request, 'forest/menu_5.html')

def menu_6(request):
    context = {'menu_6': menu_6}
    return render(request, 'forest/menu_6.html')

def menu_7(request):
    context = {'menu_7': menu_7}
    return render(request, 'forest/menu_7.html')
    
def myitems(request):
    context = {'myitems': myitems}
    return render(request, 'forest/myitems.html')

def register(request):
    context = {'register': register}
    return render(request, 'forest/register.html')
    
 #Updated settings.py: Lots of commented out stuff that I don't want to lose-probably some value but I can't get images to work yet.
 
 """
Django settings for rice_forest project.

Generated by 'django-admin startproject' using Django 2.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.2/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '84y!w3s2fx)+d0qc_bo0yt)^!utt9mex9iz_l8f4rj1_q!-kfp'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #Third-Party
    'bootstrap3',
    
    #Additions
    'forest',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'rice_forest.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'rice_forest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/

STATIC_URL = '/static/'

#My settings

#Settings for django-bootstrap3
BOOTSTRAP3 = {
    'include_jquery': True,
}
