class TodoList:
    def __init__(self):
        self.tasks = []

    def add(self, task):
        self.tasks.append({'task': task, 'done': False})

    def view(self):
        for idx, task in enumerate(self.tasks, start=1):
            status = 'Done' if task['done'] else 'Pending'
            print(f"{idx}. [{status}] {task['task']}")

    def mark_done(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            self.tasks[task_index - 1]['done'] = True
            print("Task marked as done.")
        else:
            print("Invalid task index.")

    def delete(self, task_index):
        if 1 <= task_index <= len(self.tasks):
            del self.tasks[task_index - 1]
            print("Task deleted.")
        else:
            print("Invalid task index.")


def main():
    todo_list = TodoList()

    while True:
        print("\n===== To-Do List Menu =====")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            task = input("Enter the task: ")
            todo_list.add(task)
        elif choice == '2':
            print("\n===== Your Tasks =====")
            todo_list.view()
        elif choice == '3':
            task_index = int(input("Enter the index of the task to mark as done: "))
            todo_list.mark_done(task_index)
        elif choice == '4':
            task_index = int(input("Enter the index of the task to delete: "))
            todo_list.delete(task_index)
        elif choice == '5':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
