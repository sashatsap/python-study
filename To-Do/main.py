from task import Task

user = Task()

user.add(task=input('Enter To-Do: '))
user.add(task=input('Enter To-Do: '))
user.change(choice=int(input()), task=input('Enter new To-Do: '))