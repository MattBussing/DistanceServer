import unittest

import requests


class TestAdd(unittest.TestCase):

    postUrl = 'http://127.0.0.1:5000/'
    delUrl = 'http://127.0.0.1:5000/Matt'

    delJson = {'message': 'value'}
    postJson = {'message': 'value', '_to': 'Matt'}

    def deleteMessage(self):
        return requests.delete(url=self.delUrl, json=self.delJson)

    def postMessage(self):
        return requests.post(url=self.postUrl, json=self.postJson)

    def test_good_post(self):
        """
            Checks to see if it posts
        """
        self.deleteMessage()
        self.assertEqual(self.postMessage().status_code, 200)

    def test_good_delete(self):
        """
            Checks to see if it deletes the message
        """
        self.assertEqual(self.deleteMessage().status_code, 200)

    def test_bad_post(self):
        """
            Checks to see if it posts
        """
        self.postMessage()
        self.assertEqual(self.postMessage().status_code, 400)

    def test_bad_delete(self):
        """
            Checks to see if it deletes the message
        """
        self.deleteMessage()
        self.assertEqual(self.deleteMessage().status_code, 404)


if __name__ == '__main__':
    unittest.main()
