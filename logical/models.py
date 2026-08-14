
"""Класс добавления тески в БД(пока json-файл)"""

class Task:
   id  =0

   def __init__(self, task:str, status:bool=False):
        Task.id +=1
        self.curent_id =Task.id


        self.task = task
        self.status = status





def record_serializer(obj):
    if isinstance(obj,Task):
        return {'id':obj.id, 'task':obj.task, 'status':obj.status}

    raise TypeError(f"Object of type {type(obj).__name__} is not JSON serializable")

