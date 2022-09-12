#!/usr/bin/python3
"""export data in json format"""

from json import dump
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]
    url = "https://jsonplaceholder.typicode.com"
    user = get("{}/users/{}".format(url, user_id)).json()
    todo = get('{}/todos?userId={}'.format(url, user_id)).json()
    u_name = user.get('username')
    format = {}
    format[user_id] = []
    file = '{}.json'.format(user_id)
    for value in todo:
        append = {'task': value['title'], 'completed': value['completed'],
                  'username': u_name}
        format[user_id].append(append)

    with open(file, 'w') as a:
        dump(format, a)
