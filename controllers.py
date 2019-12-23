from flask import render_template, request, redirect, url_for, jsonify
from models import ToDo, db

class AllMethods:

    def home(self):
        return render_template('index.html', data = ToDo.query.all())

    def create(self):
        description = request.get_json()['description']
        newToDo = ToDo(description = description)
        db.session.add(newToDo)
        db.session.commit()
        return jsonify({
            'description' : description
        })