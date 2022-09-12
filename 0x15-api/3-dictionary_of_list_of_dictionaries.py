#!/usr/bin/python3
"""export data in json format"""

from json import dump
import requests
from sys import argv


if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users").json()
    todo = requests.get('https://jsonplaceholder.typicode.com/todos').json()

    todo_all = {}

    for user in users:
        List_data = []
        for data in todo:
            if data.get('userId') == user.get('id'):
                data_dict = {"username": user.get('username'),
                             "task": data.get('title'),
                             "completed": data.get('completed')}
                List_data.append(data_dict)
        todo_all[user.get('id')] = List_data

    with open('todo_all_employees.json', mode='w') as a:
        dump(todo_all, a)
