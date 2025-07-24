from enum import Enum

class TaskStatuses(Enum):
    NOT_STARTED = "Not Started"
    IN_PROGRESS = "In Progress"
    DONE = "Done"

class Task:

    def __init__(self, title: str, description: str, priority: int, status: str):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status
    
    def display(self):
        """
        Display all properties with their values
        """
        for attr, value in self.__dict__.items():
            print(f"\t{attr.capitalize()}: {value}")

    def mark_done(self):
        """
        Change the value of status property to 'Done'
        """
        self.status = (TaskStatuses.DONE).value

    def update_priority(self, value: int):
        """
        Assign a new value to the priority property of the task\n
        value: holds the new value of priority
        """
        self.priority = value
    