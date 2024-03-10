from .base import *
env = environ.Env()
env.read_env(os.path.join(BASE_DIR, '.env'))
DEBUG = True
ALLOWED_HOSTS = ['*']

SECRET_KEY = env.get_value.get_value('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': env.get_value('DB_ENGINE'),
        'NAME': env.get_value('DB_NAME'),
        'USER': env.get_value('DB_USER'),
        'PASSWORD': env.get_value('DB_PW'),
        'HOST': env.get_value('DB_HOST'),
        'PORT': env.get_value('DB_PORT'),
    }
}

INTERNAL_IPS = ['127.0.0.1']