#!/usr/bin/python3
"""
Records all tasks that are owned by this employee
Format must be: "USER_ID","USERNAME","TASK_COMPLETED_STATUS","TASK_TITLE"
File name must be: USER_ID.csv
"""
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

    with open(f"{user_id}.csv", "w") as f:
        for todo in user_todos:
            strr = '"{}","{}","{}","{}"'.format(
                user_id, userName, todo.get("completed"), todo.get("title"))
            f.write(strr + '\n')


if __name__ == "__main__":
    main()
