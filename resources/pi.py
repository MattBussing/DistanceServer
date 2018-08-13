from flask_restful import Resource, reqparse

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
