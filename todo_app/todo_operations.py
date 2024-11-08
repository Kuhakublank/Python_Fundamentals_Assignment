#functions to add, view and delete tasks


tasks = []

def add_task(task):
    tasks.append(task)
    print("Task added!")

def view_tasks():
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            print(f"{i + 1}. {task}")

def delete_task(n):
    try:
        tasks.pop(n - 1)
        print("Task successfully deleted!")
    except IndexError:
        print("Invalid index. Task wasn't deleted!")
