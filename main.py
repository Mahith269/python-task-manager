
from storage import load_tasks, save_tasks


def add_task(tasks, title):
    # Find the largest existing ID
    if tasks:
        new_id = max(task["id"] for task in tasks) + 1
    else:
        new_id = 1

    # Create the new task
    task = {
        "id": new_id,
        "title": title,
        "completed": False
    }

    # Add it to the list
    tasks.append(task)

    return task

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = True
            return task

    return None

def delete_task(tasks, task_id):
    for task in tasks:
        if task["id"] == task_id:
            tasks.remove(task)
            return True

    return False

tasks = []

def list_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n--- Your Tasks ---")
    for task in tasks:
        status = "Completed" if task["completed"] else "Pending"
        print(f'{task["id"]}. {task["title"]} - {status}')


def main():
    # Load tasks when the program starts
    tasks = load_tasks()

    while True:
        print("\n===== TASK MANAGER =====")
        print("1. Add task")
        print("2. List tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ").strip()

        if choice == "1":
            title = input("Enter task title: ").strip()

            if not title:
                print("Task title cannot be empty.")
                continue

            task = add_task(tasks, title)
            save_tasks(tasks)
            print(f'Task added: {task["title"]} (ID: {task["id"]})')

        elif choice == "2":
            list_tasks(tasks)

        elif choice == "3":
            try:
                task_id = int(input("Enter task ID to complete: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue

            task = complete_task(tasks, task_id)

            if task is not None:
                save_tasks(tasks)
                print(f'Task "{task["title"]}" marked as completed.')
            else:
                print("Task not found.")

        elif choice == "4":
            try:
                task_id = int(input("Enter task ID to delete: "))
            except ValueError:
                print("Please enter a valid numeric ID.")
                continue

            if delete_task(tasks, task_id):
                save_tasks(tasks)
                print("Task deleted successfully.")
            else:
                print("Task not found.")

        elif choice == "5":
            print("Tasks saved. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-5.")

            
if __name__ == "__main__":
    main()

