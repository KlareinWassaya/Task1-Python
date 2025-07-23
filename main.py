import json
from TaskManager import *


# Display the menu of services that can be done in this program
def display_menu():
    """
    Display the menu of options such as adding, editing
    or deleting a task from the tasks list
    """
    print("Choose from the following:")
    print("1- Add a Task")
    print("2- View Tasks")
    print("3- Sort tasks")
    print("4- Mark task as done")
    print("5- Change task priority")
    print("6- Delete task")
    print("7- Save to file")
    print("8- Exit Program")


# function for saving the tasks list to tasks.json file
def save_to_file(tasks: list):
    """
    Save the list of tasks to tasks.json file
    """
    tasks_list = []
    for task in tasks:
        tasks_list.append(task.to_dict())
    with open(FILENAME, "w") as file:
        json.dump(tasks_list, file, indent=4)

    print("Tasks saved to tasks.json file successfully!")


def main():
    # If the tasks.json file is not empty, load its content at the beginning of the run
    try:
        with open(FILENAME, "r") as file:
            loaded_tasks = json.load(file)
        tasks = [Task.from_dict(Task, d=task) for task in loaded_tasks]
    except Exception as e:
        print(f"ERROR: {e}")
        tasks = []  # define tasks as a list

    display_menu()

    while True:
        try:
            choice = int(input(""))
            match choice:
                case 1:
                    add_task(tasks)
                case 2:
                    view_tasks(tasks)
                case 3:
                    sort_tasks(tasks)
                case 4:
                    mark_as_done(tasks)
                case 5:
                    change_priority(tasks)
                case 6:
                    delete_task(tasks)
                case 7:
                    save_to_file(tasks)
                case 8:
                    print("Thank you for using our application!!\n\tGoodbye")
                    break
                case _:
                    print("Wrong Choice! \nPlease choose a number from 1 to 8:")
                    continue
            display_menu()
        except Exception as e:
            print(f"ERROR: {e}")


if __name__ == "__main__":
    main()
