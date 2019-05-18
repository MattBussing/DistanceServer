from flask_restful import Resource, reqparse

# from models.message import MessageModel
# from models.people import PeopleModel\
from models.drawings import DrawingModel


class MatrixAPI(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('drawing',
                        location='json',
                        type=list,
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
    todo fix so that it either stores differently or can be pulled off differently
    Ultimately we need to use the matrix so however we get the data down will work

    def post(self):
        data = self.parser.parse_args()
        print(data)
        print(data['drawing'])

        if DrawingModel.find_by_dsr(**data):
            print(data)
            return {'message': "A drawing like this already exists. {}".format(
                data)}, 400

        drawing = DrawingModel(**data)
        print(drawing.get_actual_vals())
        try:
            drawing.save_to_db()
        except Exception as e:
            return {"message": "An error occurred while saving the item.",
                    "error": "{}".format(e)}, 500

        return {"message": "success"}, 201
