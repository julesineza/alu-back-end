#!/usr/bin/python3

"""
Script that uses a REST API to export data in the JSON format.
"""

import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch user and todos
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    username = user.get("username")

    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos", params={"userId": employee_id}).json()

    json_data = {
        str(employee_id): [
            {
                "task": task.get("title"),
                "completed": task.get("completed"),
                "username": username
            } for task in todos
        ]
    }

    filename = f"{employee_id}.json"
    with open(filename, "w") as jsonfile:
        json.dump(json_data, jsonfile)   
        