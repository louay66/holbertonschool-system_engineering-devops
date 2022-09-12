#!/usr/bin/python3
"""exprt data in csv format"""
import csv
from requests import get
from sys import argv


if __name__ == "__main__":
    user_id = argv[1]

    url = "https://jsonplaceholder.typicode.com"

    user = get("{}/users/{}".format(url, user_id)).json()

    todo = get("{}/users/{}/todos".format(url, user_id)).json()

    user_name = user.get('username')

    file = '{}.json'.format(user_id)
    forma = {}
    forma[id] = []
    for value in todo:
        append = {'task': value['title'], 'completed': value['completed'],
                   'username': user_name}
        forma[id].append(append)
    with open(file, 'w') as a:
        dump(fmt, a)
