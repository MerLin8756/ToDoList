"""Логика консольного проложения """
from task_service import add_task,show_task,clear_from_json,task_complete, read_task_from_json
from models import Task


while True:

    print('1.Добавить Задачу\n2.Удалить задачу\n3.Показать задачи\n4.Пометить задачу как выполненную\n5.Выйти')
    choice = input('Выберите то что хотите сделать: ')
    if choice not in ('1','2','3','4','5'):
        print('Неверный формат ввода')
        continue

    if choice=='1':
        record = Task(input('Введите задачу'))
        add_task(record)
        print()
    elif choice=='2':
        try:
           number = int(input('Введите номер задачи которую хотите удалить: '))
        except ValueError:
            print('Нужно ввести целое число')
            continue
        if 1<=number<=len(read_task_from_json()):
            clear_from_json(number)
        else:
            print('Такой задачи не существует')

    elif choice=='3':
        print('Ваши задачи:')
        show_task()
    elif choice=='4':
        try:
           complete_number = int(input('Какая задача уже выполнена?'))
           task_complete(complete_number)
        except ValueError:
            print('Введите целое число')

    elif choice =='5':
        break


print('Привет GitHub')