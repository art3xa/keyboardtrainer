import os
import sys
import time

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QAction, QInputDialog, QMessageBox
from pygame import mixer

from modules.data import login, get_text


class UiMainWindow(QtWidgets.QMainWindow):
    def setup_ui(self, MainWindow):
        """Установка UI"""
        mixer.init()
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1280, 780)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum,
                                           QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.verticalLayout_ = QtWidgets.QVBoxLayout()
        self.verticalLayout_.setObjectName("verticalLayout_")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.labelSpeed = QtWidgets.QLabel(self.centralwidget)
        self.labelSpeed.setObjectName("labelSpeed")
        self.verticalLayout_7.addWidget(self.labelSpeed)
        self.labelTime = QtWidgets.QLabel(self.centralwidget)
        self.labelTime.setObjectName("labelTime")
        self.verticalLayout_7.addWidget(self.labelTime)
        self.labelMistakes = QtWidgets.QLabel(self.centralwidget)
        self.labelMistakes.setObjectName("labelMistakes")
        self.verticalLayout_7.addWidget(self.labelMistakes)
        self.labelGameStatus = QtWidgets.QLabel(self.centralwidget)
        self.labelGameStatus.setObjectName("labelGameStatus")
        self.verticalLayout_7.addWidget(self.labelGameStatus)
        self.horizontalLayout_7.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.lineSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineSpeed.setReadOnly(True)
        self.lineSpeed.setObjectName("lineSpeed")
        self.verticalLayout_6.addWidget(self.lineSpeed)
        self.lineTime = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTime.setReadOnly(True)
        self.lineTime.setObjectName("lineTime")
        self.verticalLayout_6.addWidget(self.lineTime)
        self.lineMistakes = QtWidgets.QLineEdit(self.centralwidget)
        self.lineMistakes.setReadOnly(True)
        self.lineMistakes.setObjectName("lineMistakes")
        self.verticalLayout_6.addWidget(self.lineMistakes)
        self.lineGameStatus = QtWidgets.QLineEdit(self.centralwidget)
        self.lineGameStatus.setReadOnly(True)
        self.lineGameStatus.setObjectName("lineGameStatus")
        self.verticalLayout_6.addWidget(self.lineGameStatus)
        self.horizontalLayout_7.addLayout(self.verticalLayout_6)
        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                           QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem)
        self.horizontalLayout_7.setStretch(2, 1)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.horizontalLayout_6.addLayout(self.verticalLayout_5)
        spacerItem1 = QtWidgets.QSpacerItem(
            40,
            20,
            QtWidgets.QSizePolicy.MinimumExpanding,
            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_6.addItem(spacerItem1)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout()
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.labelUser = QtWidgets.QLabel(self.centralwidget)
        self.labelUser.setObjectName("labelUser")
        self.verticalLayout_9.addWidget(self.labelUser)
        self.labelAverageSpeed = QtWidgets.QLabel(self.centralwidget)
        self.labelAverageSpeed.setObjectName("labelAverageSpeed")
        self.verticalLayout_9.addWidget(self.labelAverageSpeed)
        self.labelTextsCount = QtWidgets.QLabel(self.centralwidget)
        self.labelTextsCount.setObjectName("labelTextsCount")
        self.verticalLayout_9.addWidget(self.labelTextsCount)
        self.labelTextsComplete = QtWidgets.QLabel(self.centralwidget)
        self.labelTextsComplete.setObjectName("labelTextsComplete")
        self.verticalLayout_9.addWidget(self.labelTextsComplete)
        self.horizontalLayout_8.addLayout(self.verticalLayout_9)
        self.verticalLayout_8 = QtWidgets.QVBoxLayout()
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.lineUser = QtWidgets.QLineEdit(self.centralwidget)
        self.lineUser.setReadOnly(True)
        self.lineUser.setObjectName("lineUser")
        self.verticalLayout_8.addWidget(self.lineUser)
        self.lineAverageSpeed = QtWidgets.QLineEdit(self.centralwidget)
        self.lineAverageSpeed.setReadOnly(True)
        self.lineAverageSpeed.setObjectName("lineAverageSpeed")
        self.verticalLayout_8.addWidget(self.lineAverageSpeed)
        self.lineTextsCount = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTextsCount.setReadOnly(True)
        self.lineTextsCount.setObjectName("lineTextsCount")
        self.verticalLayout_8.addWidget(self.lineTextsCount)
        self.lineTextsComplete = QtWidgets.QLineEdit(self.centralwidget)
        self.lineTextsComplete.setReadOnly(True)
        self.lineTextsComplete.setObjectName("lineTextsComplete")
        self.verticalLayout_8.addWidget(self.lineTextsComplete)
        self.horizontalLayout_8.addLayout(self.verticalLayout_8)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20,
                                            QtWidgets.QSizePolicy.Expanding,
                                            QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.horizontalLayout_8.setStretch(2, 1)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.horizontalLayout_6.addLayout(self.verticalLayout_4)
        self.horizontalLayout_6.setStretch(0, 1)
        self.horizontalLayout_6.setStretch(2, 1)
        self.verticalLayout_.addLayout(self.horizontalLayout_6)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(
            QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout.setContentsMargins(10, -1, -1, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textStatic = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textStatic.sizePolicy().hasHeightForWidth())
        self.textStatic.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textStatic.setFont(font)
        self.textStatic.setReadOnly(True)
        self.textStatic.setPlainText("")
        self.textStatic.setObjectName("textStatic")
        self.verticalLayout.addWidget(self.textStatic)
        self.textEdit = QtWidgets.QPlainTextEdit(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,
                                           QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.textEdit.setFont(font)
        self.textEdit.setPlainText("")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.verticalLayout_.addLayout(self.verticalLayout)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        self.startButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.startButton.setFont(font)
        self.startButton.setObjectName("startButton")
        self.horizontalLayout_9.addWidget(self.startButton)
        self.stopButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.stopButton.setFont(font)
        self.stopButton.setObjectName("stopButton")
        self.horizontalLayout_9.addWidget(self.stopButton)
        self.baseTextButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.baseTextButton.setFont(font)
        self.baseTextButton.setObjectName("baseTextButton")
        self.horizontalLayout_9.addWidget(self.baseTextButton)
        self.chooseTextButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.chooseTextButton.sizePolicy().hasHeightForWidth())
        self.chooseTextButton.setSizePolicy(sizePolicy)
        self.chooseTextButton.setMinimumSize(QtCore.QSize(0, 0))
        self.chooseTextButton.setMaximumSize(QtCore.QSize(16777215, 30))
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.chooseTextButton.setFont(font)
        self.chooseTextButton.setObjectName("chooseTextButton")
        self.horizontalLayout_9.addWidget(self.chooseTextButton)
        self.musicStartButton = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum,
                                           QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(
            self.musicStartButton.sizePolicy().hasHeightForWidth())
        self.musicStartButton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.musicStartButton.setFont(font)
        self.musicStartButton.setObjectName("musicStartButton")
        self.horizontalLayout_9.addWidget(self.musicStartButton)
        self.musicStopButton = QtWidgets.QPushButton(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Times New Roman")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.musicStopButton.setFont(font)
        self.musicStopButton.setObjectName("musicStopButton")
        self.horizontalLayout_9.addWidget(self.musicStopButton)
        self.verticalLayout_10.addLayout(self.horizontalLayout_9)
        self.verticalLayout_.addLayout(self.verticalLayout_10)
        self.verticalLayout_.setStretch(1, 3)
        self.verticalLayout_3.addLayout(self.verticalLayout_)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1024, 0))
        MainWindow.setMenuBar(self.menubar)
        self.user = self.menubar.addMenu('&Аккаунт')

        self.logIn = QAction('Войти', self)
        self.logIn.setShortcut('Ctrl+I')
        self.logIn.setStatusTip('Войти в аккаунт')
        self.logIn.triggered.connect(self.log_in)
        self.user.addAction(self.logIn)

        self.logOut = QAction('Выйти', self)
        self.logOut.setShortcut('Ctrl+O')
        self.logOut.setStatusTip('Выйти из аккаунта')
        self.logOut.triggered.connect(self.log_out)
        self.user.addAction(self.logOut)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        MainWindow.setCentralWidget(self.centralwidget)
        self.startButton.clicked.connect(self.start)
        self.chooseTextButton.clicked.connect(self.choose_file)
        self.stopButton.clicked.connect(self.stop)
        self.musicStartButton.clicked.connect(self.start_music)
        self.baseTextButton.clicked.connect(self.text_database)
        self.musicStopButton.clicked.connect(self.stop_music)
        self.timer = QTimer(self)
        self.mistakes = 0
        self.speed = 0
        self.aver_speed = 0
        self.login = ''
        self.static_list = ''

    def retranslateUi(self, MainWindow):
        """Перевод всех лейблов и кнопок"""
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "KeyboardTrainer"))
        self.labelSpeed.setText(_translate("MainWindow", "Скорость"))
        self.labelTime.setText(_translate("MainWindow", "Время в секундах"))
        self.labelMistakes.setText(_translate("MainWindow", "Точность"))
        self.labelGameStatus.setText(_translate("MainWindow", "Статус"))
        self.lineSpeed.setStatusTip(
            _translate(
                "MainWindow",
                "Ваша скорость в знаках в минуту за этот пробег"))
        self.lineTime.setStatusTip(
            _translate("MainWindow", "Время забега в секундах"))
        self.lineMistakes.setStatusTip(
            _translate("MainWindow", "Точность вводимого текста"))
        self.lineGameStatus.setStatusTip(
            _translate("MainWindow", "Статус игры"))
        self.labelUser.setText(_translate("MainWindow", "Имя пользователя"))
        self.labelAverageSpeed.setText(
            _translate("MainWindow", "Средняя скорость"))
        self.labelTextsCount.setText(
            _translate("MainWindow", "Кол-во текстов"))
        self.labelTextsComplete.setText(
            _translate("MainWindow", "Текстов пройдено"))
        self.lineUser.setStatusTip(
            _translate("MainWindow", "Ваше имя пользователя"))
        self.lineAverageSpeed.setStatusTip(
            _translate("MainWindow", "Ваша общая средняя скорость"))
        self.lineTextsCount.setStatusTip(
            _translate("MainWindow", "Количество доступных текстов"))
        self.lineTextsComplete.setStatusTip(
            _translate("MainWindow", "Количество пройденных вами текстов"))
        self.textStatic.setStatusTip(
            _translate("MainWindow", "Текст, с которым вы сверяетесь"))
        self.textEdit.setStatusTip(
            _translate("MainWindow", "Поле, где вы печатаете текст"))
        self.startButton.setStatusTip(
            _translate("MainWindow", "Нажмите, чтобы начать"))
        self.startButton.setText(_translate("MainWindow", "Старт"))
        self.stopButton.setStatusTip(
            _translate("MainWindow", "Остановить игру"))
        self.stopButton.setText(_translate("MainWindow", "Стоп"))
        self.baseTextButton.setStatusTip(
            _translate("MainWindow", "База встроенных текстов"))
        self.baseTextButton.setText(_translate("MainWindow", "База текстов"))
        self.chooseTextButton.setStatusTip(
            _translate("MainWindow", "Выберите свой текст из папки texts"))
        self.chooseTextButton.setText(
            _translate("MainWindow", "Выбрать свой текст"))
        self.musicStartButton.setStatusTip(
            _translate(
                "MainWindow",
                "Выберите и включите музыку из папки music"))
        self.musicStartButton.setText(
            _translate("MainWindow", "Включить музыку"))
        self.musicStopButton.setStatusTip(
            _translate("MainWindow", "Выключить музыку"))
        self.musicStopButton.setText(
            _translate("MainWindow", "Выключить музыку"))

    def log_in(self):
        """Войти в аккаунт"""
        if self.lineUser.text() == '':
            if self.lineGameStatus.text() == "Начато!":
                QMessageBox.critical(self, "Ошибка входа",
                                     "Нельзя входить во время игры",
                                     QMessageBox.Ok)
                return
            nickname, authorized = QInputDialog.getText(
                self, 'Вход', 'Введите ваше имя пользователя:')
            self.login = login(nickname)
            if self.login[0]:
                self.lineUser.setText(nickname)
                self.lineTextsComplete.setText(self.login[1])
                self.lineAverageSpeed.setText(self.login[2])
            if authorized and not self.login[0]:
                QMessageBox.critical(self, "Невалидное имя",
                                     "Введено невалидное имя",
                                     QMessageBox.Ok)
        else:
            QMessageBox.critical(self, "Ошибка входа",
                                 "Вы уже вошли", QMessageBox.Ok)

    def log_out(self):
        """Выйти из аккаунта"""
        if self.lineUser.text() != '':
            if self.lineGameStatus.text() == "Начато!":
                QMessageBox.critical(self, "Ошибка входа",
                                     "Нельзя выходить во время игры",
                                     QMessageBox.Ok)
                return
            self.lineUser.setText('')
            self.lineAverageSpeed.setText('')
            self.lineTextsComplete.setText('')
        else:
            QMessageBox.critical(self, "Ошибка выхода",
                                 "Вы не вошли в аккаунт",
                                 QMessageBox.Ok)

    def passed(self):
        """Уведомление о пройденной игре"""
        self.reset_stats()
        self.textStatic.setPlainText('')
        self.textEdit.setPlainText('')
        self.timer.stop()
        self.lineGameStatus.setText('Завершено')
        QMessageBox.information(self, "Пройдено", "Поздравляю!",
                                QMessageBox.Ok)

    def choose_file(self):
        """Выбрать текст"""
        self.stop()
        if os.path.exists('texts'):
            path = os.path.join(sys.path[0], 'texts')
            texts = \
                QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите текст',
                                                      path, '(*.txt)')[0]
            if texts == '' or '.txt' not in texts:
                return QMessageBox.critical(self, "Ошибка файла",
                                            "Принимаются только .txt файлы",
                                            QMessageBox.Ok)
            with open(texts, encoding='utf-8', errors='ignore') as file:
                text = file.encode('utf-8').decode('utf-8').read()
                if text == '':
                    return
            self.textStatic.setPlainText(text)
        else:
            return QMessageBox.critical(self, "Ошибка",
                                        "Не найдена папка texts",
                                        QMessageBox.Ok)

    def start(self):
        """Начало игры"""
        status = self.lineGameStatus.text()
        if self.textStatic.toPlainText() != "":
            if status != "Начато!":
                self.lineGameStatus.setText("Начато!")
                self.textEdit.setPlainText('')
                self.timer.start(1000)
                self.start_time = time.time()
                self.reset_stats()
            else:
                return
        else:
            self.textEdit.setPlainText("Выберите текст")

    def stop(self):
        """Остановить игру"""
        self.reset_stats()
        self.textEdit.setPlainText("Выберите текст")
        self.textStatic.setPlainText("")
        self.timer.stop()
        self.lineGameStatus.setText("Прервано")

    def text_database(self):
        """База текстов"""
        text, ok = QInputDialog.getItem(self, 'База текстов',
                                        'Выберите текст:',
                                        ('Test', 'Python',
                                         'Факты о программистах'),
                                        0, False)
        if ok and text == 'Test':
            self.text_set("Test")
        if ok and text == 'Python':
            self.text_set("Python")
        if ok and text == 'Факты о программистах':
            self.text_set("Факты о программистах")

    def text_set(self, text_name: str):
        """Выбрать свой текст из папки texts"""
        self.stop()
        text = get_text(text_name)
        if text[0]:
            self.textStatic.setPlainText(text[1])
        else:
            print("Файл перемещен или не существует")
            return QMessageBox.critical(self, "Ошибка файла",
                                        "Файл перемещен или не существует",
                                        QMessageBox.Ok)

    def start_music(self):
        """Выбрать музыку и включить"""
        mixer.music.stop()
        check_folder = os.path.exists('music')
        if check_folder:
            path = os.path.join(sys.path[0], 'music')
            musics = \
                QtWidgets.QFileDialog.getOpenFileName(self, 'Выберите музыку',
                                                      path, '(*.mp3)')[0]
            if musics == '':
                return
            if '.mp3' not in musics:
                return
            mixer.music.load(musics)
            mixer.music.play(-1)
        else:
            return QMessageBox.critical(self, "Ошибка файла",
                                        "Не найдена папка music",
                                        QMessageBox.Ok)

    def stop_music(self):
        """Остановить музыку"""
        if mixer.music.get_busy():
            mixer.music.stop()
            return
        else:
            return QMessageBox.critical(self, "Ошибка музыки",
                                        "Музыка не запущена",
                                        QMessageBox.Ok)

    def reset_stats(self):
        """Сбросить статистику"""
        self.brush_symbols([])
        self.static_list = ''
        self.lineTime.setText('0')
        self.lineSpeed.setText('0')
        self.lineMistakes.setText('0')
        self.mistakes = 0
        self.aver_speed = 0

    def brush_symbols(self, brush_list: list):
        """Закрасить символы"""
        cursor = self.textStatic.textCursor()
        char_format = QtGui.QTextCharFormat()
        for char_text in range(0, len(brush_list)):
            if brush_list[char_text][0] == 'Good':
                if char_text < len(self.static_list):
                    if brush_list[char_text] == self.static_list[char_text]:
                        continue
                cursor.setPosition(brush_list[char_text][1])
                cursor.movePosition(cursor.Right, 100)
                char_format.setBackground(QtGui.QBrush(QColor(0, 255, 0)))
                cursor.mergeCharFormat(char_format)
            elif brush_list[char_text][0] == 'Bad':
                if char_text < len(self.static_list):
                    if brush_list[char_text] == self.static_list[char_text]:
                        continue
                cursor.setPosition(brush_list[char_text][1])
                cursor.movePosition(cursor.Right, 100)
                char_format.setBackground(QtGui.QBrush(QColor(255, 0, 0)))
                cursor.mergeCharFormat(char_format)
        if len(brush_list) < len(self.static_list):
            for white in range(0, len(self.static_list)):
                if white >= len(brush_list):
                    cursor.setPosition(self.static_list[white][1])
                    cursor.movePosition(cursor.Right, 100)
                    brush = QtGui.QBrush(QColor(255, 255, 255))
                    char_format.setBackground(brush)
                    cursor.mergeCharFormat(char_format)
        self.static_list = brush_list
        return

    def get_hint(self):
        QMessageBox.information(
            self, "Приветствие", 'Приветствую! Это "Клавиатурный тренажёр"\n'
                                 'Сверху слева ты можешь нажать на "Аккаунт"'
                                 ' и войти в него для сохранения твоей статистики.\n'
                                 'А также все остальные подсказки пишутся снизу '
                                 'при наведении курсором на нужное поле. \n'
                                 'Для продолжения нажми "OK" и удачной тебе тренировки!',
            QMessageBox.Ok)
