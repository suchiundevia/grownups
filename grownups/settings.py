import os
import django_heroku
import sentry_sdk
from sentry_sdk.integrations.django import DjangoIntegration

sentry_sdk.init(
    dsn="https://95b214b847014cf2850ed39b905136d8@o450365.ingest.sentry.io/5435142",
    integrations=[DjangoIntegration()],
    traces_sample_rate=1.0,

    send_default_pii=True
)

# Base directory path
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECRET_KEY = os.environ.get('SECRET_KEY')
SECRET_KEY = "7%dc*$14_ca7+61zrv7xp4)(f0(8en9@a8b+f0ojeluq@46k*t"

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']

# Application definition

INSTALLED_APPS = [
    # In-house modules
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'storages',
    # Custom apps
    'base_app.apps.BaseAppConfig',
    'account_app.apps.AccountAppConfig',
    'activity_app.apps.ActivityAppConfig',
    # Third party apps
    'crispy_forms',
    # Social media integration apps
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    # List of login providers
    'allauth.socialaccount.providers.google',
    'allauth.socialaccount.providers.facebook',
]

# Required for google and social media login integration
SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

CSRF_TRUSTED_ORIGINS = [
    'grownups.herokuapp.com',
    'grownups.tecxure.com',
]
ROOT_URLCONF = 'grownups.urls'

# To integrate google login functionality
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
            os.path.join(BASE_DIR, 'base_app', 'templates', 'base_app'),
            os.path.join(BASE_DIR, 'account_app', 'templates', 'account_app'),
            os.path.join(BASE_DIR, 'activity_app', 'templates', 'activity_app'),
        ],
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

# Fixtures Path
FIXTURE_DIRS = (os.path.join(BASE_DIR, 'fixtures'),)

WSGI_APPLICATION = 'grownups.wsgi.application'
# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'grownups',
        'USER': 'postgres',
        'PASSWORD': 'jalebi',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

# Password validation
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
LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = '/static/'

# Save images to...
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Crispy = better form rendering using bootstrap 4 rather than bootstrap 2
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Redirect the user to the home page once login is successful
LOGIN_REDIRECT_URL = 'home'
LOGIN_URL = 'login'

# Email backend connection
SENDGRID_API_KEY = os.environ.get('SENDGRID_API_KEY')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = SENDGRID_API_KEY
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.sendgrid.net'
EMAIL_PORT = 587
EMAIL_USE_TLS = True

DEFAULT_FROM_EMAIL = 'suchi.undevia@tecxure.com'

# Variables for AWS S3 bucket connection
AWS_ACCESS_KEY_ID = os.environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = os.environ.get('AWS_SECRET_ACCESS_KEY')
# AWS_STORAGE_BUCKET_NAME = os.environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_STORAGE_BUCKET_NAME = 'grownups-bucket'
# If a user uploads a file which has the same name as an existing file, don't overwrite them
AWS_S3_FILE_OVERWRITE = False
# Recommended to set this to None as the current value is known to cause issues
AWS_DEFAULT_ACL = None
# To upload media files to S3
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

django_heroku.settings(locals())
