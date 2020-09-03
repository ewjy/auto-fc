# Import all default settings.
from .settings import *

'''import dj_database_url
DATABASES = {
    'default': dj_database_url.config(),
}'''

import pymysql
pymysql.version_info = (1, 4, 13, "final", 0)
pymysql.install_as_MySQLdb()
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'hidden',
        'HOST': 'hidden',
        'POST': 'hidden',
        'USER': 'hidden',
        'PASSWORD': 'hidden',
    }
}

# Static asset configuration.
STATIC_ROOT = 'static'

# Honor the 'X-Forwarded-Proto' header for request.is_secure().
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# Allow all host headers.
ALLOWED_HOSTS = ['*']

# Turn off DEBUG mode.
DEBUG = False