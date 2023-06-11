import os
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from app.config import db_name


# Данные для подключения к серверу БД
pg_user = os.environ.get('POSTGRES_USER')
pg_password = os.environ.get('POSTGRES_PASSWORD')
pg_alias = os.environ.get('POSTGRES_ALIAS')
pg_port = os.environ.get('POSTGRES_PORT')
app_port = os.environ.get('APP_PORT')

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://{pg_user}:{pg_password}@{pg_alias}:{pg_port}/{db_name}'

db = SQLAlchemy(app)
api = Api(app)

from app import views, models

with app.app_context():
    db.create_all()

api.add_resource(views.User, "/user")
api.add_resource(views.Record, '/record')
