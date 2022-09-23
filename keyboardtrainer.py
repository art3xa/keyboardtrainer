from PyQt5 import QtWidgets
import sys
from modules.mainWindow import MainWindow
from PyQt5 import QtGui
from PyQt5.QtWinExtras import QWinTaskbarButton, QWinTaskbarProgress


def main():
    app = QtWidgets.QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon('icon.ico'))
    window = MainWindow()
    window.setWindowIcon(QtGui.QIcon('icon.ico'))
    window.show()
    window.taskbar_button = QWinTaskbarButton()
    window.taskbar_button.setWindow(window.windowHandle())
    window.taskbar_button.setOverlayIcon(QtGui.QIcon('icon.ico'))
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
