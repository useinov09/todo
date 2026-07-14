priority_order = {'high': 3, 'medium': 2, 'low': 1}

class Task:
    """A class for saving task data"""

    def __init__(self, task_id, title, priority='medium', done=False):
        """Initialize the attributes"""
        self.task_id = task_id
        self.title = title
        self.done = done
        self.priority = priority

    def mark_done(self):
        """Mark the task as done"""
        self.done = True

    def __str__(self):
        """String representation of the task"""
        mark = '✓' if self.done else '✗'
        if self.priority == 'high':
            priority_str = '🔴'
        elif self.priority == 'medium':
            priority_str = '🟡'
        elif self.priority == 'low':
            priority_str = '🟢'
        return  f'{self.task_id}: {self.title} [{mark}] - {priority_str}'

    def to_dict(self):
        """Convert the task to a dictionary"""
        return {'task_id': self.task_id, 'title': self.title, 'priority': self.priority, 'done': self.done}

    @classmethod
    def from_dict(cls, data):
        """Taking data from the dictionary"""
        return cls(data['task_id'], data['title'], data['priority'], data['done'])