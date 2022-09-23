from modules import validator
import os
import sys


def login(name: str) -> tuple:
    """Вход в аккаунт"""
    without_tabs = ''.join(name.split())
    reg = validator.validate(name)
    speed = ''
    complete = ''
    max_len = 255 - len(os.path.join(sys.path[0], "Users"))
    if not reg and without_tabs != '' and len(name) < max_len:
        path = os.path.join(sys.path[0], "Users", name + ".txt")
        if os.path.isfile(path):
            print('Логин успешен')
        else:
            with open(path, 'w') as created_file:
                created_file.write('0' + '\n' + '0')
            print('Логин создан')
        with open(path, 'r') as state:
            lines = state.readlines()
            complete = lines[0]
            speed = lines[1]
        return not reg, complete, speed
    else:
        return not reg, complete, speed


def get_text(name: str) -> tuple:
    """Установка текста"""
    check_folder = os.path.exists('texts')
    check_file = os.path.isfile(os.path.join('texts', name + '.txt'))
    text = ''
    if check_file and check_folder:
        path = os.path.join(sys.path[0], 'texts', name + '.txt')
        with open(path, 'r', encoding='utf-8', errors='ignore') as file:
            text = file.encode('utf-8').decode('utf-8').read()
        return True, text
    else:
        return False, text
