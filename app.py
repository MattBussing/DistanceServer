from flask import Flask
from flask_restful import Api, Resource, reqparse

pi_s = []

class Pi(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
        type=str,
        required=True,
        help="This field cannot be left blank!"
    )

    def put(self, name):
        data = Pi.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, pi_s), None)
        if item is None:
            item = {'name': name, 'message': data['message']}
            pi_s.append(item)
        else:
            item.update(data)
        return item

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, pi_s), None)
        return {'item': item}, 200 if item else 404


app = Flask(__name__)

# TODO comment out
app.config['DEBUG'] = True

# app.secret_key = 'jose'
api = Api(app)

api.add_resource(Pi, '/pi/<string:name>')

if __name__ == '__main__':
    app.run(port=5000)
