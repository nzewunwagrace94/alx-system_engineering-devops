#!/usr/bin/python3
"""
Records all tasks from all employees
Format must be: { "USER_ID": [ {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task":
"TASK_TITLE", "completed": TASK_COMPLETED_STATUS}, ... ], "USER_ID":
[ {"username": "USERNAME", "task": "TASK_TITLE", "completed":
TASK_COMPLETED_STATUS}, {"username": "USERNAME", "task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS}, ... ]}
File name must be: todo_all_employees.json
"""
import json
import requests


def get_user_name(id) -> str:
    """fetch username"""
    uri = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(uri).json().get("username")
    return name


def main():
    """main func"""
    url_for_all_todos = 'https://jsonplaceholder.typicode.com/todos/'
    all_todos = requests.get(url_for_all_todos).json()

    dic = {}

    for i in all_todos:
        if str(i.get('userId')) not in dic:
            dic[str(i.get('userId'))] = []

    for i in all_todos:
        userName = get_user_name(i.get('userId'))

        d = {
            "username": f"{userName}", "task": f"{i.get('title')}",
            "completed": i.get('completed')
            }
        dic[str(i.get('userId'))].append(d)

    dt = json.dumps(dic)

    with open("todo_all_employees.json", "w") as f:
        f.write(dt)


if __name__ == "__main__":
    main()
