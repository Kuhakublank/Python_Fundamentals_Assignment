from todo_operations import add_task, view_tasks, delete_task
from utils import clr_scr, u_input

def main():
    while True:
        clr_scr()
       
        print("\n--- To-Do List Menu ---")
        print("1. Add a new to-do item")
        print("2. View all to-do items")
        print("3. Delete an item by index")

        choice = u_input("Choose an option (1,2,3) or 'exit'to terminate the program: ")
        
        if choice.lower() == 'exit':
            print("Have a great time.")
            break
        if choice == "1":
            task = u_input("Enter a new task: ")
            add_task(task)
        elif choice == "2":
            print("\nYour To-Do List:")
            view_tasks()
            u_input("Press Enter to continue...")
        elif choice == "3":
            view_tasks()
            try:
                index = int(u_input("Enter the task index to delete: "))
                delete_task(index)
            except ValueError:
                print("Invalid input. Please enter a number.")
            u_input("Press Enter to continue...")
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
