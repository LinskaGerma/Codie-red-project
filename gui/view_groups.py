from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem
)

from PySide6.QtGui import QColor

from logic.database import get_groups_matrix, get_color
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

        current_row = 0

        total_rows = 0

        # считаем строки заранее
        for category in data:
            total_rows += len(levels) + 2  # title + spacing

        self.table.setRowCount(total_rows)
        self.table.setColumnCount(10)

        self.table.clear()

        for category, subcats in data.items():

##########################new section
# CATEGORY TITLE

            self.table.setSpan(current_row, 0, 1, 10)
            self.table.setItem(current_row, 0, QTableWidgetItem(category.upper()))

            current_row += 1

##########################new section
# SUBCATEGORY HEADER

            col = 1

            for sub in subcats:
                self.table.setItem(current_row, col, QTableWidgetItem(sub))
                col += 1

            current_row += 1

##########################new section
# LEVEL ROWS

            for level in levels:

                self.table.setItem(current_row, 0, QTableWidgetItem(level))

                col = 1

                for sub in subcats:
                    value = subcats[sub][level]
                    item = QTableWidgetItem(str(value))

                    #color
                    item.setBackground(get_color(value))

                    self.table.setItem(current_row, col, item)
                    col += 1

                current_row += 1

##########################new section
# EMPTY ROW BETWEEN CATEGORIES

            current_row += 1
