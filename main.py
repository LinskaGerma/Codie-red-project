import sys
from PySide6.QtWidgets import QApplication

from gui.welcome import WelcomeWindow

app = QApplication(sys.argv)

window = WelcomeWindow()
window.show()

sys.exit(app.exec())
