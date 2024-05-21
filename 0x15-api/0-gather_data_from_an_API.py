#!/usr/bin/python3
"""All about APIs!"""
import requests
import sys


def print_data(data, id):
    """format and output data"""
    EMPLOYEE_NAME = get_name(id)
    NUMBER_OF_DONE_TASKS = len(data.get("completed"))
    TOTAL_NUMBER_OF_TASKS = data.get("undone") + NUMBER_OF_DONE_TASKS

    print("Employee {} is done with tasks({}/{}):"
          .format(get_name(id), NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))
    for i in data.get("completed"):
        print(f"\t {i}")


def main():
    """program starts here"""
    empl_todos_data = {"undone": 0, "completed": []}
    empl_id = int(sys.argv[1])

    url = 'https://jsonplaceholder.typicode.com/todos/'
    res = requests.get(url=url).json()

    for obj in res:
        if obj.get("userId") == empl_id:
            if obj.get("completed"):
                empl_todos_data['completed'].append(obj.get("title"))
            else:
                empl_todos_data["undone"] += 1

    print_data(empl_todos_data, empl_id)


def get_name(id) -> str:
    """fetch name"""
    uri = f"https://jsonplaceholder.typicode.com/users/{id}"
    name = requests.get(uri).json().get("name")
    return name


if __name__ == "__main__":
    main()
