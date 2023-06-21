from task import Task
from project import Project

task_one = Task('do homework')
task_two = Task('go for walk', note='with Vlad')

task_one.add_note('chem')

task_two.done()

school_project = Project('School')


school_project.add_task(task_one)
school_project.add_task(task_two)

print(f'All tasks: {school_project.count()}')
print(school_project)

school_project.delete_task(task_one)

print(school_project)