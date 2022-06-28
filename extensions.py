from ensurepip import bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_bootstrap import Bootstrap5
from app import app

db = SQLAlchemy(app)
migrate = Migrate(app, db)
Bootstrap5(app)
admin = Admin(app, name='admin')