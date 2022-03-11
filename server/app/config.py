import os
import sys
import urllib.parse


basedir = os.path.abspath(os.path.dirname(__file__))

# 读取配置文件中的配置
if os.path.exists('config.env'):
    print('Importing environment from .env file')
    for line in open('config.env'):
        var = line.strip().split('=')
        if len(var) == 2:
            os.environ[var[0]] = var[1].replace("\"", "")


class Config:
    '''通用配置'''
    APP_NAME = os.environ.get('APP_NAME', 'UTest')
    SECRET_KEY = os.environ.get('SECRET_KEY')

    # Email
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.sendgrid.net')
    MAIL_PORT = os.environ.get('MAIL_PORT', 587)
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', True)
    MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL', False)
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')

    # Admin邮箱配置
    ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD', '')
    ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', '')
    EMAIL_SUBJECT_PREFIX = '[{}]'.format(APP_NAME)
    EMAIL_SENDER = '{app_name} Admin <{email}>'.format(
        app_name=APP_NAME, email=MAIL_USERNAME)

    # redis配置
    REDIS_URL = os.getenv('REDIS_URL', '')
    urllib.parse.uses_netloc.append('redis')
    url = urllib.parse.urlparse(REDIS_URL)
    RQ_DEFAULT_HOST = url.hostname
    RQ_DEFAULT_PORT = url.port
    RQ_DEFAULT_PASSWORD = url.password
    RQ_DEFAULT_DB = 0

    # mysql
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL', '')
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True

    # jwt
    # JWT_TOKEN_LOCATION = 'u-token'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    '''开发环境配置'''
    DEBUG = True
    ASSETS_DEBUG = True

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN DEBUG MODE. \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class TestingConfig(Config):
    TESTING = True
    WTF_CSRF_ENABLED = False

    @classmethod
    def init_app(cls, app):
        print('THIS APP IS IN TESTING MODE.  \
                YOU SHOULD NOT SEE THIS IN PRODUCTION.')


class ProductionConfig(Config):
    '''生产环境配置'''
    DEBUG = False
    USE_RELOADER = False
    SSL_DISABLE = (os.environ.get('SSL_DISABLE', 'True') == 'True')

    @classmethod
    def init_app(cls, app):
        Config.init_app(app)
        assert os.environ.get('SECRET_KEY'), 'SECRET_KEY IS NOT SET!'


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig,
}
