
"""Класс добавления тески в БД(пока json-файл)"""
from sqlalchemy import  String
from sqlalchemy import Mapped, mapped_column
from .database import Base
class Task:
   id  =0

   def __init__(self, task:str, status:bool=False):
        Task.id +=1
        self.curent_id =Task.id


        self.task = task
        self.status = status


class User(Base):
    __table__="users"
    id:Mapped[int] =mapped_column(
        primary_key=True
    )
    username:Mapped[str]= mapped_column(
        String(64),
        unique=True,
        nullable=True

    )
    email =Mapped[str]=mapped_column(
        String(64),
        unique= True,
        nullable= False
    )
    password = Mapped[str] =mapped_column(
        String(64),
        nullable =False
    )
