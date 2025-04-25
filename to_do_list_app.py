todo_list=[]
def show_menu():
    print("\n---todo list app---")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")
def add_task():
    task=input("Enter the task: ")
    todo_list.append(task)
    print(f"{task} has been added to the list.")
def view_tasks():
    if not todo_list:
        print("No tasks in the list.")
    else:
        print("\n---Tasks---")
        for i,task in enumerate(todo_list,1):
            print(f"{i}. {task}")
def remove_task():
    try:
        task_number=int(input("Enter the task number to remove: "))
        if 1<=task_number<=len(todo_list):
            removed=todo_list.pop(task_number-1)
            print(f"{removed} has been removed from the list.")
    except:
        print("Invalid task number. Please try again.")
while True:
    show_menu()
    Choice=input("Enter your choice (1-4): ")
    match Choice:
        case "1":
            add_task()
        case "2":
            view_tasks()
        case "3":
            remove_task()
        case "4":
            print("Exiting the program.")
            break