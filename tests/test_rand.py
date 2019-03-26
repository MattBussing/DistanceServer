# Author Matt Bussing
import requests

url = 'http://127.0.0.1:5000'
test = "test"
client = "/" + test
client_url = url + client
del_url = client_url
post_url = url + "/"
del_json = {'message': 'value'}
post_json = {'message': 'value', '_to': test}

main_message_list = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

messages_deleted = False
new_count = 15
increment = 2


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


def _delete_all_messages():
    messages = _get_all_messages_and_count()[0]
    for i in messages:
        _delete_message({'message': i})


def test_get_messages():
    clean_up()
    temp = _get_all_messages_and_count()[0]
    temp.sort()
    main_message_list.sort()
    assert temp == main_message_list
