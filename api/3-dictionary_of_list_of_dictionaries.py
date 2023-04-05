#!/usr/bin/python3
"""First api request"""
import csv
import json
import requests


def get_dict(id):
    """Method to get all tasks per id"""
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
            new_dict['username'] = curr_user['username']
            new_dict['task'] = items['title']
            new_dict['completed'] = items['completed']
            todo_list.append(new_dict)
    return todo_list


if __name__ == "__main__":
    """Script that makes api request"""
    user = requests.get(
        'https://jsonplaceholder.typicode.com/users')
    user_data = user.text
    all_users = json.loads(user_data)
    final_dict = {}
    for user in all_users:
        todo_list = get_dict(str(user['id']))
        final_dict[str(user['id'])] = todo_list
        break
    with open('todo_all_employees.json', 'w', newline='') as file:
        json.dump(final_dict, file)
