from .base import *

env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = env.get_value('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': env('DB_NAME'),
        'USER': env('DB_USER'),
        'PASSWORD': env('DB_PW'),
        'HOST': env('DB_HOST'),
        'PORT': env('DB_PORT'),
    }
}

INTERNAL_IPS = ['127.0.0.1']