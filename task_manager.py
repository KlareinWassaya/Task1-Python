"""
All task management functions collected in this file, add_task, delete_task,
change_priority, mark_as_done and sort_tasks
"""

from Task import Task

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
    """
    Create a new instance of Task and add it to the tasks list
    """
    task_info = {}
    for attribute in Task.fields(Task):
        if attribute == "priority":
            priority = handle_wrong_entry(
                message="Enter priority (highest 0 - lowest 5): ",
                error_message="Priority range from 0 to 5 only!",
                range_end=6,
            )
            task_info[attribute] = priority
        elif attribute == "status":
            # user may prefer to choose the status of the task instead of marking it 'in progress' by default
            for i, status in enumerate(Task.statuses, 1):
                status = status.name.title().replace("_", " ")
                print(f"{i}- {status}")
            statuses_list = list(Task.statuses)
            status_index = handle_wrong_entry(
                message="Choose the status of this task: ",
                error_message="There is no such status, try again!",
                range_end=len(statuses_list) + 1,
                range_start=1,
            )
            task_info[attribute] = statuses_list[status_index - 1].name.title().replace("_", " ")
        else:
            value = input(f"Enter {attribute}: ")
            task_info[attribute] = value

    # Add a new task as a Task object to the tasks list
    task = Task.from_dict(Task, d=task_info)
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
            Task.display(task)


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

        reverse = option == 2
        print("Sorting Descending..." if reverse else "Sorting Ascending...")
        tasks.sort(key=lambda task: task.priority, reverse=reverse)
        print(f"Tasks sorted {'Descending' if reverse else 'Ascending'}:")
        view_tasks(tasks)
