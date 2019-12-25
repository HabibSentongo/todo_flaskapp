from flask import render_template
from controllers import AllMethods
from app import app

app._static_folder = 'templates/static'
methods = AllMethods()

@app.route('/', methods=['GET'])
def index():
    return methods.home()

@app.route('/todo/create', methods=['POST'])
def create():
    return methods.create()

@app.route('/todo/<todo_id>/complete', methods=['POST'])
def complete(todo_id):
    return methods.complete(todo_id)


if __name__ == '__main__':
    app.run(debug=True)