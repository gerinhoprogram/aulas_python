import sys

from main_window import MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QLabel


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()

    label1 = QLabel('Ola mundo')
    label1.setStyleSheet('font-size: 50px')
    window.v_layout.addWidget(label1)
    window.adJustFixedSize()

    
    window.show()

    app.exec()


