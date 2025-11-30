{{current_settings}}

# seenode settings.
import os
import dj_database_url

# Security settings
SECRET_KEY = os.environ.get('SECRET_KEY')
DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Database configuration
DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}

# Static files with WhiteNoise
i = MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")
MIDDLEWARE.insert(i + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
