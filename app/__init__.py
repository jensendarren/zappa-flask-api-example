from flask import Flask
from flask_restful import Api
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app, catch_all_404s=True)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models