from PySide6.QtGui import QColor

def get_color(value):

    if value == 0:
        return QColor(255, 150, 150)

    elif value <= 2:
        return QColor(255, 230, 150)

    return QColor(150, 255, 150)