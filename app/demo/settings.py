import os
from django.utils.translation import gettext_lazy as _
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%fz_%7dgoda68(wg&jas&b!z6=1lir7d(1)_mh($w3+og6wjal'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


MATERIALDASH_ADMIN_SITE = {
    'HEADER':  _('Demo'),
    'TITLE':  _('Demo'),
    'FAVICON':  'demo.png',
    # 'MAIN_BG_COLOR':  '#ff9b75',
    # 'MAIN_HOVER_COLOR':  '#00000060',
    # 'PROFILE_PICTURE':  'profile-background.jpeg',
    # 'PROFILE_BG':  'profile-background.jpeg',
    # 'LOGIN_LOGO':  'profile-background.jpeg',
    # 'LOGOUT_BG':  'profile-background.jpeg',
    'SHOW_THEMES':  True,
    'TRAY_REVERSE': True,
    'NAVBAR_REVERSE': True,
    'SHOW_COUNTS': False,
    'APP_ICONS': {
        'invitations': 'send',
    },
    'MODEL_ICONS': {
        'invitation': 'contact_mail',
    }
}

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

# Application definition
INSTALLED_APPS = [
    'modeltranslation',
    'materialdash',
    'materialdash.admin',

    # 'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # 'django.contrib.sites',

    'adminsortable2',
    'filefield_cache',


    'demo.countries',
    'demo.documents',
    'demo.relations',
    'demo.periods',
    'demo.profile',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'demo.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
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

WSGI_APPLICATION = 'demo.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql',
#         'HOST': os.environ.get('POSTGRES_HOST'),
#         'NAME': os.environ.get('POSTGRES_DB'),
#         'USER': os.environ.get('POSTGRES_USER'),
#         'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
#         'PORT': os.environ.get('POSTGRES_PORT'),
#     }
# }
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

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

SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LOCALE_PATHS = [
    os.path.join(BASE_DIR, 'demo/locale')
]

LANGUAGE_CODE = 'pt-br'

LANGUAGES = [
    ('en', _('English')),
    ('es', _('Spanish')),
    ('pt-br', _('Portuguese')),
    ('ru', _('Russian')),
    ('uk', _('Ukrainian')),
    ('zh-hans', _('Chinese')),
]

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
MEDIA_ROOT = os.path.join(BASE_DIR, "media")
