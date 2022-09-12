#!/usr/bin/python3
"""fetch api and put it with csv"""
import requests
from sys import argv
import csv


if __name__ == "__main__":

    user_id = int(argv[1])
    user = requests.get("https://jsonplaceholder.typicode.com/users/{}"
                        .format(user_id))
    name_user = user.json().get('username')
    todo = requests.get("https://jsonplaceholder.typicode.com/todos")

    filename = str(user_id) + '.csv'
    with open (filename, mode='w') as a:
        write = csv.writer(a, delimiter=',', quotechar='"',
                            quoting=csv.QUOTE_ALL, lineterminator='\n')
        for line in todo.json():
            if line.get('userId') == int(user_id):
                write.writerow([user_id, name_user, str(line.get('completed')),
                                 line.get('title')])