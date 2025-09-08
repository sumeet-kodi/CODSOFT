
list_of_all_tasks = []

def add_new_task_to_list():
    user_entered_description = input("Enter task description: ")
    user_entered_due_date = input("Enter due date (optional, press Enter to skip): ")

    new_task_dictionary = {
        "task_description": user_entered_description,
        "task_status": "Pending",
        "task_due_date": user_entered_due_date if user_entered_due_date else None
    }

    list_of_all_tasks.append(new_task_dictionary)
    print("✅ Task added successfully.\n")

def mark_task_as_completed():
    show_all_tasks()
    try:
        user_selected_index = int(input("Enter task number to mark as completed: "))
        if 0 <= user_selected_index < len(list_of_all_tasks):
            list_of_all_tasks[user_selected_index]["task_status"] = "Done"
            print("✅ Task marked as completed.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def delete_task_from_list():
    show_all_tasks()
    try:
        user_selected_index = int(input("Enter task number to delete: "))
        if 0 <= user_selected_index < len(list_of_all_tasks):
            list_of_all_tasks.pop(user_selected_index)
            print("🗑️ Task deleted successfully.\n")
        else:
            print("⚠️ Invalid task number.\n")
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

def show_all_tasks():
    if not list_of_all_tasks:
        print("📭 No tasks available.\n")
        return

    print("\n📋 Your To-Do List:")
    for index in range(len(list_of_all_tasks)):
        current_task = list_of_all_tasks[index]
        print(f"\nTask #{index}")
        print(f"  Description: {current_task['task_description']}")
        print(f"  Status    : {current_task['task_status']}")
        if current_task['task_due_date']:
            print(f"  Due Date  : {current_task['task_due_date']}")
    print()

def display_main_menu():
    print("=== To-Do List Menu ===")
    print("1. Add a new task")
    print("2. Mark a task as done")
    print("3. Delete a task")
    print("4. View all tasks")
    print("5. Exit")


while True:
    display_main_menu()
    user_choice_input = input("Choose an option (1-5): ")

    if user_choice_input == '1':
        add_new_task_to_list()
    elif user_choice_input == '2':
        mark_task_as_completed()
    elif user_choice_input == '3':
        delete_task_from_list()
    elif user_choice_input == '4':
        show_all_tasks()
    elif user_choice_input == '5':
        print("👋 Exiting the To-Do List. Goodbye!")
        break
    else:
        print("⚠️ Invalid option. Please try again.\n")
