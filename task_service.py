import json

def add_task(record):

    readed_list =read_task_from_json()
    if readed_list:
        record.id =max((task['id'] for task in readed_list), default=0)+1

    task = {
        'id': record.id,
        'task': record.task,
        'status':record.status
    }
    readed_list.append(task)


    save_task_in_json(readed_list)

    return

def show_task():
    tasks = read_task_from_json()
    for i, x in  enumerate(tasks):
        if x['status']==False:
               print(f'Задача №{i+1} : {x['task']}---Статус: Не выполнена')
        else:
            print(f'Задача №{i + 1} : {x['task']}---Статус: Выполнена')





def task_complete(n:int):
    readed_list = read_task_from_json()
    ind = n-1
    if ind<0 or ind>=len(readed_list):
        print('Такой задачи не существует')
    readed_list[ind]['status']=True
    save_task_in_json(readed_list)

def save_task_in_json(tasks:list):
    with open('do_list.json','w', encoding='utf-8') as file:
        json.dump(tasks, file, indent=4, ensure_ascii=False)


def read_task_from_json():

    try:
       with open('do_list.json', 'r', encoding='utf-8') as file:
           do_list  = json.load(file)

    except FileNotFoundError:
        return []
    except json.JSONDecodeError:
        print('Файл пустой, или поврежден')
        return []

    return do_list

def clear_from_json(n:int):

    ind =n-1
    tasks = read_task_from_json()
    if ind < 0 or ind >= len(tasks):
        print('Задачи не существует')
        return


    tasks.remove(tasks[ind])

    save_task_in_json(tasks)
    print('Ненужная запись удалена')








