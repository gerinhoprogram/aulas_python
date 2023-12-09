import sys

from display import Display
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variaveis import WINDOW_ICON_PATH


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    # label1 = QLabel('Ola mundo')
    # label1.setStyleSheet('font-size: 50px')
    # window.addWidgetToVLayout(label1)
    
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    display = Display()
    window.addWidgetToVLayout(display)
    
    window.show()

    app.exec()


