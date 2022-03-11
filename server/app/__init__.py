import os

from flask import Flask
from flask_compress import Compress
from flask_mail import Mail
from flask_rq import RQ
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_jwt_extended import JWTManager
from app.config import config as Config
from logging import Logger

basedir = os.path.abspath(os.path.dirname(__file__))

mail = Mail()
db = SQLAlchemy()
csrf = CSRFProtect()
compress = Compress()
jwt_manager = JWTManager()

logger = Logger(__name__)

def create_app(config):
    app = Flask(__name__)
    config_name = config

    if not isinstance(config, str):
        config_name = os.getenv('FLASK_CONFIG', 'default')

    app.config.from_object(Config[config_name])
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    # not using sqlalchemy event system, hence disabling it

    Config[config_name].init_app(app)

    # 配置插件
    mail.init_app(app)
    db.init_app(app)
    jwt_manager.init_app(app)
    csrf.init_app(app)
    compress.init_app(app)
    RQ(app)

    # 配置SSL
    if not app.debug and not app.testing and not app.config['SSL_DISABLE']:
        from flask_sslify import SSLify
        SSLify(app)

    # 配置蓝图

    from .account import account as account_blueprint
    app.register_blueprint(account_blueprint, url_prefix='/account')

    from .error import error as error_blueprint
    app.register_blueprint(error_blueprint)

    return app

