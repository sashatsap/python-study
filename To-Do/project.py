from task import Task

class Project:
    def __init__(self, name: str):
        self.name = name
        self.tasks = []

    def add_task(self, task: Task):
        self.tasks.append(task)

    def delete_task(self, task: Task):
        self.tasks.remove(task)

    def count(self):
        return len(self.tasks)

    def __str__(self):
        result = f'Project {self.name}:\n'

        for task in self.tasks:
            result += str(task)

        return result
