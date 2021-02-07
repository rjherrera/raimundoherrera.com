from .base import *
import dj_database_url

DEBUG = False

ALLOWED_HOSTS = [
    'raimundoherrera.com',
    'www.raimundoherrera.com',
]

DATABASES = {
    'default': dj_database_url.config(conn_max_age=600, ssl_require=True)
}
