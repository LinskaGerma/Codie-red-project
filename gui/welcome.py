from PySide6.QtWidgets import (
    QWidget, QLabel, QPushButton, QVBoxLayout, QMessageBox
)

from gui.add_profile import AddProfileWindow
from gui.search import SearchContactsWindow
from gui.edit_profile import EditProfileWindow
from gui.view_groups import ViewGroupsWindow
from gui.add_category import AddCategoryWindow




class WelcomeWindow(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle("UBSCOMe")

        layout = QVBoxLayout()

##########################new section
# TITLE

        layout.addWidget(QLabel("Welcome to the UBS Hobbies to Meet"))

##########################new section
# MENU BUTTONS

        btn1 = QPushButton("1. Add your profile")
        btn1.clicked.connect(self.open_add_profile)
        layout.addWidget(btn1)

        btn2 = QPushButton("2. Select contact from existing users")
        btn2.clicked.connect(self.open_search_contacts)
        layout.addWidget(btn2)

        btn3 = QPushButton("3. Add new category / group")
        btn3.clicked.connect(self.open_add_category)
        layout.addWidget(btn3)

        btn4 = QPushButton("4. View existing groups")
        btn4.clicked.connect(self.open_view_groups)
        layout.addWidget(btn4)

        btn5 = QPushButton("5. Edit your profile")
        btn5.clicked.connect(self.open_edit_profile)
        layout.addWidget(btn5)

##########################new section
# SET LAYOUT

        self.setLayout(layout)

##########################new section
# ROUTES

    def open_add_profile(self):
        self.add_window = AddProfileWindow()
        self.add_window.show()

    def open_search_contacts(self):
        self.search_window = SearchContactsWindow()
        self.search_window.show()

    def open_add_category(self):
        if not hasattr(self, "category_window") or self.category_window is None:
            self.category_window = AddCategoryWindow()

        self.category_window.show()
        self.category_window.raise_()

    def open_view_groups(self):
        self.groups_window = ViewGroupsWindow()
        self.groups_window.show()

    def open_edit_profile(self):
        self.edit_window = EditProfileWindow()
        self.edit_window.show()

    def not_ready(self):
        QMessageBox.information(self, "Info", "Feature will be added later")