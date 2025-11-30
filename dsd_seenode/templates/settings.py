{{current_settings}}

# seenode settings.
import os
if os.environ.get("ON_SEENODE", ""):
    import dj_database_url

    # Security settings
    # SECRET_KEY = os.environ.get('SECRET_KEY')
    SECRET_KEY = "f758ee6fa3842c83d1a4aae6b423d8c0"
    # DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    DEBUG = True
    ALLOWED_HOSTS = [".apps.run-on-seenode.com"]

    # Database configuration
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }

    # Static files with WhiteNoise
    i = MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")
    MIDDLEWARE.insert(i + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
