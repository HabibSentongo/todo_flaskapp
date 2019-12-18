from flask import render_template
from controllers import AllMethods
from app import app

@app.route('/', methods=['GET'])
def index():
    return AllMethods.home()


if __name__ == '__main__':
    app.run(debug=True)