# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboard.ui'
##
## Created by: Qt User Interface Compiler version 6.5.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLayout, QMainWindow, QMenuBar, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

from Custom_Widgets.Widgets import QCustomSlideMenu
import resource_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(898, 579)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
"\n"
"}\n"
"\n"
"#menu_side{\n"
"background-color:#004cff;\n"
"}\n"
"\n"
"#card1, #card2, #card3, #card4 {\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}\n"
"#header_frame{\n"
"	background-color: #fefeff;\n"
"border-radius: 20px;\n"
"}\n"
"")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_side = QCustomSlideMenu(self.centralwidget)
        self.menu_side.setObjectName(u"menu_side")
        self.menu_side.setAutoFillBackground(False)
        self.menu_side.setStyleSheet(u"background-color:#004cff;\n"
"\n"
"")
        self.verticalLayout_25 = QVBoxLayout(self.menu_side)
        self.verticalLayout_25.setSpacing(0)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_25.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.verticalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.frame_menu = QFrame(self.menu_side)
        self.frame_menu.setObjectName(u"frame_menu")
        self.frame_menu.setFrameShape(QFrame.StyledPanel)
        self.frame_menu.setFrameShadow(QFrame.Raised)
        self.verticalLayout_26 = QVBoxLayout(self.frame_menu)
        self.verticalLayout_26.setSpacing(0)
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_26.setContentsMargins(0, 0, 0, 0)
        self.frame_menutitle = QFrame(self.frame_menu)
        self.frame_menutitle.setObjectName(u"frame_menutitle")
        self.frame_menutitle.setStyleSheet(u"")
        self.frame_menutitle.setFrameShape(QFrame.StyledPanel)
        self.frame_menutitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_menutitle)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, -1, -1, 50)
        self.label_menu = QLabel(self.frame_menutitle)
        self.label_menu.setObjectName(u"label_menu")
        font = QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.label_menu.setFont(font)
        self.label_menu.setLineWidth(1)

        self.horizontalLayout_5.addWidget(self.label_menu, 0, Qt.AlignLeft|Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_menutitle)

        self.frame_menuitems = QFrame(self.frame_menu)
        self.frame_menuitems.setObjectName(u"frame_menuitems")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_menuitems.sizePolicy().hasHeightForWidth())
        self.frame_menuitems.setSizePolicy(sizePolicy)
        self.frame_menuitems.setSizeIncrement(QSize(0, 0))
        font1 = QFont()
        font1.setPointSize(8)
        self.frame_menuitems.setFont(font1)
        self.frame_menuitems.setFrameShape(QFrame.StyledPanel)
        self.frame_menuitems.setFrameShadow(QFrame.Raised)
        self.verticalLayout_28 = QVBoxLayout(self.frame_menuitems)
        self.verticalLayout_28.setSpacing(0)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_menubtns = QFrame(self.frame_menuitems)
        self.frame_menubtns.setObjectName(u"frame_menubtns")
        self.frame_menubtns.setStyleSheet(u"")
        self.frame_menubtns.setFrameShape(QFrame.StyledPanel)
        self.frame_menubtns.setFrameShadow(QFrame.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_menubtns)
        self.verticalLayout_27.setSpacing(30)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(35, 0, 0, 0)
        self.dashboard_btn = QPushButton(self.frame_menubtns)
        self.dashboard_btn.setObjectName(u"dashboard_btn")
        font2 = QFont()
        font2.setPointSize(12)
        self.dashboard_btn.setFont(font2)
        self.dashboard_btn.setStyleSheet(u"	background-color: #fefeff;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 18px ;\n"
"	border-bottom-left-radius: 18px;\n"
"")
        icon = QIcon()
        icon.addFile(u":/icons/home-blue.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(20, 20))
        self.dashboard_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.dashboard_btn)

        self.newbill_btn = QPushButton(self.frame_menubtns)
        self.newbill_btn.setObjectName(u"newbill_btn")
        self.newbill_btn.setFont(font2)
        self.newbill_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;")
        icon1 = QIcon()
        icon1.addFile(u":/icons/file-plus-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newbill_btn.setIcon(icon1)
        self.newbill_btn.setIconSize(QSize(20, 20))
        self.newbill_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.newbill_btn)

        self.statistics_btn = QPushButton(self.frame_menubtns)
        self.statistics_btn.setObjectName(u"statistics_btn")
        self.statistics_btn.setFont(font2)
        self.statistics_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/icons/bar-chart-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statistics_btn.setIcon(icon2)
        self.statistics_btn.setIconSize(QSize(20, 20))
        self.statistics_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.statistics_btn)

        self.logout_btn = QPushButton(self.frame_menubtns)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setFont(font2)
        self.logout_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;")
        icon3 = QIcon()
        icon3.addFile(u":/icons/log-out-white.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon3)
        self.logout_btn.setIconSize(QSize(20, 20))
        self.logout_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.logout_btn)


        self.verticalLayout_28.addWidget(self.frame_menubtns, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_menuitems)


        self.verticalLayout_25.addWidget(self.frame_menu)


        self.horizontalLayout.addWidget(self.menu_side)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QWidget(self.mainbody)
        self.header_frame.setObjectName(u"header_frame")
        self.header_frame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.menu = QWidget(self.header_frame)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.menu)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.menu)
        self.menu_btn.setObjectName(u"menu_btn")
        icon4 = QIcon()
        icon4.addFile(u":/icons/bars-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QSize(25, 25))
        self.menu_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.menu_btn)

        self.label_appname = QLabel(self.menu)
        self.label_appname.setObjectName(u"label_appname")
        font3 = QFont()
        font3.setFamilies([u"SF New Republic"])
        font3.setPointSize(20)
        self.label_appname.setFont(font3)

        self.horizontalLayout_6.addWidget(self.label_appname)


        self.horizontalLayout_2.addWidget(self.menu, 0, Qt.AlignLeft)

        self.space_frame = QWidget(self.header_frame)
        self.space_frame.setObjectName(u"space_frame")
        self.space_frame.setMinimumSize(QSize(150, 72))
        self.horizontalLayout_3 = QHBoxLayout(self.space_frame)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.frame = QFrame(self.space_frame)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_dashboard = QLabel(self.frame)
        self.label_dashboard.setObjectName(u"label_dashboard")
        font4 = QFont()
        font4.setFamilies([u"SF New Republic"])
        font4.setPointSize(28)
        font4.setBold(True)
        font4.setUnderline(False)
        self.label_dashboard.setFont(font4)
        self.label_dashboard.setStyleSheet(u"")

        self.horizontalLayout_4.addWidget(self.label_dashboard)


        self.horizontalLayout_3.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.space_frame, 0, Qt.AlignHCenter)

        self.profile_frame = QWidget(self.header_frame)
        self.profile_frame.setObjectName(u"profile_frame")
        self.profile_frame.setStyleSheet(u"")
        self.verticalLayout_22 = QVBoxLayout(self.profile_frame)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.profilebtn = QWidget(self.profile_frame)
        self.profilebtn.setObjectName(u"profilebtn")
        self.verticalLayout_24 = QVBoxLayout(self.profilebtn)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.profile_btn = QPushButton(self.profilebtn)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setAutoFillBackground(False)
        self.profile_btn.setStyleSheet(u"")
        icon5 = QIcon()
        icon5.addFile(u":/icons/circle-user-regular.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_btn.setIcon(icon5)
        self.profile_btn.setIconSize(QSize(70, 70))
        self.profile_btn.setFlat(True)

        self.verticalLayout_24.addWidget(self.profile_btn)


        self.verticalLayout_22.addWidget(self.profilebtn)

        self.username = QWidget(self.profile_frame)
        self.username.setObjectName(u"username")
        self.verticalLayout_23 = QVBoxLayout(self.username)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_username = QLabel(self.username)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setFont(font2)
        self.label_username.setFrameShape(QFrame.NoFrame)
        self.label_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_username)


        self.verticalLayout_22.addWidget(self.username)


        self.horizontalLayout_2.addWidget(self.profile_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.middle = QWidget(self.mainbody)
        self.middle.setObjectName(u"middle")
        self.horizontalLayout_36 = QHBoxLayout(self.middle)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.horizontalLayout_36.setContentsMargins(-1, -1, -1, 9)
        self.title_recentbill = QWidget(self.middle)
        self.title_recentbill.setObjectName(u"title_recentbill")
        font5 = QFont()
        font5.setPointSize(10)
        self.title_recentbill.setFont(font5)
        self.title_recentbill.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 20px;")
        self.verticalLayout_21 = QVBoxLayout(self.title_recentbill)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.label_recentbill = QLabel(self.title_recentbill)
        self.label_recentbill.setObjectName(u"label_recentbill")
        font6 = QFont()
        font6.setPointSize(15)
        self.label_recentbill.setFont(font6)

        self.verticalLayout_21.addWidget(self.label_recentbill)


        self.horizontalLayout_36.addWidget(self.title_recentbill, 0, Qt.AlignBottom)


        self.verticalLayout.addWidget(self.middle)

        self.body_frame = QWidget(self.mainbody)
        self.body_frame.setObjectName(u"body_frame")
        font7 = QFont()
        font7.setUnderline(False)
        self.body_frame.setFont(font7)
        self.body_frame.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.body_frame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(-1, 0, -1, -1)
        self.card1 = QFrame(self.body_frame)
        self.card1.setObjectName(u"card1")
        self.card1.setStyleSheet(u"")
        self.card1.setFrameShape(QFrame.StyledPanel)
        self.card1.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.card1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.cardbody_frame = QFrame(self.card1)
        self.cardbody_frame.setObjectName(u"cardbody_frame")
        self.cardbody_frame.setFrameShape(QFrame.StyledPanel)
        self.cardbody_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.cardbody_frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.title_frame = QFrame(self.cardbody_frame)
        self.title_frame.setObjectName(u"title_frame")
        self.title_frame.setFrameShape(QFrame.StyledPanel)
        self.title_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.title_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.label_name = QLabel(self.title_frame)
        self.label_name.setObjectName(u"label_name")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(True)
        font8.setUnderline(False)
        self.label_name.setFont(font8)
        self.label_name.setScaledContents(True)
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_name.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_name)


        self.verticalLayout_3.addWidget(self.title_frame)

        self.coust_name = QWidget(self.cardbody_frame)
        self.coust_name.setObjectName(u"coust_name")
        self.coust_name.setFont(font5)
        self.horizontalLayout_8 = QHBoxLayout(self.coust_name)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_coustomer = QLabel(self.coust_name)
        self.label_coustomer.setObjectName(u"label_coustomer")
        self.label_coustomer.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_coustomer)

        self.label_coustomername = QLabel(self.coust_name)
        self.label_coustomername.setObjectName(u"label_coustomername")
        self.label_coustomername.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_coustomername)


        self.verticalLayout_3.addWidget(self.coust_name)

        self.total = QWidget(self.cardbody_frame)
        self.total.setObjectName(u"total")
        self.total.setFont(font5)
        self.horizontalLayout_9 = QHBoxLayout(self.total)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_total = QLabel(self.total)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_total)

        self.label_price = QLabel(self.total)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setFont(font5)

        self.horizontalLayout_9.addWidget(self.label_price)


        self.verticalLayout_3.addWidget(self.total)

        self.date = QWidget(self.cardbody_frame)
        self.date.setObjectName(u"date")
        self.date.setFont(font5)
        self.horizontalLayout_10 = QHBoxLayout(self.date)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_date = QLabel(self.date)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_date)

        self.label_billdate = QLabel(self.date)
        self.label_billdate.setObjectName(u"label_billdate")
        self.label_billdate.setFont(font5)

        self.horizontalLayout_10.addWidget(self.label_billdate)


        self.verticalLayout_3.addWidget(self.date)

        self.id = QWidget(self.cardbody_frame)
        self.id.setObjectName(u"id")
        self.id.setFont(font5)
        self.horizontalLayout_11 = QHBoxLayout(self.id)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_billid = QLabel(self.id)
        self.label_billid.setObjectName(u"label_billid")
        self.label_billid.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_billid)

        self.label_id = QLabel(self.id)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setFont(font5)

        self.horizontalLayout_11.addWidget(self.label_id)


        self.verticalLayout_3.addWidget(self.id)

        self.goto_btn = QWidget(self.cardbody_frame)
        self.goto_btn.setObjectName(u"goto_btn")
        self.verticalLayout_7 = QVBoxLayout(self.goto_btn)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.arrow_btn = QPushButton(self.goto_btn)
        self.arrow_btn.setObjectName(u"arrow_btn")
        icon6 = QIcon()
        icon6.addFile(u":/icons/arrow-right-solid.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_btn.setIcon(icon6)
        self.arrow_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.arrow_btn, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.goto_btn)


        self.verticalLayout_2.addWidget(self.cardbody_frame)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.body_frame)
        self.card2.setObjectName(u"card2")
        self.card2.setStyleSheet(u"")
        self.card2.setFrameShape(QFrame.StyledPanel)
        self.card2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.card2)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.cardbody_frame_2 = QFrame(self.card2)
        self.cardbody_frame_2.setObjectName(u"cardbody_frame_2")
        self.cardbody_frame_2.setFrameShape(QFrame.StyledPanel)
        self.cardbody_frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.cardbody_frame_2)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.title_frame_5 = QFrame(self.cardbody_frame_2)
        self.title_frame_5.setObjectName(u"title_frame_5")
        self.title_frame_5.setFrameShape(QFrame.StyledPanel)
        self.title_frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.title_frame_5)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_name_5 = QLabel(self.title_frame_5)
        self.label_name_5.setObjectName(u"label_name_5")
        self.label_name_5.setFont(font8)
        self.label_name_5.setScaledContents(True)
        self.label_name_5.setAlignment(Qt.AlignCenter)
        self.label_name_5.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_name_5)


        self.verticalLayout_9.addWidget(self.title_frame_5)

        self.coust_name_5 = QWidget(self.cardbody_frame_2)
        self.coust_name_5.setObjectName(u"coust_name_5")
        self.coust_name_5.setFont(font5)
        self.horizontalLayout_24 = QHBoxLayout(self.coust_name_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_coustomer_5 = QLabel(self.coust_name_5)
        self.label_coustomer_5.setObjectName(u"label_coustomer_5")
        self.label_coustomer_5.setFont(font5)

        self.horizontalLayout_24.addWidget(self.label_coustomer_5)

        self.label_coustomername_5 = QLabel(self.coust_name_5)
        self.label_coustomername_5.setObjectName(u"label_coustomername_5")
        self.label_coustomername_5.setFont(font5)

        self.horizontalLayout_24.addWidget(self.label_coustomername_5)


        self.verticalLayout_9.addWidget(self.coust_name_5)

        self.total_5 = QWidget(self.cardbody_frame_2)
        self.total_5.setObjectName(u"total_5")
        self.total_5.setFont(font5)
        self.horizontalLayout_25 = QHBoxLayout(self.total_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_total_5 = QLabel(self.total_5)
        self.label_total_5.setObjectName(u"label_total_5")
        self.label_total_5.setFont(font5)

        self.horizontalLayout_25.addWidget(self.label_total_5)

        self.label_price_5 = QLabel(self.total_5)
        self.label_price_5.setObjectName(u"label_price_5")
        self.label_price_5.setFont(font5)

        self.horizontalLayout_25.addWidget(self.label_price_5)


        self.verticalLayout_9.addWidget(self.total_5)

        self.date_5 = QWidget(self.cardbody_frame_2)
        self.date_5.setObjectName(u"date_5")
        self.date_5.setFont(font5)
        self.horizontalLayout_26 = QHBoxLayout(self.date_5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_date_5 = QLabel(self.date_5)
        self.label_date_5.setObjectName(u"label_date_5")
        self.label_date_5.setFont(font5)

        self.horizontalLayout_26.addWidget(self.label_date_5)

        self.label_billdate_5 = QLabel(self.date_5)
        self.label_billdate_5.setObjectName(u"label_billdate_5")
        self.label_billdate_5.setFont(font5)

        self.horizontalLayout_26.addWidget(self.label_billdate_5)


        self.verticalLayout_9.addWidget(self.date_5)

        self.id_5 = QWidget(self.cardbody_frame_2)
        self.id_5.setObjectName(u"id_5")
        self.id_5.setFont(font5)
        self.horizontalLayout_27 = QHBoxLayout(self.id_5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_billid_5 = QLabel(self.id_5)
        self.label_billid_5.setObjectName(u"label_billid_5")
        self.label_billid_5.setFont(font5)

        self.horizontalLayout_27.addWidget(self.label_billid_5)

        self.label_id_5 = QLabel(self.id_5)
        self.label_id_5.setObjectName(u"label_id_5")
        self.label_id_5.setFont(font5)

        self.horizontalLayout_27.addWidget(self.label_id_5)


        self.verticalLayout_9.addWidget(self.id_5)

        self.goto_btn_2 = QWidget(self.cardbody_frame_2)
        self.goto_btn_2.setObjectName(u"goto_btn_2")
        self.verticalLayout_11 = QVBoxLayout(self.goto_btn_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.arrow_btn_2 = QPushButton(self.goto_btn_2)
        self.arrow_btn_2.setObjectName(u"arrow_btn_2")
        self.arrow_btn_2.setIcon(icon6)
        self.arrow_btn_2.setFlat(True)

        self.verticalLayout_11.addWidget(self.arrow_btn_2, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.goto_btn_2)


        self.verticalLayout_18.addWidget(self.cardbody_frame_2)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.body_frame)
        self.card3.setObjectName(u"card3")
        self.card3.setStyleSheet(u"")
        self.card3.setFrameShape(QFrame.StyledPanel)
        self.card3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.card3)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.cardbody_frame_3 = QFrame(self.card3)
        self.cardbody_frame_3.setObjectName(u"cardbody_frame_3")
        self.cardbody_frame_3.setFrameShape(QFrame.StyledPanel)
        self.cardbody_frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.cardbody_frame_3)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.title_frame_6 = QFrame(self.cardbody_frame_3)
        self.title_frame_6.setObjectName(u"title_frame_6")
        self.title_frame_6.setFrameShape(QFrame.StyledPanel)
        self.title_frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.title_frame_6)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.label_name_6 = QLabel(self.title_frame_6)
        self.label_name_6.setObjectName(u"label_name_6")
        self.label_name_6.setFont(font8)
        self.label_name_6.setScaledContents(True)
        self.label_name_6.setAlignment(Qt.AlignCenter)
        self.label_name_6.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_name_6)


        self.verticalLayout_12.addWidget(self.title_frame_6)

        self.coust_name_6 = QWidget(self.cardbody_frame_3)
        self.coust_name_6.setObjectName(u"coust_name_6")
        self.coust_name_6.setFont(font5)
        self.horizontalLayout_28 = QHBoxLayout(self.coust_name_6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_coustomer_6 = QLabel(self.coust_name_6)
        self.label_coustomer_6.setObjectName(u"label_coustomer_6")
        self.label_coustomer_6.setFont(font5)

        self.horizontalLayout_28.addWidget(self.label_coustomer_6)

        self.label_coustomername_6 = QLabel(self.coust_name_6)
        self.label_coustomername_6.setObjectName(u"label_coustomername_6")
        self.label_coustomername_6.setFont(font5)

        self.horizontalLayout_28.addWidget(self.label_coustomername_6)


        self.verticalLayout_12.addWidget(self.coust_name_6)

        self.total_6 = QWidget(self.cardbody_frame_3)
        self.total_6.setObjectName(u"total_6")
        self.total_6.setFont(font5)
        self.horizontalLayout_29 = QHBoxLayout(self.total_6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_total_6 = QLabel(self.total_6)
        self.label_total_6.setObjectName(u"label_total_6")
        self.label_total_6.setFont(font5)

        self.horizontalLayout_29.addWidget(self.label_total_6)

        self.label_price_6 = QLabel(self.total_6)
        self.label_price_6.setObjectName(u"label_price_6")
        self.label_price_6.setFont(font5)

        self.horizontalLayout_29.addWidget(self.label_price_6)


        self.verticalLayout_12.addWidget(self.total_6)

        self.date_6 = QWidget(self.cardbody_frame_3)
        self.date_6.setObjectName(u"date_6")
        self.date_6.setFont(font5)
        self.horizontalLayout_30 = QHBoxLayout(self.date_6)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_date_6 = QLabel(self.date_6)
        self.label_date_6.setObjectName(u"label_date_6")
        self.label_date_6.setFont(font5)

        self.horizontalLayout_30.addWidget(self.label_date_6)

        self.label_billdate_6 = QLabel(self.date_6)
        self.label_billdate_6.setObjectName(u"label_billdate_6")
        self.label_billdate_6.setFont(font5)

        self.horizontalLayout_30.addWidget(self.label_billdate_6)


        self.verticalLayout_12.addWidget(self.date_6)

        self.id_6 = QWidget(self.cardbody_frame_3)
        self.id_6.setObjectName(u"id_6")
        self.id_6.setFont(font5)
        self.horizontalLayout_31 = QHBoxLayout(self.id_6)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_billid_6 = QLabel(self.id_6)
        self.label_billid_6.setObjectName(u"label_billid_6")
        self.label_billid_6.setFont(font5)

        self.horizontalLayout_31.addWidget(self.label_billid_6)

        self.label_id_6 = QLabel(self.id_6)
        self.label_id_6.setObjectName(u"label_id_6")
        self.label_id_6.setFont(font5)

        self.horizontalLayout_31.addWidget(self.label_id_6)


        self.verticalLayout_12.addWidget(self.id_6)

        self.goto_btn_3 = QWidget(self.cardbody_frame_3)
        self.goto_btn_3.setObjectName(u"goto_btn_3")
        self.verticalLayout_14 = QVBoxLayout(self.goto_btn_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.arrow_btn_3 = QPushButton(self.goto_btn_3)
        self.arrow_btn_3.setObjectName(u"arrow_btn_3")
        self.arrow_btn_3.setIcon(icon6)
        self.arrow_btn_3.setFlat(True)

        self.verticalLayout_14.addWidget(self.arrow_btn_3, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.goto_btn_3)


        self.verticalLayout_19.addWidget(self.cardbody_frame_3)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.body_frame)
        self.card4.setObjectName(u"card4")
        self.card4.setStyleSheet(u"")
        self.card4.setFrameShape(QFrame.StyledPanel)
        self.card4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_20 = QVBoxLayout(self.card4)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.cardbody_frame_4 = QFrame(self.card4)
        self.cardbody_frame_4.setObjectName(u"cardbody_frame_4")
        self.cardbody_frame_4.setFrameShape(QFrame.StyledPanel)
        self.cardbody_frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.cardbody_frame_4)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.title_frame_7 = QFrame(self.cardbody_frame_4)
        self.title_frame_7.setObjectName(u"title_frame_7")
        self.title_frame_7.setFrameShape(QFrame.StyledPanel)
        self.title_frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_16 = QVBoxLayout(self.title_frame_7)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_name_7 = QLabel(self.title_frame_7)
        self.label_name_7.setObjectName(u"label_name_7")
        self.label_name_7.setFont(font8)
        self.label_name_7.setScaledContents(True)
        self.label_name_7.setAlignment(Qt.AlignCenter)
        self.label_name_7.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_name_7)


        self.verticalLayout_15.addWidget(self.title_frame_7)

        self.coust_name_7 = QWidget(self.cardbody_frame_4)
        self.coust_name_7.setObjectName(u"coust_name_7")
        self.coust_name_7.setFont(font5)
        self.horizontalLayout_32 = QHBoxLayout(self.coust_name_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_coustomer_7 = QLabel(self.coust_name_7)
        self.label_coustomer_7.setObjectName(u"label_coustomer_7")
        self.label_coustomer_7.setFont(font5)

        self.horizontalLayout_32.addWidget(self.label_coustomer_7)

        self.label_coustomername_7 = QLabel(self.coust_name_7)
        self.label_coustomername_7.setObjectName(u"label_coustomername_7")
        self.label_coustomername_7.setFont(font5)

        self.horizontalLayout_32.addWidget(self.label_coustomername_7)


        self.verticalLayout_15.addWidget(self.coust_name_7)

        self.total_7 = QWidget(self.cardbody_frame_4)
        self.total_7.setObjectName(u"total_7")
        self.total_7.setFont(font5)
        self.horizontalLayout_33 = QHBoxLayout(self.total_7)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_total_7 = QLabel(self.total_7)
        self.label_total_7.setObjectName(u"label_total_7")
        self.label_total_7.setFont(font5)

        self.horizontalLayout_33.addWidget(self.label_total_7)

        self.label_price_7 = QLabel(self.total_7)
        self.label_price_7.setObjectName(u"label_price_7")
        self.label_price_7.setFont(font5)

        self.horizontalLayout_33.addWidget(self.label_price_7)


        self.verticalLayout_15.addWidget(self.total_7)

        self.date_7 = QWidget(self.cardbody_frame_4)
        self.date_7.setObjectName(u"date_7")
        self.date_7.setFont(font5)
        self.horizontalLayout_34 = QHBoxLayout(self.date_7)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_date_7 = QLabel(self.date_7)
        self.label_date_7.setObjectName(u"label_date_7")
        self.label_date_7.setFont(font5)

        self.horizontalLayout_34.addWidget(self.label_date_7)

        self.label_billdate_7 = QLabel(self.date_7)
        self.label_billdate_7.setObjectName(u"label_billdate_7")
        self.label_billdate_7.setFont(font5)

        self.horizontalLayout_34.addWidget(self.label_billdate_7)


        self.verticalLayout_15.addWidget(self.date_7)

        self.id_7 = QWidget(self.cardbody_frame_4)
        self.id_7.setObjectName(u"id_7")
        self.id_7.setFont(font5)
        self.horizontalLayout_35 = QHBoxLayout(self.id_7)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_billid_7 = QLabel(self.id_7)
        self.label_billid_7.setObjectName(u"label_billid_7")
        self.label_billid_7.setFont(font5)

        self.horizontalLayout_35.addWidget(self.label_billid_7)

        self.label_id_7 = QLabel(self.id_7)
        self.label_id_7.setObjectName(u"label_id_7")
        self.label_id_7.setFont(font5)

        self.horizontalLayout_35.addWidget(self.label_id_7)


        self.verticalLayout_15.addWidget(self.id_7)

        self.goto_btn_4 = QWidget(self.cardbody_frame_4)
        self.goto_btn_4.setObjectName(u"goto_btn_4")
        self.verticalLayout_17 = QVBoxLayout(self.goto_btn_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.arrow_btn_4 = QPushButton(self.goto_btn_4)
        self.arrow_btn_4.setObjectName(u"arrow_btn_4")
        self.arrow_btn_4.setIcon(icon6)
        self.arrow_btn_4.setFlat(True)

        self.verticalLayout_17.addWidget(self.arrow_btn_4, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.goto_btn_4)


        self.verticalLayout_20.addWidget(self.cardbody_frame_4)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout.addWidget(self.body_frame)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 898, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.profile_btn.setDefault(False)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_menu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.newbill_btn.setText(QCoreApplication.translate("MainWindow", u" New Bill", None))
        self.statistics_btn.setText(QCoreApplication.translate("MainWindow", u" Statistics", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u" LogOut", None))
        self.menu_btn.setText("")
        self.label_appname.setText(QCoreApplication.translate("MainWindow", u"PyBill", None))
        self.label_dashboard.setText(QCoreApplication.translate("MainWindow", u"DashBoard", None))
        self.profile_btn.setText("")
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.label_recentbill.setText(QCoreApplication.translate("MainWindow", u"Recent Bills:", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer.setText(QCoreApplication.translate("MainWindow", u"Coustomer: ", None))
        self.label_coustomername.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn.setText("")
        self.label_name_5.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_5.setText(QCoreApplication.translate("MainWindow", u"Coustomer: ", None))
        self.label_coustomername_5.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_5.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_5.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_5.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_5.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_5.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_2.setText("")
        self.label_name_6.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_6.setText(QCoreApplication.translate("MainWindow", u"Coustomer: ", None))
        self.label_coustomername_6.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_6.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_6.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_6.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_6.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_6.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_6.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_3.setText("")
        self.label_name_7.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_7.setText(QCoreApplication.translate("MainWindow", u"Coustomer: ", None))
        self.label_coustomername_7.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_7.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_7.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_7.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_7.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_7.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_7.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_4.setText("")
    # retranslateUi

