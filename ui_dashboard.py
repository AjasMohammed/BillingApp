# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dashboardonEVCd.ui'
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
        MainWindow.resize(892, 705)
        font = QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        font1 = QFont()
        font1.setFamily(u"Adobe Ming Std")
        font1.setPointSize(8)
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
"#customer_name_field, #customer_contact_field, #product_name_field, #product_id_field, #product_qty_field, #product_price_field, #bill_tag_field, #stat_billtag_field{\n"
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
        self.menu = QWidget(self.mainbody)
        self.menu.setObjectName(u"menu")
        self.menu.setStyleSheet(u"")
        self.horizontalLayout_6 = QHBoxLayout(self.menu)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.menu_btn = QPushButton(self.menu)
        self.menu_btn.setObjectName(u"menu_btn")
        font4 = QFont()
        font4.setPointSize(12)
        font4.setBold(False)
        font4.setWeight(50)
        self.menu_btn.setFont(font4)
        icon4 = QIcon()
        icon4.addFile(u":/blueicons/icons/blue_icons/menu.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.menu_btn.setIcon(icon4)
        self.menu_btn.setIconSize(QSize(32, 32))
        self.menu_btn.setFlat(True)

        self.horizontalLayout_6.addWidget(self.menu_btn, 0, Qt.AlignLeft)


        self.verticalLayout.addWidget(self.menu)

        self.body_frame = QCustomStackedWidget(self.mainbody)
        self.body_frame.setObjectName(u"body_frame")
        self.dashboard = QWidget()
        self.dashboard.setObjectName(u"dashboard")
        self.verticalLayout_32 = QVBoxLayout(self.dashboard)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.header_frame = QWidget(self.dashboard)
        self.header_frame.setObjectName(u"header_frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.header_frame.sizePolicy().hasHeightForWidth())
        self.header_frame.setSizePolicy(sizePolicy1)
        self.header_frame.setStyleSheet(u"")
        self.horizontalLayout_2 = QHBoxLayout(self.header_frame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 15, 0)
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
        self.label_pybill = QLabel(self.frame)
        self.label_pybill.setObjectName(u"label_pybill")
        self.label_pybill.setMinimumSize(QSize(0, 0))
        font5 = QFont()
        font5.setFamily(u"Adobe Ming Std L")
        font5.setPointSize(28)
        font5.setBold(True)
        font5.setUnderline(False)
        font5.setWeight(75)
        self.label_pybill.setFont(font5)
        self.label_pybill.setStyleSheet(u"")
        self.label_pybill.setScaledContents(False)
        self.label_pybill.setAlignment(Qt.AlignCenter)
        self.label_pybill.setMargin(0)

        self.horizontalLayout_4.addWidget(self.label_pybill)


        self.horizontalLayout_3.addWidget(self.frame)


        self.horizontalLayout_2.addWidget(self.space_frame, 0, Qt.AlignHCenter)

        self.widget_4 = QWidget(self.header_frame)
        self.widget_4.setObjectName(u"widget_4")
        self.verticalLayout_47 = QVBoxLayout(self.widget_4)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.company_name = QLabel(self.widget_4)
        self.company_name.setObjectName(u"company_name")
        font6 = QFont()
        font6.setPointSize(20)
        self.company_name.setFont(font6)
        self.company_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_47.addWidget(self.company_name)


        self.horizontalLayout_2.addWidget(self.widget_4)

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
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.profile_btn.sizePolicy().hasHeightForWidth())
        self.profile_btn.setSizePolicy(sizePolicy2)
        self.profile_btn.setAutoFillBackground(False)
        self.profile_btn.setStyleSheet(u"border:3px solid #004cff;\n"
"border-radius:36px")
        icon5 = QIcon()
        icon5.addFile(u":/blueicons/icons/blue_icons/user.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.profile_btn.setIcon(icon5)
        self.profile_btn.setIconSize(QSize(70, 70))
        self.profile_btn.setFlat(True)

        self.verticalLayout_24.addWidget(self.profile_btn, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.verticalLayout_22.addWidget(self.profilebtn)

        self.username_frame = QWidget(self.profile_frame)
        self.username_frame.setObjectName(u"username_frame")
        self.verticalLayout_23 = QVBoxLayout(self.username_frame)
        self.verticalLayout_23.setSpacing(0)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.label_username = QLabel(self.username_frame)
        self.label_username.setObjectName(u"label_username")
        self.label_username.setFont(font3)
        self.label_username.setFrameShape(QFrame.NoFrame)
        self.label_username.setAlignment(Qt.AlignCenter)

        self.verticalLayout_23.addWidget(self.label_username)


        self.verticalLayout_22.addWidget(self.username_frame)


        self.horizontalLayout_2.addWidget(self.profile_frame, 0, Qt.AlignRight)


        self.verticalLayout_32.addWidget(self.header_frame)

        self.middle_farme = QWidget(self.dashboard)
        self.middle_farme.setObjectName(u"middle_farme")
        sizePolicy1.setHeightForWidth(self.middle_farme.sizePolicy().hasHeightForWidth())
        self.middle_farme.setSizePolicy(sizePolicy1)
        self.horizontalLayout_13 = QHBoxLayout(self.middle_farme)
        self.horizontalLayout_13.setSpacing(15)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.horizontalLayout_13.setContentsMargins(9, 9, 9, 9)
        self.mid_card1 = QWidget(self.middle_farme)
        self.mid_card1.setObjectName(u"mid_card1")
        sizePolicy1.setHeightForWidth(self.mid_card1.sizePolicy().hasHeightForWidth())
        self.mid_card1.setSizePolicy(sizePolicy1)
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
        self.card_today_label.setFont(font4)
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
        sizePolicy1.setHeightForWidth(self.mid_card2.sizePolicy().hasHeightForWidth())
        self.mid_card2.setSizePolicy(sizePolicy1)
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
        sizePolicy1.setHeightForWidth(self.mid_card3.sizePolicy().hasHeightForWidth())
        self.mid_card3.setSizePolicy(sizePolicy1)
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
        self.card_month_label.setFont(font4)
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
        sizePolicy1.setHeightForWidth(self.recent_title_frame.sizePolicy().hasHeightForWidth())
        self.recent_title_frame.setSizePolicy(sizePolicy1)
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
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.card_frame.sizePolicy().hasHeightForWidth())
        self.card_frame.setSizePolicy(sizePolicy3)
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
        self.label_bill1 = QLabel(self.title_frame)
        self.label_bill1.setObjectName(u"label_bill1")
        font11 = QFont()
        font11.setPointSize(12)
        font11.setBold(False)
        font11.setUnderline(True)
        font11.setWeight(50)
        font11.setStrikeOut(False)
        self.label_bill1.setFont(font11)
        self.label_bill1.setScaledContents(True)
        self.label_bill1.setAlignment(Qt.AlignCenter)
        self.label_bill1.setWordWrap(True)

        self.verticalLayout_8.addWidget(self.label_bill1)


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

        self.label_cust1 = QLabel(self.coust_name)
        self.label_cust1.setObjectName(u"label_cust1")
        self.label_cust1.setFont(font7)
        self.label_cust1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_8.addWidget(self.label_cust1)


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

        self.label_price1 = QLabel(self.total)
        self.label_price1.setObjectName(u"label_price1")
        self.label_price1.setFont(font7)
        self.label_price1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_9.addWidget(self.label_price1)


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

        self.label_billdate1 = QLabel(self.date)
        self.label_billdate1.setObjectName(u"label_billdate1")
        self.label_billdate1.setFont(font7)
        self.label_billdate1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_10.addWidget(self.label_billdate1)


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

        self.label_id1 = QLabel(self.id)
        self.label_id1.setObjectName(u"label_id1")
        self.label_id1.setFont(font7)
        self.label_id1.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_11.addWidget(self.label_id1)


        self.verticalLayout_3.addWidget(self.id)

        self.goto_btn = QWidget(self.cardbody_frame)
        self.goto_btn.setObjectName(u"goto_btn")
        self.verticalLayout_7 = QVBoxLayout(self.goto_btn)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.arrow_btn1 = QPushButton(self.goto_btn)
        self.arrow_btn1.setObjectName(u"arrow_btn1")
        icon7 = QIcon()
        icon7.addFile(u":/blueicons/icons/blue_icons/arrow-right.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.arrow_btn1.setIcon(icon7)
        self.arrow_btn1.setIconSize(QSize(35, 16))
        self.arrow_btn1.setFlat(True)

        self.verticalLayout_7.addWidget(self.arrow_btn1, 0, Qt.AlignRight)


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
        self.label_bill2 = QLabel(self.title_frame_5)
        self.label_bill2.setObjectName(u"label_bill2")
        self.label_bill2.setFont(font11)
        self.label_bill2.setScaledContents(True)
        self.label_bill2.setAlignment(Qt.AlignCenter)
        self.label_bill2.setWordWrap(True)

        self.verticalLayout_10.addWidget(self.label_bill2)


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

        self.label_cust2 = QLabel(self.coust_name_5)
        self.label_cust2.setObjectName(u"label_cust2")
        self.label_cust2.setFont(font7)
        self.label_cust2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_24.addWidget(self.label_cust2)


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

        self.label_price2 = QLabel(self.total_5)
        self.label_price2.setObjectName(u"label_price2")
        self.label_price2.setFont(font7)
        self.label_price2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_25.addWidget(self.label_price2)


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

        self.label_billdate2 = QLabel(self.date_5)
        self.label_billdate2.setObjectName(u"label_billdate2")
        self.label_billdate2.setFont(font7)
        self.label_billdate2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_26.addWidget(self.label_billdate2)


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

        self.label_id2 = QLabel(self.id_5)
        self.label_id2.setObjectName(u"label_id2")
        self.label_id2.setFont(font7)
        self.label_id2.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_27.addWidget(self.label_id2)


        self.verticalLayout_9.addWidget(self.id_5)

        self.goto_btn_2 = QWidget(self.cardbody_frame_2)
        self.goto_btn_2.setObjectName(u"goto_btn_2")
        self.verticalLayout_11 = QVBoxLayout(self.goto_btn_2)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.arrow_btn2 = QPushButton(self.goto_btn_2)
        self.arrow_btn2.setObjectName(u"arrow_btn2")
        self.arrow_btn2.setIcon(icon7)
        self.arrow_btn2.setIconSize(QSize(35, 16))
        self.arrow_btn2.setFlat(True)

        self.verticalLayout_11.addWidget(self.arrow_btn2, 0, Qt.AlignRight)


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
        self.label_bill3 = QLabel(self.title_frame_6)
        self.label_bill3.setObjectName(u"label_bill3")
        self.label_bill3.setFont(font11)
        self.label_bill3.setScaledContents(True)
        self.label_bill3.setAlignment(Qt.AlignCenter)
        self.label_bill3.setWordWrap(True)

        self.verticalLayout_13.addWidget(self.label_bill3)


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

        self.label_cust3 = QLabel(self.coust_name_6)
        self.label_cust3.setObjectName(u"label_cust3")
        self.label_cust3.setFont(font7)
        self.label_cust3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_28.addWidget(self.label_cust3)


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

        self.label_price3 = QLabel(self.total_6)
        self.label_price3.setObjectName(u"label_price3")
        self.label_price3.setFont(font7)
        self.label_price3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_29.addWidget(self.label_price3)


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

        self.label_billdate3 = QLabel(self.date_6)
        self.label_billdate3.setObjectName(u"label_billdate3")
        self.label_billdate3.setFont(font7)
        self.label_billdate3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_30.addWidget(self.label_billdate3)


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

        self.label_id3 = QLabel(self.id_6)
        self.label_id3.setObjectName(u"label_id3")
        self.label_id3.setFont(font7)
        self.label_id3.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_31.addWidget(self.label_id3)


        self.verticalLayout_12.addWidget(self.id_6)

        self.goto_btn_3 = QWidget(self.cardbody_frame_3)
        self.goto_btn_3.setObjectName(u"goto_btn_3")
        self.verticalLayout_14 = QVBoxLayout(self.goto_btn_3)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.arrow_btn3 = QPushButton(self.goto_btn_3)
        self.arrow_btn3.setObjectName(u"arrow_btn3")
        self.arrow_btn3.setIcon(icon7)
        self.arrow_btn3.setIconSize(QSize(35, 16))
        self.arrow_btn3.setFlat(True)

        self.verticalLayout_14.addWidget(self.arrow_btn3, 0, Qt.AlignRight)


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
        self.label_bill4 = QLabel(self.title_frame_7)
        self.label_bill4.setObjectName(u"label_bill4")
        self.label_bill4.setFont(font11)
        self.label_bill4.setScaledContents(True)
        self.label_bill4.setAlignment(Qt.AlignCenter)
        self.label_bill4.setWordWrap(True)

        self.verticalLayout_16.addWidget(self.label_bill4)


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

        self.label_cust4 = QLabel(self.coust_name_7)
        self.label_cust4.setObjectName(u"label_cust4")
        self.label_cust4.setFont(font7)
        self.label_cust4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_32.addWidget(self.label_cust4)


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

        self.label_price4 = QLabel(self.total_7)
        self.label_price4.setObjectName(u"label_price4")
        self.label_price4.setFont(font7)
        self.label_price4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_33.addWidget(self.label_price4)


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

        self.label_billdate4 = QLabel(self.date_7)
        self.label_billdate4.setObjectName(u"label_billdate4")
        self.label_billdate4.setFont(font7)
        self.label_billdate4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_34.addWidget(self.label_billdate4)


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

        self.label_id4 = QLabel(self.id_7)
        self.label_id4.setObjectName(u"label_id4")
        self.label_id4.setFont(font7)
        self.label_id4.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_35.addWidget(self.label_id4)


        self.verticalLayout_15.addWidget(self.id_7)

        self.goto_btn_4 = QWidget(self.cardbody_frame_4)
        self.goto_btn_4.setObjectName(u"goto_btn_4")
        self.verticalLayout_17 = QVBoxLayout(self.goto_btn_4)
        self.verticalLayout_17.setSpacing(0)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.verticalLayout_17.setContentsMargins(0, 0, 0, 0)
        self.arrow_btn4 = QPushButton(self.goto_btn_4)
        self.arrow_btn4.setObjectName(u"arrow_btn4")
        self.arrow_btn4.setIcon(icon7)
        self.arrow_btn4.setIconSize(QSize(35, 16))
        self.arrow_btn4.setFlat(True)

        self.verticalLayout_17.addWidget(self.arrow_btn4, 0, Qt.AlignRight)


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
        sizePolicy4 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.bill_info_frame.sizePolicy().hasHeightForWidth())
        self.bill_info_frame.setSizePolicy(sizePolicy4)
        self.bill_info_frame.setMaximumSize(QSize(10000, 10000))
        self.bill_info_frame.setStyleSheet(u"")
        self.verticalLayout_33 = QVBoxLayout(self.bill_info_frame)
        self.verticalLayout_33.setSpacing(5)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_33.setContentsMargins(9, 9, 9, 9)
        self.customer_info_frame = QFrame(self.bill_info_frame)
        self.customer_info_frame.setObjectName(u"customer_info_frame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.customer_info_frame.sizePolicy().hasHeightForWidth())
        self.customer_info_frame.setSizePolicy(sizePolicy5)
        self.customer_info_frame.setMaximumSize(QSize(16777215, 210))
        self.customer_info_frame.setFrameShape(QFrame.StyledPanel)
        self.customer_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_34 = QVBoxLayout(self.customer_info_frame)
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.verticalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.customer_label_frame = QWidget(self.customer_info_frame)
        self.customer_label_frame.setObjectName(u"customer_label_frame")
        sizePolicy3.setHeightForWidth(self.customer_label_frame.sizePolicy().hasHeightForWidth())
        self.customer_label_frame.setSizePolicy(sizePolicy3)
        self.customer_label_frame.setMaximumSize(QSize(16777215, 70))
        self.verticalLayout_35 = QVBoxLayout(self.customer_label_frame)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.customer_label = QLabel(self.customer_label_frame)
        self.customer_label.setObjectName(u"customer_label")
        sizePolicy1.setHeightForWidth(self.customer_label.sizePolicy().hasHeightForWidth())
        self.customer_label.setSizePolicy(sizePolicy1)
        font12 = QFont()
        font12.setPointSize(13)
        font12.setBold(True)
        font12.setWeight(75)
        self.customer_label.setFont(font12)
        self.customer_label.setAlignment(Qt.AlignCenter)

        self.verticalLayout_35.addWidget(self.customer_label, 0, Qt.AlignBottom)


        self.verticalLayout_34.addWidget(self.customer_label_frame)

        self.field_frame = QWidget(self.customer_info_frame)
        self.field_frame.setObjectName(u"field_frame")
        sizePolicy1.setHeightForWidth(self.field_frame.sizePolicy().hasHeightForWidth())
        self.field_frame.setSizePolicy(sizePolicy1)
        self.verticalLayout_41 = QVBoxLayout(self.field_frame)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.widget = QWidget(self.field_frame)
        self.widget.setObjectName(u"widget")
        sizePolicy3.setHeightForWidth(self.widget.sizePolicy().hasHeightForWidth())
        self.widget.setSizePolicy(sizePolicy3)
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.customer_name_field.sizePolicy().hasHeightForWidth())
        self.customer_name_field.setSizePolicy(sizePolicy6)
        self.customer_name_field.setMaximumSize(QSize(16777215, 39))
        self.customer_name_field.setFont(font3)

        self.horizontalLayout_36.addWidget(self.customer_name_field)


        self.verticalLayout_41.addWidget(self.widget)

        self.widget_5 = QWidget(self.field_frame)
        self.widget_5.setObjectName(u"widget_5")
        sizePolicy3.setHeightForWidth(self.widget_5.sizePolicy().hasHeightForWidth())
        self.widget_5.setSizePolicy(sizePolicy3)
        self.horizontalLayout_37 = QHBoxLayout(self.widget_5)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.label_3 = QLabel(self.widget_5)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font13)

        self.horizontalLayout_37.addWidget(self.label_3)

        self.customer_contact_field = QLineEdit(self.widget_5)
        self.customer_contact_field.setObjectName(u"customer_contact_field")
        sizePolicy6.setHeightForWidth(self.customer_contact_field.sizePolicy().hasHeightForWidth())
        self.customer_contact_field.setSizePolicy(sizePolicy6)
        self.customer_contact_field.setMaximumSize(QSize(16777215, 39))
        self.customer_contact_field.setFont(font3)

        self.horizontalLayout_37.addWidget(self.customer_contact_field)


        self.verticalLayout_41.addWidget(self.widget_5)


        self.verticalLayout_34.addWidget(self.field_frame)


        self.verticalLayout_33.addWidget(self.customer_info_frame)

        self.product_info_frame = QFrame(self.bill_info_frame)
        self.product_info_frame.setObjectName(u"product_info_frame")
        sizePolicy5.setHeightForWidth(self.product_info_frame.sizePolicy().hasHeightForWidth())
        self.product_info_frame.setSizePolicy(sizePolicy5)
        self.product_info_frame.setMaximumSize(QSize(16777215, 355))
        self.product_info_frame.setFrameShape(QFrame.StyledPanel)
        self.product_info_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.product_info_frame)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.widget_7 = QWidget(self.product_info_frame)
        self.widget_7.setObjectName(u"widget_7")
        sizePolicy3.setHeightForWidth(self.widget_7.sizePolicy().hasHeightForWidth())
        self.widget_7.setSizePolicy(sizePolicy3)
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
        sizePolicy3.setHeightForWidth(self.widget_6.sizePolicy().hasHeightForWidth())
        self.widget_6.setSizePolicy(sizePolicy3)
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
        sizePolicy6.setHeightForWidth(self.product_name_field.sizePolicy().hasHeightForWidth())
        self.product_name_field.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.product_id_field.sizePolicy().hasHeightForWidth())
        self.product_id_field.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.product_price_field.sizePolicy().hasHeightForWidth())
        self.product_price_field.setSizePolicy(sizePolicy6)
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
        sizePolicy6.setHeightForWidth(self.product_qty_field.sizePolicy().hasHeightForWidth())
        self.product_qty_field.setSizePolicy(sizePolicy6)
        self.product_qty_field.setMaximumSize(QSize(16777215, 39))
        self.product_qty_field.setFont(font3)
        self.product_qty_field.setInputMethodHints(Qt.ImhDigitsOnly|Qt.ImhPreferNumbers)
        self.product_qty_field.setFrame(True)
        self.product_qty_field.setClearButtonEnabled(False)

        self.horizontalLayout_41.addWidget(self.product_qty_field)


        self.verticalLayout_39.addWidget(self.widget_11)

        self.widget_12 = QWidget(self.widget_6)
        self.widget_12.setObjectName(u"widget_12")
        sizePolicy3.setHeightForWidth(self.widget_12.sizePolicy().hasHeightForWidth())
        self.widget_12.setSizePolicy(sizePolicy3)
        self.horizontalLayout_42 = QHBoxLayout(self.widget_12)
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.add_btn = QPushButton(self.widget_12)
        self.add_btn.setObjectName(u"add_btn")
        sizePolicy7 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.add_btn.sizePolicy().hasHeightForWidth())
        self.add_btn.setSizePolicy(sizePolicy7)
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
        sizePolicy8 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.bill_view.sizePolicy().hasHeightForWidth())
        self.bill_view.setSizePolicy(sizePolicy8)
        self.bill_view.setMaximumSize(QSize(700, 575))
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
        self.bill_table = QTableWidget(self.table_frame)
        if (self.bill_table.columnCount() < 6):
            self.bill_table.setColumnCount(6)
        font16 = QFont()
        font16.setPointSize(10)
        font16.setBold(True)
        font16.setWeight(75)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem1.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem2.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem3.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem4.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setTextAlignment(Qt.AlignCenter);
        __qtablewidgetitem5.setFont(font16);
        self.bill_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        self.bill_table.setObjectName(u"bill_table")
        self.bill_table.setEnabled(True)
        sizePolicy7.setHeightForWidth(self.bill_table.sizePolicy().hasHeightForWidth())
        self.bill_table.setSizePolicy(sizePolicy7)
        self.bill_table.setBaseSize(QSize(0, 0))
        self.bill_table.setFont(font)
        self.bill_table.viewport().setProperty("cursor", QCursor(Qt.CrossCursor))
        self.bill_table.setFrameShape(QFrame.Panel)
        self.bill_table.setFrameShadow(QFrame.Plain)
        self.bill_table.setLineWidth(1)
        self.bill_table.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        self.bill_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContentsOnFirstShow)
        self.bill_table.setAutoScrollMargin(16)
        self.bill_table.setEditTriggers(QAbstractItemView.DoubleClicked|QAbstractItemView.EditKeyPressed)
        self.bill_table.setDragEnabled(False)
        self.bill_table.setDragDropOverwriteMode(True)
        self.bill_table.setDragDropMode(QAbstractItemView.NoDragDrop)
        self.bill_table.setAlternatingRowColors(True)
        self.bill_table.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.bill_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bill_table.setTextElideMode(Qt.ElideRight)
        self.bill_table.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.bill_table.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.bill_table.setShowGrid(True)
        self.bill_table.setGridStyle(Qt.SolidLine)
        self.bill_table.setSortingEnabled(False)
        self.bill_table.setWordWrap(True)
        self.bill_table.setCornerButtonEnabled(True)
        self.bill_table.horizontalHeader().setVisible(False)
        self.bill_table.horizontalHeader().setCascadingSectionResizes(True)
        self.bill_table.horizontalHeader().setDefaultSectionSize(150)
        self.bill_table.horizontalHeader().setHighlightSections(True)
        self.bill_table.horizontalHeader().setStretchLastSection(True)
        self.bill_table.verticalHeader().setCascadingSectionResizes(False)
        self.bill_table.verticalHeader().setHighlightSections(True)
        self.bill_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_40.addWidget(self.bill_table)


        self.verticalLayout_36.addWidget(self.table_frame)

        self.bill_tag_frame = QFrame(self.bill_view)
        self.bill_tag_frame.setObjectName(u"bill_tag_frame")
        sizePolicy5.setHeightForWidth(self.bill_tag_frame.sizePolicy().hasHeightForWidth())
        self.bill_tag_frame.setSizePolicy(sizePolicy5)
        self.bill_tag_frame.setFrameShape(QFrame.StyledPanel)
        self.bill_tag_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.bill_tag_frame)
        self.horizontalLayout_43.setSpacing(6)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, -1, -1, 9)
        self.widget_3 = QWidget(self.bill_tag_frame)
        self.widget_3.setObjectName(u"widget_3")
        sizePolicy3.setHeightForWidth(self.widget_3.sizePolicy().hasHeightForWidth())
        self.widget_3.setSizePolicy(sizePolicy3)
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
        sizePolicy2.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy2)
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
        sizePolicy7.setHeightForWidth(self.bill_tag_field.sizePolicy().hasHeightForWidth())
        self.bill_tag_field.setSizePolicy(sizePolicy7)
        self.bill_tag_field.setMaximumSize(QSize(123, 30))
        self.bill_tag_field.setFont(font17)
        self.bill_tag_field.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.bill_tag_field.setStyleSheet(u"")
        self.bill_tag_field.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_44.addWidget(self.bill_tag_field)


        self.horizontalLayout_43.addWidget(self.widget_3)

        self.widget_2 = QWidget(self.bill_tag_frame)
        self.widget_2.setObjectName(u"widget_2")
        sizePolicy7.setHeightForWidth(self.widget_2.sizePolicy().hasHeightForWidth())
        self.widget_2.setSizePolicy(sizePolicy7)
        self.widget_2.setMaximumSize(QSize(16777215, 16777215))
        self.horizontalLayout_45 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_45.setSpacing(0)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_45.setContentsMargins(3, 15, 0, 15)
        self.save_btn = QPushButton(self.widget_2)
        self.save_btn.setObjectName(u"save_btn")
        sizePolicy9 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(25)
        sizePolicy9.setHeightForWidth(self.save_btn.sizePolicy().hasHeightForWidth())
        self.save_btn.setSizePolicy(sizePolicy9)
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
        self.verticalLayout_42 = QVBoxLayout(self.statistics)
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.body = QFrame(self.statistics)
        self.body.setObjectName(u"body")
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_43 = QVBoxLayout(self.body)
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.selection_frame = QFrame(self.body)
        self.selection_frame.setObjectName(u"selection_frame")
        sizePolicy1.setHeightForWidth(self.selection_frame.sizePolicy().hasHeightForWidth())
        self.selection_frame.setSizePolicy(sizePolicy1)
        self.selection_frame.setMaximumSize(QSize(561, 16777215))
        self.selection_frame.setFrameShape(QFrame.StyledPanel)
        self.selection_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_46 = QHBoxLayout(self.selection_frame)
        self.horizontalLayout_46.setSpacing(10)
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.horizontalLayout_46.setContentsMargins(-1, -1, 65, -1)
        self.frame_2 = QFrame(self.selection_frame)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy1.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy1)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.label_9 = QLabel(self.frame_2)
        self.label_9.setObjectName(u"label_9")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy10)
        self.label_9.setFont(font7)
        self.label_9.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_47.addWidget(self.label_9)

        self.vis_type = QComboBox(self.frame_2)
        self.vis_type.addItem("")
        self.vis_type.addItem("")
        self.vis_type.addItem("")
        self.vis_type.setObjectName(u"vis_type")
        sizePolicy2.setHeightForWidth(self.vis_type.sizePolicy().hasHeightForWidth())
        self.vis_type.setSizePolicy(sizePolicy2)
        self.vis_type.setFont(font7)
        self.vis_type.setEditable(True)
        self.vis_type.setSizeAdjustPolicy(QComboBox.AdjustToContentsOnFirstShow)
        self.vis_type.setFrame(True)

        self.horizontalLayout_47.addWidget(self.vis_type, 0, Qt.AlignLeft)


        self.horizontalLayout_46.addWidget(self.frame_2)

        self.frame_3 = QFrame(self.selection_frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_48 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.label_10 = QLabel(self.frame_3)
        self.label_10.setObjectName(u"label_10")
        sizePolicy10.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy10)
        self.label_10.setFont(font7)

        self.horizontalLayout_48.addWidget(self.label_10)

        self.vis_timeframe = QComboBox(self.frame_3)
        self.vis_timeframe.addItem("")
        self.vis_timeframe.addItem("")
        self.vis_timeframe.addItem("")
        self.vis_timeframe.setObjectName(u"vis_timeframe")
        self.vis_timeframe.setEnabled(True)
        sizePolicy2.setHeightForWidth(self.vis_timeframe.sizePolicy().hasHeightForWidth())
        self.vis_timeframe.setSizePolicy(sizePolicy2)
        self.vis_timeframe.setFont(font7)

        self.horizontalLayout_48.addWidget(self.vis_timeframe, 0, Qt.AlignLeft)


        self.horizontalLayout_46.addWidget(self.frame_3, 0, Qt.AlignLeft)

        self.vis_btn = QPushButton(self.selection_frame)
        self.vis_btn.setObjectName(u"vis_btn")
        self.vis_btn.setEnabled(False)
        sizePolicy11 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.vis_btn.sizePolicy().hasHeightForWidth())
        self.vis_btn.setSizePolicy(sizePolicy11)
        self.vis_btn.setMaximumSize(QSize(105, 50))
        self.vis_btn.setFont(font16)
        self.vis_btn.setStyleSheet(u"background-color: #004cff;\n"
"border-radius:8px;\n"
"color: rgb(255, 255, 255);")
        icon10 = QIcon()
        icon10.addFile(u":/whiteicons/icons/white_icons/activity.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.vis_btn.setIcon(icon10)
        self.vis_btn.setIconSize(QSize(30, 30))

        self.horizontalLayout_46.addWidget(self.vis_btn)


        self.verticalLayout_43.addWidget(self.selection_frame, 0, Qt.AlignLeft)

        self.chart_frame = QFrame(self.body)
        self.chart_frame.setObjectName(u"chart_frame")
        self.chart_frame.setFrameShape(QFrame.StyledPanel)
        self.chart_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_44 = QVBoxLayout(self.chart_frame)
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.stackedWidget = QStackedWidget(self.chart_frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.bar_chart_page = QWidget()
        self.bar_chart_page.setObjectName(u"bar_chart_page")
        self.verticalLayout_45 = QVBoxLayout(self.bar_chart_page)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.frame_4 = QFrame(self.bar_chart_page)
        self.frame_4.setObjectName(u"frame_4")
        sizePolicy1.setHeightForWidth(self.frame_4.sizePolicy().hasHeightForWidth())
        self.frame_4.setSizePolicy(sizePolicy1)
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_46 = QVBoxLayout(self.frame_4)
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_11 = QLabel(self.frame_4)
        self.label_11.setObjectName(u"label_11")
        sizePolicy1.setHeightForWidth(self.label_11.sizePolicy().hasHeightForWidth())
        self.label_11.setSizePolicy(sizePolicy1)
        font20 = QFont()
        font20.setPointSize(18)
        font20.setBold(False)
        font20.setUnderline(True)
        font20.setWeight(50)
        self.label_11.setFont(font20)
        self.label_11.setAlignment(Qt.AlignCenter)

        self.verticalLayout_46.addWidget(self.label_11)


        self.verticalLayout_45.addWidget(self.frame_4)

        self.chart_vis_frame = QFrame(self.bar_chart_page)
        self.chart_vis_frame.setObjectName(u"chart_vis_frame")
        self.chart_vis_frame.setFrameShape(QFrame.StyledPanel)
        self.chart_vis_frame.setFrameShadow(QFrame.Raised)

        self.verticalLayout_45.addWidget(self.chart_vis_frame)

        self.stackedWidget.addWidget(self.bar_chart_page)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.stackedWidget.addWidget(self.page_4)

        self.verticalLayout_44.addWidget(self.stackedWidget)


        self.verticalLayout_43.addWidget(self.chart_frame)


        self.verticalLayout_42.addWidget(self.body)

        self.body_frame.addWidget(self.statistics)
        self.bills_history = QWidget()
        self.bills_history.setObjectName(u"bills_history")
        self.verticalLayout_48 = QVBoxLayout(self.bills_history)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.card_views = QFrame(self.bills_history)
        self.card_views.setObjectName(u"card_views")
        self.card_views.setFrameShape(QFrame.StyledPanel)
        self.card_views.setFrameShadow(QFrame.Raised)
        self.verticalLayout_49 = QVBoxLayout(self.card_views)
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")

        self.verticalLayout_48.addWidget(self.card_views)

        self.body_frame.addWidget(self.bills_history)
        self.bill_history = QWidget()
        self.bill_history.setObjectName(u"bill_history")
        self.verticalLayout_50 = QVBoxLayout(self.bill_history)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.frame_5 = QFrame(self.bill_history)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_51 = QVBoxLayout(self.frame_5)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.frame_6 = QFrame(self.frame_5)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_6)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.widget_13 = QWidget(self.frame_6)
        self.widget_13.setObjectName(u"widget_13")
        self.verticalLayout_53 = QVBoxLayout(self.widget_13)
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_name = QLabel(self.widget_13)
        self.label_name.setObjectName(u"label_name")
        font21 = QFont()
        font21.setPointSize(18)
        font21.setUnderline(True)
        self.label_name.setFont(font21)
        self.label_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_53.addWidget(self.label_name)


        self.verticalLayout_52.addWidget(self.widget_13)


        self.verticalLayout_51.addWidget(self.frame_6, 0, Qt.AlignTop)

        self.frame_7 = QFrame(self.frame_5)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_49 = QHBoxLayout(self.frame_7)
        self.horizontalLayout_49.setSpacing(30)
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.horizontalLayout_49.setContentsMargins(20, 15, 20, 20)
        self.frame_8 = QFrame(self.frame_7)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy3.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy3)
        self.frame_8.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_8)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_54.setContentsMargins(50, -1, -1, -1)
        self.bill_tableView = QTableView(self.frame_8)
        self.bill_tableView.setObjectName(u"bill_tableView")
        sizePolicy3.setHeightForWidth(self.bill_tableView.sizePolicy().hasHeightForWidth())
        self.bill_tableView.setSizePolicy(sizePolicy3)
        self.bill_tableView.setMaximumSize(QSize(550, 16777215))
        self.bill_tableView.setFont(font7)
        self.bill_tableView.setProperty("showDropIndicator", True)
        self.bill_tableView.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.bill_tableView.setVerticalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.bill_tableView.setHorizontalScrollMode(QAbstractItemView.ScrollPerPixel)
        self.bill_tableView.horizontalHeader().setMinimumSectionSize(110)
        self.bill_tableView.horizontalHeader().setDefaultSectionSize(120)

        self.verticalLayout_54.addWidget(self.bill_tableView)


        self.horizontalLayout_49.addWidget(self.frame_8)

        self.frame_9 = QFrame(self.frame_7)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy)
        self.frame_9.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_55 = QVBoxLayout(self.frame_9)
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.widget_26 = QWidget(self.frame_9)
        self.widget_26.setObjectName(u"widget_26")
        self.horizontalLayout_60 = QHBoxLayout(self.widget_26)
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.widget_27 = QWidget(self.widget_26)
        self.widget_27.setObjectName(u"widget_27")
        self.horizontalLayout_61 = QHBoxLayout(self.widget_27)
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_15 = QLabel(self.widget_27)
        self.label_15.setObjectName(u"label_15")
        self.label_15.setFont(font18)
        self.label_15.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_61.addWidget(self.label_15)


        self.horizontalLayout_60.addWidget(self.widget_27)

        self.widget_28 = QWidget(self.widget_26)
        self.widget_28.setObjectName(u"widget_28")
        self.horizontalLayout_62 = QHBoxLayout(self.widget_28)
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.label_custname = QLabel(self.widget_28)
        self.label_custname.setObjectName(u"label_custname")
        self.label_custname.setFont(font3)
        self.label_custname.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_62.addWidget(self.label_custname)


        self.horizontalLayout_60.addWidget(self.widget_28)


        self.verticalLayout_55.addWidget(self.widget_26)

        self.widget_14 = QWidget(self.frame_9)
        self.widget_14.setObjectName(u"widget_14")
        self.horizontalLayout_51 = QHBoxLayout(self.widget_14)
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.widget_18 = QWidget(self.widget_14)
        self.widget_18.setObjectName(u"widget_18")
        self.horizontalLayout_50 = QHBoxLayout(self.widget_18)
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.label_12 = QLabel(self.widget_18)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setFont(font18)
        self.label_12.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_50.addWidget(self.label_12)


        self.horizontalLayout_51.addWidget(self.widget_18)

        self.widget_21 = QWidget(self.widget_14)
        self.widget_21.setObjectName(u"widget_21")
        self.horizontalLayout_56 = QHBoxLayout(self.widget_21)
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.label_id = QLabel(self.widget_21)
        self.label_id.setObjectName(u"label_id")
        self.label_id.setFont(font3)
        self.label_id.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_56.addWidget(self.label_id)


        self.horizontalLayout_51.addWidget(self.widget_21)


        self.verticalLayout_55.addWidget(self.widget_14)

        self.widget_15 = QWidget(self.frame_9)
        self.widget_15.setObjectName(u"widget_15")
        self.horizontalLayout_54 = QHBoxLayout(self.widget_15)
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.widget_19 = QWidget(self.widget_15)
        self.widget_19.setObjectName(u"widget_19")
        self.horizontalLayout_52 = QHBoxLayout(self.widget_19)
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_13 = QLabel(self.widget_19)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font18)
        self.label_13.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_52.addWidget(self.label_13)

        self.widget_22 = QWidget(self.widget_19)
        self.widget_22.setObjectName(u"widget_22")
        self.horizontalLayout_57 = QHBoxLayout(self.widget_22)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.label_date_2 = QLabel(self.widget_22)
        self.label_date_2.setObjectName(u"label_date_2")
        self.label_date_2.setFont(font3)
        self.label_date_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_57.addWidget(self.label_date_2)


        self.horizontalLayout_52.addWidget(self.widget_22)


        self.horizontalLayout_54.addWidget(self.widget_19)


        self.verticalLayout_55.addWidget(self.widget_15)

        self.widget_16 = QWidget(self.frame_9)
        self.widget_16.setObjectName(u"widget_16")
        self.widget_16.setFont(font7)
        self.horizontalLayout_55 = QHBoxLayout(self.widget_16)
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.widget_20 = QWidget(self.widget_16)
        self.widget_20.setObjectName(u"widget_20")
        self.horizontalLayout_53 = QHBoxLayout(self.widget_20)
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.label_14 = QLabel(self.widget_20)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setFont(font18)
        self.label_14.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_53.addWidget(self.label_14)


        self.horizontalLayout_55.addWidget(self.widget_20)

        self.widget_23 = QWidget(self.widget_16)
        self.widget_23.setObjectName(u"widget_23")
        self.horizontalLayout_58 = QHBoxLayout(self.widget_23)
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.label_amount = QLabel(self.widget_23)
        self.label_amount.setObjectName(u"label_amount")
        self.label_amount.setFont(font3)
        self.label_amount.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_58.addWidget(self.label_amount)


        self.horizontalLayout_55.addWidget(self.widget_23)


        self.verticalLayout_55.addWidget(self.widget_16)

        self.widget_17 = QWidget(self.frame_9)
        self.widget_17.setObjectName(u"widget_17")
        self.horizontalLayout_59 = QHBoxLayout(self.widget_17)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.widget_25 = QWidget(self.widget_17)
        self.widget_25.setObjectName(u"widget_25")
        self.verticalLayout_56 = QVBoxLayout(self.widget_25)
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.export_btn = QPushButton(self.widget_25)
        self.export_btn.setObjectName(u"export_btn")
        sizePolicy2.setHeightForWidth(self.export_btn.sizePolicy().hasHeightForWidth())
        self.export_btn.setSizePolicy(sizePolicy2)
        self.export_btn.setMaximumSize(QSize(80, 30))
        self.export_btn.setFont(font13)
        self.export_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.export_btn.setLayoutDirection(Qt.RightToLeft)
        self.export_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        icon11 = QIcon()
        icon11.addFile(u":/blueicons/icons/blue_icons/download.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.export_btn.setIcon(icon11)
        self.export_btn.setIconSize(QSize(20, 20))
        self.export_btn.setFlat(False)

        self.verticalLayout_56.addWidget(self.export_btn)


        self.horizontalLayout_59.addWidget(self.widget_25)

        self.widget_24 = QWidget(self.widget_17)
        self.widget_24.setObjectName(u"widget_24")
        self.verticalLayout_57 = QVBoxLayout(self.widget_24)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.delete_btn = QPushButton(self.widget_24)
        self.delete_btn.setObjectName(u"delete_btn")
        sizePolicy2.setHeightForWidth(self.delete_btn.sizePolicy().hasHeightForWidth())
        self.delete_btn.setSizePolicy(sizePolicy2)
        self.delete_btn.setMaximumSize(QSize(80, 30))
        self.delete_btn.setFont(font13)
        self.delete_btn.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.delete_btn.setLayoutDirection(Qt.RightToLeft)
        self.delete_btn.setStyleSheet(u"background-color: rgb(255, 255, 255);\n"
"border-radius: 10px;\n"
"")
        icon12 = QIcon()
        icon12.addFile(u":/blueicons/icons/blue_icons/trash-2.svg", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_btn.setIcon(icon12)
        self.delete_btn.setIconSize(QSize(20, 20))
        self.delete_btn.setFlat(False)

        self.verticalLayout_57.addWidget(self.delete_btn)


        self.horizontalLayout_59.addWidget(self.widget_24)


        self.verticalLayout_55.addWidget(self.widget_17, 0, Qt.AlignHCenter)


        self.horizontalLayout_49.addWidget(self.frame_9)


        self.verticalLayout_51.addWidget(self.frame_7)


        self.verticalLayout_50.addWidget(self.frame_5)

        self.body_frame.addWidget(self.bill_history)

        self.verticalLayout.addWidget(self.body_frame)

        self.verticalSpacer = QSpacerItem(20, 35, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.horizontalLayout.addWidget(self.mainbody)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 892, 19))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)

        self.body_frame.setCurrentIndex(4)
        self.profile_btn.setDefault(False)
        self.add_btn.setDefault(False)
        self.save_btn.setDefault(False)
        self.vis_type.setCurrentIndex(0)
        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label_menu.setText(QCoreApplication.translate("MainWindow", u"MENU", None))
        self.dashboard_btn.setText(QCoreApplication.translate("MainWindow", u" Dashboard", None))
        self.newbill_btn.setText(QCoreApplication.translate("MainWindow", u" New Bill", None))
        self.statistics_btn.setText(QCoreApplication.translate("MainWindow", u" Statistics", None))
        self.logout_btn.setText(QCoreApplication.translate("MainWindow", u" LogOut", None))
        self.menu_btn.setText(QCoreApplication.translate("MainWindow", u"Dashboard", None))
        self.label_pybill.setText(QCoreApplication.translate("MainWindow", u"Py Bill", None))
        self.company_name.setText(QCoreApplication.translate("MainWindow", u"company_name", None))
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
        self.label_bill1.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_cust1.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price1.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate1.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id1.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn1.setText("")
        self.label_bill2.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_5.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_cust2.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_5.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price2.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_5.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate2.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_5.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id2.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn2.setText("")
        self.label_bill3.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_6.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_cust3.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_6.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price3.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_6.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate3.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_6.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id3.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn3.setText("")
        self.label_bill4.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_coustomer_7.setText(QCoreApplication.translate("MainWindow", u"Customer: ", None))
        self.label_cust4.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_total_7.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_price4.setText(QCoreApplication.translate("MainWindow", u"price", None))
        self.label_date_7.setText(QCoreApplication.translate("MainWindow", u"Date:", None))
        self.label_billdate4.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_billid_7.setText(QCoreApplication.translate("MainWindow", u"Bill ID:", None))
        self.label_id4.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.arrow_btn4.setText("")
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
        ___qtablewidgetitem = self.bill_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem1 = self.bill_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem2 = self.bill_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Qty", None));
        ___qtablewidgetitem3 = self.bill_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Price", None));
        ___qtablewidgetitem4 = self.bill_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        ___qtablewidgetitem5 = self.bill_table.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Customer Contact", None));
        self.label.setText(QCoreApplication.translate("MainWindow", u"Bill Tag :", None))
        self.bill_tag_field.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.save_btn.setText(QCoreApplication.translate("MainWindow", u"Save", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Select Type:", None))
        self.vis_type.setItemText(0, QCoreApplication.translate("MainWindow", u"BarChart", None))
        self.vis_type.setItemText(1, QCoreApplication.translate("MainWindow", u"LineGraph", None))
        self.vis_type.setItemText(2, QCoreApplication.translate("MainWindow", u"PieChart", None))

        self.vis_type.setCurrentText(QCoreApplication.translate("MainWindow", u"BarChart", None))
        self.vis_type.setPlaceholderText(QCoreApplication.translate("MainWindow", u"select type", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"TimeFrame:", None))
        self.vis_timeframe.setItemText(0, QCoreApplication.translate("MainWindow", u"Today", None))
        self.vis_timeframe.setItemText(1, QCoreApplication.translate("MainWindow", u"This Week", None))
        self.vis_timeframe.setItemText(2, QCoreApplication.translate("MainWindow", u"This Month", None))

        self.vis_btn.setText(QCoreApplication.translate("MainWindow", u"Visualise", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Bar Chart", None))
        self.label_name.setText(QCoreApplication.translate("MainWindow", u"Bill Name", None))
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Customer :", None))
        self.label_custname.setText(QCoreApplication.translate("MainWindow", u"name", None))
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Bill ID : ", None))
        self.label_id.setText(QCoreApplication.translate("MainWindow", u"id", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Bill date : ", None))
        self.label_date_2.setText(QCoreApplication.translate("MainWindow", u"date", None))
        self.label_14.setText(QCoreApplication.translate("MainWindow", u"Total Amount :", None))
        self.label_amount.setText(QCoreApplication.translate("MainWindow", u"amount", None))
        self.export_btn.setText(QCoreApplication.translate("MainWindow", u"Export", None))
        self.delete_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

