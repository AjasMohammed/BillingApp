import sys

from ui_dashboard_1 import *
from ui_login import Ui_MainWindow as Ui_Loginwindow

from Custom_Widgets.Widgets import *

import csv
import os
from datetime import datetime
from PyQt5.QtSql import QSqlDatabase, QSqlQuery


        # DATABASE INNITIALISATION
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName("pybill.db")
db.open()

query = QSqlQuery()
query.exec_("CREATE TABLE IF NOT EXISTS users ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "username TEXT NOT NULL UNIQUE,"
                    "password TEXT NOT NULL,"
                    "company TEXT NOT NULL"
                    ");")


class MainWindow(QMainWindow):
    def __init__(self, username, password, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.id = None
        self.username = username
        self.password = password
        self.company = None


        query.prepare("SELECT id, company FROM users WHERE username=? And password=?")
        query.addBindValue(username)
        query.addBindValue(password)

        if query.exec_():
            while query.next():
                self.id = query.value(0)
                self.company = query.value(1)
        else:
            print("Query execution failed.")
        
        print(self.id)
        print(self.username)
        print(self.password)
        print(self.company)


        # Setting the default page to dashboard
        self.ui.body_frame.setCurrentWidget(self.ui.dashboard)

        self.ui.add_btn.clicked.connect(self.clickme)


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        self.show()

    def load_info(self):
        self.ui.company_name.setText(self.company)
        self.ui.label_username.setText(self.username)
        self.ui.bill_table.horizontalHeader().setVisible(True)
        







        ###########CREATE CHART###############

    def create_barchart(self):

        # jason objects to hold data
        names = {}
        id = {}
        price = {}
        qty = {}

        row_count = 0


        with open("product.csv", 'r') as file:
            # reader = csv.reader(file, delimiter=",")
            reader = csv.DictReader(file)

            for row in reader:

                date_str = row['date']

                date = datetime.strptime(date_str, "%Y-%m-%d")
                week = date.isocalendar()[1]

                # print(row)

    def clickme(self):
        file_path = os.path.expanduser("~")
        print(file_path)
        print("clicked")
        print(self.username, self.password, self.company)
        
    def set_items(self):

        item = QTableWidgetItem()
        item.setText("ABCD")
        self.ui.bill_table.setItem(0,0,item)


        

class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Loginwindow()
        self.ui.setupUi(self)

        # BUTTON CLICKS
        self.ui.goto_login.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.login_frame))
        self.ui.goto_signup.clicked.connect(lambda : self.ui.stackedWidget.setCurrentWidget(self.ui.signup_frame))

        self.ui.signup_btn.clicked.connect(self.signup_info)
        self.ui.login_btn.clicked.connect(self.login_info)

        self.ui.auth_frame.setCurrentWidget(self.ui.login_frame)


        self.username = ""
        self.password = ""
        self.company_name = ""




        self.show()
    
    def signup_info(self):
        self.username = self.ui.username_field_signup.text()
        self.password = self.ui.password_field_signup.text()
        self.company_name = self.ui.company_name_field.text()


        if self.password == "" or self.username == "" or self. company_name == "":
            QMessageBox.warning(self, "Invalid Input!", "Don't leave fields empty")

        query.prepare("SELECT * FROM users WHERE username=?")
        query.addBindValue(self.username)

        if query.exec_() and query.next():

            QMessageBox.warning(self, "User Exists", "The entered username already exists. Please choose a different username.")

        else:

            print("User Doesn't Exist")
            QMessageBox.information(self, "User Created", "The user is created.")

            # # Insert the new user into the database
            query.prepare("INSERT INTO users (username, password, company) VALUES (?, ?, ?)")
            query.addBindValue(self.username)
            query.addBindValue(self.password)
            query.addBindValue(self.company_name)
            query.exec_()

            self.open_dash_window() # OPENS THE MAIN WINDOW

    def login_info(self):
        self.username = self.ui.username_field_login.text().strip()
        self.password = self.ui.password_field_login.text()
        # print(self.username=="")


        # if self.password == "" or self.username == "":
        if not self.username:
            QMessageBox.warning(self, "Invalid Input!", "Don't leave fields empty")
        else:

            query.prepare("SELECT * FROM users WHERE username=? AND password=?")
            query.addBindValue(self.username)
            query.addBindValue(self.password)

            if query.exec_() and query.next():

                self.open_dash_window()
            else :
                QMessageBox.warning(self, "LogIn Error", "The User Doesn't Exist")
        

    def open_dash_window(self):

        window = MainWindow(self.username, self.password)

        self.close()
        ui = window.ui
        window.load_info()
        window.create_barchart()
        window.set_items()
        window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)


    login_window = LoginWindow()

    login_window.show()
    sys.exit(app.exec_())