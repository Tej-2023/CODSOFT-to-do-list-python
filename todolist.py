import sys

# Initialize an empty to-do list
todo_list = []

def display_menu():
    print("\nTo-Do List Application")
    print("1. View To-Do List")
    print("2. Add Task")
    print("3. Update Task")
    print("4. Remove Task")
    print("5. Exit")

def view_todo_list():
    if not todo_list:
        print("\nYour to-do list is empty.")
    else:
        print("\nTo-Do List:")
        for idx, task in enumerate(todo_list, 1):
            print(f"{idx}. {task}")

def add_task():
    task = input("\nEnter the task: ")
    todo_list.append(task)
    print("Task added successfully.")

def update_task():
    view_todo_list()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to update: "))
            if 1 <= task_num <= len(todo_list):
                new_task = input("Enter the new task: ")
                todo_list[task_num - 1] = new_task
                print("Task updated successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def remove_task():
    view_todo_list()
    if todo_list:
        try:
            task_num = int(input("\nEnter the task number to remove: "))
            if 1 <= task_num <= len(todo_list):
                todo_list.pop(task_num - 1)
                print("Task removed successfully.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        try:
            choice = int(input("\nEnter your choice: "))
            if choice == 1:
                view_todo_list()
            elif choice == 2:
                add_task()
            elif choice == 3:
                update_task()
            elif choice == 4:
                remove_task()
            elif choice == 5:
                print("Exiting the application.")
                sys.exit()
            else:
                print("Invalid choice. Please enter a number between 1 and 5.")
        except ValueError:
            print("Please enter a valid number.")

if __name__ == "__main__":
    main()
