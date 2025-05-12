
# mini project 2 : simple to do list

print("Welcome to the To-Do List App!")
print("You can add, view, and remove tasks.")
print("Type 'exit' to quit the app.")
print(" write 'add' to add a task")
print(" write 'view' to view all tasks")
print(" write 'remove' to remove a task")

tasks = []

while True:
    command = input("Enter a command: ").strip().lower()
    if command == 'add':
        task = input("Entre the task you want to add: ")
        tasks.append(task)
        print(f"Task '{task}' added to the list.")
    elif command == 'view':
        if tasks:
            print("our tasks are:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")
        else:
            print("No tasks in the list.")
    elif command == 'remove':
        try:
            task_number = int(input("Enter the task number to remove: "))
            if 1 <= task_number <= len(tasks):
                removed_task = tasks.pop(task_number - 1)
                print(f"Task '{removed_task}' removed from the list.")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")
    elif command == 'exit':
        print("Thank you for using the To-Do List App. Goodbye!")
        break
    else:
        print("Invalid command. Please try again.")
