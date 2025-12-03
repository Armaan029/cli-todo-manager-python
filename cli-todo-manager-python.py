import json
import os

DATA_FILE = "tasks.json"

def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return []

def save_tasks(tasks):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)

def add_task():
    title = input("Task title: ")
    priority = input("Priority (low/medium/high): ").lower()
    task = {
        "title": title,
        "priority": priority,
        "done": False
    }
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    print("Task added.")

def list_tasks(filter_priority=None):
    tasks = load_tasks()
    if not tasks:
        print("No tasks found.")
        return

    for idx, task in enumerate(tasks, start=1):
        if filter_priority and task["priority"] != filter_priority:
            continue
        status = "✓" if task["done"] else " "
        print(f"{idx}. [{status}] {task['title']} (priority: {task['priority']})")

def mark_done():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to mark.")
        return

    list_tasks()
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]["done"] = True
            save_tasks(tasks)
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    tasks = load_tasks()
    if not tasks:
        print("No tasks to delete.")
        return

    list_tasks()
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            removed = tasks.pop(index)
            save_tasks(tasks)
            print(f"Deleted task: {removed['title']}")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def filter_by_priority():
    priority = input("Enter priority to filter (low/medium/high): ").lower()
    print(f"\nTasks with priority: {priority}")
    list_tasks(filter_priority=priority)

def main():
    while True:
        print("\n=== CLI To-Do Manager ===")
        print("1. Add task")
        print("2. List all tasks")
        print("3. Mark task as done")
        print("4. Delete task")
        print("5. Filter tasks by priority")
        print("6. Exit")

        choice = input("Enter choice (1-6): ")

        if choice == "1":
            add_task()
        elif choice == "2":
            list_tasks()
        elif choice == "3":
            mark_done()
        elif choice == "4":
            delete_task()
        elif choice == "5":
            filter_by_priority()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
