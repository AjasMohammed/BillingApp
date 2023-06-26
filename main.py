import sys

from ui_dashboard import *
from Custom_Widgets.Widgets import *

import csv
from datetime import datetime

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        ########################################################################
        # APPLY JSON STYLESHEET
        ########################################################################
        # self = QMainWindow class
        # self.ui = Ui_MainWindow / user interface class
        loadJsonStyle(self, self.ui)
        ########################################################################


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

                print(row)


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()

    window.create_barchart()

    window.show()
    sys.exit(app.exec_())
