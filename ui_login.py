# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loginiNwMIz.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 513)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.auth_frame = QStackedWidget(self.centralwidget)
        self.auth_frame.setObjectName(u"auth_frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.auth_frame.sizePolicy().hasHeightForWidth())
        self.auth_frame.setSizePolicy(sizePolicy)
        self.auth_frame.setMaximumSize(QSize(16777215, 438))
        font = QFont()
        font.setPointSize(10)
        self.auth_frame.setFont(font)
        self.signup_frame = QWidget()
        self.signup_frame.setObjectName(u"signup_frame")
        self.verticalLayout_3 = QVBoxLayout(self.signup_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.frame = QFrame(self.signup_frame)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.widget_15 = QWidget(self.frame)
        self.widget_15.setObjectName(u"widget_15")
        self.verticalLayout_13 = QVBoxLayout(self.widget_15)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.goto_login = QPushButton(self.widget_15)
        self.goto_login.setObjectName(u"goto_login")
        self.goto_login.setLayoutDirection(Qt.RightToLeft)
        icon = QIcon()
        icon.addFile(u":/blueicons/icons/blue_icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.goto_login.setIcon(icon)
        self.goto_login.setFlat(True)

        self.verticalLayout_13.addWidget(self.goto_login, 0, Qt.AlignLeft)


        self.verticalLayout_2.addWidget(self.widget_15, 0, Qt.AlignTop)

        self.widget_16 = QWidget(self.frame)
        self.widget_16.setObjectName(u"widget_16")
        self.verticalLayout_14 = QVBoxLayout(self.widget_16)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.pushButton = QPushButton(self.widget_16)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy2)
        self.pushButton.setMinimumSize(QSize(100, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 100))
        self.pushButton.setStyleSheet(u"border:3px solid #004cff;\n"
"border-radius:50px")
        icon1 = QIcon()
        icon1.addFile(u":/blueicons/icons/blue_icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)
        self.pushButton.setIconSize(QSize(60, 110))
        self.pushButton.setFlat(True)

        self.verticalLayout_14.addWidget(self.pushButton, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_2.addWidget(self.widget_16, 0, Qt.AlignTop)

        self.widget = QWidget(self.frame)
        self.widget.setObjectName(u"widget")
        sizePolicy.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy)
        self.verticalLayout_5 = QVBoxLayout(self.widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.widget_3 = QWidget(self.widget)
        self.widget_3.setObjectName(u"widget_3")
        self.horizontalLayout = QHBoxLayout(self.widget_3)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 15, -1)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        font1.setWeight(75)
        self.label.setFont(font1)

        self.horizontalLayout.addWidget(self.label)

        self.username_field_signup = QLineEdit(self.widget_3)
        self.username_field_signup.setObjectName(u"username_field_signup")
        self.username_field_signup.setMinimumSize(QSize(150, 27))
        self.username_field_signup.setFont(font)
        self.username_field_signup.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(156, 156, 156);")

        self.horizontalLayout.addWidget(self.username_field_signup)


        self.verticalLayout_5.addWidget(self.widget_3)

        self.widget_4 = QWidget(self.widget)
        self.widget_4.setObjectName(u"widget_4")
        self.horizontalLayout_2 = QHBoxLayout(self.widget_4)
        self.horizontalLayout_2.setSpacing(20)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, 15, -1)
        self.label_2 = QLabel(self.widget_4)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font1)

        self.horizontalLayout_2.addWidget(self.label_2)

        self.password_field_signup = QLineEdit(self.widget_4)
        self.password_field_signup.setObjectName(u"password_field_signup")
        self.password_field_signup.setMinimumSize(QSize(150, 27))
        self.password_field_signup.setFont(font)
        self.password_field_signup.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(156, 156, 156);")
        self.password_field_signup.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_field_signup.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_2.addWidget(self.password_field_signup)


        self.verticalLayout_5.addWidget(self.widget_4)

        self.widget_6 = QWidget(self.widget)
        self.widget_6.setObjectName(u"widget_6")
        self.horizontalLayout_3 = QHBoxLayout(self.widget_6)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font1)

        self.horizontalLayout_3.addWidget(self.label_3)

        self.company_name_field = QLineEdit(self.widget_6)
        self.company_name_field.setObjectName(u"company_name_field")
        self.company_name_field.setMinimumSize(QSize(150, 27))
        self.company_name_field.setFont(font)
        self.company_name_field.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(156, 156, 156);")

        self.horizontalLayout_3.addWidget(self.company_name_field)


        self.verticalLayout_5.addWidget(self.widget_6)

        self.widget_5 = QWidget(self.widget)
        self.widget_5.setObjectName(u"widget_5")
        self.verticalLayout_6 = QVBoxLayout(self.widget_5)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(9, 15, 9, 9)
        self.signup_btn = QPushButton(self.widget_5)
        self.signup_btn.setObjectName(u"signup_btn")
        sizePolicy2.setHeightForWidth(self.signup_btn.sizePolicy().hasHeightForWidth())
        self.signup_btn.setSizePolicy(sizePolicy2)
        self.signup_btn.setMinimumSize(QSize(115, 35))
        self.signup_btn.setMaximumSize(QSize(212, 47))
        font2 = QFont()
        font2.setPointSize(16)
        font2.setBold(False)
        font2.setWeight(50)
        self.signup_btn.setFont(font2)
        self.signup_btn.setLayoutDirection(Qt.LeftToRight)
        self.signup_btn.setStyleSheet(u"background-color: #004cff;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        icon2 = QIcon()
        icon2.addFile(u":/whiteicons/icons/white_icons/log-in.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.signup_btn.setIcon(icon2)
        self.signup_btn.setIconSize(QSize(25, 25))
        self.signup_btn.setCheckable(False)
        self.signup_btn.setFlat(True)

        self.verticalLayout_6.addWidget(self.signup_btn, 0, Qt.AlignHCenter)


        self.verticalLayout_5.addWidget(self.widget_5)


        self.verticalLayout_2.addWidget(self.widget)


        self.verticalLayout_3.addWidget(self.frame)

        self.auth_frame.addWidget(self.signup_frame)
        self.login_frame = QWidget()
        self.login_frame.setObjectName(u"login_frame")
        self.verticalLayout_11 = QVBoxLayout(self.login_frame)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.frame_2 = QFrame(self.login_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.widget_13 = QWidget(self.frame_2)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_12 = QVBoxLayout(self.widget_13)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.goto_signup = QPushButton(self.widget_13)
        self.goto_signup.setObjectName(u"goto_signup")
        self.goto_signup.setFont(font)
        self.goto_signup.setLayoutDirection(Qt.RightToLeft)
        self.goto_signup.setIcon(icon)
        self.goto_signup.setIconSize(QSize(20, 20))
        self.goto_signup.setFlat(True)

        self.verticalLayout_12.addWidget(self.goto_signup, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.widget_13)

        self.widget_8 = QWidget(self.frame_2)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_4 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.pushButton_2 = QPushButton(self.widget_8)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy2.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy2)
        self.pushButton_2.setMinimumSize(QSize(100, 0))
        self.pushButton_2.setMaximumSize(QSize(16777215, 100))
        self.pushButton_2.setStyleSheet(u"border:3px solid #004cff;\n"
"border-radius:50px")
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QSize(60, 110))
        self.pushButton_2.setFlat(True)

        self.horizontalLayout_4.addWidget(self.pushButton_2, 0, Qt.AlignHCenter|Qt.AlignTop)


        self.verticalLayout_4.addWidget(self.widget_8, 0, Qt.AlignVCenter)

        self.widget_2 = QWidget(self.frame_2)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy)
        self.verticalLayout_9 = QVBoxLayout(self.widget_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.widget_7 = QWidget(self.widget_2)
        self.widget_7.setObjectName(u"widget_7")
        self.horizontalLayout_7 = QHBoxLayout(self.widget_7)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, -1, 15, -1)
        self.label_7 = QLabel(self.widget_7)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label_7)

        self.username_field_login = QLineEdit(self.widget_7)
        self.username_field_login.setObjectName(u"username_field_login")
        self.username_field_login.setMinimumSize(QSize(150, 27))
        self.username_field_login.setFont(font)
        self.username_field_login.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.username_field_login.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(156, 156, 156);")
        self.username_field_login.setClearButtonEnabled(False)

        self.horizontalLayout_7.addWidget(self.username_field_login)


        self.verticalLayout_9.addWidget(self.widget_7)

        self.widget_12 = QWidget(self.widget_2)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_8 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_8.setSpacing(20)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(-1, -1, 15, -1)
        self.label_8 = QLabel(self.widget_12)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font1)

        self.horizontalLayout_8.addWidget(self.label_8)

        self.password_field_login = QLineEdit(self.widget_12)
        self.password_field_login.setObjectName(u"password_field_login")
        self.password_field_login.setMinimumSize(QSize(150, 27))
        self.password_field_login.setFont(font)
        self.password_field_login.setStyleSheet(u"border-radius: 10px;\n"
"border: 1px solid;\n"
"border-color: rgb(156, 156, 156);")
        self.password_field_login.setInputMethodHints(Qt.ImhHiddenText|Qt.ImhNoAutoUppercase|Qt.ImhNoPredictiveText|Qt.ImhSensitiveData)
        self.password_field_login.setEchoMode(QLineEdit.Password)

        self.horizontalLayout_8.addWidget(self.password_field_login)


        self.verticalLayout_9.addWidget(self.widget_12)

        self.widget_14 = QWidget(self.widget_2)
        self.widget_14.setObjectName(u"widget_14")
        self.verticalLayout_10 = QVBoxLayout(self.widget_14)
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(9, 15, 9, 9)
        self.login_btn = QPushButton(self.widget_14)
        self.login_btn.setObjectName(u"login_btn")
        sizePolicy2.setHeightForWidth(self.login_btn.sizePolicy().hasHeightForWidth())
        self.login_btn.setSizePolicy(sizePolicy2)
        self.login_btn.setMinimumSize(QSize(115, 35))
        self.login_btn.setMaximumSize(QSize(212, 37))
        self.login_btn.setFont(font2)
        self.login_btn.setStyleSheet(u"background-color: #004cff;\n"
"color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        self.login_btn.setIcon(icon2)
        self.login_btn.setIconSize(QSize(25, 25))
        self.login_btn.setCheckable(False)
        self.login_btn.setFlat(True)

        self.verticalLayout_10.addWidget(self.login_btn)


        self.verticalLayout_9.addWidget(self.widget_14, 0, Qt.AlignHCenter)


        self.verticalLayout_4.addWidget(self.widget_2)


        self.verticalLayout_11.addWidget(self.frame_2)

        self.auth_frame.addWidget(self.login_frame)

        self.verticalLayout.addWidget(self.auth_frame, 0, Qt.AlignHCenter)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 622, 21))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.auth_frame.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.auth_frame.setStyleSheet(QCoreApplication.translate("MainWindow", u"border-radius: 10px;\n"
"border-color: rgb(156, 156, 156);", None))
        self.goto_login.setText(QCoreApplication.translate("MainWindow", u"Existing User", None))
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"User Name      :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Password        :", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Company Name :", None))
        self.signup_btn.setText(QCoreApplication.translate("MainWindow", u"Sign Up ", None))
#if QT_CONFIG(shortcut)
        self.signup_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
        self.goto_signup.setText(QCoreApplication.translate("MainWindow", u"New User ", None))
        self.pushButton_2.setText("")
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"User Name      :", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Password        :", None))
        self.login_btn.setText(QCoreApplication.translate("MainWindow", u"Log In", None))
#if QT_CONFIG(shortcut)
        self.login_btn.setShortcut(QCoreApplication.translate("MainWindow", u"Return", None))
#endif // QT_CONFIG(shortcut)
    # retranslateUi

