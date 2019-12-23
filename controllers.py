from flask import render_template, request, redirect, url_for, jsonify
from models import ToDo, db
import sys

class AllMethods:

    def home(self):
        return render_template('index.html', data = ToDo.query.all())

    def create(self):
        error = False
        body = {}
        try:
            description = request.get_json()['description']
            newToDo = ToDo(description = description)
            db.session.add(newToDo)
            db.session.commit()
            body = {'description' : newToDo.description}
        except:
            error = True
            db.session.rollback()
            print(sys.exec_info())
        finally:
            db.session.close()
        return jsonify(body)