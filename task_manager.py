from task import Task
from storage import Storage

class TaskManager:
    """A class to manage tasks"""

    def __init__(self, filename):
        """Initialize the attributes"""
        self.storage = Storage(filename)
        self.tasks = self.storage.load()

    def add_task(self, title, done=False):
        """Add a task to the tasks list"""
        task_id = self._get_next_id()
        new_task = Task(task_id, title, done)
        self.tasks.append(new_task)
        self.storage.save(self.tasks)
        return new_task

    def _get_next_id(self):
        """Return the next id for the task"""
        if not self.tasks:
            return 1
        return max(task.task_id for task in self.tasks) + 1

    def find_task(self, task_id):
        """Looking for a task"""
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        return None

    def mark_done(self, task_id):
        """Mark a task as done"""
        task = self.find_task(task_id)

        if task is None:
            return False

        task.mark_done()
        self.storage.save(self.tasks)
        return True

    def remove_task(self, task_id):
        """Remove a task"""
        task = self.find_task(task_id)

        if task is None:
            return False

        self.tasks.remove(task)
        self.storage.save(self.tasks)
        return True

    def remove_all_tasks(self):
        """Remove all tasks"""
        if not self.tasks:
            return False

        self.tasks.clear()
        self.storage.save(self.tasks)
        return True

    def rename_task(self, old_task_id, new_title):
        """Rename a task"""
        task = self.find_task(old_task_id)

        if task is None:
            return False

        task.title = new_title
        self.storage.save(self.tasks)
        return True

    def get_tasks(self, filter_by=None):
        """Return tasks, optionally filtered by status"""
        if filter_by == 'done':
            return [task for task in self.tasks if task.done]

        if filter_by == 'undone':
            return [task for task in self.tasks if not task.done]

        return self.tasks