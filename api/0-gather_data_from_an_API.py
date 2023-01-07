#!/usr/bin/python3
"""
Write a Python script that, using this REST API,
for a given employee ID, returns information about his/her TODO list progress.
"""

from requests import get
from sys import argv


def api_todo():
    """
    This function accepts an integer as a parameter, which is the employee ID
    """
    employee_id = int(argv[1])
    employee_name = ""
    number_of_task = 0
    number_of_done_task = 0
    titles_of_task = []
    user_url = get("https://jsonplaceholder.typicode.com/users").json()
    task_url = get("https://jsonplaceholder.typicode.com/todos").json()

    for user in user_url:
        if user['id'] == employee_id:
            employee_name = user['name']

    for task in task_url:
        if task['userId'] == employee_id:
            if task['completed']:
                titles_of_task.append(task['title'])
                number_of_done_task += 1
            number_of_task += 1

    print("Employee {} is done with tasks({}/{}):".format(employee_name,
                                                          number_of_done_task,
                                                          number_of_task))

    for title in titles_of_task:
        print("\t " + title)

if __name__ == "__main__":
    api_todo()
