from flask import render_template
from models import ToDo

class AllMethods:

    def home():
        return render_template('index.html', data = ToDo.query.all())