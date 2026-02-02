# todo list
# menu 
# allow user to add, view, and delete tasks
# store tasks
# loops

def display_menu():
    print("\nTodo List Menu:")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Delete Task")
    print("4. Exit")
    
def user_choice():
    try:
        choice = int(input("Choose a option 1-4: "))
        return choice
    except ValueError:
        print("Please choose a NUMBER between 1-4: ")
        return None

tasks_list = []

while True:
    display_menu()
    choice = user_choice()
    
    if choice is None:
        continue
        
    print(f"You selected: {choice}\n")
    
    if choice == 1:
        task = input("Enter a new task: ")
        tasks_list.append(task)
        print(f"Task '{task}' added.\n")
        
    elif choice == 2:
        if not tasks_list:
            print("No existing tasks yet.\n")
        else:
            print("Your task: ")
            for i, task in enumerate(tasks_list, start=1):
                print(f"{i}, {task}")
            print()
        
    elif choice == 3:
        if not tasks_list:
            print("No existing task to delete.\n")
        else:
            for i, task in enumerate(tasks_list, start=1):
                print(f"{i}. {task}")
        try:
            task_id = int(input("Enter the task number you want deleted: "))
            removed_task = tasks_list.pop(task_id - 1)
            print(f"Removed task: {removed_task}\n")
            
        except (ValueError, IndexError):
            print("Choose a valid task(cant be out of range)\n")         
        
    elif choice == 4:
        print("Exiting ToDo List...")
        break
    
    else:
        print("INVALID CHOICE, PLEASE TRY AGAIN\n")
        
        
        