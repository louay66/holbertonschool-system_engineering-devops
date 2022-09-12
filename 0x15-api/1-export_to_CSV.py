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

    file = '{}.csv'.format(user_id)

    with open(file, 'w') as a:

        for line in todo:
            line = [line['userId'], user_name,
                    line['completed'], line['title']]
            write = csv.writer(a, quoting=csv.QUOTE_ALL)
            write.writerow(line)
