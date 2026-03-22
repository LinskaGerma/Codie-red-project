from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QMessageBox
)

from logic.database import add_category


class AddCategoryWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Add Category / Group")

        layout = QVBoxLayout()

##########################new section
# CATEGORY INPUT

        layout.addWidget(QLabel("Enter category"))

        self.category_input = QLineEdit()
        layout.addWidget(self.category_input)

##########################new section
# SUBCATEGORY INPUT

        layout.addWidget(QLabel("Enter subcategory"))

        self.subcategory_input = QLineEdit()
        layout.addWidget(self.subcategory_input)

##########################new section
# SAVE BUTTON

        save_button = QPushButton("Save Category")
        save_button.clicked.connect(self.save_category)

        layout.addWidget(save_button)

        self.setLayout(layout)

##########################new section
# SAVE CATEGORY LOGIC

    def save_category(self):

        category = self.category_input.text().lower().strip()
        subcategory = self.subcategory_input.text().lower().strip()

        if not category or not subcategory:
            QMessageBox.warning(self, "Error", "Fill both fields")
            return

        result = add_category(category, subcategory)

        if result == "duplicate":
            QMessageBox.warning(
                self,
                "Duplicate",
                "This category and subcategory already exist"
            )

        elif result == "subcategory_added":
            QMessageBox.information(
                self,
                "Info",
                f"Category '{category}' exists.\nSubcategory added."
            )

        elif result == "new_category_added":
            QMessageBox.information(
                self,
                "Success",
                f"New category '{category}' created."
            )

        self.category_input.clear()
        self.subcategory_input.clear()