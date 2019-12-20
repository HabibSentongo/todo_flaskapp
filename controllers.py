from flask import render_template, request, redirect, url_for
from models import ToDo, db

class AllMethods:

    def home(self):
        return render_template('index.html', data = ToDo.query.all())

    def create(self):
        description = request.form.get('description', '')
        newToDo = ToDo(description = description)
        db.session.add(newToDo)
        db.session.commit()
        return redirect(url_for('index'))