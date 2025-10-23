#!/usr/bin/python3

"""
Script that uses a REST API to export Records all tasks from all employees.
"""

import json
import requests



if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users  = requests.get("https://jsonplaceholder.typicode.com/users").json()

    for user in users :
        json_data = {
            str(user): [
                {
                    "task": task.get("title"),
                    "completed": task.get("completed"),
                    "username": user
                } for task in todos

            ]
        }   

    with open ("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_data,jsonfile)   