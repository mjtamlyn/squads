import os

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
import dj_database_url


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ.get('SECRET_KEY', 'monkeys')
DEBUG = not (os.environ.get('DEBUG', '') == 'False')
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'squads',
    'social_auth',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS += (
    'django.core.context_processors.request',
)

ROOT_URLCONF = 'squads.urls'
WSGI_APPLICATION = 'squads.wsgi.application'


# Database
DATABASES = {'default': dj_database_url.config(default='postgres://localhost/squads')}


# Internationalization
LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files
STATIC_URL = '/static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'static'),)


# Email
EMAIL_SUBJECT_PREFIX = '[OUCofA Squads] '
DEFAULT_FROM_EMAIL = 'noreply@oucofa.co.uk'
EMAIL_HOST = os.environ.get('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.environ.get('SENDGRID_USERNAME', '')
EMAIL_HOST_PASSWORD = os.environ.get('SENDGRID_PASSWORD', '')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND', 'django.core.mail.backends.console.EmailBackend')


# Apps
AUTH_USER_MODEL = 'squads.User'
SOCIAL_AUTH_USER_MODEL = 'squads.User'
AUTHENTICATION_BACKENDS = (
    'social_auth.backends.facebook.FacebookBackend',
    'django.contrib.auth.backends.ModelBackend',
)
FACEBOOK_APP_ID = os.environ.get('FACEBOOK_APP_ID', '302914746566919')
FACEBOOK_API_SECRET = os.environ.get('FACEBOOK_SECRET', '9ace9d9750b6f4ef0cf97d7345af6ec8')
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
LOGIN_URL = '/login/facebook/'
LOGIN_REDIRECT_URL = '/'
