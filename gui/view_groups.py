from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
)

from PySide6.QtCore import Qt
from PySide6.QtGui import QFont

from logic.group_service import get_groups_matrix
from gui.utils import get_color


class ViewGroupsWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Groups Overview")

        layout = QVBoxLayout()

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

        self.load_data()

##########################new section
# LOAD DATA

    def load_data(self):

        data = get_groups_matrix()
        levels = ["beginner", "middle", "advanced", "professional"]

        max_subcats = max(len(sub) for sub in data.values())

        total_rows = sum(len(levels) + 2 for _ in data)

        self.table.setRowCount(total_rows)
        self.table.setColumnCount(max_subcats + 1)
        self.table.clearContents()

        current_row = 0

        for category, subcats in data.items():

##########################new section
# CATEGORY TITLE

            title = QTableWidgetItem(category.upper())
            title.setFont(QFont("Arial", 10, QFont.Bold))
            title.setTextAlignment(Qt.AlignCenter)

            self.table.setSpan(current_row, 0, 1, max_subcats + 1)
            self.table.setItem(current_row, 0, title)

            current_row += 1

##########################new section
# SUBCATEGORIES

            col = 1
            for sub in subcats:
                item = QTableWidgetItem(sub)
                item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(current_row, col, item)
                col += 1

            current_row += 1

##########################new section
# LEVELS

            for level in levels:

                level_item = QTableWidgetItem(level)
                level_item.setTextAlignment(Qt.AlignCenter)
                self.table.setItem(current_row, 0, level_item)

                col = 1
                for sub in subcats:
                    value = subcats[sub][level]

                    item = QTableWidgetItem(str(value))
                    item.setTextAlignment(Qt.AlignCenter)
                    item.setBackground(get_color(value))

                    self.table.setItem(current_row, col, item)
                    col += 1

                current_row += 1

            current_row += 1

        self.table.resizeColumnsToContents()