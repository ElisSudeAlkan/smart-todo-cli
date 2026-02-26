import sys
from .manager import add_task, list_tasks, delete_task

def run():
    command = sys.argv[1]

    if command == "add":
        title = " ".join(sys.argv[2:])
        add_task(title)
        print("Task added")

    elif command == "list":
        tasks = list_tasks()
        for i, t in enumerate(tasks):
            print(i, "-", t["title"])

    elif command == "delete":
        index = int(sys.argv[2])
        delete_task(index)
        print("Task deleted")