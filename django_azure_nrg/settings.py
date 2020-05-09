"""
Django settings for django_azure_nrg project.

Generated by 'django-admin startproject' using Django 3.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'b54i)k+4)u@8uon*c%b5b)&$@x9wxqs3)0+b0mrr^-ho*jmv4v'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['localhost', '127.0.0.1','*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

#    'debug_toolbar',
    'extra_views',
#    'datetimewidget',
    'django_filters',
    'django_tables2',
    'django_bootstrap_breadcrumbs',

    'crispy_forms',

#    'countries',

    'countries.apps.CountriesConfig',
    'metrics.apps.MetricsConfig',
    'fetchparams.apps.FetchparamsConfig',
    'scheduler.apps.SchedulerConfig',
    'datapool.apps.DatapoolConfig',
    
]

MIDDLEWARE = [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',    
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'django_azure_nrg.urls'

DJANGO_TABLES2_TEMPLATE = 'django_tables2/bootstrap4.html'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
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

WSGI_APPLICATION = 'django_azure_nrg.wsgi.application'

INTERNAL_IPS = [
    # ...
    '127.0.0.2',
    # ...
]



# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'sql_server.pyodbc',
        'NAME': 'nrg-trading-db',
        'HOST': 'tcp:nrg-trading-srv.database.windows.net',
        #'HOST': 'kapassle',
        'USER': 'trading-usr',
        'PASSWORD': 'Tr@d1ng!',
        'PORT': '',
        'OPTIONS': {
            'driver': 'ODBC Driver 17 for SQL Server',
        },
     }
}

        
##    'default': {
##        'ENGINE': 'sql_server.pyodbc',
##        'NAME': 'nrg-trading-db-django',
##        #'HOST': 'tcp:nrg-trading-srv.database.windows.net',
##        'HOST': 'kapassle',
##        'USER': 'trading-usr',
##        'PASSWORD': 'Tr@d1ng!',
##        'PORT': '',
##        'OPTIONS': {
##            'driver': 'ODBC Driver 17 for SQL Server',
##        },        
##     },
##    'maindata': {
##        'ENGINE': 'sql_server.pyodbc',
##        'NAME': 'nrg-trading-db',
##        'HOST': 'tcp:nrg-trading-srv.database.windows.net',
##        #'HOST': 'kapassle',
##        'USER': 'trading-usr',
##        'PASSWORD': 'Tr@d1ng!',
##        'PORT': '',
##        'OPTIONS': {
##            'driver': 'ODBC Driver 17 for SQL Server',
##        },        
##     }
##}


##DATABASES = {
##    'default': {
##        'ENGINE': 'django.db.backends.sqlite3',
##        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
##    }
##}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LOGIN_REDIRECT_URL = 'MainMenu'
#LOGOUT_REDIRECT_URL = 'https://www.nrg.com/home.html' #'MainMenu'
LOGOUT_REDIRECT_URL = 'MainMenu'



#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'el'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True




# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

import os
CURRENT_PATH = os.path.abspath(os.path.dirname(__file__))

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))

if DEBUG:
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

STATIC_ROOT = os.path.join(PROJECT_ROOT, 'staticfiles')
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    os.path.join(CURRENT_PATH, 'static'),
)


#DATABASE_APPS_MAPPING = {'countries': 'maindata', 'scheduler': 'maindata'}
#DATABASE_ROUTERS = ['scheduler.routers.NrgAzureRouter']
