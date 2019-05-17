from flask_restful import Resource, reqparse

# from models.message import MessageModel
# from models.people import PeopleModel\
from models.drawings import DrawingModel


class MatrixAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('drawing',
                        location='json',
                        type=str,
                        required=True,
                        help="Message field cannot be left blank!"
                        )
    parser.add_argument('recipient',
                        location='json',
                        type=str,
                        required=True,
                        help="Recipient field cannot be left blank!"
                        )
    parser.add_argument('sender',
                        location='json',
                        type=str,
                        required=True,
                        help="Recipient field cannot be left blank!"
                        )

    def post(self):
        data = self.parser.parse_args()
        # print(data)

        if DrawingModel.find_by_drawing(data['drawing']):
            return {'message': "A drawing like this already exists."}, 400

        drawing = DrawingModel(**data)
        try:
            drawing.save_to_db()
        except Exception as e:
            return {"message": "An error occurred while saving the item.",
                    "error": "{}".format(e)}, 500

        return {"message": "success"}, 201
