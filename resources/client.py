from flask_restful import Resource, reqparse

from models.counter import Counter
from models.message import MessageModel


class Client(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, _to):
        messages = MessageModel.find_all(_to)
        counter = Counter.find_counter(_to)
        count = 0
        if counter is not None:
            count = counter.count
        all = []
        if messages:
            # TODO: FIX THIS TO SEND DATE TIME
            all = [m.json() for m in messages]

        return {'messages': all, 'count': count}, 200

    def delete(self, _to):
        data = self.parser.parse_args()
        message = MessageModel.search_for_message(_to=_to, **data)
        if not message:
            return {'message': "The message does not exist"}, 404

        try:
            message.delete_from_db()
        except:
            return ({"message":
                     "An error occurred while saving the item to the database."
                     },                    500)

        return {"message": "Item Deleted"}, 200
