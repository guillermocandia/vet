import os

# Identificador del cliente
# se usará para soporte y para el repositorio de archivos media
CLIENTE_ID = 'dev'
CLIENTE_NOMBRE = 'Clínica Veterinaria'

DEBUG = True

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'sd=upaz9jwxoy@@w-qxy&$fc$aui_g*@-gsus+c2juvu0fx#%v'
ALLOWED_HOSTS = []


# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'app.recursos.localidades',
    #'app.vet.base',
    #'app.vet.personal',
    #'app.vet.personal.permisos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'Veterinario.urls'

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
                'django.contrib.messages.context_processors.messages'
            ],
        },
    },
]

WSGI_APPLICATION = 'Veterinario.wsgi.application'


# Internationalization
LANGUAGE_CODE = 'es'
TIME_ZONE = 'America/Santiago'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Database
if DEBUG:
    DATABASES = {
                 'default': {
                             'ENGINE': 'django.db.backends.mysql',
                             'NAME': 'veterinario0',
                             'USER': 'root',
                             'PASSWORD': '',
                             'HOST': '127.0.0.1',
                             'PORT': '3306',
                             }
                 }
else:
    DATABASES = {
                 'default': {
                             'ENGINE': 'django.db.backends.mysql',
                             'NAME': 'veterinario0',
                             'USER': 'root',
                             'PASSWORD': '',
                             'HOST': '127.0.0.1',
                             'PORT': '3306',
                             }
                 }


# Static files (CSS, JavaScript, Images)
if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
    MEDIA_ROOT = BASE_DIR + '/media/'
else:
    pass
