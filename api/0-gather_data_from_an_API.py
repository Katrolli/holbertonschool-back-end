#!/usr/bin/python3
"""First api request"""
import json
import requests
from sys import argv


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

    count = 0
    completed_todos = []

    for items in curr_todo:
        if items['userId'] == curr_user['id']:
            count += 1
            if items['completed']:
                completed_todos.append(items)

    print('Employee {} is done with tasks({}/{}):'.format(
        curr_user['name'], len(completed_todos), count))

    for completed in completed_todos:
        print(f"\t{completed['title']}")
