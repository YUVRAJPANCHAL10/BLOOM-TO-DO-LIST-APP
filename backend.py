
# My first Python project: To-Do List
tasks = []

def show_menu():
    print("\n===== TO-DO LIST =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Mark done")
    print("4. Delete task")
    print("5. Exit")


def add_task():
    new_task = input("Enter your task: ")
    if not new_task:
        print("Task cannot be empty!")
        return
    tasks.append({"task": new_task, "done": False})
    print("Task added successfully!")


def view_task():
    if not tasks:
        print("No tasks added yet!")
        return
    for i, item in enumerate(tasks, start=1):
        status = "Completed" if item["done"] else "Pending"
        print(f"{i}. {item['task']} : {status}")


def mark_done():
    view_task()
    if not tasks:
        print("No tasks available!")
        return
    try:
        index = int(input("Enter task number to mark as done: ")) - 1

        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            print(f"'{tasks[index]['task']}' marked as completed!")
        else:
            print("Enter a valid task number!")
    except ValueError:
        print("Please enter a valid number!")


def delete_task():
    if not tasks:
        print("No tasks available!")
        return
    view_task()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            deleted_task = tasks.pop(index)
            print(f"'{deleted_task['task']}' deleted successfully!")
        else:
            print("Enter a valid task number!")
    except ValueError:
        print("Please enter a valid number!")


while True:
    show_menu()
    try:
        choice = int(input("Choose an option (1-5): "))
        if choice == 1:
            add_task()
        elif choice == 2:
            view_task()
        elif choice == 3:
            mark_done()
        elif choice == 4:
            delete_task()
        elif choice == 5:
            print("Goodbyeee!")
            break
        else:
            print("Choose a valid option from 1-5!")
    except ValueError:
        print("Please enter a number!")