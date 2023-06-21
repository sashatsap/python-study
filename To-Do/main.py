from task import Task

task_one = Task('do homework')
task_two = Task('go for walk', note='with Vlad')

task_one.add_note('chem')

task_two.done()

print(task_one)
print(task_two)
