import os

from django.utils._os import safe_join

BASE_DIR = os.path.dirname(os.path.dirname(__file__))

SECRET_KEY = os.environ['SECRET_KEY']
DEBUG = os.environ['ENV'] == 'DEV'
TEMPLATE_DEBUG = DEBUG

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'rest_framework',
    'compressor',
    'storages',
    'raven.contrib.django.raven_compat',

    'frontend',
    'api',
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

ROOT_URLCONF = 'PROJECT_NAME.urls'

WSGI_APPLICATION = 'PROJECT_NAME.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': os.environ.get('POSTGRES_HOST', 'localhost'),
        'NAME': os.environ.get(
            'POSTGRES_NAME',
            os.environ['POSTGRES_USER'],
        ),
        'USER': os.environ['POSTGRES_USER'],
        'PASSWORD': os.environ['POSTGRES_PASSWORD'],
    },
}

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = safe_join(BASE_DIR, 'static')
MEDIA_ROOT = safe_join(BASE_DIR, 'media')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'compressor.finders.CompressorFinder',
)

if DEBUG:
    STATIC_URL = '/static/'
    MEDIA_URL = '/media/'
else:
    AWS_ACCESS_KEY_ID = os.environ['AWS_ACCESS_KEY_ID']
    AWS_SECRET_ACCESS_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
    AWS_STORAGE_BUCKET_NAME = 'PROJECT_NAME'
    AWS_QUERYSTRING_AUTH = False
    AWS_IS_GZIPPED = True
    DEFAULT_FILE_STORAGE = 'PROJECT_NAME.s3.MediaStorage'
    STATICFILES_STORAGE = 'PROJECT_NAME.s3.StaticStorage'
    COMPRESS_STORAGE = 'PROJECT_NAME.s3.StaticStorage'
    STATIC_URL = 'https://PROJECT_NAME.s3.amazonaws.com/static/'
    MEDIA_URL = 'https://PROJECT_NAME.s3.amazonaws.com/media/'

COMPRESS_ENABLED = True
COMPRESS_OFFLINE = not DEBUG
COMPRESS_OUTPUT_DIR = 'cache'
COMPRESS_PRECOMPILERS = (
    ('text/x-scss', 'django_libsass.SassCompiler'),
)

if 'SENTRY_DSN' in os.environ:
    RAVEN_CONFIG = {
        'dsn': os.environ['SENTRY_DSN'],
    }

