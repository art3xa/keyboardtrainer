import os
import sys


class GameLogic:
    def __init__(self):
        self.mistakes = 0
        self.speed = 0
        self.len_edit_text = 0

    def check_edit(self, static: str, edit: str):
        """Проверка символов"""
        brush_list = []
        self.speed += 1
        self.len_edit_text = len(edit)
        if len(static) > len(edit):
            self.mistakes = 0
            for word in range(len(edit)):
                if edit[word] == static[word]:
                    brush_list.append(('Good', word))
                else:
                    brush_list.append(('Bad', word))
                    self.mistakes += 1
            return brush_list
        return

    def check_win(self, text: str, text_edit: str, login: str):
        """Проверка победы и запись статистики"""
        file = ''
        if len(text) == len(text_edit) and text == text_edit:
            if login != '':
                file = os.path.join(sys.path[0], "Users", login + '.txt')
                return True, file
            else:
                return True, file
        return False, file

    def make_stat(self, time: int):
        """Запись динамической статистики"""
        if time != 0:
            speed = round(60 * self.speed / time)
            if self.mistakes == 0:
                mistakes = 100
            else:
                mistakes = round(
                    ((self.len_edit_text - self.mistakes)
                     / self.len_edit_text) * 100)
            return speed, mistakes
