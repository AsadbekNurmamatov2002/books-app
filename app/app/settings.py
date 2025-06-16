import os
from pathlib import Path
from decouple import config
from django.utils.translation import gettext_lazy as _
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/
SECRET_KEY = config('SECRET_KEY', default="coding")
DEBUG = config('DEBUG', default=False, cast=bool)
# SECURITY WARNING: keep the secret key used in production secret!

if DEBUG:
    ALLOWED_HOSTS = [
        ".railway.app",
        "http://0.0.0.0:8000",
    ]

CSRF_TRUSTED_ORIGINS = [
    "https://*.railway.app"
]

# HTTPS
CSRF_COOKIE_SECURE=not DEBUG
SESSION_COOKIE_SECURE=not DEBUG

ALLOWED_HOSTS = ["*"]


# Application definition nima

INSTALLED_APPS = [
    "unfold",
    "unfold.contrib.filters",
    "unfold.contrib.forms",
    "unfold.contrib.import_export",
    


    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # intolled
    'ckeditor',
    'import_export',
    # myapps
    'books.apps.BooksConfig',
    'settingsite.apps.SettingsiteConfig',
    "users.apps.UsersConfig",
    


]
IMPORT_EXPORT_USE_TRANSACTIONS = True
# Django Unfold sozlamalari
UNFOLD = {
    "SITE_TITLE": _("Administration Kitoblar"),  # Tarjima qilinadigan sarlavha
    "SITE_HEADER": _("Administration Kitoblar"),
    "SITE_URL": "/",
    "THEME": "dark",  # dark, light yoki auto
    "COLORS": {
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
        },
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "ru": "🇫🇷",
                "uz": "🇧🇪",
            },
        },
    },
}


LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = 'user/login'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware', #added
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.locale.LocaleMiddleware', # added
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "templates"],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'settingsite.context_processors.site_settings',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

# Add these at the top of your settings.py


# Replace the DATABASES section of your settings.py with this
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': config('PGDATABASE'),
        'USER': config('PGUSER'),
        'PASSWORD': config('PGPASSWORD'),
        'HOST': config('PGHOST'),
        'PORT': config('PGPORT', cast=int),
        'OPTIONS': {
            'sslmode': 'require',
        }
    }
}
# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/
LANGUAGE_CODE = 'uz'  # Standart til
LANGUAGES = [
    ('uz', _('Oʻzbekcha')),
    ('en', _('English')),
    ('ru', _('Русский')),
]


LOCALE_PATHS = [BASE_DIR / 'locale']  # Tarjima fayllari joylashuvi
UNFOLD.update({
    "LANGUAGE_CODE": LANGUAGE_CODE,
    "LANGUAGES": {
        "navigation": [
            {"code": "uz", "label": "Oʻzbekcha", "flag": "🇺🇿"},
            {"code": "en", "label": "English", "flag": "🇬🇧"},
            {"code": "ru", "label": "Русский", "flag": "🇷🇺"},
        ]
    },
    "EXTENSIONS": {
        "modeltranslation": {
            "flags": {
                "en": "🇬🇧",
                "ru": "🇷🇺",
                "uz": "🇺🇿",
            },
        },
    },
    "LOCALE_PATHS": LOCALE_PATHS,
})

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]

# CKEditor Configuration
CKEDITOR_UPLOAD_PATH = 'uploads/'
CKEDITOR_IMAGE_BACKEND = "pillow"
CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'
CKEDITOR_CONFIGS = {
    'default':
        {
            'toolbar': 'full',
            'width': 'auto',
            'extraPlugins': ','.join([
                'codesnippet',
            ]),
        },
}
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field


STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
        "OPTIONS": {
            "location": BASE_DIR / "media",  # media fayllar saqlanadigan papka
            "base_url": "/media/",          # media fayllarga URL
        },
    },
    "staticfiles": {
        "BACKEND": "django.contrib.staticfiles.storage.StaticFilesStorage",
    },
}

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
