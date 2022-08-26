from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

# Create App
def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'semicircle_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    # Import Blueprint 블루프린트 인스턴스 가져오기
    from .views import views
    from .auth import auth

    # Apply Blueprint 플라스크 앱에 등록하기
    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    
    # DB에 사용할 모델 불러오기
    from .models import User, Note  # from .models import *
    create_database(app)

    # flask-login 적용
    login_manager = LoginManager()
    login_manager.login_view = 'auth.sign_in'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(id)  # primary_key
 
    return app

# 데이터 베이스 생성 함수
def create_database(app):
    # db파일이 확인안될 때만 생성
    if not path.exists('website/' + DB_NAME):
        db.create_all(app=app)
        print('>>> Create DB')