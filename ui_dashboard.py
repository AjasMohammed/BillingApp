# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardotgtrJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu
from Custom_Widgets.Widgets import QCustomStackedWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(985, 718)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Adobe Ming Std")
        font1.setBold(False)
        font1.setWeight(50)
        self.centralwidget.setFont(font1)
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
"}\n"
"#dashboard_btn, #logout_btn, #newbill_btn, #statistics_btn{\n"
"padding: 10px 5px;\n"
"text-align: left;\n"
"}\n"
"#customer_name_field, #customer_contact_field, #product_name_field, #product_id_field, #product_qty_field, #product_price_field, #bill_tag_field{\n"
"border-radius:5px;\n"
"}\n"
"#customer_info_frame, #product_info_frame, #bill_view{\n"
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
        font2 = QFont()
        font2.setPointSize(15)
        font2.setBold(True)
        font2.setWeight(75)
        self.label_menu.setFont(font2)
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
        self.frame_menuitems.setFont(font)
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
        self.dashboard_btn.setStyleSheet(u"background-color: #fefeff;\n"
"border-top-left-radius: 18px ;\n"
"border-bottom-left-radius: 18px;\n"
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
        self.newbill_btn.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/whiteicons/icons/white_icons/file-plus.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.newbill_btn.setIcon(icon1)
        self.newbill_btn.setIconSize(QSize(20, 20))
        self.newbill_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.newbill_btn)

        self.statistics_btn = QPushButton(self.frame_menubtns)
        self.statistics_btn.setObjectName(u"statistics_btn")
        self.statistics_btn.setFont(font3)
        self.statistics_btn.setStyleSheet(u"")
        icon2 = QIcon()
        icon2.addFile(u":/whiteicons/icons/white_icons/bar-chart.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.statistics_btn.setIcon(icon2)
        self.statistics_btn.setIconSize(QSize(20, 20))
        self.statistics_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.statistics_btn)

        self.logout_btn = QPushButton(self.frame_menubtns)
        self.logout_btn.setObjectName(u"logout_btn")
        self.logout_btn.setFont(font3)
        self.logout_btn.setStyleSheet(u"")
        icon3 = QIcon()
        icon3.addFile(u":/whiteicons/icons/white_icons/log-out.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.logout_btn.setIcon(icon3)
        self.logout_btn.setIconSize(QSize(20, 20))
        self.logout_btn.setFlat(True)

        self.verticalLayout_27.addWidget(self.logout_btn)


        self.verticalLayout_28.addWidget(self.frame_menubtns, 0, Qt.AlignTop)


        self.verticalLayout_26.addWidget(self.frame_menuitems)


        self.verticalLayout_25.addWidget(self.frame_menu)

        self.verticalSpacer_2 = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_25.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.menu_side)

        self.mainbody = QWidget(self.centralwidget)
        self.mainbody.setObjectName(u"mainbody")
        self.verticalLayout = QVBoxLayout(self.mainbody)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.header_frame = QWidget(self.mainbody)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy1)
        self.header_frame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
        self.menu = QWidget(self.header_frame)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.menu)
        self.horizontalLayout_6.setSpacing(5)
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
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_dashboard = QLabel(self.frame)
        self.label_dashboard.setObjectName(u"label_dashboard")
        self.label_dashboard.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily(u"Adobe Ming Std L")
        font5.setPointSize(28)
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setWeight(75)
        self.label_dashboard.setFont(font5)
        self.label_dashboard.setStyleSheet(u"")
        self.label_dashboard.setScaledContents(False)
        self.label_dashboard.setAlignment(Qt.AlignCenter)
        self.label_dashboard.setMargin(0)

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
        self.profilebtn.setStyleSheet(u"border:1px solid #0000;")
        self.verticalLayout_24 = QVBoxLayout(self.profilebtn)
        self.verticalLayout_24.setSpacing(0)
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.verticalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.profile_btn = QPushButton(self.profilebtn)
        self.profile_btn.setObjectName(u"profile_btn")
        self.profile_btn.setAutoFillBackground(False)
        self.profile_btn.setStyleSheet(u"border:3px solid #004cff;\n"
"border-radius:36px")
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

        self.body_frame = QCustomStackedWidget(self.mainbody)
        self.body_frame.setObjectName(u"body_frame")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_32 = QVBoxLayout(self.dashboard)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.middle_farme = QWidget(self.dashboard)
        self.middle_farme.setObjectName(u"middle_farme")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.middle_farme.sizePolicy().hasHeightForWidth())
        self.middle_farme.setSizePolicy(sizePolicy2)
        self.horizontalLayout_13 = QHBoxLayout(self.middle_farme)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.mid_card1 = QWidget(self.middle_farme)
        self.mid_card1.setObjectName(u"mid_card1")
        sizePolicy2.setHeightForWidth(self.mid_card1.sizePolicy().hasHeightForWidth())
        self.mid_card1.setSizePolicy(sizePolicy2)
        self.verticalLayout_31 = QVBoxLayout(self.mid_card1)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.frame_today_title = QFrame(self.mid_card1)
        self.frame_today_title.setObjectName(u"frame_today_title")
        self.frame_today_title.setMaximumSize(QSize(1000, 60))
        self.frame_today_title.setFrameShape(QFrame.StyledPanel)
        self.frame_today_title.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.frame_today_title)
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(9, 9, 9, 9)
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
        sizePolicy2.setHeightForWidth(self.mid_card2.sizePolicy().hasHeightForWidth())
        self.mid_card2.setSizePolicy(sizePolicy2)
        self.verticalLayout_5 = QVBoxLayout(self.mid_card2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.frame_weektitle = QFrame(self.mid_card2)
        self.frame_weektitle.setObjectName(u"frame_weektitle")
        self.frame_weektitle.setMaximumSize(QSize(16777215, 60))
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
        sizePolicy2.setHeightForWidth(self.mid_card3.sizePolicy().hasHeightForWidth())
        self.mid_card3.setSizePolicy(sizePolicy2)
        self.verticalLayout_30 = QVBoxLayout(self.mid_card3)
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.frame_monthtitle = QFrame(self.mid_card3)
        self.frame_monthtitle.setObjectName(u"frame_monthtitle")
        self.frame_monthtitle.setMaximumSize(QSize(16777215, 60))
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

        self.body_frame_2 = QWidget(self.dashboard)
        self.body_frame_2.setObjectName(u"body_frame_2")
        self.body_frame_2.setLayoutDirection(Qt.LeftToRight)
        self.verticalLayout_4 = QVBoxLayout(self.body_frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 9)
        self.recent_title_frame = QWidget(self.body_frame_2)
        self.recent_title_frame.setObjectName(u"recent_title_frame")
        sizePolicy2.setHeightForWidth(self.recent_title_frame.sizePolicy().hasHeightForWidth())
        self.recent_title_frame.setSizePolicy(sizePolicy2)
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
        sizePolicy1.setHeightForWidth(self.card_frame.sizePolicy().hasHeightForWidth())
        self.card_frame.setSizePolicy(sizePolicy1)
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
        self.verticalLayout_8.setSpacing(0)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_8.setSpacing(0)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_10.setSpacing(0)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_24.setSpacing(0)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_25.setSpacing(0)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_26.setSpacing(0)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_28.setSpacing(0)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_29.setSpacing(0)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_30.setSpacing(0)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_32.setSpacing(0)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
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
        self.horizontalLayout_34.setSpacing(0)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
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
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
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

        self.body_frame.addWidget(self.dashboard)
        self.newbill = QWidget()
        self.newbill.setObjectName(u"newbill")
        self.newbill.setStyleSheet(u"")
        self.horizontalLayout_23 = QHBoxLayout(self.newbill)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.bill_info_frame = QWidget(self.newbill)
        self.bill_info_frame.setObjectName(u"bill_info_frame")
        self.bill_info_frame.setMaximumSize(QSize(10000, 10000))
        self.bill_info_frame.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.bill_info_frame)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.customer_info_frame = QFrame(self.bill_info_frame)
        self.customer_info_frame.setObjectName(u"customer_info_frame")
        self.customer_info_frame.setFrameShape(QFrame.StyledPanel)
        self.customer_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.customer_info_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.customer_label_frame = QWidget(self.customer_info_frame)
        self.customer_label_frame.setObjectName(u"customer_label_frame")
        self.verticalLayout_35 = QVBoxLayout(self.customer_label_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.customer_label = QLabel(self.customer_label_frame)
        self.customer_label.setObjectName(u"customer_label")
        font12 = QFont()
        font12.setPointSize(13)
        font12.setBold(True)
        font12.setWeight(75)
        self.customer_label.setFont(font12)

        self.verticalLayout_35.addWidget(self.customer_label)


        self.verticalLayout_34.addWidget(self.customer_label_frame)

        self.field_frame = QWidget(self.customer_info_frame)
        self.field_frame.setObjectName(u"field_frame")
        self.verticalLayout_41 = QVBoxLayout(self.field_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget = QWidget(self.field_frame)
        self.widget.setObjectName(u"widget")
        self.horizontalLayout_36 = QHBoxLayout(self.widget)
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")
        font13 = QFont()
        font13.setPointSize(12)
        font13.setBold(True)
        font13.setWeight(75)
        self.label_2.setFont(font13)

        self.horizontalLayout_36.addWidget(self.label_2)

        self.customer_name_field = QLineEdit(self.widget)
        self.customer_name_field.setObjectName(u"customer_name_field")
        sizePolicy3 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.customer_name_field.sizePolicy().hasHeightForWidth())
        self.customer_name_field.setSizePolicy(sizePolicy3)
        self.customer_name_field.setMaximumSize(QSize(16777215, 39))
        self.customer_name_field.setFont(font3)

        self.horizontalLayout_36.addWidget(self.customer_name_field)


        self.verticalLayout_41.addWidget(self.widget)

        self.widget_5 = QWidget(self.field_frame)
        self.widget_5.setObjectName(u"widget_5")
        self.horizontalLayout_37 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font13)

        self.horizontalLayout_37.addWidget(self.label_3)

        self.customer_contact_field = QLineEdit(self.widget_5)
        self.customer_contact_field.setObjectName(u"customer_contact_field")
        sizePolicy3.setHeightForWidth(self.customer_contact_field.sizePolicy().hasHeightForWidth())
        self.customer_contact_field.setSizePolicy(sizePolicy3)
        self.customer_contact_field.setMaximumSize(QSize(16777215, 39))
        self.customer_contact_field.setFont(font3)

        self.horizontalLayout_37.addWidget(self.customer_contact_field)


        self.verticalLayout_41.addWidget(self.widget_5)


        self.verticalLayout_34.addWidget(self.field_frame)


        self.verticalLayout_33.addWidget(self.customer_info_frame)

        self.product_info_frame = QFrame(self.bill_info_frame)
        self.product_info_frame.setObjectName(u"product_info_frame")
        self.product_info_frame.setFrameShape(QFrame.StyledPanel)
        self.product_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.product_info_frame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_7 = QWidget(self.product_info_frame)
        self.widget_7.setObjectName(u"widget_7")
        self.verticalLayout_38 = QVBoxLayout(self.widget_7)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_4 = QLabel(self.widget_7)
        self.label_4.setObjectName(u"label_4")
        font14 = QFont()
        font14.setPointSize(12)
        font14.setBold(True)
        font14.setUnderline(True)
        font14.setWeight(75)
        self.label_4.setFont(font14)
        self.label_4.setAlignment(Qt.AlignCenter)

        self.verticalLayout_38.addWidget(self.label_4)


        self.verticalLayout_37.addWidget(self.widget_7)

        self.widget_6 = QWidget(self.product_info_frame)
        self.widget_6.setObjectName(u"widget_6")
        self.verticalLayout_39 = QVBoxLayout(self.widget_6)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.widget_8 = QWidget(self.widget_6)
        self.widget_8.setObjectName(u"widget_8")
        self.horizontalLayout_38 = QHBoxLayout(self.widget_8)
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.label_5 = QLabel(self.widget_8)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font13)

        self.horizontalLayout_38.addWidget(self.label_5)

        self.product_name_field = QLineEdit(self.widget_8)
        self.product_name_field.setObjectName(u"product_name_field")
        sizePolicy3.setHeightForWidth(self.product_name_field.sizePolicy().hasHeightForWidth())
        self.product_name_field.setSizePolicy(sizePolicy3)
        self.product_name_field.setMaximumSize(QSize(16777215, 39))
        self.product_name_field.setFont(font3)
        self.product_name_field.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_38.addWidget(self.product_name_field)


        self.verticalLayout_39.addWidget(self.widget_8)

        self.widget_10 = QWidget(self.widget_6)
        self.widget_10.setObjectName(u"widget_10")
        self.horizontalLayout_39 = QHBoxLayout(self.widget_10)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.label_6 = QLabel(self.widget_10)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font13)

        self.horizontalLayout_39.addWidget(self.label_6)

        self.product_id_field = QLineEdit(self.widget_10)
        self.product_id_field.setObjectName(u"product_id_field")
        sizePolicy3.setHeightForWidth(self.product_id_field.sizePolicy().hasHeightForWidth())
        self.product_id_field.setSizePolicy(sizePolicy3)
        self.product_id_field.setMaximumSize(QSize(16777215, 39))
        self.product_id_field.setFont(font3)

        self.horizontalLayout_39.addWidget(self.product_id_field)


        self.verticalLayout_39.addWidget(self.widget_10)

        self.widget_9 = QWidget(self.widget_6)
        self.widget_9.setObjectName(u"widget_9")
        self.horizontalLayout_40 = QHBoxLayout(self.widget_9)
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.label_7 = QLabel(self.widget_9)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font13)

        self.horizontalLayout_40.addWidget(self.label_7)

        self.product_price_field = QLineEdit(self.widget_9)
        self.product_price_field.setObjectName(u"product_price_field")
        sizePolicy3.setHeightForWidth(self.product_price_field.sizePolicy().hasHeightForWidth())
        self.product_price_field.setSizePolicy(sizePolicy3)
        self.product_price_field.setMaximumSize(QSize(16777215, 39))
        self.product_price_field.setFont(font3)
        self.product_price_field.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)

        self.horizontalLayout_40.addWidget(self.product_price_field)


        self.verticalLayout_39.addWidget(self.widget_9)

        self.widget_11 = QWidget(self.widget_6)
        self.widget_11.setObjectName(u"widget_11")
        self.horizontalLayout_41 = QHBoxLayout(self.widget_11)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.label_8 = QLabel(self.widget_11)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font13)

        self.horizontalLayout_41.addWidget(self.label_8)

        self.product_qty_field = QLineEdit(self.widget_11)
        self.product_qty_field.setObjectName(u"product_qty_field")
        sizePolicy3.setHeightForWidth(self.product_qty_field.sizePolicy().hasHeightForWidth())
        self.product_qty_field.setSizePolicy(sizePolicy3)
        self.product_qty_field.setMaximumSize(QSize(16777215, 39))
        self.product_qty_field.setFont(font3)
        self.product_qty_field.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.product_qty_field.setFrame(True)
        self.product_qty_field.setClearButtonEnabled(False)

        self.horizontalLayout_41.addWidget(self.product_qty_field)


        self.verticalLayout_39.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        self.horizontalLayout_42 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.add_btn = QPushButton(self.widget_12)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy4)
        self.add_btn.setMaximumSize(QSize(120, 40))
        font15 = QFont()
        font15.setPointSize(18)
        font15.setBold(False)
        font15.setUnderline(False)
        font15.setWeight(50)
        self.add_btn.setFont(font15)
        self.add_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:12px;")
        icon8 = QIcon()
        icon8.addFile(u":/blueicons/icons/blue_icons/plus-circle.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.add_btn.setIcon(icon8)
        self.add_btn.setIconSize(QSize(22, 22))
        self.add_btn.setAutoDefault(False)
        self.add_btn.setFlat(True)

        self.horizontalLayout_42.addWidget(self.add_btn)


        self.verticalLayout_39.addWidget(self.widget_12)


        self.verticalLayout_37.addWidget(self.widget_6)


        self.verticalLayout_33.addWidget(self.product_info_frame)


        self.horizontalLayout_23.addWidget(self.bill_info_frame)

        self.bill_view = QWidget(self.newbill)
        self.bill_view.setObjectName(u"bill_view")
        sizePolicy.setHeightForWidth(self.bill_view.sizePolicy().hasHeightForWidth())
        self.bill_view.setSizePolicy(sizePolicy)
        self.bill_view.setStyleSheet(u"")
        self.verticalLayout_36 = QVBoxLayout(self.bill_view)
        self.verticalLayout_36.setSpacing(9)
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.verticalLayout_36.setContentsMargins(9, 9, 9, 20)
        self.table_frame = QFrame(self.bill_view)
        self.table_frame.setObjectName(u"table_frame")
        self.table_frame.setFrameShape(QFrame.StyledPanel)
        self.table_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_40 = QVBoxLayout(self.table_frame)
        self.verticalLayout_40.setSpacing(9)
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.verticalLayout_40.setContentsMargins(9, 9, 9, 9)
        self.tableWidget = QTableWidget(self.table_frame)
        if (self.tableWidget.columnCount() < 4):
            self.tableWidget.setColumnCount(4)
        font16 = QFont()
        font16.setPointSize(10)
        font16.setBold(True)
        font16.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font16);
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font16);
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font16);
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font16);
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        if (self.tableWidget.rowCount() < 17):
            self.tableWidget.setRowCount(17)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(0, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(1, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(2, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(3, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(4, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(5, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(6, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(7, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(8, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(9, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(10, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(11, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(12, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(13, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(14, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(15, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.tableWidget.setVerticalHeaderItem(16, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem40)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setEnabled(True)
        sizePolicy4.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy4)
        self.tableWidget.setBaseSize(QSize(0, 0))
        self.tableWidget.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.tableWidget.setFrameShape(QFrame.Panel)
        self.tableWidget.setFrameShadow(QFrame.Plain)
        self.tableWidget.setLineWidth(1)
        self.tableWidget.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.tableWidget.setAutoScrollMargin(16)
        self.tableWidget.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.tableWidget.setDragEnabled(False)
        self.tableWidget.setDragDropOverwriteMode(True)
        self.tableWidget.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.tableWidget.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.SolidLine)
        self.tableWidget.setSortingEnabled(False)
        self.tableWidget.setWordWrap(True)
        self.tableWidget.setCornerButtonEnabled(True)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(150)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setHighlightSections(True)
        self.tableWidget.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_40.addWidget(self.tableWidget)


        self.verticalLayout_36.addWidget(self.table_frame)

        self.bill_tag_frame = QFrame(self.bill_view)
        self.bill_tag_frame.setObjectName(u"bill_tag_frame")
        self.bill_tag_frame.setFrameShape(QFrame.StyledPanel)
        self.bill_tag_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.bill_tag_frame)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, -1, -1, 9)
        self.widget_3 = QWidget(self.bill_tag_frame)
        self.widget_3.setObjectName(u"widget_3")
        font17 = QFont()
        font17.setPointSize(10)
        font17.setBold(False)
        font17.setWeight(50)
        self.widget_3.setFont(font17)
        self.horizontalLayout_44 = QHBoxLayout(self.widget_3)
        self.horizontalLayout_44.setSpacing(3)
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.horizontalLayout_44.setContentsMargins(5, 5, 6, 5)
        self.label = QLabel(self.widget_3)
        self.label.setObjectName(u"label")
        sizePolicy5 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy5)
        font18 = QFont()
        font18.setPointSize(11)
        font18.setBold(True)
        font18.setWeight(75)
        self.label.setFont(font18)
        self.label.setScaledContents(False)
        self.label.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_44.addWidget(self.label)

        self.bill_tag_field = QLineEdit(self.widget_3)
        self.bill_tag_field.setObjectName(u"bill_tag_field")
        sizePolicy4.setHeightForWidth(self.bill_tag_field.sizePolicy().hasHeightForWidth())
        self.bill_tag_field.setSizePolicy(sizePolicy4)
        self.bill_tag_field.setMaximumSize(QSize(123, 30))
        self.bill_tag_field.setFont(font17)
        self.bill_tag_field.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bill_tag_field.setStyleSheet(u"")
        self.bill_tag_field.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.bill_tag_field)


        self.horizontalLayout_43.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.bill_tag_frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy4.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy4)
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_45 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(3, 15, 0, 15)
        self.save_btn = QPushButton(self.widget_2)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(25)
        sizePolicy6.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy6)
        self.save_btn.setMaximumSize(QSize(70, 33))
        font19 = QFont()
        font19.setPointSize(14)
        font19.setBold(False)
        font19.setUnderline(False)
        font19.setWeight(50)
        self.save_btn.setFont(font19)
        self.save_btn.setLayoutDirection(Qt.RightToLeft)
        self.save_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius:10px;\n"
"border:3px solid #fff;\n"
"")
        icon9 = QIcon()
        icon9.addFile(u":/blueicons/icons/blue_icons/save.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.save_btn.setIcon(icon9)
        self.save_btn.setIconSize(QSize(20, 20))
        self.save_btn.setFlat(True)

        self.horizontalLayout_45.addWidget(self.save_btn, 0, Qt.AlignRight)


        self.horizontalLayout_43.addWidget(self.widget_2)


        self.verticalLayout_36.addWidget(self.bill_tag_frame)


        self.horizontalLayout_23.addWidget(self.bill_view)

        self.body_frame.addWidget(self.newbill)
        self.statistics = QWidget()
        self.statistics.setObjectName(u"statistics")
        self.body_frame.addWidget(self.statistics)

        self.verticalLayout.addWidget(self.body_frame)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 985, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.profile_btn.setDefault(False)
        self.body_frame.setCurrentIndex(1)
        self.add_btn.setDefault(False)
        self.save_btn.setDefault(False)


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
        self.label_coustomer.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_coustomername.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn.setText("")
        self.label_name_5.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_5.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_coustomername_5.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_5.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_5.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_5.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_5.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_5.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_2.setText("")
        self.label_name_6.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_6.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_coustomername_6.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_6.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_6.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_6.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_6.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_6.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_6.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_3.setText("")
        self.label_name_7.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_7.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_coustomername_7.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_7.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price_7.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_7.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate_7.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_7.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id_7.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn_4.setText("")
        self.customer_label.setText(QCoreApplication.translate("MainWindow", u"Customer Info :", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Name            :", None))
        self.customer_name_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"customer name", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Email\\Phone :", None))
        self.customer_contact_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"contact", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Product Details", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Name      :", None))
        self.product_name_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"product Name", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"ID           :", None))
        self.product_id_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"product ID", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Price       :", None))
        self.product_price_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"QTY         :", None))
        self.product_qty_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"quantity", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"ADD", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Qty", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem4 = self.tableWidget.verticalHeaderItem(0)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem5 = self.tableWidget.verticalHeaderItem(1)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem6 = self.tableWidget.verticalHeaderItem(2)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem7 = self.tableWidget.verticalHeaderItem(3)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem8 = self.tableWidget.verticalHeaderItem(4)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem9 = self.tableWidget.verticalHeaderItem(5)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem10 = self.tableWidget.verticalHeaderItem(6)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem11 = self.tableWidget.verticalHeaderItem(7)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem12 = self.tableWidget.verticalHeaderItem(8)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem13 = self.tableWidget.verticalHeaderItem(9)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem14 = self.tableWidget.verticalHeaderItem(10)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem15 = self.tableWidget.verticalHeaderItem(11)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem16 = self.tableWidget.verticalHeaderItem(12)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem17 = self.tableWidget.verticalHeaderItem(13)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem18 = self.tableWidget.verticalHeaderItem(14)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem19 = self.tableWidget.verticalHeaderItem(15)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem20 = self.tableWidget.verticalHeaderItem(16)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"19", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem21 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"rgegrg", None));
        ___qtablewidgetitem22 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"gergeg", None));
        ___qtablewidgetitem23 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"gerge", None));
        ___qtablewidgetitem24 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"gergreg", None));
        ___qtablewidgetitem25 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"fsdfgsgfg", None));
        ___qtablewidgetitem26 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"gegege", None));
        ___qtablewidgetitem27 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"gergregr", None));
        ___qtablewidgetitem28 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"gerg", None));
        ___qtablewidgetitem29 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"egregrr", None));
        ___qtablewidgetitem30 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"ergege", None));
        ___qtablewidgetitem31 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"gergreg", None));
        ___qtablewidgetitem32 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"gergre", None));
        ___qtablewidgetitem33 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"gegerg", None));
        ___qtablewidgetitem34 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"ergegegre", None));
        ___qtablewidgetitem35 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"gergerge", None));
        ___qtablewidgetitem36 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"grgrg", None));
        ___qtablewidgetitem37 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"gegerg", None));
        ___qtablewidgetitem38 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"gergregreg", None));
        ___qtablewidgetitem39 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"ergegegre", None));
        ___qtablewidgetitem40 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"grgrr", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Bill Tag :", None))
        self.bill_tag_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
    # retranslateUi

