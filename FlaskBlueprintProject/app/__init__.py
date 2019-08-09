from flask_wtf import CSRFProtect
from flask import Flask
from flask_sqlalchemy import SQLAlchemy


# import  pymysql
# pymysql.install_as_MySQLdb()

csrf = CSRFProtect()
models = SQLAlchemy()

def create_app(config_name):
    """创建app"""
    app = Flask(__name__)
    app.config.from_object("settings.DEBUG_CONFIG")

    #惰性加载
    csrf.init_app(app)
    models.init_app(app)

    #注册蓝图
    from .main import main as mainBlueProject
    app.register_blueprint(mainBlueProject)

    return app
