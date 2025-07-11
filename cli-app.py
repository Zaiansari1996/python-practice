print("Welcome To Your Task Manager")
tasks = []


def tasks_menu():
    print("enter following number related to your inquiry")
    print("\n1: Enter the task\n2: view the tasks\n3: Delete the task\n4: Exit")


# tasks_menu()
while True:
    tasks_menu()
    choice = input("Enter your choice: ")
    if choice == "1":
        new_task = input("Enter the new task")
        tasks.append(new_task)
        print("Task saved successfully")
    elif choice == "2":
        print("Below are the tasks currently saved in your task Manager")
        for i, task in enumerate(tasks):
            print(f"{i+1} : {task}")
    elif choice == "3":
        task_no = int(input("Enter the task number in the list to delete"))
        if 0 < task_no <= len(tasks):
            tasks.pop(task_no - 1)
            print(f"{task_no} deleted successfully")
        else:
            print("Invalid number.")
    elif choice == "4":
        break
    else:
        print("Invalid")

print("Existed the program")