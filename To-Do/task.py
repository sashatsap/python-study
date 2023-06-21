from list import List


class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Task(List):
    def add(self, task):
        super().__init__(task)
        self.task_list.append(self.task)
        print(self.task_list)
