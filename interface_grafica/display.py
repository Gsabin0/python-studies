from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLineEdit
from Variaveis import BIG_FONT_SIZE, MINIMUM_WIDTH, TEXT_MARGIN

class Display(QLineEdit):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()
    
    def configStyle(self):
        self.setStyleSheet(f'font-size: {BIG_FONT_SIZE}px;')
        self.setMinimumHeight(BIG_FONT_SIZE*2)
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        