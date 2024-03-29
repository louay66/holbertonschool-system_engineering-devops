#!/usr/bin/python3
""" fetch api"""
import requests
from sys import argv


if __name__ == "__main__":

    user_id = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name_user = user.json().get('name')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")
    avrge_todos = 0
    completed = 0

    for tk in todo.json():
        if tk.get("userId") == int(user_id):
            avrge_todos += 1
            if tk.get('completed'):
                completed += 1
    print(
        "Employee {} is done with tasks({}/{}):"
        .format(name_user, completed, avrge_todos))

    for titel in todo.json():
        if titel.get("userId") == int(user_id) and titel.get('completed'):
            print("\t {}".format(titel.get('title')))
