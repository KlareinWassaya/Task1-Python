from enum import Enum


class Task:
    statuses = Enum("statuses", "NOT_STARTED IN_PROGRESS DONE")

    def __init__(self, title: str, description: str, priority: int, status: str):
        self.title = title
        self.description = description
        self.priority = priority
        self.status = status

    def fields(self):
        """
        Return the name of properties to be filled in this function
        """
        return ["title", "description", "priority", "status"]
    
    def to_dict(self):
        """
        Convert the type of task to dictionary for saving in json file
        """
        return {
            "title": self.title,
            "description": self.description,
            "priority": self.priority,
            "status": self.status
        }

    def from_dict(self, d):  
        """
        Create a Task object from a dictionary\n
        d: a dictionary having its keys the same as the Task attributes
        """
        return self(d["title"], d["description"], d["priority"], d["status"])
    
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
        self.status = "Done"

    def update_priority(self, value: int):
        """
        Assign a new value to the priority property of the task\n
        value: holds the new value of priority
        """
        self.priority = value
    