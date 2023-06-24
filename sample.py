from PySide2.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QWidget, QTableWidget, QTableWidgetItem, QPushButton, QLineEdit

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.table_widget = QTableWidget()
        self.fields_layout = QVBoxLayout()
        self.add_button = QPushButton("Add")

        self.add_button.clicked.connect(self.add_row)

        self.central_widget = QWidget()
        self.central_widget.setLayout(self.fields_layout)
        self.setCentralWidget(self.central_widget)

        self.fields_layout.addWidget(QLineEdit())
        self.fields_layout.addWidget(QLineEdit())
        self.fields_layout.addWidget(self.add_button)
        self.fields_layout.addWidget(self.table_widget)

    def add_row(self):
        row_count = self.table_widget.rowCount()
        self.table_widget.insertRow(row_count)

        # Retrieve the input values from the fields
        input1 = self.fields_layout.itemAt(0).widget().text()
        input2 = self.fields_layout.itemAt(1).widget().text()

        # Create QTableWidgetItem objects and populate the cells of the new row
        item1 = QTableWidgetItem(input1)
        item2 = QTableWidgetItem(input2)

        self.table_widget.setItem(row_count, 0, item1)
        self.table_widget.setItem(row_count, 1, item2)

if __name__ == '__main__':
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec_()
