tasks = []

def add_task():
    task = input("Enter task: ")

    tasks.append({
        "title": task,
        "completed": False
    })

    print("Task added successfully!")


def view_tasks():

    if not tasks:
        print("No tasks available.")
        return

    print("\nTasks:")

    for index, task in enumerate(tasks, start=1):

        status = "✓" if task["completed"] else "✗"

        print(f"{index}. {task['title']} [{status}]")


def complete_task():

    view_tasks()

    try:
        task_num = int(input("Enter task number to complete: "))

        tasks[task_num - 1]["completed"] = True

        print("Task marked as completed!")

    except (ValueError, IndexError):
        print("Invalid task number.")


def delete_task():

    view_tasks()

    try:
        task_num = int(input("Enter task number to delete: "))

        removed_task = tasks.pop(task_num - 1)

        print(f"Deleted: {removed_task['title']}")

    except (ValueError, IndexError):
        print("Invalid task number.")


def main():

    while True:

        print("\n===== TO-DO LIST =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Complete Task")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_task()

        elif choice == "2":
            view_tasks()

        elif choice == "3":
            complete_task()

        elif choice == "4":
            delete_task()

        elif choice == "5":
            print("Goodbye!")
            break

        else:
            print("Invalid choice")


main()