import json

from task import Task

class Storage:
    """A class for uploading tasks"""

    def __init__(self, filename):
        """Initialize the attributes"""
        self.filename = filename

    def load(self):
        """Load tasks"""
        try:
            with open(self.filename, "r") as f:
                row_data = json.load(f)
            return [Task.from_dict(line) for line in row_data]
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def save(self, tasks):
        """Save a task"""
        data = [task.to_dict() for task in tasks]
        with open(self.filename, "w") as f:
            json.dump(data, f, indent=4)