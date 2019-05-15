import os

from flask import Flask
from flask_restful import Api

from resources.client import Client
from resources.form import MessageForm, UserForm
from resources.home import Home
from resources.thinking_of import ThinkingOf

app = Flask(__name__)

app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
    'DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)

api.add_resource(Home, '/')
api.add_resource(MessageForm, '/send')
api.add_resource(UserForm, '/user')
api.add_resource(Client, '/data/<string:_to>')
api.add_resource(ThinkingOf, '/thinking_of/<string:_to>')


if __name__ == '__main__':
    from db import db
    db.init_app(app)

    if app.config['DEBUG']:
        @app.before_first_request
        def create_tables():
            db.create_all()

    app.run(port=5000)
