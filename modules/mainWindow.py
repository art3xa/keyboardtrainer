import os.path
import sys
import time
from argparse import Namespace
from PyQt5 import QtCore, QtWidgets
from modules.logic import GameLogic
from modules import UI
from modules.data import login


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = UI.UiMainWindow()
        self.ui.setup_ui(self)
        self.logic = GameLogic()
        self.aver_speed = 0
        self.logic.speed = 0
        self.logic.mistakes = 0
        self.path = os.path.join(sys.path[0], "texts")
        self.ui.lineTextsCount.setText(str(len(os.listdir(self.path))))
        self.ui.timer.timeout.connect(self.make_statistic)
        self.ui.startButton.clicked.connect(self.drop_stats)
        self.ui.stopButton.clicked.connect(self.drop_stats)
        self.ui.baseTextButton.clicked.connect(self.drop_stats)
        self.ui.chooseTextButton.clicked.connect(self.drop_stats)

    def set_args(self, data: Namespace):
        """Установить параметры"""
        if data.login is not None:
            self.ui.lineUser.setText(data.login)
            information = login(data.login)
            self.ui.lineTextsComplete.setText(information[1])
            self.ui.lineAverageSpeed.setText(information[2])
        if data.name_of_text is not None:
            self.ui.text_set(data.name_of_text)
        return

    def make_total_statistic(self, file: str):
        """Записать общую статистику"""
        with open(file, 'r') as state:
            lines = state.readlines()
            speed = (self.aver_speed + int(lines[1])) / 2
            lines[0] = str(int(lines[0]) + 1)
            lines[1] = '\n' + str(round(speed))
            self.ui.lineAverageSpeed.setText(str(round(speed)))
            self.ui.lineTextsComplete.setText(lines[0])
        with open(file, 'w') as state:
            for line in lines:
                state.write(line)

    def drop_stats(self):
        """Сбросить статистику"""
        if self.ui.lineGameStatus.text() != "Начато!":
            self.logic.speed = 0
            self.aver_speed = 0
            self.logic.speed = 0
            self.logic.mistakes = 0
        return

    def event(self, event):
        """Обработка событий"""
        if event.type() == QtCore.QEvent.PolishRequest:
            self.ui.get_hint()
        if event.type() == QtCore.QEvent.KeyRelease:
            self.ui.lineTextsCount.setText(str(len(os.listdir(self.path))))
            if self.ui.lineGameStatus.text() == "Начато!" and \
                    self.ui.textStatic.toPlainText() != '':
                win = self.logic.check_win(self.ui.textStatic.toPlainText(),
                                           self.ui.textEdit.toPlainText(),
                                           self.ui.lineUser.text())
                if win[0]:
                    if win[1] != '':
                        self.make_total_statistic(win[1])
                    self.ui.passed()
                self.make_statistic()
                self.checker()
                return True
            else:
                self.ui.textEdit.setPlainText("Выберите текст")
        return QtWidgets.QMainWindow.event(self, event)

    def make_statistic(self):
        """Синхронизация статистики"""
        game_time = round(time.time() - self.ui.start_time)
        if game_time > 0:
            self.ui.lineTime.setText(str(game_time))
            stat = self.logic.make_stat(game_time)
            self.aver_speed = stat[1]
            self.ui.lineSpeed.setText(str(stat[0]) + " зн./мин")
            self.ui.lineMistakes.setText(str(stat[1]) + "%")

    def checker(self):
        """Проверить и закрасить символы"""
        points = self.logic.check_edit(self.ui.textStatic.toPlainText(),
                                       self.ui.textEdit.toPlainText())
        if points is None:
            return
        self.ui.brush_symbols(points)
