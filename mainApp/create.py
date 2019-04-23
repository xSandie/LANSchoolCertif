import os
import click
from flask import Flask

from mainApp.config.setting import config
from mainApp.libs.cache import cache
from mainApp.models.base import db


def register_blueprints(app):#注册蓝图
    from mainApp.api.certif import snnu
    app.register_blueprint(snnu, url_prefix='/snnu')


def create_app(config_name=None):
    if config_name is None:
        config_name = os.getenv('FLASK_CONFIG', 'development')
    app=Flask(__name__)#不要漏掉本函数参数
    app.config.from_object(config[config_name])
    #上面进行基本配置
    register_blueprints(app)
    db.init_app(app)
    cache.init_app(app)
    with app.app_context():
        db.create_all()
    register_shell_context(app)
    register_commands(app)
    return app #一定要记得返回创建的核心对象app


def register_shell_context(app):
    @app.shell_context_processor
    def make_shell_context():
        return dict(app=app,db=db)

def register_commands(app):
    @app.cli.command('initdb')
    def initdb():
        click.echo("Initializing the database")
        with app.app_context():
            db.drop_all()
            db.create_all()
        click.echo("Done")
