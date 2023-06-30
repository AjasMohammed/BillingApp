import sys

from ui_dashboard import *
from ui_login import Ui_MainWindow as Ui_Loginwindow

from Custom_Widgets.Widgets import *

import csv
import os
from datetime import datetime
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import hashlib


# PATH WHERE THE DATABASE WILL BE CREATED
system_user_path = os.path.expanduser("~")
app_path = os.path.join(system_user_path, "Pybill")

os.makedirs(app_path, exist_ok=True)

        # DATABASE INNITIALISATION
db_path = os.path.join(app_path, "users.db")
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName(db_path)
db.open()

query = QSqlQuery()
query.exec_("CREATE TABLE IF NOT EXISTS users ("
                    "id INTEGER PRIMARY KEY AUTOINCREMENT,"
                    "username TEXT NOT NULL UNIQUE,"
                    "password TEXT NOT NULL,"
                    "company TEXT NOT NULL"
                    ");")

def hash_item(item):

    # Create a SHA-256 hash object
    hash_object = hashlib.sha256()

    # Convert the item to bytes and hash it
    hash_object.update(item.encode('utf-8'))

    # Get the hashed item as a hexadecimal string
    hashed_item = hash_object.hexdigest()

    return hashed_item


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
        


        # CREATES A DB TO STORE USER SPECIFIC INFORMATION
        folder_path = self.create_user_folder()
        self.user_db_path = os.path.join(folder_path, "bill_info.db")
        self.user_db = QSqlDatabase.addDatabase("QSQLITE")
        self.user_db.setDatabaseName(self.user_db_path)
        self.user_db.open()
        print("connection : ", self.user_db.open())

        self.query = QSqlQuery(self.user_db)

        self.query.exec_("""CREATE TABLE IF NOT EXISTS bill_info (
                         bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         bill_name TEXT NOT NULL,
                         total REAL NOT NULL,
                         created_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")
        if self.query.exec_():
            print("good")
        else:
            print("error")
            print(self.query.lastQuery())
            print(self.query.lastError().text())

        


        # Setting the default page to dashboard
        self.ui.body_frame.setCurrentWidget(self.ui.dashboard)


        self.ui.add_btn.clicked.connect(self.add_products)
        self.ui.save_btn.clicked.connect(self.save_table)


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################
        self.show()


    def create_user_folder(self):
        folder_name = self.username
        folder_path = os.path.join(app_path, folder_name)

        # CREATES A FOLDER IN THE NAME OF USER
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)
        return folder_path


    def load_ui_info(self):
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


    def add_products(self):
        try:
            customer_name = self.ui.customer_name_field.text()
            customer_contact = self.ui.customer_contact_field.text()

            product_name = self.ui.product_name_field.text()
            product_id = self.ui.product_id_field.text()
            product_price = float(self.ui.product_price_field.text())
            product_qty = int(self.ui.product_qty_field.text())

            assert all([product_name, product_id, product_price, product_qty]), "Connot leave the product fields empty"
            
        except AssertionError as e:
            QMessageBox.warning(self, "Empty Fields", str(e))
            print(e)
        
        except ValueError:
            QMessageBox.warning(self, "Wrong Input!", "Wrong input for the field!")
            


        else:
            data = [product_name,  product_id, product_qty, product_price, customer_name, customer_contact]

            row = self.ui.bill_table.rowCount()

            self.ui.bill_table.insertRow(row)

            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.ui.bill_table.setItem(row, col, item)
            
            # Clear the input fields
            self.ui.customer_name_field.clear()
            self.ui.customer_contact_field.clear()
            self.ui.product_name_field.clear()
            self.ui.product_id_field.clear()
            self.ui.product_price_field.clear()
            self.ui.product_qty_field.clear()



    def save_table(self):
        bill_tag = self.ui.bill_tag_field.text()

        # CEATES TABLE TO STORE THE BILL
        self.query.exec_(f"""CREATE TABLE IF NOT EXISTS {bill_tag} (
                         item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                         product_name TEXT NOT NULL,
                         product_id TEXT NOT NULL,
                         price REAL NOT NULL,
                         quantity INTEGER NOT NULL,
                         customer_name TEXT,
                         customer_contact TEXT
        )""")

        rows = self.ui.bill_table.rowCount()

        # ITERATES THROUGH THE TABLE WIDGET AND ADDS THE VALUES TO THE DB TABLE
        for row in range(rows):
            prod_name = self.ui.bill_table.item(row, 0).text()
            prod_id = self.ui.bill_table.item(row, 1).text()
            qty = self.ui.bill_table.item(row, 2).text()
            price = self.ui.bill_table.item(row, 3).text()
            cust_name = self.ui.bill_table.item(row, 4).text()
            cust_contact = self.ui.bill_table.item(row, 5).text()

            self.query.prepare(f"""INSERT INTO {bill_tag} (product_name, product_id, price, quantity,
                              customer_name, customer_contact)
                               VALUES (?, ?, ?, ?, ?, ?)""")
            self.query.addBindValue(prod_name)
            self.query.addBindValue(prod_id)
            self.query.addBindValue(float(price))
            self.query.addBindValue(int(qty))
            self.query.addBindValue(cust_name)
            self.query.addBindValue(cust_contact)

            if not self.query.exec_():
                print("Error inserting values:", self.query.lastError().text())

        # ADDS THE BILL TO THE bill_info TABLE
        self.query.prepare(f"""INSERT INTO bill_info (bill_name, total)
                           VALUES (?, (SELECT SUM(price * quantity) FROM {bill_tag}))""")
        self.query.addBindValue(bill_tag)
        if not self.query.exec_():
            print(self.query.lastQuery())
            print(self.query.lastError().text())
        else:
            self.ui.bill_table.clearContents()
            self.ui.bill_table.setRowCount(0)


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_Loginwindow()
        self.ui.setupUi(self)

        # BUTTON CLICKS
        self.ui.goto_login.clicked.connect(lambda : self.ui.auth_frame.setCurrentWidget(self.ui.login_frame))
        self.ui.goto_signup.clicked.connect(lambda : self.ui.auth_frame.setCurrentWidget(self.ui.signup_frame))

        self.ui.signup_btn.clicked.connect(self.signup_info)
        self.ui.login_btn.clicked.connect(self.login_info)

        self.ui.auth_frame.setCurrentWidget(self.ui.login_frame)

        # Initialize the completer model
        self.completer_model = QStringListModel()

        # Connect the completer to the username field
        self.ui.username_field_login.setCompleter(self.auto_complete())


        self.username = ""
        self.password = ""
        self.company_name = ""

        self.auto_complete()


        self.show()
    
    def signup_info(self):
        self.username = self.ui.username_field_signup.text()
        password = self.ui.password_field_signup.text()
        self.company_name = self.ui.company_name_field.text()

        self.password = hash_item(password) # HASHED PASSWORD

        if len(password) < 4 or len(self.username) < 4 or self. company_name == "":
            QMessageBox.warning(self, "Invalid Input!", "Must contain atleast 4 characters")


        query.prepare("SELECT * FROM users WHERE username=?")
        query.addBindValue(self.username)

        if query.exec_() and query.next():
            QMessageBox.warning(self, "User Exists", "The entered username already exists. Please choose a different username.")

        else:
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
        password = self.ui.password_field_login.text()

        self.password = hash_item(password)
        print(self.password)

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
        
    
    def auto_complete(self):

        previous_users = []

        query.prepare("SELECT username FROM users")
        if query.exec_():
            while query.next():
                user = query.value(0)
                previous_users.append(user)

        # Set the completer model with previous usernames
        self.completer_model.setStringList(previous_users)

        # Create the completer widget
        completer = QCompleter()
        completer.setModel(self.completer_model)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        return completer


    def open_dash_window(self):

        window = MainWindow(self.username, self.password)

        self.close()
        ui = window.ui
        window.load_ui_info()
        window.create_barchart()
        window.show()



if __name__ == "__main__":
    app = QApplication(sys.argv)


    login_window = LoginWindow()

    login_window.show()
    sys.exit(app.exec_())