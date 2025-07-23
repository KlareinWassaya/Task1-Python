import json
from enum import Enum

FILENAME = "tasks.json"


def handle_wrong_entry(
    message: str, error_message: str, range_end: int, range_start: int = 0
):
    """
    Handle the case where user tries to enter invalid entry\n
    message: the prompt to be printed in input()\n
    error_message: the desired error message to be printed when the input is out of range\n
    range_end: the exclusive end of the ranging period\n
    range_start: 0 by default, the starting of the ranging period, can be modified by user
    """
    print(f"start = {range_start}, end = {range_end}")
    while True:
        try:
            variable = int(input(message))

            if variable not in range(range_start, range_end):
                print(error_message)
            else:
                return variable
        except Exception as e:
            print(f"ERROR: {e}")


# Add a new task to the list based on properties entered by the user
def add_task(tasks: list):
    title = input("Enter Title of the task: ")  # Request the title of the task
    description = input(
        "Enter description of the task: "
    )  # Request the description of the task

    priority = handle_wrong_entry(
        message="Enter priority (highest 0 - lowest 5): ",
        error_message="Priority range from 0 to 5 only!",
        range_end=6,
    )

    # user may prefer to choose the status of the task instead of marking it 'in progress' by default
    statuses = Enum("statuses", "NOT_STARTED IN_PROGRESS DONE")
    for i, status in enumerate(statuses, 1):
        status = status.name.lower().replace("_", " ")
        print(f"{i}- {status}")
    statuses_list = list(statuses)
    status_index = handle_wrong_entry(
        message="Choose the status of this task: ",
        error_message="There is no such status, try again!",
        range_end=len(statuses_list) + 1,
        range_start=1,
    )
    task_status = statuses_list[status_index - 1]

    # Add a new task as a dictionary to the tasks list
    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "status": task_status.name.lower().replace("_", " "),
    }
    tasks.append(task)
    print("Task added Successfully!!\n")


# Display the tasks on screen, organized in a simple way for easy human reading
def view_tasks(tasks: list):
    """
    Display the list of tasks, written in a human friendly style
    """
    if not tasks:
        print("Your tasks list is empty\nEnjoy your free day!!\n")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"Task {i}:")
            for property, value in task.items():
                print(f"\t{property}: {value}")


# Mark a task as 'done' based on user's input
def mark_as_done(tasks: list):
    """
    Display the list of tasks and prompt the user to choose a task to be marked as done
    """
    if not tasks:
        print(
            f"Your tasks list is empty, try adding a task or filling the {FILENAME} and restart the program"
        )
    else:
        view_tasks(
            tasks
        )  # Display the tasks to allow the user to know which task to change

        # Ask the user to enter the id of the task, handle wrong entry
        choice = handle_wrong_entry(
            message="Choose the task id to mark as done: ",
            error_message="There is no task with this id",
            range_end=len(tasks) + 1,
            range_start=1,
        )

        # Set the status of the chosen task as 'done'
        tasks[choice - 1]["status"] = "done"
        print(f"Task {choice} marked as done successfully!")


# Change the priority of a task based on user's input
def change_priority(tasks: list):
    """
    Display the list of tasks and prompt the user to choose a task to change its priority
    """
    if not tasks:
        print(
            f"Your tasks list is empty, try adding a task or filling the {FILENAME} and restart the program"
        )
    else:
        view_tasks(tasks)  # Display the tasks to allow user to choose from them

        # Ask the user to enter the id of the task, handle wrong entry
        choice = handle_wrong_entry(
            message="Choose the task id to change its priority: ",
            error_message="There is no such task with this id!",
            range_start=1,
            range_end=len(tasks) + 1,
        )

        # Ask the user to enter new value for priority, handle wrong entry
        new_priority = handle_wrong_entry(
            message="Enter new priority: ",
            error_message="Priority range from 0 to 5 only!",
            range_end=6,
        )

        # Update the priority in the tasks list
        tasks[choice - 1]["priority"] = new_priority


# Delete a task based on user's choice
def delete_task(tasks: list):
    """
    Display the list of tasks and prompt the user to choose a task to be deleted
    """
    if not tasks:
        print(
            f"Your tasks list is empty, try adding a task or filling the {FILENAME} and restart the program"
        )
    else:
        view_tasks(tasks)  # Display the tasks to allow user to choose from them

        # Ask the user to enter the id of the task, handle wrong entry
        choice = handle_wrong_entry(
            message="Choose the task id to be deleted: ",
            error_message="There is no such task with this id!",
            range_start=1,
            range_end=len(tasks) + 1,
        )

        # allow the user to think again before deleting a task
        if (
            (
                str(input(f"Are you sure you want to delete task {choice}? (y/n): "))[0]
            ).lower()
            == "y"
        ):
            tasks.pop(choice - 1)
            print(f"Task {choice} deleted successfully!")
        else:
            print(f"Task {choice} is not deleted")


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
    with open(FILENAME, "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved to tasks.json file successfully!")


# function for sorting tasks based on the user choice either ascending or descending
def sort_tasks(tasks: list):
    """
    Sort the tasks based on the priority ascending or descending according to the user choice
    """
    if not tasks:
        print("Your tasks list is empty, nothing found to be sorted")
    else:
        option = handle_wrong_entry(
            message="1- Ascending\n2- Descending\n1 or 2?\n",
            error_message="No such option",
            range_start=1,
            range_end=3,
        )
        
        reverse = (option == 2)
        print("Sorting Descending..." if reverse else "Sorting Ascending...")
        tasks.sort(key=lambda task: task["priority"], reverse=reverse)
        print(f"Tasks sorted {'Descending' if reverse else 'Ascending'}:")
        view_tasks(tasks)


def main():
    # If the tasks.json file is not empty, load its content at the beginning of the run
    try:
        with open(FILENAME, "r") as file:
            tasks = json.load(file)
    except:
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
        except:
            print("wrong entry")


if __name__ == "__main__":
    main()
