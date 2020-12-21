import os
import psycopg2
from decouple import config
from dj_database_url import parse as dburl

# BASE_DIR = Define o caminho de partida do projeto para as demais configurações
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

SECRET_KEY = config('SECRET_KEY')

SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

ALLOWED_HOSTS = ['*']

DEBUG = config('DEBUG', default=False, cast=bool)

INTERNAL_IPS = ['127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'grappelli',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'companies',
    'servers',
    'process',
    'modules',
    'systems',
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

ROOT_URLCONF = 'control.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/')],
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

WSGI_APPLICATION = 'control.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': config('ENGINE'),
        'NAME': config('NAME'),
        'USER': config('ROLE'),
        'PASSWORD': config('PASSWORD'),
        'HOST': config('HOST'),
        'PORT': config('PORT'),
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
LANGUAGE_CODE='pt-BR'

TIME_ZONE='America/Sao_Paulo'

USE_I18N=True

USE_L10N=True

USE_TZ=True

# Define a formatação para valores
DECIMAL_SEPARATOR=','
USE_THOUSAND_SEPARATOR=True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/
# Arquivos usados na renderização, exemplo: HTML
# STATICFILES_DIRS = Define os diretórios que serão vasculhados pelo FileSystemFinder.
STATICFILES_DIRS=(
    os.path.join(BASE_DIR, 'static'),
)

# STATIC_ROOT = Define o diretório onde serão armazenados os arquivos estáticos coletados
STATIC_ROOT='staticfiles'
# STATIC_URL = Define o prefixo de URL para referência aos arquivos estáticos. exemplo: { static '/static/img.jpg}
STATIC_URL='/static/'

MEDIA_ROOT=os.path.abspath(os.path.join(BASE_DIR, 'static/media/'))
# MEDIA_URL = Define o prefixo de URL para referência a arquivos de mídia (uploads).
MEDIA_URL='/media/'

# Comando que faz um backup do arquivo .env renomeando para que o git o carregue consigo
# O conteúdo deste arquivo, deverá substituir o conteúdo do arquivo .env em outro computador
if os.path.isfile('.env'):
   os.system("cp -r -f .env .env.backup")

# Retorna os erros em produção para adm
ADMINS=[('Marcos', 'lgerardlucas@gmail.com',)]

PRINCIPAL_AUTH_URL_NAMESPACE='control'

GRAPPELLI_ADMIN_TITLE = "Py-Controle-Serve"
GRAPPELLI_SWITCH_USER = True
