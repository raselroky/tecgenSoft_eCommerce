
from pathlib import Path
import os
from django.middleware.csrf import CsrfViewMiddleware
from datetime import timedelta
class WebSocketMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # Skip CSRF for WebSocket requests
        if request.path.startswith("/ws/"):
            setattr(request, '_dont_enforce_csrf_checks', True)
        return self.get_response(request)
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-0&g$tv&6-c!cy)rjbp_%4h19jlw!sby9h(e7tmqwqzsyhb99i*'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework_simplejwt',
    'rest_framework',
    'drf_yasg',
    'corsheaders',
    'channels',
    'helper',
    'user',
    'catalog',
    'store',
    'product',
    'campaign',
    'order',
    'configure',
    'payment',
    'stock',
    'wishlist',
    'cartitem',
    'notification',
    'location',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'corsheaders.middleware.CorsMiddleware', 
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tecgen.settings.WebSocketMiddleware',

]

ROOT_URLCONF = 'tecgen.urls'
ASGI_APPLICATION = 'tecgen.asgi.application'
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
            ],
        },
    },
]

WSGI_APPLICATION = 'tecgen.wsgi.application'

# Database


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
#STATICFILES_DIRS =[os.path.join(BASE_DIR, 'static')]
STATICSSTORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        # 'rest_framework.authentication.TokenAuthentication',
        # 'rest_framework.authentication.SessionAuthentication',
        # 'rest_framework.authentication.BasicAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ), 

    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
    'EXCEPTION_HANDLER': 'rest_framework.views.exception_handler',
    'DEFAULT_FILTER_BACKENDS': (
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
        'rest_framework.filters.OrderingFilter',
    )
}



CORS_ALLOW_CREDENTIALS = True
CORS_ALLOW_ALL_ORIGINS = True
CORS_ALLOW_HEADERS = [
    "accept",
    "accept-encoding",
    "authorization",
    "content-type",
    "dnt",
    "origin",
    "user-agent",
    "x-csrftoken",
    "x-requested-with",
]
CORS_ALLOW_HEADERS = ["*"]
CORS_ALLOW_METHODS = [
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
]


X_FRAME_OPTIONS = 'ALLOWALL'
XS_SHARING_ALLOWED_METHODS = ['POST','GET','OPTIONS', 'PUT', 'DELETE']

CSRF_TRUSTED_ORIGINS=["http://www.tecgensoft.com","http://tecgensoft.com"]




# SECURE_SSL_REDIRECT = True

# SSL_STORE_ID='shobl656ef44d52976'
# SSL_STORE_PASSWORD='shobl656ef44d52976@ssl'
# SSL_BASE_URL='https://5e90-103-142-170-229.ngrok-free.app'

# AMARPAY_STORE_ID='aamarpaytest'
# AMARPAY_SIGNATURE_KEY='dbb74894e82415a2f7ff0ec3a97e4183'
# AMARPAY_BASE_URL='https://sandbox.aamarpay.com/jsonpost.php'

# AMARPAY_MERCHANT_ID='shob'
# AMARPAY_LIVE_STORE_ID='shob'
# AMARPAY_LIVE_SIGNATURE_KEY='64b8a1c5474e92d67541689d5f3a09c7'
# AMARPAY_LIVE_BASE_URL='https://secure.aamarpay.com/jsonpost.php'

# SMS_TOKEN='b092777221e1fd03d2221e74e4d4073e4d21cffd'
# SMS_URL='https://sysadmin.muthobarta.com/api/v1/'

# FRONTEND_BASE_URL='https://shob.com.bd'
# BACKEND_BASE_URL='http://192.168.68.130'


# from celery import Celery
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tecgen.settings')
# celery_app = Celery('tecgen')
# celery_app.config_from_object('django.conf:settings', namespace='CELERY')
# celery_app.autodiscover_tasks(lambda: INSTALLED_APPS)


CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://redis:6379',
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        }
    }
}

CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('redis', 6379)],
        },
    },
}


SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=2), 
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),  
    'AUTH_TOKEN_CLASSES': ('rest_framework_simplejwt.tokens.AccessToken',),
    'TOKEN_TYPE_CLAIM': 'token_type',
}


AUTH_USER_MODEL = 'user.User'