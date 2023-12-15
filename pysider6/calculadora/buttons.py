from typing import Optional
from PySide6.QtWidgets import QPushButton, QGridLayout, QWidget
from variaveis import MEDIUM_FONT_SIZE

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size:, {MEDIUM_FONT_SIZE}px;')
        
        # configura font
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setItalic(True)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid__mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self._makeGrid()

    def _makeGrid(self):
        for linha_numero, row in enumerate(self._grid__mask):
            for coluna_numero, texto_botao in enumerate(row):
                # print(row)
                button = Button(texto_botao)

                # if texto_botao not in '0123456789.':
                #     button.set

                self.addWidget(button, linha_numero, coluna_numero)