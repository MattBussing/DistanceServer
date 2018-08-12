from flask import Flask, render_template, make_response
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
        data = self.parser.parse_args()
        item = next(filter(lambda x: x['name'] == name, pi_s), None)
        if item is None:
            item = {'name': name, 'message': data['message']}
            pi_s.append(item)
        else:
            item.update(data)
        return item, 201

    def get(self, name):
        item = next(filter(lambda x: x['name'] == name, pi_s), None)
        return {'item': item}, 200 if item else 404

class Form(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )
    parser.add_argument('name',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
    )

    def get(self, name):
        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('form.html', name=name),200,headers)


    def post(self,name):
        data = self.parser.parse_args()
        item = next(filter(lambda x: x['name'] == data['name'], pi_s), None)
        if item is None:
            item = {'name': data['name'], 'message': data['message']}
            pi_s.append(item)
        else:
            item.update(data)

        headers = {'Content-Type': 'text/html'}
        return make_response(render_template('posted.html', name=data.name),200,headers)


app = Flask(__name__)

app.config['DEBUG'] = True

# app.secret_key = 'jose'
api = Api(app)

api.add_resource(Pi, '/pi/<string:name>')
api.add_resource(Form, '/form/<string:name>')

if __name__ == '__main__':
    app.run(port=5000)
