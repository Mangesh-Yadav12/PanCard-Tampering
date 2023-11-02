import os
from   os import environ

class Config(object):

    DEBUG = False
    TESTING = False
    
    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = 'mangesh@123'

    DB_NAME = "production-db"
    DB_USERNAME = "root"
    DB_PASSWORD = "pianalytix"

    UPLOADS = "/home/username/app/app/static/uploads"

    SESSION_COOKIE_SECURE = True
    DEFAULT_THEME = None

class DevelopmentConfig(Config):
    DEBUG = True
    SESSION_COOKIE_SECURE = False

class DebugConfig(Config):
    DEBUG = False
