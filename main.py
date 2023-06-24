import sys

from ui_dashboard import *
from Custom_Widgets.Widgets import *


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
        
    # def checkButtonGroup(self):
    #     btn = self.sender()
    #     group = btn.group
    #     groupBtns = getattr(self, "group_btns_"+str(group))
    #     active = getattr(self, "group_active_"+str(group))
    #     notActive = getattr(self, "group_not_active_"+str(group))

    #     for x in groupBtns:
    #         if not x == btn:
    #             x.setStyleSheet(notActive)
    #             x.active = False

    #     btn.setStyleSheet(active)
    #     btn.active = True


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)


    window = MainWindow()

    window.show()
    sys.exit(app.exec_())
