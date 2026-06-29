class Task:
    """A class for saving task data"""

    def __init__(self, task_id, title, done=False):
        """Initialize the attributes"""
        self.task_id = task_id
        self.title = title
        self.done = done

    def mark_done(self):
        """Mark the task as done"""
        self.done = True

    def __str__(self):
        """String representation of the task"""
        mark = '✓' if self.done else '✗'
        return  f'{self.task_id}: {self.title} [{mark}]'

    def to_dict(self):
        """Convert the task to a dictionary"""
        return {'task_id': self.task_id, 'title': self.title, 'done': self.done}

    @classmethod
    def from_dict(cls, data):
        """Taking data from the dictionary"""
        return cls(data['task_id'], data['title'], data['done'])