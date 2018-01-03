from datetime import timedelta

DEBUG = True
LOG_LEVEL = 'DEBUG'  # CRITICAL / ERROR / WARNING / INFO / DEBUG

SERVER_NAME = 'localhost:8000'
SECRET_KEY = 'secret'


# Flask-Mail.
MAIL_DEFAULT_SENDER = 'admin@local.host'
MAIL_SERVER = 'smtp.gmail.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USE_SSL = False
MAIL_USERNAME = 'you@gmail.com'
MAIL_PASSWORD = 'yourpassword'

# Celery.
CELERY_BROKER_URL = 'redis://redis'
CELERY_RESULT_BACKEND = 'redis://redis'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 5

# SQLAlchemy
SQLALCHEMY_DATABASE_URI = 'postgresql://postgres@postgres:5432/snakeeyes'
SQLALCHEMY_TRACK_MODIFICATIONS = False

# User
SEED_ADMIN_EMAIL = 'dev@local.host'
SEED_ADMIN_PASSWORD = 'devpassword'
REMEMBER_COOKIE_DURATION = timedelta(days=90)

