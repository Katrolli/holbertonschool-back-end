#!/usr/bin/python3
"""First api request"""
import json
import requests
from sys import argv
import csv


if __name__ == "__main__":
    """Script that makes api request"""

    id = argv[1]
    todos = requests.get(
        'https://jsonplaceholder.typicode.com/todos')

    user = requests.get(
        'https://jsonplaceholder.typicode.com/users/{}'.format(id))

    todo_data = todos.text
    user_data = user.text

    curr_user = json.loads(user_data)
    curr_todo = json.loads(todo_data)

    with open('{}.csv'.format(id), 'w', newline='') as file:
        for items in curr_todo:
            if items['userId'] == curr_user['id']:
                ls = (id, curr_user['username'], str(
                    items['completed']), items['title'])
                writer = csv.writer(file, delimiter=',',
                                    quotechar='"', quoting=csv.QUOTE_ALL)
                writer.writerow(ls)
