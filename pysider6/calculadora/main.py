import sys

from display import Display
from main_window import MainWindow
from info import Info
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication, QLabel
from variaveis import WINDOW_ICON_PATH
from qt_material import apply_stylesheet
from buttons import Button
from buttons import ButtonsGrid


if __name__ == '__main__':
    app = QApplication(sys.argv)

    apply_stylesheet(app, theme='dark_teal.xml')

    window = MainWindow()

    info = Info('2.0 ^ 10.0 = 1024')
    window.addWidgetToVLayout(info)

    # label1 = QLabel('Ola mundo')
    # label1.setStyleSheet('font-size: 50px')
    # window.addWidgetToVLayout(label1)
    
    #icone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #display
    display = Display()
    window.addWidgetToVLayout(display)

    #grid
    buttonsGrid = ButtonsGrid()
    window.v_layout.addLayout(buttonsGrid)

    #button
    # button = Button('Texto')
    # buttonsGrid.addWidget(button, 0, 0)

    # button2 = Button('Texto2')
    # buttonsGrid.addWidget(button2, 0, 1)

    # buttonsGrid.addWidget(Button('0'), 0, 0)
    # buttonsGrid.addWidget(Button('1'), 0, 1)
    # buttonsGrid.addWidget(Button('2'), 0, 2)
    
    window.show()

    app.exec()


