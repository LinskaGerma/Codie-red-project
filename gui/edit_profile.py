from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton,
    QVBoxLayout, QLineEdit, QComboBox,
    QCheckBox, QMessageBox
)

from logic.database import (
    find_users_by_email,
    update_user_by_id,
    delete_user_by_id
)


class EditProfileWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("Edit Profile")

        self.selected_user = None

        layout = QVBoxLayout()

##########################new section
# EMAIL INPUT

        layout.addWidget(QLabel("Enter your email"))

        self.email_input = QLineEdit()
        layout.addWidget(self.email_input)

        load_button = QPushButton("Load Profiles")
        load_button.clicked.connect(self.load_profiles)
        layout.addWidget(load_button)

##########################new section
# PROFILE BUTTONS

        self.buttons_layout = QVBoxLayout()
        layout.addLayout(self.buttons_layout)

##########################new section
# FORM

        layout.addWidget(QLabel("Name"))
        self.name_input = QLineEdit()
        layout.addWidget(self.name_input)

        layout.addWidget(QLabel("Level"))
        self.level_box = QComboBox()
        self.level_box.addItems(["beginner", "middle", "advanced", "professional"])
        layout.addWidget(self.level_box)

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
# ACTION BUTTONS

        save_button = QPushButton("Save Changes")
        save_button.clicked.connect(self.save_changes)
        layout.addWidget(save_button)

        delete_button = QPushButton("Delete Profile")
        delete_button.clicked.connect(self.delete_profile)
        layout.addWidget(delete_button)

##########################new section
# DELETE ALL (UX SAFE)

        delete_all_button = QPushButton("Delete ALL profiles")
        delete_all_button.setEnabled(False)
        layout.addWidget(delete_all_button)

        self.setLayout(layout)

##########################new section
# LOAD PROFILES

    def load_profiles(self):

        email = self.email_input.text().strip()

        users = find_users_by_email(email)

        # clear buttons
        while self.buttons_layout.count():
            child = self.buttons_layout.takeAt(0)
            if child.widget():
                child.widget().deleteLater()

        if not users:
            QMessageBox.warning(self, "Error", "No profiles found")
            return

        for user in users:

            text = f"{user['category']} | {user['subcategory']} | {user['level']}"

            btn = QPushButton(text)

            btn.clicked.connect(lambda _, u=user: self.select_profile(u))

            self.buttons_layout.addWidget(btn)

##########################new section
# SELECT PROFILE

    def select_profile(self, user):

        self.selected_user = user

        self.name_input.setText(user["name"])
        self.level_box.setCurrentText(user["level"])
        self.city_input.setText(user["city"])

        days = user.get("days", [])

        self.mon.setChecked("Monday" in days)
        self.tue.setChecked("Tuesday" in days)
        self.wed.setChecked("Wednesday" in days)
        self.thu.setChecked("Thursday" in days)
        self.fri.setChecked("Friday" in days)
        self.sat.setChecked("Saturday" in days)
        self.sun.setChecked("Sunday" in days)

        self.time_box.setCurrentText(user.get("time", "evening"))

##########################new section
# SAVE CHANGES

    def save_changes(self):

        if not self.selected_user:
            QMessageBox.warning(self, "Error", "Select profile first")
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

        updated_profile = self.selected_user.copy()

        updated_profile["name"] = self.name_input.text().strip()
        updated_profile["level"] = self.level_box.currentText()
        updated_profile["city"] = self.city_input.text().strip().lower()
        updated_profile["days"] = selected_days
        updated_profile["time"] = self.time_box.currentText()

        update_user_by_id(updated_profile["id"], updated_profile)

        QMessageBox.information(self, "Success", "Profile updated")

##########################new section
# DELETE PROFILE

    def delete_profile(self):

        if not self.selected_user:
            QMessageBox.warning(self, "Error", "Select profile first")
            return

        delete_user_by_id(self.selected_user["id"])

        QMessageBox.information(self, "Deleted", "Profile removed")

        self.selected_user = None
        self.clear_form()

##########################new section
# CLEAR FORM

    def clear_form(self):

        self.name_input.clear()
        self.city_input.clear()

        for d in [self.mon, self.tue, self.wed, self.thu, self.fri, self.sat, self.sun]:
            d.setChecked(False)

        self.level_box.setCurrentIndex(0)
        self.time_box.setCurrentIndex(0)