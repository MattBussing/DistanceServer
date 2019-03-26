# Author Matt Bussing
import requests


def wrapper(url):

    test = "test"
    client_url = url + test
    del_url = client_url
    thinking_of = "thinking-of"
    thinking_url = url + thinking_of + '/' + test

    main_message_list = ['lol', 'sadfads', 'i hate lol', 'asdfasdfasdf']

    def _clean_up(need_to: bool = False):
        _post_all_messages()

    def _post_all_messages():
        _delete_all_messages()
        for i in main_message_list:
            assert 200 == _post_message(
                post_data={'message': i, '_to': test}).status_code

    def _delete_all_messages():
        messages = _get_all_messages_and_count()[0]
        for i in messages:
            assert 200 == _delete_message({'message': i}).status_code

    def _delete_message(del_data):
        return requests.delete(url=del_url, json=del_data)

    def _post_message(post_data):
        return requests.post(url=url, json=post_data)

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

    def test_get_messages():
        _clean_up()
        temp = _get_all_messages_and_count()[0]
        temp.sort()
        main_message_list.sort()
        assert temp == main_message_list

    def test_increase_count():
        requests.delete(url=thinking_url).status_code
        increment = 2
        assert 200 == _increaset_count(increment).status_code
        temp = _get_all_messages_and_count()[1]
        assert increment == temp
        old = increment
        increment = 5
        assert 200 == _increaset_count(increment).status_code
        temp = _get_all_messages_and_count()[1]
        assert old + increment == temp

    def test_increase_count_pt_2():
        # this is where we test the delete fxn
        assert 200 == requests.delete(url=thinking_url).status_code

        # this is just to make sure that everything
        # works by deleting and trying again
        test_increase_count()

    test_increase_count()
    test_increase_count_pt_2()
    test_get_messages()


def test_wrapper():
    wrapper('http://127.0.0.1:5000/')
    wrapper("https://distance-pi.herokuapp.com/")
