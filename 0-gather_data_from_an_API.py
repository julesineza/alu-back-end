#!/usr/bin/python3
import requests
import sys

employeeId = int(sys.argv[1])

user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employeeId}").json()
name = user["name"]

todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}").json()

doneWork = 0
totalWork = len(todos)
completed_tasks = []

for task in todos:
    if task["completed"]:
        completed_tasks.append(task["title"])
        doneWork += 1

print(f"Employee {name} is done with tasks({doneWork}/{totalWork}):")
for title in completed_tasks:
    print(f"\t {title}")
    