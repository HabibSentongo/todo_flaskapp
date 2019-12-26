from flask import render_template, request, redirect, url_for, jsonify
from models import ToDo, db
import sys

class AllMethods:

    def home(self):
        return render_template('index.html', data = ToDo.query.order_by('id').all())

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

    def complete(self, todo_id):
        error = False
        body = {}
        try:
            completed = request.get_json()['completed']
            todo = ToDo.query.get(todo_id)
            todo.completed = completed
            db.session.commit()
            body = {
                'description' : todo.description,
                'status' : todo.completed
                }
        except:
            error = True
            db.session.rollback()
            print(sys.exec_info())
        finally:
            db.session.close()
        return jsonify(body)

    def delete(self, todo_id):
        error = False
        body = {}
        try:
            ToDo.query.filter_by(id = todo_id).delete()
            db.session.commit()
            body = {
                'messege' : f'Task {todo_id} successfully Thanosed!',
                'status' : 202
                }
        except:
            error = True
            db.session.rollback()
            print(sys.exec_info())
        finally:
            db.session.close()
        return jsonify(body)