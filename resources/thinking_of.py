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

        # counter = Counter.find_counter(_to)
        # old_count = counter.count
        # print(old_count)
        # # this is so we can increment each one
        # if old_count:
        #     counter.delete_from_db()
        #     self.count = old_count + increase_count_by
        # else:
        #     self.count = increase_count_by

    def delete(self, _to):
        counter = Counter.find_counter(_to=_to)
        if not counter:
            return {'message': "The counter doesn't exist"}, 404

        try:
            counter.delete_from_db()
        except:
            return {"message": "An error occurred while deleting the item (count) in the database."}, 500
        return {"message": "Count Deleted"}, 200
