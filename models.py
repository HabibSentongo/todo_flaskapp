from views import app
from flask_sqlalchemy import SQLAlchemy

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class ToDo(db.Model):
    __tablename__ = 'todo'
    id = db.Column(db.Integer, primary_key = True)