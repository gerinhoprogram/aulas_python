from display import Display
from PySide6.QtCore import Slot
from PySide6.QtWidgets import QPushButton, QGridLayout
from variaveis import MEDIUM_FONT_SIZE
from utils import numero_ou_ponto, vazio

class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        # self.setStyleSheet(f'font-size:, {MEDIUM_FONT_SIZE}px;')
        
        # configura font
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        font.setBold(True)
        self.setFont(font)
        self.setMinimumSize(75, 75)

class ButtonsGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self._grid__mask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = Display
        self._makeGrid()

    # gera a grid calculadora
    def _makeGrid(self):

        # print em linhas
        for linha_numero, row in enumerate(self._grid__mask):

            # print colunas
            for coluna_numero, texto_botao in enumerate(row):
                
                # texto do botao
                button = Button(texto_botao)

                # não é numero nem ponto e vazio
                if not numero_ou_ponto(texto_botao) and vazio:
                    button.setProperty('class', 'danger')

                # if texto_botao not in '0123456789.':
                #     button.font.setBold(True)

                self.addWidget(button, linha_numero, coluna_numero)
                
                # verificada botao clicado
                buttonSlot = self.marca_botao_display(
                    self.inseri_texto_display,
                    button,
                )
                button.clicked.connect(buttonSlot)

    def marca_botao_display(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def inseri_texto_display(self, button):
        # self.display.setText('Clicked')
        button_text = button.text()
        self.display.insert(button_text)