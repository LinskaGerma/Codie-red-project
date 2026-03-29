from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QMessageBox
)

from logic.user_service import add_category


class AddCategoryWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Add Category / Group")

        layout = QVBoxLayout()

##########################new section
# CATEGORY INPUT

        layout.addWidget(QLabel("Enter category"))

        self.category_input = QLineEdit()
        self.category_input.setPlaceholderText("e.g. sport, music")
        layout.addWidget(self.category_input)

##########################new section
# SUBCATEGORY INPUT

        layout.addWidget(QLabel("Enter subcategory"))

        self.subcategory_input = QLineEdit()
        self.subcategory_input.setPlaceholderText("e.g. tennis, guitar")
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

        category = self.category_input.text().strip().lower()
        subcategory = self.subcategory_input.text().strip().lower()

##########################new section
# VALIDATION

        if not category or not subcategory:
            QMessageBox.warning(self, "Error", "Both fields are required")
            return

        if len(category) < 2 or len(subcategory) < 2:
            QMessageBox.warning(self, "Error", "Too short values")
            return

##########################new section
# SAVE

        result = add_category(category, subcategory)

##########################new section
# FEEDBACK

        if result == "duplicate":

            QMessageBox.warning(
                self,
                "Duplicate",
                f"'{category} → {subcategory}' already exists"
            )

        elif result == "subcategory_added":

            QMessageBox.information(
                self,
                "Updated",
                f"Category '{category}' exists.\nSubcategory '{subcategory}' added."
            )

        elif result == "new_category_added":

            QMessageBox.information(
                self,
                "Success",
                f"New category '{category}' created with '{subcategory}'"
            )

##########################new section
# CLEAR

        self.clear_form()

##########################new section

    def clear_form(self):

        self.category_input.clear()
        self.subcategory_input.clear()

        self.category_input.setFocus()