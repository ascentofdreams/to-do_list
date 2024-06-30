import sys
from os import getcwd


def add_task():
    print("Чтобы добавить задачу, пожалуйста введите название. (m) - возврат к меню")
    task_name = input()
    if task_name.lower() in {'m', 'q'}:
        action_menu(task_name.lower())
    else:
        with open(f'{getcwd()}/tasks.txt', mode='a', encoding='utf-8') as f:
            f.write(f"{task_name};0\n")
        f.close()
        print('Задача успешно добавлена!')
        action_menu(input())


def view_tasks():
    status = {'0': 'Невыполненная', '1': 'Выполненная'}
    with open(f'{getcwd()}/tasks.txt', encoding='utf-8') as f:
        tasks_list = f.readlines()
        if tasks_list:
            tasks_list = list(map(lambda x: (x[:-3], status[x[-2:-1]]), tasks_list))
            for task in enumerate(tasks_list):
                print(f'Задача №{task[0] + 1}, Название: {task[1][0]}, Статус: {task[1][1]}')
        else:
            print('На текущий момент задач нет.')
    f.close()
    action_menu(input())


def del_task():
    with open(f'{getcwd()}/tasks.txt', encoding='utf-8') as f:
        tasks_list = f.readlines()
    f.close()
    if tasks_list:
        print('Какую задачу вы хотите удалить?')
        task_num = input(f'Номер: ')
        if task_num.lower() in {'m', 'q'}:
            action_menu(task_num.lower())
        elif task_num.isalnum():
            try:
                task_num = int(task_num)
            except:
                print('Вы не ввели номер задачи, хотите вернуться в меню?')
                back_menu('3')
            if 0 < task_num <= len(tasks_list):
                del tasks_list[task_num - 1]
                with open(f'{getcwd()}/tasks.txt', mode='w', encoding='utf-8') as f:
                    for task in tasks_list:
                        f.write(task)
                f.close()
                print('Готово, задача удалена!')
                action_menu(input())
            else:
                print("Ошибка! Номер задачи должен быть натуральным числом \n"
                      "и не должен превышать максимальное количество задач.")
                action_menu('m')
    else:
        print('На данный момент задач нет.')
        action_menu(input())


def status_task():
    with open(f'{getcwd()}/tasks.txt', encoding='utf-8') as f:
        tasks_list = f.readlines()
    f.close()
    if tasks_list:
        print('Напишите номер задачи которую нужно отметить. (m) - возврат к меню')
        task_num = input(f'Номер: ')
        if task_num.lower() in {'m', 'q'}:
            action_menu(task_num.lower())
        elif task_num.isalnum():
            try:
                task_num = int(task_num)
            except:
                print('Вы не ввели номер задачи, хотите вернуться в меню?')
                back_menu('4')
            if 0 < task_num <= len(tasks_list):
                if tasks_list[task_num - 1][-2] == '0':
                    tasks_list[task_num - 1] = tasks_list[task_num - 1][:-2] + '1\n'
                    with open(f'{getcwd()}/tasks.txt', mode='w', encoding='utf-8') as f:
                        for task in tasks_list:
                            f.write(task)
                    f.close()
                    print('Готово, задача отмечена выполненной!')
                    print(f"Задача №{task_num}, Название: {tasks_list[task_num - 1][:-3]}, Статус: Выполненная")
                    action_menu(input())
                else:
                    print('Кажется эта задача уже является выполненной, хотите вернуться в меню?')
                    back_menu('4')
            else:
                print("Ошибка! Номер задачи должен быть натуральным числом \n"
                      "и не должен превышать максимальное количество задач.")
                action_menu('m')
    else:
        print('На данный момент нельзя проверить статус задач, поскольку их нет.')
        action_menu(input())


def help_menu():
    print("(1...4) - Переход к одному из действий меню")
    print("(M/m) - Переход в меню действий")
    print("(Q/q) - Выйти")
    action_menu(input())


def action_menu(action):
    action_list = {'1': add_task, '2': view_tasks, '3': del_task, '4': status_task, 'm': menu, 'h': help_menu}
    if action.lower() == 'q':
        sys.exit()
    elif action.lower() in {'1', '2', '3', '4', 'm'}:
        print("------------------------")
        action_list[action.lower()]()
    elif action.lower() in {'h', 'help'}:
        print("------------------------")
        action_list['h']()
    else:
        print('Вы не ввели номер действия, перенаправляю вас обратно в меню.')
        menu()


def menu():
    print("Вот основное меню:", sep='\n')
    print("(1) Добавить задачу")
    print("(2) Просмотреть задачи")
    print("(3) Удалить задачу")
    print("(4) Отметить задачу как выполненную")
    print("(q) Выйти")
    print("Если вдруг что-то не понятно, (help/h) - выведет справку доступных команд")
    action_menu(input())


def back_menu(num_action):
    action = input('(y/n)')
    while action not in {'y', 'n'}:
        print("Введите 'y' или 'n'.")
        action = input('(y/n)')
    if action == 'y':
        action_menu('m')
    elif action == 'n':
        action_menu(num_action)


if __name__ == "__main__":
    print("Привет! Чтобы продолжить, пожалуйста ознакомься с меню действий.")
    menu()
