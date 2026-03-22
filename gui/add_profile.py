from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QComboBox,
    QCheckBox, QMessageBox
)

from logic.database import save_user, load_database


class AddProfileWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Add Profile")

        layout = QVBoxLayout()

##########################new section
# NAME

        layout.addWidget(QLabel("Name Surname"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

##########################new section
# EMAIL

        layout.addWidget(QLabel("Email"))
        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

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
# LEVEL

        layout.addWidget(QLabel("Level"))

        self.level_box = QComboBox()
        self.level_box.addItems(["beginner", "middle", "advanced", "professional"])
        layout.addWidget(self.level_box)

##########################new section
# CITY

        layout.addWidget(QLabel("City"))
        self.city_input = QLineEdit()
        layout.addWidget(self.city_input)

##########################new section
# DAYS

        layout.addWidget(QLabel("Select available days"))

        self.mon = QCheckBox("Monday")
        self.tue = QCheckBox("Tuesday")
        self.wed = QCheckBox("Wednesday")
        self.thu = QCheckBox("Thursday")
        self.fri = QCheckBox("Friday")
        self.sat = QCheckBox("Saturday")
        self.sun = QCheckBox("Sunday")

        for d in [self.mon, self.tue, self.wed, self.thu, self.fri, self.sat, self.sun]:
            layout.addWidget(d)

##########################new section
# TIME

        layout.addWidget(QLabel("Preferred time"))

        self.time_box = QComboBox()
        self.time_box.addItems(["morning", "afternoon", "evening"])
        layout.addWidget(self.time_box)

##########################new section
# SAVE BUTTON

        save_button = QPushButton("Save Profile")
        save_button.clicked.connect(self.save_profile)
        layout.addWidget(save_button)

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
# SAVE PROFILE

    def save_profile(self):

        name = self.name_input.text().strip()
        email = self.email_input.text().strip()
        city = self.city_input.text().strip()

        if not name or not email:
            QMessageBox.warning(self, "Error", "Name and Email are required")
            return

        selected_days = []

        if self.mon.isChecked():
            selected_days.append("Monday")
        if self.tue.isChecked():
            selected_days.append("Tuesday")
        if self.wed.isChecked():
            selected_days.append("Wednesday")
        if self.thu.isChecked():
            selected_days.append("Thursday")
        if self.fri.isChecked():
            selected_days.append("Friday")
        if self.sat.isChecked():
            selected_days.append("Saturday")
        if self.sun.isChecked():
            selected_days.append("Sunday")

        profile = {
            "name": name,
            "email": email,
            "category": self.category_box.currentText(),
            "subcategory": self.subcategory_box.currentText(),
            "level": self.level_box.currentText(),
            "city": city.lower(),
            "days": selected_days,
            "time": self.time_box.currentText()
        }

        save_user(profile)

        QMessageBox.information(self, "Success", "Profile saved successfully")

        self.clear_form()

##########################new section
# CLEAR FORM

    def clear_form(self):

        self.name_input.clear()
        self.email_input.clear()
        self.city_input.clear()

        for d in [self.mon, self.tue, self.wed, self.thu, self.fri, self.sat, self.sun]:
            d.setChecked(False)

        self.level_box.setCurrentIndex(0)
        self.time_box.setCurrentIndex(0)