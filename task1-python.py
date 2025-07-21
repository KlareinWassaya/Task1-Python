import json


# Add a new task to the list based on properties entered by the user
def add_task(i, tasks):
    title = str(input("Enter Title of the task: "))  # Request the title of the task
    description = str(
        input("Enter description of the task: ")
    )  # Request the description of the task

    while True:
        try:
            priority = int(
                input("Enter priority (highest 0 - lowest 5): ")
            )  # Request the priority of the task
            # Handle wrong entry of priority until user enters a valid priority from 0-5
            while priority not in range(6):
                print("Priority range from 0 to 5 only!")
                priority = int(input("Enter correct priority: \n"))
            break
        except:
            print("invalid entry")

    # user may prefer to choose the status of the task instead of marking it 'in progress' by default
    statuses = ["not started", "in progress", "done"]
    i = 1
    for status in statuses:
        print(f"{i}- {status}")
        i += 1
    while True:
        try:
            status_index = int(input("Choose the status of this task: ")) - 1
            while status_index not in range(len(statuses)):
                print("There is no such status, try again:")
                status_index = int(input(""))
            task_status = statuses[status_index]
            break
        except:
            print("invalid entry")

    # Add a new task as a dictionary to the tasks list
    task = {
        "title": title,
        "description": description,
        "priority": priority,
        "status": task_status,
    }
    tasks.append(task)
    print("Task added Successfully!!\n")

    return tasks


# Display the tasks on screen, organized in a simple way for easy human reading
def view_tasks(tasks):
    i = 1
    if tasks:
        for task in tasks:
            print(f"Task {i}:")
            for property, value in task.items():
                print(f"\t{property}: {value}")
            i += 1
    else:
        print("Your tasks list is empty\nEnjoy your free day!!\n")


# Sort the tasks list based on the priority ascending, 0 is the highest, 5 is the lowest
def sort_tasks(tasks):
    if tasks:
        tasks.sort(key=lambda x: x["priority"])
        print("Tasks sorted ascending:")
    else:
        print("There are no tasks to be sorted")


# Mark a task as 'done' based on user's input
def mark_as_done(tasks):
    if tasks:
        view_tasks(
            tasks
        )  # Display the tasks to allow the user to know which task to change

        # Ask the user to enter the id of the task, handle wrong entry
        while True:
            try:
                choice = int(input("Choose the task id to mark as done: "))
                while choice < 1 or choice > len(tasks):
                    print("There is no task with this id")
                    choice = int(input("Choose a correct ID: "))
                break  # if the user enters a correct choice, break from the infinite loop and continue
            except:
                print("You made a mistake, try again")

        # Set the status of the chosen task as 'done'
        tasks[choice - 1]["status"] = "done"
        print("Task ", choice, "marked as done successfully!")
    else:
        print(
            "Your tasks list is empty, try adding a task or filling the tasks.json and restart the program"
        )

    return tasks


# Change the priority of a task based on user's input
def change_priority(tasks):
    if tasks:
        view_tasks(tasks)  # Display the tasks to allow user to choose from them

        # Ask the user to enter the id of the task, handle wrong entry
        while True:
            try:
                choice = int(input("Choose the task id to its priority: "))
                while choice < 1 or choice > len(tasks):
                    print("There is no task with this id")
                    choice = int(input("Choose a correct ID: "))
                break  # if the user enters a correct choice, break from the infinite loop and continue
            except:
                print("You made a mistake, try again")

        # Ask the user to enter new value for priority, handle wrong entry
        while True:
            try:
                new_priority = int(input("Enter new priority: "))
                while new_priority > 5 or new_priority < 0:
                    print("Priority range from 0 to 5 only!")
                    new_priority = int(input("Enter correct priority: \n"))
                break
            except:
                print("invalid entry")

        # Update the priority in the tasks list
        tasks[choice - 1]["priority"] = new_priority
    else:
        print(
            "Your tasks list is empty, try adding a task or filling the tasks.json and restart the program"
        )

    return tasks


# Delete a task based on user's choice
def delete_task(tasks):
    if tasks:
        view_tasks(tasks)  # Display the tasks to allow user to choose from them

        # Ask the user to enter the id of the task, handle wrong entry
        while True:
            try:
                choice = int(input("Choose the id of the task to be deleted: "))
                while choice < 1 or choice > len(tasks):
                    print("There is no task with this id")
                    choice = int(input("Choose a correct ID: "))
                break  # if the user enters a correct choice, break from the infinite loop and continue
            except:
                print("You made a mistake, try again")

        # allow the user to think again before deleting a task
        if (
            (
                str(input(f"Are you sure you want to delete task {choice}? (y/n): "))[0]
            ).lower()
            == "y"
        ):
            del tasks[choice - 1]
            print("Task", choice, "deleted successfully!")
        else:
            print("Task", choice, "is not deleted")
    else:
        print(
            "Your tasks list is empty, try adding a task or filling the tasks.json and restart the program"
        )

    return tasks


# Display the menu of services that can be done in this program
def display_menu():
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
def save_to_file(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

    print("Tasks saved to tasks.json file successfully!")


def main():
    # If the tasks.json file is not empty, load its content at the beginning of the run
    try:
        with open("tasks.json", "r") as file:
            tasks = json.load(file)
    except:
        tasks = []  # define tasks as a list

    display_menu()

    while True:
        try:
            choice = int(input(""))
            match choice:
                case 1:
                    i = int(len(tasks))
                    tasks = add_task(i, tasks)
                case 2:
                    view_tasks(tasks)
                case 3:
                    sort_tasks(tasks)
                    view_tasks(tasks)
                case 4:
                    tasks = mark_as_done(tasks)
                case 5:
                    tasks = change_priority(tasks)
                case 6:
                    tasks = delete_task(tasks)
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
