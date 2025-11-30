{{current_settings}}

# seenode settings.
import os
if os.environ.get("ON_SEENODE", ""):
    import dj_database_url

    # Security settings.
    SECRET_KEY = os.environ.get('SECRET_KEY')
    DEBUG = os.environ.get('DEBUG', 'False').lower() == 'true'
    ALLOWED_HOSTS = [".apps.run-on-seenode.com"]

    # Configure production database.
    DATABASES = {
        'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
    }

    # Use whitenoise to manage static files.
    i = MIDDLEWARE.index("django.middleware.security.SecurityMiddleware")
    MIDDLEWARE.insert(i + 1, "whitenoise.middleware.WhiteNoiseMiddleware")

    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "staticfiles"
    STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
