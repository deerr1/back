import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ioyid7a5$rrlr5l1)vvw3-)%p0pt3+du$7pqq3j37_itev=llk'

DEBUG = True

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'db_name',
        'USER':'username',
        'PASSWORD':'pass',
        'HOST':'localhost',
        'PORT':'1111',
    }
}


