#!/usr/bin/python3

"""
Script that uses a REST API to export Records all tasks from all employees.
"""

import json
import requests



if __name__ == "__main__":

    todos = requests.get("https://jsonplaceholder.typicode.com/todos").json()
    users  = requests.get("https://jsonplaceholder.typicode.com/users").json()

    json_data = {}

    for user in users:
        user_tasks = [
            {
                "username": user["username"],
                "task": task["title"],
                "completed": task["completed"]
            }
            for task in todos if task["userId"] == user["id"]
        ]
        json_data[str(user["id"])] = user_tasks

    with open("todo_all_employees.json", "w") as jsonfile:
        json.dump(json_data, jsonfile, indent=4)