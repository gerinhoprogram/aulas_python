import sys

from buttons import Button, ButtonsGrid
from buttons import ButtonsGrid
from display import Display
from info import Info
from main_window import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from variaveis import WINDOW_ICON_PATH
from qt_material import apply_stylesheet


if __name__ == '__main__':
    app = QApplication(sys.argv)

    extra = {

        # Button colors
        'danger': '#dc3545',
        'warning': '#ffc107',
        'success': '#17a2b8',

        # Font
        'font_family': 'Roboto',
    }

    apply_stylesheet(app, theme='dark_teal.xml', invert_secondary=True, extra=extra)

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
    buttonsGrid = ButtonsGrid(display)
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


