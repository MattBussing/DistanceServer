from flask_restful import Resource, reqparse

from models.thought_of import ThoughtOfModel


class ThinkingOf(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('increase_count_by',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, _to):
        thought_of = ThoughtOfModel.find_count(_to)
        return {'thought_of': thought_of}, 200

    def post(self, _to):
        data = self.parser.parse_args()
        thought = ThoughtOfModel(_to=_to, **data)
        try:
            thought.save_to_db()
        except:
            return {"message": "An error occurred while saving the item (count) to the database."}, 500
        return {"message": "Count increased"}, 200
