
import json
import os

# To-Do List Manager Class

class TodoList:
    def __init__(self, filename="todo_list.json"):
        self.filename = filename
        self.tasks = self.load_tasks()

    # Load tasks from a file
    def load_tasks(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                return json.load(f)
        return []

    # Save tasks to a file
    def save_tasks(self):
        with open(self.filename, "w") as f:
            json.dump(self.tasks, f, indent=4)

    # Add a task to the list
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        self.save_tasks()
        print(f"Task added: {task}")

    # List all tasks
    def list_tasks(self):
        if not self.tasks:
            print("No tasks found.")
        else:
            for i, task in enumerate(self.tasks, 1):
                status = "√" if task["completed"] else "x"
                print(f"{i}. {task['task']} [{status}]")

    # Mark a task as complete
    def complete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            self.tasks[task_number - 1]["completed"] = True
            self.save_tasks()
            print(f"Task {task_number} marked as complete.")
        else:
            print("Invalid task number.")

    # Delete a task
    def delete_task(self, task_number):
        if 0 < task_number <= len(self.tasks):
            deleted_task = self.tasks.pop(task_number - 1)
            self.save_tasks()
            print(f"Task deleted: {deleted_task['task']}")
        else:
            print("Invalid task number.")

def main():
    todo = TodoList()

    while True:
        print("\nCommands: add, list, complete <number>, delete <number>, exit")
        command = input("Enter command: ").strip().lower()

        if command == "add":
            task = input("Enter task: ").strip()
            todo.add_task(task)

        elif command == "list":
            todo.list_tasks()

        elif command.startswith("complete"):
            try:
                task_number = int(command.split()[1])
                todo.complete_task(task_number)
            except (IndexError, ValueError):
                print("Invalid command. Usage: complete <task_number>")

        elif command.startswith("delete"):
            try:
                task_number =int(command.split()[1])
                todo.delete_task(task_number)
            except (IndexError, ValueError):
                print("Invalid command. Usage: delete <task_number>")
        elif command == "exit":
            print("Goodbye!")
            break

        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()

