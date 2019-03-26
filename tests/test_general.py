
import requests


class General():
    def __init__(self, url):
        self.url = url
        # url = 'http://127.0.0.1:5000/'
        self.post_url = url
        self.del_url = url + 'test'

        self.del_json = {'message': 'value'}
        self.post_json = {'message': 'value', '_to': 'test'}

    def delete_message():
        return requests.delete(url=del_url, json=del_json)

    def post_message():
        return requests.post(url=post_url, json=post_json)

    def test_good_post():
        """
            Checks to see if it posts
        """
        delete_message()
        assert post_message().status_code == 200

    def test_good_delete():
        """
            Checks to see if it deletes the message
        """
        assert delete_message().status_code == 200

    def test_bad_post():
        """
            Checks to see if it posts
        """
        post_message()

        assert post_message().status_code == 400

    def test_bad_delete():
        """
            Checks to see if it deletes the message
        """
        delete_message()
        assert delete_message().status_code == 404


General("https://distance-pi.herokuapp.com/")
