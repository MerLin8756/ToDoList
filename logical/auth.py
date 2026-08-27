"""Файл по авторизации пользователя в нашем приложении (пока что консольном)"""
from logical.hash_password import hash_password

from database import SessionLocal
from models import User
from sqlalchemy import select

def register(
        username:str,
        email:str,
        password:str
):
    pasword_hash =hash_password(password)
    with SessionLocal()  as session:
        user =User(
            username =username,
            email= email,
            password =pasword_hash
        )
        session.add(user)
        session.commit()
        return user

def get_user_by_username(username:str):
    with SessionLocal as session:
        statement  = select(User).where(User.username==username)

    user  = session.scalar(statement)
    if not user:
        return None


def authenticate_user(username:str,
                      password:str
 ):
    password_hash  = hash_password(password)
    with SessionLocal() as session:
        statement =select(User).where(User.username==username)
        user =session.scalar(statement)
        if not user:
            return None

        if password_hash!=user.password:
            return None
        return user
