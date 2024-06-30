import sys
from os import getcwd


def add_task():
    print("------------------------")
    print("Чтобы добавить задачу, пожалуйста введите название.")
    task_name = input()
    with open(f'{getcwd()}/tasks.txt', mode='a', encoding='utf-8') as f:
        f.write(f"1;{task_name};0\n")


def view_tasks():
    status = {'0': 'Невыполненная', '1': 'Выполненная'}
    print("------------------------")
    with open(f'{getcwd()}/tasks.txt', encoding='utf-8') as f:
        tasks_list = f.readlines()
        tasks_list = list(map(lambda x: (x[0:x.rfind(';')], status[x[x.rfind(';') + 1:-1]]), tasks_list))
        for task in enumerate(tasks_list):
            print(f'Задание №{task[0]+1}, Название: {task[1][0]}, Статус: {task[1][1]}')


def del_task():
    print("------------------------")


def status_task():
    print("------------------------")


def menu():
    action_list = {'1': add_task, '2': view_tasks, '3': del_task, '4': status_task}
    print("------------------------")
    print("Вот основное меню:", sep='\n')
    print("(1) Добавить задачу")
    print("(2) Просмотреть задачи")
    print("(3) Удалить задачу")
    print("(4) Отметить задачу как выполненную")
    print("(q) Выйти", end='')
    action = input()
    if action == 'q':
        sys.exit()
    elif action in {'1', '2', '3', '4'}:
        action_list[action]()


if __name__ == "__main__":
    print("Привет! Чтобы продолжить, пожалуйста ознакомься с меню действий.")
    menu()
