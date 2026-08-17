"""Файл для хэширования пароля будем подтаскивать данные из сайта, драть пароль если пользователь новый и
хэщировать добавляя его в базу"""
import hashlib


def hash_password(psswd:str )->str:
    crypt =hashlib.sha256()
    b =bytes(psswd,'utf-8')
    crypt.update(b)
    return crypt.hexdigest()
print(hash_password(''))


