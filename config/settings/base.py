from datetime import datetime, timezone
from decimal import Decimal

import environ


# Build paths inside the project like this: root(...)
env = environ.Env()

root = environ.Path(__file__) - 3
apps_root = root.path('aqua_airdrop2_checker')

BASE_DIR = root()


# Base configurations
# --------------------------------------------------------------------------

ROOT_URLCONF = 'config.urls'
WSGI_APPLICATION = 'config.wsgi.application'

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'


# Application definition
# --------------------------------------------------------------------------

DJANGO_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.sitemaps',
]

THIRD_PARTY_APPS = [
    'constance',
]

LOCAL_APPS = [
    'aqua_airdrop2_checker.taskapp',
    'aqua_airdrop2_checker.airdrop2',
]

INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS


# Middleware configurations
# --------------------------------------------------------------------------

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Template configurations
# --------------------------------------------------------------------------

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            root('aqua_airdrop2_checker', 'templates'),
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


# Fixture configurations
# --------------------------------------------------------------------------

FIXTURE_DIRS = [
    root('aqua_airdrop2_checker', 'fixtures'),
]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators
# --------------------------------------------------------------------------

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/
# --------------------------------------------------------------------------

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

SITE_ID = 1


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/
# --------------------------------------------------------------------------

STATIC_URL = '/static/'
STATIC_ROOT = root('static')

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

STATICFILES_DIRS = [
    root('aqua_airdrop2_checker', 'assets'),
]

MEDIA_URL = '/media/'
MEDIA_ROOT = root('media')


CELERY_ENABLED = env.bool('CELERY_ENABLED', default=True)
if CELERY_ENABLED:
    # Celery configuration
    # --------------------------------------------------------------------------

    CELERY_ACCEPT_CONTENT = ['json']
    CELERY_TASK_SERIALIZER = 'json'
    CELERY_TASK_IGNORE_RESULT = True


# Cache configuration
# --------------------------------------------------------------------------

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.redis.RedisCache',
        'LOCATION': env('REDIS_BACKEND', default='redis://127.0.0.1:6379'),
    }
}


# Rest framework configuration
# http://www.django-rest-framework.org/api-guide/settings/
# --------------------------------------------------------------------------

REST_FRAMEWORK = {
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
}


# Constance configuration
# https://django-constance.readthedocs.io/en/latest/
# --------------------------------------------------------------------------

CONSTANCE_CONFIG = {
    'AQUA_PRICE': (Decimal('0.0390995'), 'Aqua price used in airdrop.', Decimal),
    'SHARE_PRICE': (Decimal('4.9914546'), 'Share price used in airdrop.', Decimal),
    'SNAPSHOT_TIME': (datetime(2022, 1, 15, 0, 0, 0, tzinfo=timezone.utc), 'Snapshot time.', datetime),
    'MAX_LOCK_TERM': (94694400, 'Max lock term.', int),
    'MAX_LOCK_BOOST': (Decimal(3), 'Max lock boost', Decimal),
    'REWARD_CAP': (Decimal(10 ** 7), 'Airdrop cap', Decimal),
}

REWARD_CAP_EXCEPTIONS = [
    # Upbit
    'GCWEER57MBVRXA4I426VL3PSWWM72SSZ3AZ5TGBDSWJMTDFVCABWNZIF',
    # GOPAX
    'GCXDR4QZ4OTVX6433DPTXELCSEWQ4E5BIPVRRJMUR6M3NT4JCVIDALZO',
    'GAZANXSPY2N3MANBJYLATYGMXDLHZMO57KDST6AN5MOKXEP3OBUFPV66',
    # Probit
    'GATHSLHLMK3OFQKRSMSCOODEFABR2GWMVW2LUESZZPL6ZHMVCVP5JBXU',
    'GBE27W2DJZS4AFFR2HVZBK4KHD4TQQ4ITB2AQTYA5L57K6ZTRWPJUDH6',
    'GBP3BTNFQKP65QZTJQRKCUSZKUO66KFTH53SM5LR2SAMFRBJWKNKJAOK',
    # Coinone
    'GCOEPUFA4VGWIEEYCSTLOJX2OTUYZ42M6C7HNX4NANIRUNKOFCBXCBHY',
    'GBHMB55GUN23HBWH4YGRPEZWHNL523JTUBS6KSCQ5OPTN4KHYRPJVE6S',
    'GAGCX4RX6OAZMPNRGDMHLQ7OMHXZM7I3CZO2ISXCJ3OMNDPE5Q7ENCDA',
    'GCAXOLGVBICF3CY5ESBLCBBKACSVBJ55XTK4NO3FDZ5UIK3BRABCCWZC',
    'GA7XXJ3PGGSOX2A5YAAFDFIZDMODHGWVL7RQTKIUKWCZAQYLIH7SNMFZ',
    # Bithumb
    'GBFP2QMU46T4TWUMTF6GX7EZQEY3F3IM2O6E6IRIRNDFXQZO26S5HNIG',
    # MEXC
    'GCDBX7GTQWJFTAJCJUGV4KXJZE6Q527YRLW75GYDJ2ODSVBOXCS4W7VS',
    # Liquid
    'GA7OPN4A3JNHLPHPEWM4PJDOYYDYNZOM7ES6YL3O7NC3PRY3V3UX6ANM',
    'GBQQE6EYNAD6ZXSXKDOABWG3GNCKLNY7DBREHGM3TLVBGSGUBF475M4Y',
    'GDSKFYNMZWTB3V5AN26CEAQ27643Q3KB4X6MY4UTO2LIIDFND4SPQZYU',
]
