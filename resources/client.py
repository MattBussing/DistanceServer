from flask_restful import Resource, reqparse
from resources.message import MessageModel


class Client(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="You cannot leave the message blank"
    )

    def post(self, _to):
        data = self.parser.parse_args()
        if MessageModel.search_for_message(data.message, _to):
            return {'message': "A message like this already exists: {}\n'{}' already exists.".format(_to, data.message)}, 400

        message = MessageModel(_to, data.message)
        try:
            message.save_to_db()
        except:
            return {"message": "An error occurred while saving the item to the database."}, 500

        return message.json(), 201

    def get(self, _to):
        messages = MessageModel.find_all(_to)
    if messages:
        all = { 'messages' : [ m.json() for m in messages ] }
    else:
        all = { 'messages' : [ 'none' ]

    return all , 200
