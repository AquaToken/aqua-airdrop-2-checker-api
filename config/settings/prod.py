import sentry_sdk
from kombu import Exchange, Queue  # NOQA
from sentry_sdk.integrations.celery import CeleryIntegration
from sentry_sdk.integrations.django import DjangoIntegration

from config.settings.base import *  # noqa: F403


environ.Env.read_env()


DEBUG = False

ADMINS = env.json('ADMINS')

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

SECRET_KEY = env('SECRET_KEY')


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# --------------------------------------------------------------------------

DATABASES = {
    'default': env.db(),
}


# Email settings
# --------------------------------------------------------------------------

EMAIL_CONFIG = env.email()
vars().update(EMAIL_CONFIG)

SERVER_EMAIL_SIGNATURE = env('SERVER_EMAIL_SIGNATURE', default='aqua_airdrop2_checker'.capitalize())
DEFAULT_FROM_EMAIL = SERVER_EMAIL = SERVER_EMAIL_SIGNATURE + ' <{0}>'.format(env('SERVER_EMAIL'))


# Celery configurations
# http://docs.celeryproject.org/en/latest/configuration.html
# --------------------------------------------------------------------------
if CELERY_ENABLED:
    CELERY_BROKER_URL = env('CELERY_BROKER_URL')

    CELERY_TASK_DEFAULT_QUEUE = 'aqua_airdrop2_checker-celery-queue'
    CELERY_TASK_DEFAULT_EXCHANGE = 'aqua_airdrop2_checker-exchange'
    CELERY_TASK_DEFAULT_ROUTING_KEY = 'celery.aqua_airdrop2_checker'
    CELERY_TASK_QUEUES = (
        Queue(
            CELERY_TASK_DEFAULT_QUEUE,
            Exchange(CELERY_TASK_DEFAULT_EXCHANGE),
            routing_key=CELERY_TASK_DEFAULT_ROUTING_KEY,
        ),
    )


# Sentry config
# -------------

SENTRY_DSN = env('SENTRY_DSN', default='')
SENTRY_ENABLED = True if SENTRY_DSN else False

if SENTRY_ENABLED:
    sentry_sdk.init(
        SENTRY_DSN,
        traces_sample_rate=0.2,
        integrations=[DjangoIntegration(), CeleryIntegration()],
    )
