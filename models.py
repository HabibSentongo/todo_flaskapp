from app import app
import os
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

migrate = Migrate(app, db)
class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key = True)
    description = db.Column(db.String, nullable = False)
    due = db.Column(db.DateTime, nullable = False, default = datetime.utcnow)
    completed = db.Column(db.Boolean, nullable = False, default = False)
    def __repr__():
        return f'<ID: {self.id}, Description: {self.description}, Due: {self.due}>'
