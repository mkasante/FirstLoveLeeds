"""
Django settings for firstlove project.

Generated by 'django-admin startproject' using Django 1.10.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os
from django.core.urlresolvers import reverse_lazy
import dj_database_url


# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Login/Logout url
LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('welcome:index')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*q3979tq^dql6txf1y$y^dy5q9h-t6sxii+j*8#gr^k1yfxl(g'

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = True

ENVIRONMENT = "LIVE"

ALLOWED_HOSTS = ['*']
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# Application definition

INSTALLED_APPS = [
	'django.contrib.admin',
	'django.contrib.auth',
	'django.contrib.contenttypes',
	'django.contrib.sessions',
	'django.contrib.messages',
	'django.contrib.staticfiles',
	'rest_framework',
	'member',
	'api',
	'welcome',
	'event',
]

REST_FRAMEWORK = {
	'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAdminUser',),
	'PAGE_SIZE': 50
}

MIDDLEWARE_CLASSES = [
	'django.middleware.security.SecurityMiddleware',
	'django.contrib.sessions.middleware.SessionMiddleware',
	'django.middleware.common.CommonMiddleware',
	'django.middleware.csrf.CsrfViewMiddleware',
	'django.contrib.auth.middleware.AuthenticationMiddleware',
	'django.contrib.messages.middleware.MessageMiddleware',
	'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'firstlove.urls'

TEMPLATES = [
	{
		'BACKEND': 'django.template.backends.django.DjangoTemplates',
		'DIRS': [
			# insert your TEMPLATE_DIRS here
			os.path.join(BASE_DIR, "templates")
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

WSGI_APPLICATION = 'firstlove.wsgi.application'

# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
# Database
DATABASES = {
	'default': {}
}

# Set production environment
if ENVIRONMENT == "TEST":
	DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
	DATABASES['default']['NAME'] = 'firstloveleeds'
	DATABASES['default']['USER'] = 'firstloveleeds'
	DATABASES['default']['PASSWORD'] = '14leeds20'
	DATABASES['default']['CONN_MAX_AGE'] = 1000


elif ENVIRONMENT == "LIVE":
	DATABASES['default'] = dj_database_url.parse(os.environ.get("DATABASE_URL"),
		conn_max_age=600)

else:
	DATABASES = {
		'default': {
			'ENGINE': 'django.db.backends.sqlite3',
			'NAME': os.path.join(BASE_DIR, 'firstloveleeds.db'),
		}
	}


# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
	{'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', },
	{'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', },
	{'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', },
	{'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator', },
]


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-gb'
TIME_ZONE = 'Europe/London'
USE_I18N = True
USE_L10N = True
USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
	os.path.join(BASE_DIR, "firstlove/static"),
]

STATIC_ROOT = os.path.join(BASE_DIR, "templates")
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
