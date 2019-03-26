# Author Matt Bussing
import requests

url = 'http://127.0.0.1:5000'
# url = "https://distance-pi.herokuapp.com"

test = "test"
client = "/" + test
client_url = url + client
del_url = client_url
post_url = url + "/"
del_json = {'message': 'value'}
post_json = {'message': 'value', '_to': test}

thinking_of = "thinking-of"
thinking_url = client_url + "/" + thinking_of

main_message_list = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

messages_deleted = False
new_count = 15


def clean_up(need_to: bool = False):
    # global messages_deleted
    # if not messages_deleted or need_to:
    #     messages_deleted = True
    #     # _delete_all_messages()
    for i in main_message_list:
        _post_message(post_data={'message': i, '_to': test})


def _delete_message(del_data):
    requests.delete(url=del_url, json=del_data)


def _post_message(post_data):
    return requests.post(url=post_url, json=post_data)


def _get_all_messages_and_count():
    req_data = requests.get(url=client_url)
    message_list = []
    count = 0
    if(req_data.status_code == 200):
        data = req_data.json()
        message_list = data['messages']
        if data['count'] is not None:
            count = data['count']
    else:
        print(req_data.status_code)
    return (message_list, count)


def _increaset_count(increment):
    return requests.post(url=thinking_url, json={
        "increase_by": increment})


def test_increase_count():
    assert 200 == requests.delete(url=thinking_url).status_code
    increment = 2
    _increaset_count(increment)
    temp = _get_all_messages_and_count()[1]
    assert increment == temp
    old = increment
    increment = 5
    _increaset_count(increment)
    temp = _get_all_messages_and_count()[1]
    assert old + increment == temp


def test_increase_count_pt_2():
    # this is just to make sure that everything
    # works by deleting and trying again
    test_increase_count()
