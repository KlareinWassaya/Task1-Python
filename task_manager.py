"""
All task management functions collected in this file, add_task, delete_task,
change_priority, mark_as_done and sort_tasks
"""

from task import *

FILENAME = "tasks.json"


def input_valid_integer(
    message: str, range_end: int, range_start: int = 0
):
    """
    Handle the case where user tries to enter invalid entry\n
    message: the prompt to be printed in input()\n
    range_end: the exclusive end of the ranging period\n
    range_start: 0 by default, the starting of the ranging period, can be modified by user
    """
    while True:
        try:
            variable = int(input(message))

            if variable not in range(range_start, range_end):
                print(f"Value {variable} is not in range {range_start} -> {range_end - 1}")
            else:
                return variable
        except Exception as e:
            print(f"ERROR: {e}")


# Add a new task to the list based on properties entered by the user
def add_task(tasks: list):
    """
    Create a new instance of Task and add it to the tasks list
    """
    title = input("Enter Title of the task: ")
    description = input("Enter Description of the task: ")
    
    priority = input_valid_integer(
        message="Enter priority (highest 0 - lowest 5): ",
        range_end=6,
    )

    # user may prefer to choose the status of the task instead of marking it 'in progress' by default
    for i, status in enumerate(TaskStatuses, 1):
        status = status.value
        print(f"{i}- {status}")
    status_index = input_valid_integer(
        message="Choose the status of this task: ",
        range_end=len(TaskStatuses) + 1,
        range_start=1,
    )
    task_status = list(TaskStatuses)[status_index - 1].value

    # Add a new task as a Task object to the tasks list
    task = Task(title, description, priority, task_status)
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
            print(f"Task {i}")
            task.display()


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
        choice = input_valid_integer(
            message="Choose the task id to mark as done: ",
            range_end=len(tasks) + 1,
            range_start=1,
        )

        # Set the status of the chosen task as 'done'
        tasks[choice - 1].mark_done()
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
        choice = input_valid_integer(
            message="Choose the task id to change its priority: ",
            range_start=1,
            range_end=len(tasks) + 1,
        )

        # Ask the user to enter new value for priority, handle wrong entry
        new_priority = input_valid_integer(
            message="Enter new priority: ",
            range_end=6,
        )

        # Update the priority in the tasks list
        tasks[choice - 1].update_priority(new_priority)
        print(f"Priority of Task {choice} updated successfully")


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
        choice = input_valid_integer(
            message="Choose the task id to be deleted: ",
            range_start=1,
            range_end=len(tasks) + 1,
        )

        # allow the user to think again before deleting a task
        confirm = input(f"Are you sure you want to delete task {choice}? (y/n): ")[0].lower()
        if confirm == "y":
            tasks.pop(choice - 1)
            print(f"Task {choice} deleted successfully!")
        else:
            print(f"Task {choice} is not deleted")


# function for sorting tasks based on the user choice either ascending or descending
def sort_tasks(tasks: list):
    """
    Sort the tasks based on the priority ascending or descending according to the user choice
    """
    if not tasks:
        print("Your tasks list is empty, nothing found to be sorted")
    else:
        option = input_valid_integer(
            message="1- Ascending\n2- Descending\n1 or 2?\n",
            range_start=1,
            range_end=3,
        )

        reverse = option == 2
        print("Sorting Descending..." if reverse else "Sorting Ascending...")
        tasks.sort(key=lambda task: task.priority, reverse=reverse)
        print(f"Tasks sorted {'Descending' if reverse else 'Ascending'}:")
        view_tasks(tasks)
