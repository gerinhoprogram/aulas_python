from typing import Optional
import PySide6.QtCore
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QVBoxLayout, QWidget)

class MainWindow(QMainWindow):
    def __init__(self, parent: QWidget | None = None, *args, **kwargs) -> None:
        super().__init__(parent, *args, **kwargs)

        # configuração basica
        self.cw = QWidget()
        self.v_layout = QVBoxLayout()
        self.cw.setLayout(self.v_layout)
        self.setCentralWidget(self.cw)

        # título
        self.setWindowTitle('Calculadora')


    # ajustando tamanho da janelas
    def adJustFixedSize(self):
        self.adjustSize()
        self.setFixedSize(self.width(), self.height())
        