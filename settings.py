import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMINS = (
    ('Wilian', 'contato@stancke.com.br'),
)

SITE_ID=u'4e434095e28a3608af00001d'

GRAPPELLI_ADMIN_TITLE = 'OpenSocialCRM'


MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django_mongodb_engine',
        'NAME': 'crm',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}

TIME_ZONE = 'America/Sao_Paulo'

# Language code for this installation. All choices can be found here:
# http://www.i18nguy.com/unicode/language-identifiers.html
LANGUAGE_CODE = 'pt-br'

USE_I18N = True
USE_L10N = True

MEDIA_URL = '/media/'

PROJECT_PATH = os.path.realpath(os.path.dirname(__file__))

MEDIA_ROOT = os.path.join(PROJECT_PATH, 'media')
STATIC_ROOT = os.path.join(PROJECT_PATH, 'static')

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = '/static/'

#ADMIN_MEDIA_PREFIX = '/static/admin/'
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"


STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)


SECRET_KEY = 'j--i+z1z6*h5^vf87h#71mqs!6mqrhckx!cnat)^6$#z$cx$^q'

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.auth",
    "django.core.context_processors.request",
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
#     'django.template.loaders.eggs.Loader',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.locale.LocaleMiddleware'
)

LANGUAGE_CODE = 'pt-br'
ROOT_URLCONF = 'opensocialcrm.urls'


ROOT_PATH = os.path.dirname(__file__)

TEMPLATE_DIRS = (
    ROOT_PATH + '/templates'
)

INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'grappelli',
    'django.contrib.admin',
    'django_mongodb_engine',
    'djangotoolbox',
    'redes_sociais',
    'campanhas',
    'crm',
)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}
