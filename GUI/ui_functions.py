from functools import partial

from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QWidget
from PyQt5 import QtCore

from gui_main import Main


def init_functional(widget: QWidget) -> None:
    _UIFunctions.set_default(widget)
    _UIFunctions.set_shadows(widget)

    _UIFunctions.on_button_click(widget)


class _UIFunctions(Main):
    def set_default(self):
        """Configures the main parameters of the window."""
        self.stacked_widget.setCurrentWidget(self.home_page)
        self.setWindowFlags(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)

    def set_shadows(self):
        """Sets shadows"""
        shadows: list = list()
        # Defining shadows
        shadows.append(
            QGraphicsDropShadowEffect(blurRadius=8, xOffset=3, yOffset=3))

        # So far, there is only one shadow. Between the menu bar and the main window.

        # Apply shadows
        for shadow in shadows:
            self.menu_widget.setGraphicsEffect(shadow)

    def on_button_click(self):
        """Configures actions when buttons are clicked."""
        # Exit Button
        self.shutdown_btn.clicked.connect(self.close)

        # Nav Buttons
        for nav_button in self.nav_buttons.findChildren(QPushButton):
            nav_button.clicked.connect(partial(_change_current_widget, self, nav_button))

    def change_current_widget(self, button):
        buttons = {  # TODO: It is worth updating
            "   Image Editor": 1,
            "   Document Editor": 2,
            "   Databases": 3,
            "   Profile": 4,
            "   Settings": 5
        }
        self.stacked_widget.setCurrentIndex(buttons[button.text()])


def _change_current_widget(widget, button: QPushButton) -> None:
    _UIFunctions.change_current_widget(widget, button)
