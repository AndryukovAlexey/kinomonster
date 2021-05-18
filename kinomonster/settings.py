from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3ac0ymm*+wn71k=_5l3qx=nv%=9%1!$!c3$993$artit_sr2rm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["192.168.99.100"]



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'movies.apps.MoviesConfig',
    'users.apps.UsersConfig',
    'django.contrib.sites',

    # 'allauth',
    # 'allauth.account',
    # 'allauth.socialaccount',
    # 'allauth.socialaccount.providers.vk',
    # 'allauth.socialaccount.providers.google',

    'social_django',
]

SOCIAL_AUTH_PIPELINE = (
 
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
    'kinomonster.pipeline.soc_auth', 
)

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'kinomonster.urls'

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
                'django.contrib.messages.context_processors.messages',

                'social_django.context_processors.backends',
            ],
        },
    },
]

WSGI_APPLICATION = 'kinomonster.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db/db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'ru-RU'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, "static")

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

LOGIN_REDIRECT_URL = 'home-page'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 465
EMAIL_HOST_USER = 'helpkinomonster@gmail.com'
EMAIL_HOST_PASSWORD = '7k47d95t'
EMAIL_USE_SSL = True

AUTHENTICATION_BACKENDS = (
    'users.auth.EmailAuthBackend',
    'django.contrib.auth.backends.ModelBackend',

    # 'allauth.account.auth_backends.AuthenticationBackend',

    'social_core.backends.vk.VKOAuth2', 
    'social_core.backends.google.GoogleOAuth2',
)


SOCIAL_AUTH_VK_OAUTH2_KEY = '7814917'
SOCIAL_AUTH_VK_OAUTH2_SECRET = 'ADLxG6iho67FuFJsoiLM'
SOCIAL_AUTH_VK_OAUTH2_SCOPE = ['email']

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = '751507064299-5vdsedtav29c3e47e62atlem8o2s1ek6.apps.googleusercontent.com'
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = 'fFZEdkSFZ-UEMEbLLHcEYjqd'

REDIC_HOST = '192.168.99.100'
REDIC_PORT = '6379'
CELERY_REDIS_PASSWORD = "dklafjruwqrujlkafionjoqwri09tuwq90tiqw9uttlskndlkjhfhjflhjdf"
CELERY_BROKER_URL = 'redis://:' + CELERY_REDIS_PASSWORD + '@' + REDIC_HOST + ':' +  REDIC_PORT + '/0'
CELERY_TIMEZONE = "Europe/Moscow"
CELERY_TASK_TRACK_STARTED = True
CELERY_TASK_TIME_LIMIT = 30 * 60
CELERY_RESULT_BACKEND = 'redis://:' + CELERY_REDIS_PASSWORD + '@' + REDIC_HOST + ':' +  REDIC_PORT + '/0'
FLOWER_PORT = '5555'
# CELERYBEAT_PID_FILE = 'kinomonster'


LOGOUT_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

SITE_ID = 1
