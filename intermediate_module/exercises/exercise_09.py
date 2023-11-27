# Exercise - Task list with undo and redo
# Music to code =)
# Everybody wants to rule the world - Tears for fears
# todo = [] -> task list
# todo = ['make coffee'] -> Add make coffee
# todo = ['make coffee', 'walk'] -> Add walk
# undo = ['make coffee',] -> Redo ['walk']
# undo = [] -> Redo ['walk', 'make coffee']
#redo = todo ['make coffee']
#redo = todo ['make coffee', 'walk']
import os


def list(tasks):
    print()
    if not tasks:
        print('No tasks to list')
        return

    print('Tasks:')
    for task in tasks:
        print(f'\t{task}')
    print()


def undo(tasks, tasks_redo):
    print()
    if not tasks:
        print('No tasks to undo')
        return

    task = tasks.pop()
    print(f'{task=} removed from task list.')
    tasks_redo.append(task)
    print()


def redo(tasks, tasks_redo):
    print()
    if not tasks_redo:
        print('No tasks to redo')
        return

    task = task.pop()
    print(f'{task=} added to task list.')
    tasks.append(task)
    print()


def add(task, tasks):
    print()
    task = task.strip()
    if not task:
        print('You did not enter a task.')
        return
    print(f'{task=} added to task list.')
    tasks.append(task)
    print()


tasks = []
tasks_redo = []

while True:
    print('Commands: list, undo and redo')
    task = input('Enter a task or command: ')
    
    commands = {
        'list': lambda: list(tasks),
        'undo': lambda: undo(tasks, tasks_redo),
        'redo': lambda: redo(tasks, tasks_redo),
        'clear': lambda: os.system('clear'),
        'add': lambda: add(task, tasks),
    }
    command = commands.get(task) if commands.get(task) is not None else \
        commands['add']
    command()

    # if task == 'list':
    #     list(tasks)
    #     continue
    # elif task == 'undo':
    #     undo(tasks, tasks_redo)
    #     list(tasks)
    #     continue
    # elif task == 'redo':
    #     redo(tasks, tasks_redo)
    #     list(tasks)
    #     continue
    # elif task == 'clear':
    #     os.system('clear')
    #     continue
    # else:
    #     add(task, tasks)
    #     list(tasks)
    #     continue