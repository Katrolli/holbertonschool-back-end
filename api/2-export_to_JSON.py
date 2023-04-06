#!/usr/bin/python3
"""First api request"""
import csv
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

    todo_list = []
    for items in curr_todo:
        if items['userId'] == curr_user['id']:
            new_dict = {}
            new_dict['task'] = items['title']
            new_dict['completed'] = items['completed']
            new_dict['username'] = curr_user['username']
            todo_list.append(new_dict)
    final_dict = {str(curr_user['id']): todo_list}
    with open('{}.json'.format(id), 'w', newline='') as file:
        json.dump(final_dict, file)
