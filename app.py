from flask import Flask
from flask_restful import Api
from resources.form import Form
from resources.client import Client

app = Flask(__name__)

app.config['DEBUG'] = True

api = Api(app)

api.add_resource(Client, '/pi/<string:_to>')
api.add_resource(Form, '/form')

if __name__ == '__main__':
    app.run(port=5000)
