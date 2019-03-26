from flask_restful import Resource, reqparse

from models.message import MessageModel
from models.thought_of import ThoughtOfModel


class Client(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('message',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, _to):
        messages = MessageModel.find_all(_to)
        # print("messages", messages)
        thought_of = ThoughtOfModel.find_count(_to).count
        # print(thought_of)
        all = []
        if messages:
            all = [m.json()["message"] for m in messages]

        return {'messages': all, 'thought_of': thought_of}, 200

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
