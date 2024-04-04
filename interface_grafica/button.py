from PySide6.QtWidgets import QPushButton, QGridLayout
from Variaveis import MEDIUM_FONT_SIZE
from uteis import isEmpty, isNUmOrDot
from display import Display
from PySide6.QtCore import Slot


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font =  self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(65, 70)


class ButtonGrid(QGridLayout):
    def __init__(self, display: Display, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['',  '0', '.', '='],
        ]
        self.display = display
        self._makeGrid()

    def _makeGrid(self):
        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNUmOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                self.addWidget(button, i, j)
                buttonSlot = self._makeButtonDisplaySlot(
                    self._insertButtonTextToDisplay,
                    button,
                )
                button.clicked.connect(buttonSlot)  # type: ignore

    def _makeButtonDisplaySlot(self, func, *args, **kwargs):
        @Slot(bool)
        def realSlot(_):
            func(*args, **kwargs)
        return realSlot

    def _insertButtonTextToDisplay(self, button):
        button_text = button.text()
        self.display.insert(button_text)