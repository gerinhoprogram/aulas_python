# QApplication e QPushButton de PySide6.QtWidgets
# QApplication -> O Widget principal da aplicação
# QPushButton -> Um botão
# PySide6.QtWidgets -> Onde estão os widgets do PySide6
import sys

from PySide6.QtWidgets import QApplication, QPushButton, QWidget, QGridLayout

app = QApplication(sys.argv)

botao = QPushButton('Texto do botão')
botao.setStyleSheet('font-size: 40px; color: red')

botao2 = QPushButton('Texto do botão 2')
botao2.setStyleSheet('font-size: 40px; color: blue')

botao3 = QPushButton('Texto do botão 3')
botao3.setStyleSheet('font-size: 40px; color: green')

central_widget = QWidget()
layout = QGridLayout()
central_widget.setLayout(layout)

layout.addWidget(botao, 1, 1, 1, 1)
layout.addWidget(botao2, 1, 2, 1, 1)
layout.addWidget(botao3, 3, 1, 1,2)

central_widget.show()

#botao.show()  # Adiciona o widget na hierarquia e exibe a janela

app.exec()  # O loop da aplicação