#!/usr/bin/python3
"""
Script that uses a REST API to return information about
an employee's TODO list progress.
"""

import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch user data
    user = requests.get(
        f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    ).json()
    name = user.get("name")

    # Fetch todos for this user
    todos = requests.get(
        f"https://jsonplaceholder.typicode.com/todos",
        params={"userId": employee_id}
    ).json()

    # Compute total and completed tasks
    total_tasks = len(todos)
    done_tasks = [task for task in todos if task.get("completed")]

    # Display output
    print(f"Employee {name} is done with tasks({len(done_tasks)}/{total_tasks}):")
    for task in done_tasks:
        print(f"\t {task.get('title')}")
