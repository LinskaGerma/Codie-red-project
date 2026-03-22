from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QComboBox, QTableWidget,
    QTableWidgetItem, QMessageBox
)

from logic.database import search_users, load_database


class SearchContactsWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Search Contacts")

        layout = QVBoxLayout()

##########################new section
# CATEGORY

        layout.addWidget(QLabel("Category"))

        self.category_box = QComboBox()
        self.load_categories()
        layout.addWidget(self.category_box)

##########################new section
# SUBCATEGORY

        layout.addWidget(QLabel("Subcategory"))

        self.subcategory_box = QComboBox()
        layout.addWidget(self.subcategory_box)

        self.category_box.currentTextChanged.connect(self.update_subcategories)
        self.update_subcategories(self.category_box.currentText())

##########################new section
# SEARCH BUTTON

        search_button = QPushButton("Search")
        search_button.clicked.connect(self.perform_search)
        layout.addWidget(search_button)

##########################new section
# TABLE

        self.table = QTableWidget()
        layout.addWidget(self.table)

        self.setLayout(layout)

##########################new section
# LOAD CATEGORIES

    def load_categories(self):
        database = load_database()
        self.category_box.clear()
        self.category_box.addItems(list(database.keys()))

##########################new section
# UPDATE SUBCATEGORIES

    def update_subcategories(self, category):
        database = load_database()

        self.subcategory_box.clear()

        if category in database:
            self.subcategory_box.addItems(list(database[category].keys()))

##########################new section
# PERFORM SEARCH

    def perform_search(self):

        category = self.category_box.currentText()
        subcategory = self.subcategory_box.currentText()

        users = search_users(category, subcategory)

        if not users:
            QMessageBox.information(self, "Info", "No users found")
            self.table.setRowCount(0)
            return

        self.table.setRowCount(len(users))
        self.table.setColumnCount(6)

        self.table.setHorizontalHeaderLabels([
            "Name",
            "Email",
            "Level",
            "City",
            "Days",
            "Time"
        ])

        for row, user in enumerate(users):

            self.table.setItem(row, 0, QTableWidgetItem(user["name"]))
            self.table.setItem(row, 1, QTableWidgetItem(user["email"]))
            self.table.setItem(row, 2, QTableWidgetItem(user["level"]))
            self.table.setItem(row, 3, QTableWidgetItem(user["city"]))
            self.table.setItem(row, 4, QTableWidgetItem(", ".join(user.get("days", []))))
            self.table.setItem(row, 5, QTableWidgetItem(user.get("time", "")))