# Import necessary libraries
import calendar
import sys
from datetime import datetime, timedelta
import time

# Import UI components
from ui_dashboard import *
from ui_login import Ui_MainWindow as Ui_Loginwindow

# Import custom widgets
from Custom_Widgets.Widgets import *

# Import additional libraries
import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery
import hashlib

# Import report generation libraries
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors

# Import QtCharts for charts support
from PySide2.QtCharts import QtCharts

# Define the PATH where the database will be created
system_user_path = os.path.expanduser("~")
app_path = os.path.join(system_user_path, "Pybill")

# Create the application directory if it doesn't exist
os.makedirs(app_path, exist_ok=True)

# DATABASE INITIALIZATION
# Define the path to the SQLite database file
db_path = os.path.join(app_path, "users.db")

# Create and open the SQLite database connection
db = QSqlDatabase.addDatabase("QSQLITE")
db.setDatabaseName(db_path)
db.open()

# Prepare a query to create a 'users' table if it doesn't exist
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
        # Initialize the QMainWindow class
        QMainWindow.__init__(self)

        # Create and set up the UI using the Ui_MainWindow class
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Initialize class attributes
        self.id = None
        self.username = username
        self.password = password
        self.company = None

        # Prepare a query to retrieve user information from the 'users' table
        query.prepare("SELECT id, company FROM users WHERE username=? And password=?")
        query.addBindValue(username)
        query.addBindValue(password)

        # Execute the query and fetch user data
        if query.exec_():
            while query.next():
                self.id = query.value(0)
                self.company = query.value(1)
        else:
            print("Query execution failed.")

        # Initialize dynamic_frame to None
        self.dynamic_frame = None

        # CREATES A DB TO STORE USER-SPECIFIC INFORMATION
        # Create a folder for the user and set the user-specific database path
        folder_path = self.create_user_folder()
        self.user_db_path = os.path.join(folder_path, "bill_info.db")
        self.user_db = QSqlDatabase.addDatabase("QSQLITE")
        self.user_db.setDatabaseName(self.user_db_path)
        self.user_db.open()
        print("connection : ", self.user_db.open())

        # Prepare a query to create a 'bill_info' table if it doesn't exist
        self.query = QSqlQuery(self.user_db)
        self.query.prepare("""CREATE TABLE IF NOT EXISTS bill_info (
                             bill_id INTEGER PRIMARY KEY AUTOINCREMENT,
                             bill_name TEXT NOT NULL,
                             total REAL NOT NULL,
                             created_date DATETIME DEFAULT CURRENT_TIMESTAMP
        )""")

        # Execute the query to create the table or print an error message if it fails
        if self.query.exec_():
            print("good")
        else:
            print("error")
            print(self.query.lastQuery())
            print(self.query.lastError().text())

        # Set the default page to the dashboard
        self.ui.body_frame.setCurrentWidget(self.ui.dashboard)

        # Connect button clicks to their corresponding functions
        self.ui.add_btn.clicked.connect(self.add_products)
        self.ui.save_btn.clicked.connect(self.save_table)
        self.ui.more_btn.clicked.connect(self.create_dynamic_frame)
        self.ui.vis_btn.clicked.connect(self.chart_selection)
        self.ui.logout_btn.clicked.connect(self.log_out)

        # Connect navigation buttons to their corresponding page switches
        self.ui.to_dynamic.clicked.connect(self.callit)
        self.ui.to_home.clicked.connect(lambda: self.ui.body_frame.setCurrentWidget(self.ui.dashboard))

        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # Apply the custom stylesheet using the loadJsonStyle function
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################

        # Call the count_data() function to update the displayed data
        self.count_data()

        # Display the main window
        self.show()

    def callit(self):
        self.create_dynamic_frame()
        self.ui.body_frame.setCurrentWidget(self.ui.bills_history)


    def create_user_folder(self):
        # Define the folder name using the username
        folder_name = self.username
        
        # Create the complete folder path by joining app_path and folder_name
        folder_path = os.path.join(app_path, folder_name)

        # CREATES A FOLDER IN THE NAME OF THE USER
        # Check if the folder already exists, and if not, create it
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        # Return the path of the created folder
        return folder_path


    def load_ui_info(self):
        # Set the window title and window icon
        self.setWindowTitle("PyBill")
        icon = QIcon(":/blueicons/icons/blue_icons/printer.svg")
        self.setWindowIcon(icon)

        # Set the company name, username, and make the horizontal header visible
        self.ui.company_name.setText(self.company)
        self.ui.label_username.setText(self.username)
        self.ui.bill_table.horizontalHeader().setVisible(True)

        # Call functions to populate the dashboard_billcard and display the bar chart for 'This Week'
        self.dashboard_billcard()
        self.bar_chart('This Week')


        ###########CREATE CHART###############


    # Define a function to handle chart selection based on the chosen time frame
    def chart_selection(self):
        # Get the selected time frame from the combo box
        time_frame = self.ui.chart_timeframe.currentText()

        # If there's an existing chart widget, remove it
        if self.ui.chart_vis_frame is not None:
            while self.ui.chart_vis_frame.layout().count():
                item = self.ui.chart_vis_frame.layout().takeAt(0)
        
        # Choose to display a bar chart for 'This Week' or 'This Month' based on the selected time frame
        if time_frame == "This Week":
            self.bar_chart(time_frame)
        elif time_frame == 'This Month':
            self.bar_chart(time_frame)


    @staticmethod
    def date_calc(week_number):
        # Get the current year
        year = datetime.today().year

        # Find the first day of the year
        first_day = datetime(year, 1, 1)

        # Find the first day of the week (Monday) of the given week number
        days_to_add = (week_number - 1) * 7
        first_day_of_week = first_day + timedelta(days=days_to_add)

        # Find the last day of the week (Sunday) of the given week number
        last_day_of_week = first_day_of_week + timedelta(days=6)

        # Format the first and last day as 'YYYY-MM-DD' strings
        first_day = first_day_of_week.strftime('%Y-%m-%d')
        last_day = last_day_of_week.strftime('%Y-%m-%d')

        # Return the first and last day of the week
        return first_day, last_day


    def bar_chart(self, arg):
        # Retrieve data from the database based on the argument (arg) provided
        bills = self.get_data(arg)

        # Initialize lists to store categories and corresponding amounts for the bar chart
        categories = []
        amount = []

        if arg == 'This Week':
            # For 'This Week', extract day and bill amount data from each bill entry
            for bill in bills:
                day = datetime.strptime(bill['bill_date'], "%Y-%m-%d").strftime('%A')
                categories.append(day)
                amount.append(bill['bill_amount'])

        elif arg == 'This Month':
            # For 'This Month', extract week and bill amount data from each bill entry
            for week, amt in bills.items():
                week = self.date_calc(week)
                start = "/".join(week[0].split('-')[1:])
                end = "/".join(week[1].split('-')[1:])
                categories.append(f"({start} - {end})")
                amount.append(amt)

        # If there are amounts in the list, add an extra value to set the y-axis range
        if amount:
            n = max(amount)
            amount.append(n + (n * 0.1))

        # Create a bar chart
        chart = QtCharts.QChart()
        chart.setTitle(f"{arg}'s Performance")

        # Create a bar series
        series = QtCharts.QBarSeries()
        set0 = QtCharts.QBarSet(arg)
        set0.append(amount)
        series.append(set0)

        # Set the width of the bars
        series.setBarWidth(0.3)

        # Add the series to the chart
        chart.addSeries(series)

        # Create a category axis for the x-axis
        axis_x = QtCharts.QBarCategoryAxis()
        axis_x.append(categories)
        chart.addAxis(axis_x, Qt.AlignBottom)

        # Attach the series to the x-axis
        series.attachAxis(axis_x)

        # Create a value axis for the y-axis
        axis_y = QtCharts.QValueAxis()
        chart.addAxis(axis_y, Qt.AlignLeft)

        # Attach the series to the y-axis
        series.attachAxis(axis_y)

        # Add animation to the chart
        chart.setAnimationOptions(QtCharts.QChart.AllAnimations)

        # Create a chart view
        chart_view = QtCharts.QChartView(chart)
        chart_view.setRenderHint(QPainter.Antialiasing)

        # Add the chart view to the chart visualization frame
        self.ui.chart_vis_frame.layout().addWidget(chart_view)


    @staticmethod
    def time_frame(arg):
    # Get the current date
        current_date = datetime.today()

        if arg == "week":
            # Calculate the start of the current week (Monday)
            start_of_week = current_date - timedelta(days=current_date.weekday())
            # Calculate the end of the current week (Sunday)
            end_of_week = start_of_week + timedelta(days=6)
            return start_of_week, end_of_week

        elif arg == "month":
            # Calculate the start of the current month (1st day)
            start_of_month = current_date.replace(day=1)
            # Calculate the end of the current month (last day)
            end_of_month = start_of_month + timedelta(days=calendar.monthrange(start_of_month.year, start_of_month.month)[1])
            return start_of_month, end_of_month


    def get_data(self, arg):
        # Retrieve data from the database based on the argument (arg) provided

        if arg == 'This Week':
            # Calculate the start and end of the current week
            start_of_week, end_of_week = self.time_frame("week")

            # Prepare the SQL query to retrieve data within the current week
            self.query.prepare("""
                SELECT DATE(created_date) AS week_number, SUM(total) FROM bill_info 
                WHERE created_date BETWEEN :start_date AND :end_date
                GROUP BY DATE(created_date) 
                ORDER BY created_date
            """)

            # Bind the start and end dates to the query
            self.query.bindValue(":start_date", str(start_of_week.date()))
            self.query.bindValue(":end_date", str(end_of_week.date()))

            if self.query.exec_():
                print("Done")

            else:
                # Query execution failed, handle the error
                print("Query Error:", self.query.lastError().text())

        elif arg == "This Month":
            # Calculate the start and end of the current month
            start_of_month, end_of_month = self.time_frame("month")
            
            # Prepare the SQL query to retrieve data within the current month
            self.query.prepare("""
                SELECT DATE(created_date) AS week_number, SUM(total) FROM bill_info 
                WHERE created_date BETWEEN :start_date AND :end_date
                GROUP BY DATE(created_date) 
                ORDER BY created_date
            """)

            # Bind the start and end dates to the query
            self.query.bindValue(":start_date", str(start_of_month))
            self.query.bindValue(":end_date", str(end_of_month))

            if self.query.exec_():
                # Initialize a dictionary to store weekly data
                bill = {}
                # Iterate over the result set and retrieve the data
                while self.query.next():
                    date = datetime.strptime(self.query.value(0), '%Y-%m-%d')
                    amount = self.query.value(1)

                    # Get the week number using isocalendar
                    week_number = datetime.isocalendar(date)[1]

                    # Store the data in the dictionary, summing amounts for the same week number
                    if week_number in bill:
                        bill[week_number] += amount
                    else:
                        bill[week_number] = amount

                # Return the dictionary with weekly data
                return bill

            else:
                # Query execution failed, handle the error
                print("Query Error:", self.query.lastError().text())
                print("Query Error:", self.query.lastQuery())

        # For 'This Week' and 'This Month', process the query result and return the list of bills
        bills = []
        while self.query.next():
            bill = {}

            # Get bill date and amount from the query result
            bill['bill_date'] = self.query.value(0)
            bill["bill_amount"] = self.query.value(1)
            bills.append(bill)

        # Return the list of bills
        return bills


    def add_products(self):
        try:
            # Get input values from the user interface
            customer_name = self.ui.customer_name_field.text()
            customer_contact = self.ui.customer_contact_field.text()

            product_name = self.ui.product_name_field.text()
            product_id = self.ui.product_id_field.text()
            product_price = float(self.ui.product_price_field.text())
            product_qty = int(self.ui.product_qty_field.text())

            # Check if all product fields are filled, raise an exception if any is empty
            assert all([product_name, product_id, product_price, product_qty]), "Cannot leave the product fields empty"

        except AssertionError as e:
            # Show a warning message box for empty fields and print the error message
            QMessageBox.warning(self, "Empty Fields", str(e))
            print(e)

        except ValueError:
            # Show a warning message box for wrong input and inform the user about the error
            QMessageBox.warning(self, "Wrong Input!", "Wrong input for the field!")

        else:
            # If all fields have valid data, proceed with adding the product to the bill table

            # Create a list with product and customer information
            data = [product_name, product_id, product_qty, product_price, customer_name, customer_contact]

            # Get the current row count of the bill table
            row = self.ui.bill_table.rowCount()

            # Insert a new row into the bill table
            self.ui.bill_table.insertRow(row)

            # Populate the new row with data from the 'data' list
            for col, value in enumerate(data):
                item = QTableWidgetItem(str(value))
                self.ui.bill_table.setItem(row, col, item)

            # Clear the input fields after adding the product
            self.ui.customer_name_field.clear()
            self.ui.customer_contact_field.clear()
            self.ui.product_name_field.clear()
            self.ui.product_id_field.clear()
            self.ui.product_price_field.clear()
            self.ui.product_qty_field.clear()


    def save_table(self):
        # Get the bill tag from the user interface and capitalize it
        bill_tag = self.ui.bill_tag_field.text().capitalize()
        # Clear the bill tag input field
        self.ui.bill_tag_field.clear()

        # CREATE TABLE TO STORE THE BILL
        # Execute the SQL query to create a table for the current bill
        self.query.exec_(f"""CREATE TABLE IF NOT EXISTS {bill_tag} (
                        item_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        product_name TEXT NOT NULL,
                        product_id TEXT NOT NULL,
                        price REAL NOT NULL,
                        quantity INTEGER NOT NULL,
                        customer_name TEXT,
                        customer_contact TEXT
        )""")

        # Get the number of rows in the bill table
        rows = self.ui.bill_table.rowCount()

        # ITERATE THROUGH THE TABLE WIDGET AND ADD THE VALUES TO THE DB TABLE
        for row in range(rows):
            # Get data from each cell in the bill table
            prod_name = self.ui.bill_table.item(row, 0).text()
            prod_id = self.ui.bill_table.item(row, 1).text()
            qty = self.ui.bill_table.item(row, 2).text()
            price = self.ui.bill_table.item(row, 3).text()
            cust_name = self.ui.bill_table.item(row, 4).text()
            cust_contact = self.ui.bill_table.item(row, 5).text()

            # Prepare and execute the SQL query to insert values into the current bill table
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

        # ADD THE BILL TO THE bill_info TABLE
        # Prepare and execute the SQL query to insert bill information into the bill_info table
        self.query.prepare(f"""INSERT INTO bill_info (bill_name, total)
                        VALUES (?, (SELECT SUM(price * quantity) FROM {bill_tag}))""")
        self.query.addBindValue(bill_tag)
        if not self.query.exec_():
            print(self.query.lastQuery())
            print(self.query.lastError().text())
        else:
            # Clear the contents of the bill table and set row count to 0
            self.ui.bill_table.clearContents()
            self.ui.bill_table.setRowCount(0)

        # Update the dashboard bill card
        self.dashboard_billcard()


    def create_dynamic_frame(self):
        # Retrieve bills data from the database
        bills = self.__fetch_table()

        if self.dynamic_frame is not None:
            # Delete the existing dynamic frame and clear the layout
            self.dynamic_frame.deleteLater()
            while self.ui.card_views.layout().count():
                item = self.ui.card_views.layout().takeAt(0)

        # Create a new dynamic frame
        self.dynamic_frame = QFrame(self.ui.card_views)
        self.dynamic_frame.setObjectName("dynamic_frame")

        # Create the layout for the dynamic frame
        self.vertical_layout = QVBoxLayout(self.dynamic_frame)
        self.vertical_layout.setObjectName("vertical_layout")

        # Number of bills to show per page
        bills_per_page = 4
        current_row_layout = None

        # Loop through all bills from the database and create cards
        for i, bill_data in enumerate(bills):
            if i % bills_per_page == 0:
                # Create a new horizontal layout for each row of cards
                current_row_layout = QHBoxLayout()
                current_row_layout.setObjectName(f"row_layout_{i}")
                self.vertical_layout.addLayout(current_row_layout)

            # Create a frame for each bill card
            item_frame = QFrame()
            item_frame.setObjectName(f"item_frame_{i}")

            # Set the stylesheet for the card frame
            item_frame.setStyleSheet("""
                QFrame {
                    background-color: white;
                    border-radius: 10px; /* Set the border-radius to control the curvature */
                    margin: 10px; /* Add some margin around the card */
                }
            """)

            # Set a fixed width and height for the cards
            card_width = 220
            card_height = 250
            item_frame.setFixedSize(card_width, card_height)

            # Create labels for each item and add them to the card layout
            bill_name_label = QLabel(f"<u>{bill_data['bill_name'].capitalize()}</u>", item_frame)
            total_label = QLabel(f"Total: {bill_data['bill_amount']}", item_frame)
            bill_id_label = QLabel(f"Bill ID: {bill_data['bill_id']}", item_frame)
            bill_date_label = QLabel(f"Bill Date: {bill_data['bill_date']}", item_frame)

            label_styles = """
                margin: 5px; /* Add some margin between the labels */
                padding-left:10px;
                font-size: 13px;
            """

            # Apply styles to the labels
            bill_name_label.setStyleSheet("font-size:15px;margin: 5px;")
            total_label.setStyleSheet(label_styles)
            bill_id_label.setStyleSheet(label_styles)
            bill_date_label.setStyleSheet(label_styles)

            # Set a fixed width and height for the labels
            label_width = 150
            label_height = 40
            bill_name_label.setFixedSize(label_width, label_height)
            total_label.setFixedSize(label_width, label_height)
            bill_id_label.setFixedSize(label_width, label_height)
            bill_date_label.setFixedSize(label_width, label_height)

            # Center align the labels in each card
            bill_name_label.setAlignment(Qt.AlignCenter)
            total_label.setAlignment(Qt.AlignLeft)
            bill_id_label.setAlignment(Qt.AlignLeft)
            bill_date_label.setAlignment(Qt.AlignLeft)

            # Set bold font for the "Bill name" label
            font = bill_name_label.font()
            font.setBold(True)
            bill_name_label.setFont(font)

            # Create a vertical layout for each card
            card_layout = QVBoxLayout(item_frame)
            card_layout.setAlignment(Qt.AlignTop)  # Align the card contents to the top
            card_layout.setContentsMargins(10, 10, 10, 10)  # Add margins around the card

            # Add the labels to the card layout
            card_layout.addWidget(bill_name_label)
            card_layout.addWidget(total_label)
            card_layout.addWidget(bill_id_label)
            card_layout.addWidget(bill_date_label)

            # Create a button for each card with an icon
            button = QPushButton()
            button.setObjectName(f"bill_{bill_data['bill_id']}")
            icon7 = QIcon()
            icon7.addFile(u":/blueicons/icons/blue_icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
            button.setIcon(icon7)
            button.setIconSize(QSize(35, 20))
            button.setFlat(True)
            button.setStyleSheet("background-color: #fff;")

            # Add stretching space to push the button to the right side
            card_layout.addStretch()

            # Add the button to the card layout
            card_layout.addWidget(button)

            # Connect the button's clicked signal to a slot for handling the button click event
            button.clicked.connect(self.bill_btn)  # Replace "self.bill_btn" with the appropriate slot function

            # Set the vertical layout for the item frame
            item_frame.setLayout(card_layout)

            # Add the item frame to the current row layout
            current_row_layout.addWidget(item_frame)

        # Set the layout for the dynamic frame
        self.dynamic_frame.setLayout(self.vertical_layout)

        # Create a scroll area to hold the dynamic frame
        self.scroll_area = QScrollArea(self.ui.card_views)
        self.scroll_area.setObjectName("scroll_area")
        self.scroll_area.setWidgetResizable(True)

        # Create a widget to hold the dynamic frame
        self.scroll_widget = QWidget()
        self.scroll_layout = QVBoxLayout(self.scroll_widget)
        self.scroll_layout.setContentsMargins(0, 0, 0, 0)
        self.scroll_layout.addWidget(self.dynamic_frame)  # Add the dynamic frame to the scroll widget
        self.scroll_area.setWidget(self.scroll_widget)
        self.scroll_widget.setStyleSheet("background-color: #eff9fe;")

        # Add the scroll area to the card_views frame
        self.ui.verticalLayout_49.addWidget(self.scroll_area)

        # Switch to the bills_history page in the user interface
        self.ui.body_frame.setCurrentWidget(self.ui.bills_history)


    def dashboard_billcard(self):
        # Retrieve bills data from the database
        bills = self.__fetch_table(True)
        cards = {}

        # Prepare data for each bill card
        for i in range(1, 5):
            cards[f'label_bill{i}'] = str(bills[i-1]['bill_name'])
            cards[f'label_id{i}'] = str(bills[i-1]['bill_id'])
            cards[f'label_price{i}'] = str(bills[i-1]['bill_amount'])
            cards[f'label_billdate{i}'] = str(bills[i-1]['bill_date'])
            cards[f'arrow_btn{i}'] = f'bill_{bills[i-1]["bill_id"]}'

        # Update the user interface with the data for each bill card
        for i in cards:
            # Get the user interface element corresponding to the current card item
            item = getattr(self.ui, i, None)
            if item:
                if 'arrow' in i:
                    # For the arrow button, set its object name to the corresponding bill ID and connect its clicked signal to the bill_btn slot
                    item.setObjectName(cards[i])
                    item.clicked.connect(self.bill_btn)
                else:
                    # For other labels, set their text to the corresponding data from the database
                    item.setText(cards[i])


    def bill_btn(self):
        # Get the button that triggered the event (sender)
        btn = self.sender()

        # Extract the bill ID from the button's object name
        bill_id = int(btn.objectName().split("_")[1])

        # Fetch the detailed information of the selected bill from the database
        bill_info = self.__fetch_table(bill_id=bill_id)[0]
        bill_name = bill_info["bill_name"]
        bill_total = bill_info["bill_amount"]
        bill_date = bill_info["bill_date"]
        bill_time = bill_info["bill_time"]

        # Load the table with the items of the selected bill
        self.__load_table(bill_name)

        # Update the labels in the bill history page with the selected bill information
        self.ui.label_id.setText(str(bill_id))
        self.ui.label_date_2.setText(str(bill_date))
        self.ui.label_amount.setText(str(bill_total))
        self.ui.label_name.setText(str(bill_name).capitalize())

        # Connect the export button's clicked signal to the __bill_export method with the selected bill information as arguments
        self.ui.export_btn.clicked.connect(lambda: self.__bill_export(bill_name, bill_id, bill_total, bill_date, bill_time))

        # Connect the delete button's clicked signal to the __bill_del method with the selected bill information as arguments
        self.ui.delete_btn.clicked.connect(lambda: self.__bill_del(bill_name, bill_id))

        # Switch to the bill_history page in the user interface
        self.ui.body_frame.setCurrentWidget(self.ui.bill_history)
                

    def __bill_del(self, bill_name, bill_id):
        # Show a confirmation dialog box to ask for deletion confirmation
        reply = QMessageBox.question(None, "Confirm Deletion", "Are you sure you want to delete?", 
                                    QMessageBox.Yes | QMessageBox.No, QMessageBox.No)

        # If the user confirms the deletion
        if reply == QMessageBox.Yes:
            # Delete the specified table associated with the bill
            delete_table_query = f"DROP TABLE IF EXISTS {bill_name}"
            self.query.exec_(delete_table_query)

            # Delete the row from the 'bill_info' table based on the bill_id
            delete_row_query = "DELETE FROM bill_info WHERE bill_id = ?"
            self.query.prepare(delete_row_query)
            self.query.addBindValue(bill_id)

            # Execute the delete row query
            if self.query.exec_():
                print("Table and row deleted successfully.")
                # Update the dashboard and bills history with the latest data
                self.dashboard_billcard()
                self.create_dynamic_frame()
            else:
                print("Error deleting table or row:", self.query.lastError().text())
        else:
            # If the user cancels the deletion, do nothing
            pass


    def __bill_export(self, bill_name, bill_id, bill_total, bill_date, bill_time):
        # Fetch the product details for the specified bill
        products = self.__fetch_bill(bill_name)
        
        # Create a file dialog and set its properties
        file_dialog = QFileDialog()
        file_dialog.setWindowTitle("Save Bill")
        file_dialog.setAcceptMode(QFileDialog.AcceptSave)
        file_dialog.setNameFilter("PDF Files (*.pdf);;All Files (*)")

        # Set the default filename using bill_name and bill_id
        default_file_name = f"{bill_name}_{bill_id}.pdf"
        file_dialog.selectFile(default_file_name)

        # Show the file dialog and get the selected file path
        if file_dialog.exec_() == QFileDialog.Accepted:
            file_path = file_dialog.selectedFiles()[0]

            # Set up the PDF document
            pdf_file = f"{bill_name}_invoice.pdf"
            # Create a PDF document
            doc = SimpleDocTemplate(file_path, pagesize=letter)
            story = []
            
            # Create styles for the document
            styles = getSampleStyleSheet()
            title_style = styles["Title"]
            normal_style = styles["Normal"]
            bold_style = styles["Heading1"]

            # Add the title of the invoice
            title = f"{bill_name.capitalize()} Invoice"
            story.append(Paragraph(title, title_style))
            story.append(Spacer(1, 24))

            space = "&nbsp;"
            # Add bill information to the document
            bill_info = f"Bill ID:{space} <b>{bill_id}</b>{space*20}Date:{space} <b>{bill_date}</b>{space*20}Time:{space} <b>{bill_time}</b> <br/><br/>Total Amount: <b>{bill_total}</b>  <br/><br/>"

            bill_info_style = ParagraphStyle(
                                    'BillInfoStyle',
                                    parent=normal_style,
                                    fontSize=12,
                                    leading=14,
                                    leftIndent=40,
                                    spaceAfter=10
                                    )
            
            bill_info_paragraph = Paragraph(bill_info, bill_info_style)
            story.append(bill_info_paragraph)
            story.append(Spacer(1, 12))

            table_title = "<u>Products</u>"
            story.append(Paragraph(table_title, bold_style))
            story.append(Spacer(1,12))

            # Add product details to the story in a table format
            product_data = [["No.", "Name", "ID", "Price", "Quantity"]]
            for i, product in enumerate(products, 1):
                product_data.append([str(i), product["prod_name"], product["prod_id"], str(product["prod_price"]), str(product["prod_qty"])])
            
            # Create a table with the product data
            product_table = Table(product_data)
            
            # Customize the TableStyle for the product table
            product_table.setStyle(TableStyle([
                ('BACKGROUND', (0, 0), (-1, 0), colors.white),
                ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),
                ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
                ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
                ('FONTSIZE', (0, 0), (-1, 0), 12),  # Set the font size to 12
                ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
                ('BACKGROUND', (0, 1), (-1, -1), colors.white),
                ('GRID', (0, 0), (-1, -1), 1, colors.black),  # Add grid lines to all cells
                ('INNERGRID', (0, 0), (-1, -1), 1, colors.black),  # Add inner grid lines to all cells
                ('BOX', (0, 0), (-1, -1), 1, colors.black),  # Add border around the table
                ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),  # Center align the content vertically
                ('LEFTPADDING', (0, 0), (-1, -1), 6),  # Add left padding to the cells
                ('RIGHTPADDING', (0, 0), (-1, -1), 6),  # Add right padding to the cells
            ]))

            # Set the column widths and row heights to increase the size of the table
            product_table._argW[1] = 100  # Width of the first column
            product_table._argW[2] = 70   # Width of the second column
            product_table._argW[3] = 70   # Width of the third column
            product_table._argW[4] = 100  # Width of the fourth column
            product_table._argH[0] = 30   # Height of the first row

            story.append(product_table)
            story.append(Spacer(1, 12))

            # Build the PDF document
            doc.build(story)
            print(f"Bills exported to '{file_path}'")


    def __load_table(self, bill_name):
        # Fetch product details for the specified bill_name
        bill_data = self.__fetch_bill(bill_name)

        # Create a QStandardItemModel with the appropriate dimensions
        model = QStandardItemModel(len(bill_data), 4)
        model.setHorizontalHeaderLabels(["Name", "ID", "Price", "Quantity"])

        # Populate the model with data from the bill_data list of dictionaries
        for row, product in enumerate(bill_data):
            for col, (key, value) in enumerate(product.items()):
                item = QStandardItem(str(value))
                model.setItem(row, col, item)

                # Align the items in each column to the center
                item.setTextAlignment(Qt.AlignCenter)

        # Create the QTableView and set the model
        table_view = self.ui.bill_tableView
        table_view.setModel(model)

        # Optionally, set the table view properties
        table_view.setEditTriggers(QTableView.NoEditTriggers)  # Make the cells non-editable
        table_view.resizeRowsToContents()  # Resize the rows to fit the contents
        table_view.resizeColumnsToContents()  # Resize the columns to fit the contents

        # Set the stretchLastSection property to True to stretch the last section to fill the view
        table_view.horizontalHeader().setStretchLastSection(True)

        # Show the table view
        table_view.show()
    

    def __fetch_bill(self, bill_name):
        # List to store the fetched product details for the specified bill_name
        bill_data = []

        # Prepare a query to fetch all rows from the specified bill table
        self.query.prepare(f'SELECT *  FROM {bill_name} ORDER BY item_id ASC')

        # Execute the query to fetch the data
        if self.query.exec_():
            # Iterate over the result set and retrieve product details for each row
            while self.query.next():
                item = {}
                item["prod_name"] = self.query.value(1)
                item["prod_id"] = self.query.value(2)
                item["prod_price"] = self.query.value(3)
                item["prod_qty"] = self.query.value(4)

                # Append the product details to the bill_data list
                bill_data.append(item)
        
        # Return the list of product details for the specified bill_name
        return bill_data



    def __fetch_table(self, limit=False, **condition):
            if limit == True:
                self.query.prepare("SELECT * FROM bill_info ORDER BY created_date DESC LIMIT 4")
            elif condition:
                key, value = list(condition.items())[0]
                self.query.prepare(f'SELECT * FROM bill_info WHERE {key}={value}')
            else:
                self.query.prepare("SELECT * FROM bill_info ORDER BY created_date DESC")
            bills = []
            # Execute the query
            if self.query.exec_():
            # Iterate over the result set and retrieve the data
                while self.query.next():
                    bill = {}
                    bill["bill_id"] = self.query.value(0)
                    bill["bill_name"] = self.query.value(1)
                    bill["bill_amount"] = self.query.value(2)
                    datetime_string = self.query.value(3)
                    # Parse the datetime string into a datetime object
                    dt_object = datetime.strptime(datetime_string, '%Y-%m-%d %H:%M:%S')
                    # Extract the date part from the datetime object
                    bill["bill_date"] = dt_object.date()
                    bill["bill_time"] = dt_object.time()
                    bills.append(bill)
            return bills


    def count_data(self):
        # Get today's date
        today = datetime.today().date()

        ##############################
        # Fetch statistics for today
        ##############################

        # Count the number of bills and calculate the total amount for today
        self.query.prepare("SELECT COUNT(*), SUM(total) FROM bill_info WHERE DATE(created_date) = :today")
        self.query.bindValue(":today", today)
        if self.query.exec_():
            if self.query.next():
                today_count = self.query.value(0)  # Number of bills for today
                total_amount = self.query.value(1)  # Total amount for today
                self.ui.no_label_1.setText(str(today_count))  # Update the UI with the number of bills for today
                if isinstance(total_amount, str):
                    self.ui.total_label_1.setText(str(0))
                else:
                    self.ui.total_label_1.setText(str(total_amount))  # Update the UI with the total amount for today
            else:
                print("No data added today.")
        else:
            print("Query Error:", self.query.lastError().text())

        ################################
        # Fetch statistics for this week
        ################################

        # Calculate the start and end dates of the current week
        start_of_week, end_of_week = self.time_frame("week")

        # Count the number of bills and calculate the total amount for this week
        self.query.prepare("SELECT COUNT(*), SUM(total) FROM bill_info WHERE DATE(created_date) BETWEEN :start AND :stop")
        self.query.bindValue(":start", str(start_of_week))
        self.query.bindValue(":stop", str(end_of_week))
        if self.query.exec_():
            if self.query.next():
                this_week_count = self.query.value(0)  # Number of bills for this week
                total_amount = self.query.value(1)  # Total amount for this week
                self.ui.no_label_2.setText(str(this_week_count))  # Update the UI with the number of bills for this week
                if isinstance(total_amount, str):
                    self.ui.total_label_2.setText(str(0))
                else:
                    self.ui.total_label_2.setText(str(total_amount))  # Update the UI with the total amount for this week
            else:
                print("No data added this week.")
        else:
            print("Query Error:", self.query.lastError().text())

        #################################
        # Fetch statistics for this month
        #################################

        # Calculate the start and end dates of the current month
        start_of_month, end_of_month = self.time_frame("month")

        # Count the number of bills and calculate the total amount for this month
        self.query.prepare("SELECT COUNT(*), SUM(total) FROM bill_info WHERE DATE(created_date) BETWEEN :start AND :stop")
        self.query.bindValue(":start", str(start_of_month))
        self.query.bindValue(":stop", str(end_of_month))
        if self.query.exec_():
            if self.query.next():
                this_month_count = self.query.value(0)  # Number of bills for this month
                total_amount = self.query.value(1)  # Total amount for this month
                self.ui.no_label_3.setText(str(this_month_count))  # Update the UI with the number of bills for this month
                if isinstance(total_amount, str):
                    self.ui.total_label_3.setText(str(0))
                else:
                    self.ui.total_label_3.setText(str(total_amount))  # Update the UI with the total amount for this month
            else:
                print("No data added this month.")
        else:
            print("Query Error:", self.query.lastError().text())


    def log_out(self):
        # Clear the user-related attributes to log out the user
        self.username = None
        self.company = None
        self.id = None
        self.password = None

        # Wait for a short delay before closing the application (1 second in this case)
        time.sleep(1)
        self.close()


class LoginWindow(QMainWindow):
    def __init__(self, parent=None):
        # Initialize the main login window
        QMainWindow.__init__(self)
        self.ui = Ui_Loginwindow()
        self.ui.setupUi(self)

        # Database connection setup (not shown in the code)

        # Set window properties
        self.setWindowTitle("LogIn")
        self.setFixedSize(500, 500)
        icon = QIcon(':/blueicons/icons/blue_icons/users.svg')
        self.setWindowIcon(icon)

        # Connect button clicks to corresponding functions
        self.ui.goto_login.clicked.connect(lambda: self.ui.auth_frame.setCurrentWidget(self.ui.login_frame))
        self.ui.goto_signup.clicked.connect(lambda: self.ui.auth_frame.setCurrentWidget(self.ui.signup_frame))

        self.ui.signup_btn.clicked.connect(self.signup_info)
        self.ui.login_btn.clicked.connect(self.login_info)

        self.ui.auth_frame.setCurrentWidget(self.ui.login_frame)

        # Initialize variables to store username, password, and company name
        self.username = ""
        self.password = ""
        self.company_name = ""

        # Autocomplete for the username field
        self.auto_complete()

        # Load styles and show the window
        loadJsonStyle(self, self.ui, jsonFiles={
            'login_styles.json'
        })
        self.show()

    def signup_info(self):
        # Retrieve user information from signup form
        self.username = self.ui.username_field_signup.text()
        password = self.ui.password_field_signup.text()
        self.company_name = self.ui.company_name_field.text()

        # Hash the password
        self.password = hash_item(password) # HASHED PASSWORD (not shown in the code)

        # Validate the entered data
        if len(password) < 4 or len(self.username) < 4 or self.company_name == "":
            QMessageBox.warning(self, "Invalid Input!", "Must contain at least 4 characters")
            return

        # Check if the username already exists in the database
        query.prepare("SELECT * FROM users WHERE username=?")
        query.addBindValue(self.username)

        if query.exec_() and query.next():
            QMessageBox.warning(self, "User Exists", "The entered username already exists. Please choose a different username.")
            return

        else:
            # Insert the new user into the database
            query.prepare("INSERT INTO users (username, password, company) VALUES (?, ?, ?)")
            query.addBindValue(self.username)
            query.addBindValue(self.password)
            query.addBindValue(self.company_name)
            query.exec_()

            QMessageBox.information(self, "User Created", "The user is created.")
            # Open the main dashboard window
            self.open_dash_window()

    def login_info(self):
        # Retrieve user information from login form
        self.username = self.ui.username_field_login.text().strip()
        password = self.ui.password_field_login.text()

        # Hash the password
        self.password = hash_item(password) # HASHED PASSWORD (not shown in the code)
        print(self.password)

        # Validate the entered data
        if not self.username:
            QMessageBox.warning(self, "Invalid Input!", "Don't leave fields empty")
            return

        # Check if the username and hashed password combination exists in the database
        query.prepare("SELECT * FROM users WHERE username=? AND password=?")
        query.addBindValue(self.username)
        query.addBindValue(self.password)

        if query.exec_() and query.next():
            # If the combination exists, open the main dashboard window
            self.open_dash_window()
        else:
            QMessageBox.warning(self, "LogIn Error", "The User Doesn't Exist")

    def auto_complete(self):
        # Fetch previous usernames from the database
        previous_users = []

        query.prepare("SELECT username FROM users")
        if query.exec_():
            while query.next():
                user = query.value(0)
                previous_users.append(user)

        # Set up the completer model with previous usernames
        self.completer_model = QStringListModel(previous_users)

        # Create the completer widget
        completer = QCompleter()
        completer.setModel(self.completer_model)
        completer.setCaseSensitivity(Qt.CaseInsensitive)

        # Set the completer for the username field
        self.ui.username_field_login.setCompleter(completer)

    def open_dash_window(self):
        # Open the main dashboard window and pass username and password as parameters
        window = MainWindow(self.username, self.password)
        self.close()
        window.load_ui_info()
        window.show()


if __name__ == "__main__":
    # Create the application and the login window
    app = QApplication(sys.argv)
    login_window = LoginWindow()
    login_window.show()
    sys.exit(app.exec_())
