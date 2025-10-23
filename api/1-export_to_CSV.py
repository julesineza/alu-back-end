#!/usr/bin/python3

"""
Script that uses a REST API to export data in the CSV format.
"""

import csv
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch user and todos
    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employee_id}").json()
    username = user.get("username")

    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos", params={"userId": employee_id}).json()

    # Prepare CSV data
    filename = f"{employee_id}.csv"
    with open(filename, "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        for task in todos:
            writer.writerow([
                str(employee_id),
                username,
                str(task.get("completed")),
                task.get("title")
            ])
