#!/usr/bin/python3

"""
script that extracts data from api and writes the data to a csv file
"""
import csv
import requests
import sys

if __name__ == "__main__":
    employeeId = int(sys.argv[1])

    user = requests.get(f"https://jsonplaceholder.typicode.com/users/{employeeId}").json()
    name = user["name"]

    todos = requests.get(f"https://jsonplaceholder.typicode.com/todos?userId={employeeId}").json()

    data = []
    outputFile = f"{employeeId}.csv"

    for task in todos:
        if task["completed"]:
            data.append([f"{employeeId}",name,"True",task["title"]])
        data.append([f"{employeeId}",name,"False",task["title"]])
        



    with open(outputFile,"w",newline='') as csvfile :
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(data)
    