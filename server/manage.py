#!/usr/bin/env python
import os
import subprocess

from flask_script import Manager, Shell, Server
from redis import Redis
from rq import Connection, Queue, Worker

from app import create_app, db
from app.models import Role, User
from app.config import Config

# 创建app，通过 FLASK_CONFIG 的环境变量获取 app 配置的环境变量
app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)


def make_shell_context():
    '''在App上下文中运行Shell'''
    return dict(app=app, db=db, User=User, Role=Role)


manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('run_server', Server(host="0.0.0.0"))


@manager.command
def recreate_db():
    """重新创建数据库"""
    db.drop_all()
    db.create_all()
    db.session.commit()


@manager.option(
    '-n',
    '--number-users',
    default=10,
    type=int,
    help='产生的假用户条数',
    dest='number_users')
def add_fake_data(number_users):
    """生成假数据"""
    User.generate_fake(count=number_users)


@manager.command
def setup_general():
    """生成基础数据"""
    Role.insert_roles()
    admin_query = Role.query.filter_by(name='Administrator')
    if admin_query.first() is not None:
        if User.query.filter_by(email=Config.ADMIN_EMAIL).first() is None:
            user = User(
                first_name='Admin',
                last_name='Account',
                password=Config.ADMIN_PASSWORD,
                confirmed=True,
                email=Config.ADMIN_EMAIL)
            db.session.add(user)
            db.session.commit()
            print('Added administrator {}'.format(user.full_name()))


@manager.command
def run_worker():
    """运行Worker"""
    listen = ['default']
    conn = Redis(
        host=app.config['RQ_DEFAULT_HOST'],
        port=app.config['RQ_DEFAULT_PORT'],
        db=0,
        password=app.config['RQ_DEFAULT_PASSWORD'])

    with Connection(conn):
        worker = Worker(map(Queue, listen))
        worker.work()


if __name__ == '__main__':
    manager.run()
