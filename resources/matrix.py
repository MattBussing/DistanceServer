from flask import redirect, url_for
from flask_restful import Resource, reqparse

# from models.message import MessageModel
# from models.people import PeopleModel


class MatrixAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('data',
                        type=str,
                        required=True,
                        help="Message field cannot be left blank!"
                        )
    # parser.add_argument('recipient',
    #                     type=str,
    #                     required=True,
    #                     help="Recipient field cannot be left blank!"
    #                     )

    def post(self):
        data = self.parser.parse_args()
        # since put it will update regardless
        # TODO delete
        # if MessageModel.search_for_message(**data):
        #     return {'message': "A message like this already exists."}, 400
        #
        # message = MessageModel(**data)
        # try:
        #     message.save_to_db()
        # except Exception as e:
        #     return {"message": "An error occurred while saving the item.",
        #             "error": "{}".format(e)}, 500

        print(data['data'])
        return redirect(url_for("home"))
