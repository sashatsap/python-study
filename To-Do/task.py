class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name


class Task:
    def __init__(self):
        self.task_list = []

    def add(self, task):
        self.task = task
        self.task_list.append(self.task)
        print(self.task_list)

    def change(self, choice, task):
        self.choice = choice
        try:
            self.task_list[choice] = task
            print(self.task_list)
        except IndexError:
            print(f'You dont have {choice} task')
