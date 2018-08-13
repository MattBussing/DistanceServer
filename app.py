from flask import Flask
from flask_restful import Api
from resources.form import Form
from resources.pi import Pi

app = Flask(__name__)

app.config['DEBUG'] = True

api = Api(app)

api.add_resource(Pi, '/pi/<string:name>')
api.add_resource(Form, '/form/<string:name>')

if __name__ == '__main__':
    app.run(port=5000)
