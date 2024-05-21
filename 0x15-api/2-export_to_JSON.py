#!/usr/bin/python3
"""
Records all tasks that are owned by this employee
Format must be: { "USER_ID": [{"task": "TASK_TITLE",
"completed": TASK_COMPLETED_STATUS, "username": "USERNAME"},
{"task": "TASK_TITLE", "completed": TASK_COMPLETED_STATUS, "username":
"USERNAME"}, ... ]}
File name must be: USER_ID.json
"""
import json
import requests
import sys


def get_user_name(id) -> str:
    """fetch username"""
    uri = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(uri).json().get("username")
    return name


def main():
    """main func"""
    url_for_all_todos = 'https://jsonplaceholder.typicode.com/todos/'
    user_id = int(sys.argv[1])
    userName = get_user_name(user_id)

    all_todos = requests.get(url_for_all_todos).json()
    user_todos = [i for i in all_todos if i.get("userId") == user_id]

    todos = []

    for todo in user_todos:
        obj = {"task": f'{todo.get("title")}', "completed":
               todo.get("completed"), "username": userName}
        todos.append(obj)

    data = {f"{user_id}": todos}
    dt = json.dumps(data)

    with open(f"{user_id}.json", "w") as f:
        f.write(dt)


if __name__ == "__main__":
    main()
