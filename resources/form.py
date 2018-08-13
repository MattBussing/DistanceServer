from flask_restful import Resource, reqparse
from flask import render_template, make_response

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
