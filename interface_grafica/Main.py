import sys
from info import Info
from display import Display
from Main_calculadora import MainWindow
from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication
from Variaveis import WINDOW_ICON_PATH
from styles import setupTheme
from button import ButtonGrid


if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme()
    window = MainWindow()
    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    # info
    info = Info('Sua conta')
    window.addToVLayout(info)

    # Display
    display = Display()
    window.addToVLayout(display)

    # GRID
    buttonGrid = ButtonGrid(display, info, window)
    window.vLayout.addLayout(buttonGrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()
