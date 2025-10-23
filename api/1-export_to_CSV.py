#!/usr/bin/python3
import requests
import sys
import s

employeeId = int(sys.argv[1])

user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employeeId}").json()
name = user["name"]

todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}").json()

data = []

for task in todos:
    if task["completed"]:
        data.append([f"{employeeId}",name,"True",task["title"]])
    data.append([f"{employeeId}",name,"False",task["title"]])
    




    