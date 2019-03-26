from flask_restful import Resource, reqparse

from models.counter import Counter


class ThinkingOf(Resource):
    parser = reqparse.RequestParser()
    parser.add_argument('increase_by',
                        type=int,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def get(self, _to):
        count = Counter.find_count(_to).count
        return {'count': count}, 200

    def post(self, _to):
        data = self.parser.parse_args()
        counter = Counter.find_counter(_to=_to)
        count = data["increase_by"]
        print("coutner", counter)
        print("count", count)

        if counter is not None:
            print("eyo")
            count += counter.count
            counter.delete_from_db()
        thought = Counter(_to, count)
        try:
            thought.save_to_db()
        except:
            return {"message": "An error occurred while saving the item (count) to the database."}, 500
        return {"message": "Count increased"}, 200

    def delete(self, _to):
        counter = Counter.find_counter(_to=_to)
        print("delete: counter:", counter)
        if counter is None:
            return {'message': "The counter doesn't exist"}, 404
        try:
            counter.delete_from_db()
        except:
            return {"message": "An error occurred while deleting the item (count) in the database."}, 500
        return {"message": "Count Deleted"}, 200
