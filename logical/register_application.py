from logical.main import main
from logical.auth import register, authenticate_user



while True:
    print('Выберете что хотите сделать:\n1.Зарегистрироваться\n2.Войти в систему')
    n= input()
    if n=='1':
        print('Введите имя пользователя почту и пароль')
        nm =input('Имя пользователя: ')
        eml =input('Пароль: ')
        pssw =input('Пароль: ')
        if authenticate_user(nm,pssw)==None :
            register(nm,eml,pssw)
    if n=='2':
        print('Введите почту и пароль')
        nm = input('Имя пользователя: ')
        pssw = input('Пароль: ')
        if authenticate_user(nm,pssw):
            main()
        else:
            print('Пользователь не найден')