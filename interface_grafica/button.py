from PySide6.QtWidgets import QPushButton, QGridLayout
from Variaveis import MEDIUM_FONT_SIZE
from uteis import isEmpty, isNUmOrDot, isValidNumber
from display import Display
from PySide6.QtCore import Slot
from typing import TYPE_CHECKING
import math
if TYPE_CHECKING:
    from display import Display
    from info import Info
    from Main_calculadora import MainWindow


class Button(QPushButton):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.config_style()

    def config_style(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(65, 70)


class ButtonGrid(QGridLayout):

    def __init__(self, display: 'Display', info: 'Info', window: 'MainWindow', *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self._gridMask = [
            ['C', 'D', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]
        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._equationInitialValue = 'Sua conta'
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self._make_grid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _make_grid(self):
        self.display.eqPressed.connect(self._eq)
        self.display.delPressed.connect(self._backspace)
        self.display.clearPressed.connect(self._clear())
        self.display.inputPressed.connect(self._insert_to_display)
        self.display.operatorPressed.connect(self._config_left_op)
        for i, row in enumerate(self._gridMask):
            for j, button_text in enumerate(row):
                button = Button(button_text)
                if not isNUmOrDot(button_text) and not isEmpty(button_text):
                    button.setProperty('cssClass', 'specialButton')
                    self._config_special_button(button)
                self.addWidget(button, i, j)
                slot = self._make_slot(self._insert_to_display, button_text)
                self._connect_button_clicked(button, slot)

    @staticmethod
    def _connect_button_clicked(button, slot):
        button.clicked.connect(slot)

    def _config_special_button(self, button):
        text = button.text()

        if text == 'C':
            self._connect_button_clicked(button, self._clear)

        if text == 'D':
            self._connect_button_clicked(button, self.display.backspace)

        if text == 'N':
            self._connect_button_clicked(button, self._invert_number)

        if text in '+-/*^':
            self._connect_button_clicked(
                button,
                self._make_slot(self._config_left_op, text)
            )

        if text == '=':
            self._connect_button_clicked(button, self._eq)

    @Slot()
    def _make_slot(self, func, *args, **kwargs):
        @Slot(bool)
        def real_slot(_):
            func(*args, **kwargs)
        return real_slot

    @Slot()
    def _invert_number(self):
        displayText = self.display.text()
        if not isValidNumber(displayText):
            return
        newNumber = float(displayText) * -1
        if newNumber.is_integer():
            newNumber = int(newNumber)
        self.display.setText(str(newNumber))
        self.display.setFocus()

    @Slot()
    def _insert_to_display(self, text):
        newDisplayValue = self.display.text() + text
        if not isValidNumber(newDisplayValue):
            return
        self.display.insert(text)
        self.display.setFocus()

    @Slot()
    def _clear(self):
        print('Vou fazer outra coisa aqui')
        self._left = None
        self._right = None
        self._op = None
        self.equation = self._equationInitialValue
        self.display.clear()
        self.display.setFocus()

    @Slot()
    def _config_left_op(self, text):
        displayText = self.display.text()  # Deverá ser meu número _left
        self.display.clear()  # Limpa o display
        self.display.setFocus()

        # Se a pessoa clicou no operador sem
        # configurar qualquer número
        if not isValidNumber(displayText) and self._left is None:
            self._show_error('Você não digitou nada.')
            return

        # Se houver algo no número da esquerda,
        # não fazemos nada. Aguardaremos o número da direita.
        if self._left is None:
            self._left = float(displayText)

        self._op = text
        self.equation = f'{self._left} {self._op} ??'

    @Slot()
    def _eq(self):
        displayText = self.display.text()

        if not isValidNumber(displayText) or self._left is None:
            self._show_error('Conta incompleta.')
            return

        self._right = float(displayText)
        self.equation = f'{self._left} {self._op} {self._right}'
        result = 'error'

        try:
            if '^' in self.equation and isinstance(self._left, int | float):
                result = math.pow(self._left, self._right)

            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._show_error('Divisão por zero.')
        except OverflowError:
            self._show_error('Essa conta não pode ser realizada.')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')
        self._left = result
        self._right = None
        self.display.setFocus()

        if result == 'error':
            self._left = None

    def _make_dialog(self, text):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(text)
        return msgBox

    @Slot()
    def _backspace(self):
        self.display.backspace()
        self.display.setFocus()

    def _show_error(self, text):
        msgBox = self._make_dialog(text)
        msgBox.setIcon(msgBox.Icon.Critical)
        msgBox.exec()
        self.display.setFocus()

    def _show_info(self, text):
        msgBox = self._make_dialog(text)
        msgBox.setIcon(msgBox.Icon.Information)
        msgBox.exec()
        self.display.setFocus()
