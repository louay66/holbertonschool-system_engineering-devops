#!/usr/bin/python3
""" fetch api"""

import requests
from sys import argv


if __name__ == "__main__":
    try:
        int(argv[1])
    except Exception as f:
        exit(1)
    
    user_id = argv[1]
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{user_id}")
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
        f"Employee {name_user} is done with tasks({completed}/{avrge_todos}):")

    for titel in todo.json():
        if titel.get("userId") == int(user_id) and titel.get('completed'):
            print("\t{}".format(titel.get('title')))
