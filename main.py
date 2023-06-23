import sys

from ui_modified import *
from Custom_Widgets.Widgets import loadJsonStyle


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

        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()

    window.show()
    sys.exit(app.exec())
