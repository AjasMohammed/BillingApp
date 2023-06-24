# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardDWkMhN.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu, QPushButton

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1016, 712)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font = QFont()
        font.setFamily(u"Adobe Ming Std")
        font.setBold(False)
        font.setWeight(50)
        self.centralwidget.setFont(font)
        self.centralwidget.setStyleSheet(u"*{\n"
"	color: #000;\n"
"	border: none;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #eff9fe;\n"
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
"#mid_card1, #mid_card2, #mid_card3{\n"
"	background-color: #fefeff;\n"
"	border-radius: 20px;\n"
"}")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.menu_side = QCustomSlideMenu(self.centralwidget)
        self.menu_side.setObjectName(u"menu_side")
        self.menu_side.setMinimumSize(QSize(230, 0))
        self.menu_side.setMaximumSize(QSize(230, 16777215))
        self.menu_side.setAutoFillBackground(False)
        self.menu_side.setStyleSheet(u"background-color:#004cff;")
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
        font1 = QFont()
        font1.setPointSize(15)
        font1.setBold(True)
        font1.setWeight(75)
        self.label_menu.setFont(font1)
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
        font2 = QFont()
        font2.setPointSize(8)
        self.frame_menuitems.setFont(font2)
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
        font3 = QFont()
        font3.setPointSize(12)
        self.dashboard_btn.setFont(font3)
        self.dashboard_btn.setStyleSheet(u"	background-color: #fefeff;\n"
"	padding: 10px 5px;\n"
"	text-align: left;\n"
"	border-top-left-radius: 18px ;\n"
"	border-bottom-left-radius: 18px;\n"
"")
        icon = QIcon()
        icon.addFile(u":/blueicons/icons/blue_icons/home.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.dashboard_btn.setIcon(icon)
        self.dashboard_btn.setIconSize(QSize(20, 20))
        self.dashboard_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.dashboard_btn)

        self.newbill_btn = QPushButton(self.frame_menubtns)
        self.newbill_btn.setObjectName(u"newbill_btn")
        self.newbill_btn.setFont(font3)
        self.newbill_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;\n"
"")
        icon1 = QIcon()
        icon1.addFile(u":/whiteicons/icons/white_icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newbill_btn.setIcon(icon1)
        self.newbill_btn.setIconSize(QSize(20, 20))
        self.newbill_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.newbill_btn)

        self.statistics_btn = QPushButton(self.frame_menubtns)
        self.statistics_btn.setObjectName(u"statistics_btn")
        self.statistics_btn.setFont(font3)
        self.statistics_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;")
        icon2 = QIcon()
        icon2.addFile(u":/whiteicons/icons/white_icons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statistics_btn.setIcon(icon2)
        self.statistics_btn.setIconSize(QSize(20, 20))
        self.statistics_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.statistics_btn)

        self.logout_btn = QPushButton(self.frame_menubtns)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setFont(font3)
        self.logout_btn.setStyleSheet(u"	padding: 10px 5px;\n"
"	text-align: left;")
        icon3 = QIcon()
        icon3.addFile(u":/whiteicons/icons/white_icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.horizontalLayout_6.setContentsMargins(10, 9, 0, 70)
        self.menu_btn = QPushButton(self.menu)
        self.menu_btn.setObjectName(u"menu_btn")
        icon4 = QIcon()
        icon4.addFile(u":/blueicons/icons/blue_icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QSize(32, 32))
        self.menu_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.menu_btn)

        self.label_appname = QLabel(self.menu)
        self.label_appname.setObjectName(u"label_appname")
        font4 = QFont()
        font4.setFamily(u"Adobe Ming Std L")
        font4.setPointSize(15)
        font4.setBold(True)
        font4.setWeight(75)
        self.label_appname.setFont(font4)

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
        font5 = QFont()
        font5.setFamily(u"Adobe Ming Std L")
        font5.setPointSize(28)
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setWeight(75)
        self.label_dashboard.setFont(font5)
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
        icon5.addFile(u":/blueicons/icons/blue_icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
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
        self.label_username.setFont(font3)
        self.label_username.setFrameShape(QFrame.NoFrame)
        self.label_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_username)


        self.verticalLayout_22.addWidget(self.username)


        self.horizontalLayout_2.addWidget(self.profile_frame, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.header_frame, 0, Qt.AlignTop)

        self.body_frame = QStackedWidget(self.mainbody)
        self.body_frame.setObjectName(u"body_frame")
        self.body_framePage1 = QWidget()
        self.body_framePage1.setObjectName(u"body_framePage1")
        self.verticalLayout_32 = QVBoxLayout(self.body_framePage1)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.middle_farme = QWidget(self.body_framePage1)
        self.middle_farme.setObjectName(u"middle_farme")
        self.horizontalLayout_13 = QHBoxLayout(self.middle_farme)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.mid_card1 = QWidget(self.middle_farme)
        self.mid_card1.setObjectName(u"mid_card1")
        self.verticalLayout_31 = QVBoxLayout(self.mid_card1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_today_title = QFrame(self.mid_card1)
        self.frame_today_title.setObjectName(u"frame_today_title")
        self.frame_today_title.setFrameShape(QFrame.StyledPanel)
        self.frame_today_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_today_title)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.card_today_label = QLabel(self.frame_today_title)
        self.card_today_label.setObjectName(u"card_today_label")
        font6 = QFont()
        font6.setPointSize(12)
        font6.setBold(False)
        font6.setWeight(50)
        self.card_today_label.setFont(font6)
        self.card_today_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_20.addWidget(self.card_today_label)


        self.verticalLayout_31.addWidget(self.frame_today_title)

        self.frame_today_body = QFrame(self.mid_card1)
        self.frame_today_body.setObjectName(u"frame_today_body")
        self.frame_today_body.setFrameShape(QFrame.StyledPanel)
        self.frame_today_body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_today_body)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.no_today = QWidget(self.frame_today_body)
        self.no_today.setObjectName(u"no_today")
        self.horizontalLayout_21 = QHBoxLayout(self.no_today)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.no_today_label = QLabel(self.no_today)
        self.no_today_label.setObjectName(u"no_today_label")
        font7 = QFont()
        font7.setPointSize(10)
        self.no_today_label.setFont(font7)
        self.no_today_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.no_today_label)

        self.no_label_1 = QLabel(self.no_today)
        self.no_label_1.setObjectName(u"no_label_1")
        self.no_label_1.setFont(font7)
        self.no_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_21.addWidget(self.no_label_1)


        self.verticalLayout_29.addWidget(self.no_today)

        self.today_total = QWidget(self.frame_today_body)
        self.today_total.setObjectName(u"today_total")
        self.horizontalLayout_22 = QHBoxLayout(self.today_total)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.today_total_label = QLabel(self.today_total)
        self.today_total_label.setObjectName(u"today_total_label")
        self.today_total_label.setFont(font7)
        self.today_total_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.today_total_label)

        self.total_label_1 = QLabel(self.today_total)
        self.total_label_1.setObjectName(u"total_label_1")
        self.total_label_1.setFont(font7)
        self.total_label_1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_22.addWidget(self.total_label_1)


        self.verticalLayout_29.addWidget(self.today_total)


        self.verticalLayout_31.addWidget(self.frame_today_body)


        self.horizontalLayout_13.addWidget(self.mid_card1)

        self.mid_card2 = QWidget(self.middle_farme)
        self.mid_card2.setObjectName(u"mid_card2")
        self.verticalLayout_5 = QVBoxLayout(self.mid_card2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_weektitle = QFrame(self.mid_card2)
        self.frame_weektitle.setObjectName(u"frame_weektitle")
        self.frame_weektitle.setFrameShape(QFrame.StyledPanel)
        self.frame_weektitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_weektitle)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.card_week_label = QLabel(self.frame_weektitle)
        self.card_week_label.setObjectName(u"card_week_label")
        font8 = QFont()
        font8.setPointSize(12)
        font8.setBold(False)
        font8.setUnderline(False)
        font8.setWeight(50)
        self.card_week_label.setFont(font8)
        self.card_week_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_14.addWidget(self.card_week_label)


        self.verticalLayout_5.addWidget(self.frame_weektitle)

        self.frame_weekbody = QFrame(self.mid_card2)
        self.frame_weekbody.setObjectName(u"frame_weekbody")
        self.frame_weekbody.setFrameShape(QFrame.StyledPanel)
        self.frame_weekbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_6 = QVBoxLayout(self.frame_weekbody)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.no_week = QWidget(self.frame_weekbody)
        self.no_week.setObjectName(u"no_week")
        self.horizontalLayout_15 = QHBoxLayout(self.no_week)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.no_week_label = QLabel(self.no_week)
        self.no_week_label.setObjectName(u"no_week_label")
        self.no_week_label.setFont(font7)
        self.no_week_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.no_week_label)

        self.no_label_2 = QLabel(self.no_week)
        self.no_label_2.setObjectName(u"no_label_2")
        self.no_label_2.setFont(font7)
        self.no_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_15.addWidget(self.no_label_2)


        self.verticalLayout_6.addWidget(self.no_week)

        self.week_total = QWidget(self.frame_weekbody)
        self.week_total.setObjectName(u"week_total")
        self.horizontalLayout_16 = QHBoxLayout(self.week_total)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.week_total_label = QLabel(self.week_total)
        self.week_total_label.setObjectName(u"week_total_label")
        self.week_total_label.setFont(font7)
        self.week_total_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.week_total_label)

        self.total_label_2 = QLabel(self.week_total)
        self.total_label_2.setObjectName(u"total_label_2")
        self.total_label_2.setFont(font7)
        self.total_label_2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_16.addWidget(self.total_label_2)


        self.verticalLayout_6.addWidget(self.week_total)


        self.verticalLayout_5.addWidget(self.frame_weekbody)


        self.horizontalLayout_13.addWidget(self.mid_card2)

        self.mid_card3 = QWidget(self.middle_farme)
        self.mid_card3.setObjectName(u"mid_card3")
        self.verticalLayout_30 = QVBoxLayout(self.mid_card3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_monthtitle = QFrame(self.mid_card3)
        self.frame_monthtitle.setObjectName(u"frame_monthtitle")
        self.frame_monthtitle.setFrameShape(QFrame.StyledPanel)
        self.frame_monthtitle.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_monthtitle)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.card_month_label = QLabel(self.frame_monthtitle)
        self.card_month_label.setObjectName(u"card_month_label")
        self.card_month_label.setFont(font6)
        self.card_month_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_17.addWidget(self.card_month_label)


        self.verticalLayout_30.addWidget(self.frame_monthtitle)

        self.frame_monthbody = QFrame(self.mid_card3)
        self.frame_monthbody.setObjectName(u"frame_monthbody")
        self.frame_monthbody.setFrameShape(QFrame.StyledPanel)
        self.frame_monthbody.setFrameShadow(QFrame.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_monthbody)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.no_month = QWidget(self.frame_monthbody)
        self.no_month.setObjectName(u"no_month")
        self.horizontalLayout_18 = QHBoxLayout(self.no_month)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.no_month_label = QLabel(self.no_month)
        self.no_month_label.setObjectName(u"no_month_label")
        self.no_month_label.setFont(font7)
        self.no_month_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.no_month_label)

        self.no_label_3 = QLabel(self.no_month)
        self.no_label_3.setObjectName(u"no_label_3")
        self.no_label_3.setFont(font7)
        self.no_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_18.addWidget(self.no_label_3)


        self.verticalLayout_21.addWidget(self.no_month)

        self.month_total = QWidget(self.frame_monthbody)
        self.month_total.setObjectName(u"month_total")
        self.horizontalLayout_19 = QHBoxLayout(self.month_total)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.month_total_label = QLabel(self.month_total)
        self.month_total_label.setObjectName(u"month_total_label")
        self.month_total_label.setFont(font7)
        self.month_total_label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.month_total_label)

        self.total_label_3 = QLabel(self.month_total)
        self.total_label_3.setObjectName(u"total_label_3")
        self.total_label_3.setFont(font7)
        self.total_label_3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_19.addWidget(self.total_label_3)


        self.verticalLayout_21.addWidget(self.month_total)


        self.verticalLayout_30.addWidget(self.frame_monthbody)


        self.horizontalLayout_13.addWidget(self.mid_card3)


        self.verticalLayout_32.addWidget(self.middle_farme)

        self.body_frame_2 = QWidget(self.body_framePage1)
        self.body_frame_2.setObjectName(u"body_frame_2")
        self.body_frame_2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.body_frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.recent_title_frame = QWidget(self.body_frame_2)
        self.recent_title_frame.setObjectName(u"recent_title_frame")
        self.recent_title_frame.setFont(font7)
        self.recent_title_frame.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.horizontalLayout_12 = QHBoxLayout(self.recent_title_frame)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_recentbill = QLabel(self.recent_title_frame)
        self.label_recentbill.setObjectName(u"label_recentbill")
        font9 = QFont()
        font9.setPointSize(15)
        self.label_recentbill.setFont(font9)

        self.horizontalLayout_12.addWidget(self.label_recentbill)

        self.more_btn = QPushButton(self.recent_title_frame)
        self.more_btn.setObjectName(u"more_btn")
        self.more_btn.setFont(font3)
        self.more_btn.setLayoutDirection(Qt.RightToLeft)
        icon6 = QIcon()
        icon6.addFile(u":/blueicons/icons/blue_icons/arrow-right-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.more_btn.setIcon(icon6)
        self.more_btn.setIconSize(QSize(25, 20))
        self.more_btn.setFlat(True)

        self.horizontalLayout_12.addWidget(self.more_btn, 0, Qt.AlignLeft)


        self.verticalLayout_4.addWidget(self.recent_title_frame)

        self.card_frame = QWidget(self.body_frame_2)
        self.card_frame.setObjectName(u"card_frame")
        font10 = QFont()
        font10.setUnderline(False)
        self.card_frame.setFont(font10)
        self.card_frame.setStyleSheet(u"")
        self.horizontalLayout_7 = QHBoxLayout(self.card_frame)
        self.horizontalLayout_7.setSpacing(20)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(10, 10, 10, 10)
        self.card1 = QFrame(self.card_frame)
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
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setUnderline(True)
        font11.setWeight(50)
        font11.setStrikeOut(False)
        self.label_name.setFont(font11)
        self.label_name.setScaledContents(True)
        self.label_name.setAlignment(Qt.AlignCenter)
        self.label_name.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_name)


        self.verticalLayout_3.addWidget(self.title_frame)

        self.coust_name = QWidget(self.cardbody_frame)
        self.coust_name.setObjectName(u"coust_name")
        self.coust_name.setFont(font7)
        self.horizontalLayout_8 = QHBoxLayout(self.coust_name)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_coustomer = QLabel(self.coust_name)
        self.label_coustomer.setObjectName(u"label_coustomer")
        self.label_coustomer.setFont(font7)
        self.label_coustomer.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_coustomer)

        self.label_coustomername = QLabel(self.coust_name)
        self.label_coustomername.setObjectName(u"label_coustomername")
        self.label_coustomername.setFont(font7)
        self.label_coustomername.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_coustomername)


        self.verticalLayout_3.addWidget(self.coust_name)

        self.total = QWidget(self.cardbody_frame)
        self.total.setObjectName(u"total")
        self.total.setFont(font7)
        self.horizontalLayout_9 = QHBoxLayout(self.total)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label_total = QLabel(self.total)
        self.label_total.setObjectName(u"label_total")
        self.label_total.setFont(font7)
        self.label_total.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_total)

        self.label_price = QLabel(self.total)
        self.label_price.setObjectName(u"label_price")
        self.label_price.setFont(font7)
        self.label_price.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_price)


        self.verticalLayout_3.addWidget(self.total)

        self.date = QWidget(self.cardbody_frame)
        self.date.setObjectName(u"date")
        self.date.setFont(font7)
        self.horizontalLayout_10 = QHBoxLayout(self.date)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_date = QLabel(self.date)
        self.label_date.setObjectName(u"label_date")
        self.label_date.setFont(font7)
        self.label_date.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_date)

        self.label_billdate = QLabel(self.date)
        self.label_billdate.setObjectName(u"label_billdate")
        self.label_billdate.setFont(font7)
        self.label_billdate.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_billdate)


        self.verticalLayout_3.addWidget(self.date)

        self.id = QWidget(self.cardbody_frame)
        self.id.setObjectName(u"id")
        self.id.setFont(font7)
        self.horizontalLayout_11 = QHBoxLayout(self.id)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.label_billid = QLabel(self.id)
        self.label_billid.setObjectName(u"label_billid")
        self.label_billid.setFont(font7)
        self.label_billid.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_billid)

        self.label_id = QLabel(self.id)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setFont(font7)
        self.label_id.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_id)


        self.verticalLayout_3.addWidget(self.id)

        self.goto_btn = QWidget(self.cardbody_frame)
        self.goto_btn.setObjectName(u"goto_btn")
        self.verticalLayout_7 = QVBoxLayout(self.goto_btn)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.arrow_btn = QPushButton(self.goto_btn)
        self.arrow_btn.setObjectName(u"arrow_btn")
        icon7 = QIcon()
        icon7.addFile(u":/blueicons/icons/blue_icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_btn.setIcon(icon7)
        self.arrow_btn.setIconSize(QSize(35, 16))
        self.arrow_btn.setFlat(True)

        self.verticalLayout_7.addWidget(self.arrow_btn, 0, Qt.AlignRight)


        self.verticalLayout_3.addWidget(self.goto_btn)


        self.verticalLayout_2.addWidget(self.cardbody_frame)


        self.horizontalLayout_7.addWidget(self.card1)

        self.card2 = QFrame(self.card_frame)
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
        self.label_name_5.setFont(font11)
        self.label_name_5.setScaledContents(True)
        self.label_name_5.setAlignment(Qt.AlignCenter)
        self.label_name_5.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_name_5)


        self.verticalLayout_9.addWidget(self.title_frame_5)

        self.coust_name_5 = QWidget(self.cardbody_frame_2)
        self.coust_name_5.setObjectName(u"coust_name_5")
        self.coust_name_5.setFont(font7)
        self.horizontalLayout_24 = QHBoxLayout(self.coust_name_5)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.label_coustomer_5 = QLabel(self.coust_name_5)
        self.label_coustomer_5.setObjectName(u"label_coustomer_5")
        self.label_coustomer_5.setFont(font7)
        self.label_coustomer_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_coustomer_5)

        self.label_coustomername_5 = QLabel(self.coust_name_5)
        self.label_coustomername_5.setObjectName(u"label_coustomername_5")
        self.label_coustomername_5.setFont(font7)
        self.label_coustomername_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_coustomername_5)


        self.verticalLayout_9.addWidget(self.coust_name_5)

        self.total_5 = QWidget(self.cardbody_frame_2)
        self.total_5.setObjectName(u"total_5")
        self.total_5.setFont(font7)
        self.horizontalLayout_25 = QHBoxLayout(self.total_5)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.label_total_5 = QLabel(self.total_5)
        self.label_total_5.setObjectName(u"label_total_5")
        self.label_total_5.setFont(font7)
        self.label_total_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_total_5)

        self.label_price_5 = QLabel(self.total_5)
        self.label_price_5.setObjectName(u"label_price_5")
        self.label_price_5.setFont(font7)
        self.label_price_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_price_5)


        self.verticalLayout_9.addWidget(self.total_5)

        self.date_5 = QWidget(self.cardbody_frame_2)
        self.date_5.setObjectName(u"date_5")
        self.date_5.setFont(font7)
        self.horizontalLayout_26 = QHBoxLayout(self.date_5)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.label_date_5 = QLabel(self.date_5)
        self.label_date_5.setObjectName(u"label_date_5")
        self.label_date_5.setFont(font7)
        self.label_date_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_date_5)

        self.label_billdate_5 = QLabel(self.date_5)
        self.label_billdate_5.setObjectName(u"label_billdate_5")
        self.label_billdate_5.setFont(font7)
        self.label_billdate_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_billdate_5)


        self.verticalLayout_9.addWidget(self.date_5)

        self.id_5 = QWidget(self.cardbody_frame_2)
        self.id_5.setObjectName(u"id_5")
        self.id_5.setFont(font7)
        self.horizontalLayout_27 = QHBoxLayout(self.id_5)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_billid_5 = QLabel(self.id_5)
        self.label_billid_5.setObjectName(u"label_billid_5")
        self.label_billid_5.setFont(font7)
        self.label_billid_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_billid_5)

        self.label_id_5 = QLabel(self.id_5)
        self.label_id_5.setObjectName(u"label_id_5")
        self.label_id_5.setFont(font7)
        self.label_id_5.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_id_5)


        self.verticalLayout_9.addWidget(self.id_5)

        self.goto_btn_2 = QWidget(self.cardbody_frame_2)
        self.goto_btn_2.setObjectName(u"goto_btn_2")
        self.verticalLayout_11 = QVBoxLayout(self.goto_btn_2)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.arrow_btn_2 = QPushButton(self.goto_btn_2)
        self.arrow_btn_2.setObjectName(u"arrow_btn_2")
        self.arrow_btn_2.setIcon(icon7)
        self.arrow_btn_2.setIconSize(QSize(35, 16))
        self.arrow_btn_2.setFlat(True)

        self.verticalLayout_11.addWidget(self.arrow_btn_2, 0, Qt.AlignRight)


        self.verticalLayout_9.addWidget(self.goto_btn_2)


        self.verticalLayout_18.addWidget(self.cardbody_frame_2)


        self.horizontalLayout_7.addWidget(self.card2)

        self.card3 = QFrame(self.card_frame)
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
        self.label_name_6.setFont(font11)
        self.label_name_6.setScaledContents(True)
        self.label_name_6.setAlignment(Qt.AlignCenter)
        self.label_name_6.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_name_6)


        self.verticalLayout_12.addWidget(self.title_frame_6)

        self.coust_name_6 = QWidget(self.cardbody_frame_3)
        self.coust_name_6.setObjectName(u"coust_name_6")
        self.coust_name_6.setFont(font7)
        self.horizontalLayout_28 = QHBoxLayout(self.coust_name_6)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.label_coustomer_6 = QLabel(self.coust_name_6)
        self.label_coustomer_6.setObjectName(u"label_coustomer_6")
        self.label_coustomer_6.setFont(font7)
        self.label_coustomer_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_coustomer_6)

        self.label_coustomername_6 = QLabel(self.coust_name_6)
        self.label_coustomername_6.setObjectName(u"label_coustomername_6")
        self.label_coustomername_6.setFont(font7)
        self.label_coustomername_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_coustomername_6)


        self.verticalLayout_12.addWidget(self.coust_name_6)

        self.total_6 = QWidget(self.cardbody_frame_3)
        self.total_6.setObjectName(u"total_6")
        self.total_6.setFont(font7)
        self.horizontalLayout_29 = QHBoxLayout(self.total_6)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.label_total_6 = QLabel(self.total_6)
        self.label_total_6.setObjectName(u"label_total_6")
        self.label_total_6.setFont(font7)
        self.label_total_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_total_6)

        self.label_price_6 = QLabel(self.total_6)
        self.label_price_6.setObjectName(u"label_price_6")
        self.label_price_6.setFont(font7)
        self.label_price_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_price_6)


        self.verticalLayout_12.addWidget(self.total_6)

        self.date_6 = QWidget(self.cardbody_frame_3)
        self.date_6.setObjectName(u"date_6")
        self.date_6.setFont(font7)
        self.horizontalLayout_30 = QHBoxLayout(self.date_6)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.label_date_6 = QLabel(self.date_6)
        self.label_date_6.setObjectName(u"label_date_6")
        self.label_date_6.setFont(font7)
        self.label_date_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_date_6)

        self.label_billdate_6 = QLabel(self.date_6)
        self.label_billdate_6.setObjectName(u"label_billdate_6")
        self.label_billdate_6.setFont(font7)
        self.label_billdate_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_billdate_6)


        self.verticalLayout_12.addWidget(self.date_6)

        self.id_6 = QWidget(self.cardbody_frame_3)
        self.id_6.setObjectName(u"id_6")
        self.id_6.setFont(font7)
        self.horizontalLayout_31 = QHBoxLayout(self.id_6)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.label_billid_6 = QLabel(self.id_6)
        self.label_billid_6.setObjectName(u"label_billid_6")
        self.label_billid_6.setFont(font7)
        self.label_billid_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_billid_6)

        self.label_id_6 = QLabel(self.id_6)
        self.label_id_6.setObjectName(u"label_id_6")
        self.label_id_6.setFont(font7)
        self.label_id_6.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_id_6)


        self.verticalLayout_12.addWidget(self.id_6)

        self.goto_btn_3 = QWidget(self.cardbody_frame_3)
        self.goto_btn_3.setObjectName(u"goto_btn_3")
        self.verticalLayout_14 = QVBoxLayout(self.goto_btn_3)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.arrow_btn_3 = QPushButton(self.goto_btn_3)
        self.arrow_btn_3.setObjectName(u"arrow_btn_3")
        self.arrow_btn_3.setIcon(icon7)
        self.arrow_btn_3.setIconSize(QSize(35, 16))
        self.arrow_btn_3.setFlat(True)

        self.verticalLayout_14.addWidget(self.arrow_btn_3, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.goto_btn_3)


        self.verticalLayout_19.addWidget(self.cardbody_frame_3)


        self.horizontalLayout_7.addWidget(self.card3)

        self.card4 = QFrame(self.card_frame)
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
        self.label_name_7.setFont(font11)
        self.label_name_7.setScaledContents(True)
        self.label_name_7.setAlignment(Qt.AlignCenter)
        self.label_name_7.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_name_7)


        self.verticalLayout_15.addWidget(self.title_frame_7)

        self.coust_name_7 = QWidget(self.cardbody_frame_4)
        self.coust_name_7.setObjectName(u"coust_name_7")
        self.coust_name_7.setFont(font7)
        self.horizontalLayout_32 = QHBoxLayout(self.coust_name_7)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.label_coustomer_7 = QLabel(self.coust_name_7)
        self.label_coustomer_7.setObjectName(u"label_coustomer_7")
        self.label_coustomer_7.setFont(font7)
        self.label_coustomer_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_coustomer_7)

        self.label_coustomername_7 = QLabel(self.coust_name_7)
        self.label_coustomername_7.setObjectName(u"label_coustomername_7")
        self.label_coustomername_7.setFont(font7)
        self.label_coustomername_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_coustomername_7)


        self.verticalLayout_15.addWidget(self.coust_name_7)

        self.total_7 = QWidget(self.cardbody_frame_4)
        self.total_7.setObjectName(u"total_7")
        self.total_7.setFont(font7)
        self.horizontalLayout_33 = QHBoxLayout(self.total_7)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.label_total_7 = QLabel(self.total_7)
        self.label_total_7.setObjectName(u"label_total_7")
        self.label_total_7.setFont(font7)
        self.label_total_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_total_7)

        self.label_price_7 = QLabel(self.total_7)
        self.label_price_7.setObjectName(u"label_price_7")
        self.label_price_7.setFont(font7)
        self.label_price_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_price_7)


        self.verticalLayout_15.addWidget(self.total_7)

        self.date_7 = QWidget(self.cardbody_frame_4)
        self.date_7.setObjectName(u"date_7")
        self.date_7.setFont(font7)
        self.horizontalLayout_34 = QHBoxLayout(self.date_7)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_date_7 = QLabel(self.date_7)
        self.label_date_7.setObjectName(u"label_date_7")
        self.label_date_7.setFont(font7)
        self.label_date_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_date_7)

        self.label_billdate_7 = QLabel(self.date_7)
        self.label_billdate_7.setObjectName(u"label_billdate_7")
        self.label_billdate_7.setFont(font7)
        self.label_billdate_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_billdate_7)


        self.verticalLayout_15.addWidget(self.date_7)

        self.id_7 = QWidget(self.cardbody_frame_4)
        self.id_7.setObjectName(u"id_7")
        self.id_7.setFont(font7)
        self.horizontalLayout_35 = QHBoxLayout(self.id_7)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.label_billid_7 = QLabel(self.id_7)
        self.label_billid_7.setObjectName(u"label_billid_7")
        self.label_billid_7.setFont(font7)
        self.label_billid_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_billid_7)

        self.label_id_7 = QLabel(self.id_7)
        self.label_id_7.setObjectName(u"label_id_7")
        self.label_id_7.setFont(font7)
        self.label_id_7.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_id_7)


        self.verticalLayout_15.addWidget(self.id_7)

        self.goto_btn_4 = QWidget(self.cardbody_frame_4)
        self.goto_btn_4.setObjectName(u"goto_btn_4")
        self.verticalLayout_17 = QVBoxLayout(self.goto_btn_4)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.arrow_btn_4 = QPushButton(self.goto_btn_4)
        self.arrow_btn_4.setObjectName(u"arrow_btn_4")
        self.arrow_btn_4.setIcon(icon7)
        self.arrow_btn_4.setIconSize(QSize(35, 16))
        self.arrow_btn_4.setFlat(True)

        self.verticalLayout_17.addWidget(self.arrow_btn_4, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.goto_btn_4)


        self.verticalLayout_20.addWidget(self.cardbody_frame_4)


        self.horizontalLayout_7.addWidget(self.card4)


        self.verticalLayout_4.addWidget(self.card_frame)


        self.verticalLayout_32.addWidget(self.body_frame_2)

        self.body_frame.addWidget(self.body_framePage1)
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.body_frame.addWidget(self.page)

        self.verticalLayout.addWidget(self.body_frame)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1016, 21))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.profile_btn.setDefault(False)
        self.body_frame.setCurrentIndex(1)


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
        self.label_appname.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_dashboard.setText(QCoreApplication.translate("MainWindow", u"Py Bill", None))
        self.profile_btn.setText("")
        self.label_username.setText(QCoreApplication.translate("MainWindow", u"username", None))
        self.card_today_label.setText(QCoreApplication.translate("MainWindow", u"Today", None))
        self.no_today_label.setText(QCoreApplication.translate("MainWindow", u"No. of Bills :", None))
        self.no_label_1.setText(QCoreApplication.translate("MainWindow", u"quantity", None))
        self.today_total_label.setText(QCoreApplication.translate("MainWindow", u"Total Amount :", None))
        self.total_label_1.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.card_week_label.setText(QCoreApplication.translate("MainWindow", u"This Week", None))
        self.no_week_label.setText(QCoreApplication.translate("MainWindow", u"No. of Bills :", None))
        self.no_label_2.setText(QCoreApplication.translate("MainWindow", u"quantity", None))
        self.week_total_label.setText(QCoreApplication.translate("MainWindow", u"Total Amount :", None))
        self.total_label_2.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.card_month_label.setText(QCoreApplication.translate("MainWindow", u"This Month", None))
        self.no_month_label.setText(QCoreApplication.translate("MainWindow", u"No. of Bills :", None))
        self.no_label_3.setText(QCoreApplication.translate("MainWindow", u"quantity", None))
        self.month_total_label.setText(QCoreApplication.translate("MainWindow", u"Total Amount :", None))
        self.total_label_3.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.label_recentbill.setText(QCoreApplication.translate("MainWindow", u"Recent Bills:", None))
        self.more_btn.setText(QCoreApplication.translate("MainWindow", u"More  ", None))
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

