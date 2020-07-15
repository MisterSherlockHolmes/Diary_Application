# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'diary.ui'
##
## Created by: Qt User Interface Compiler version 5.14.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QMetaObject, QObject, QPoint,
    QRect, QSize, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QLinearGradient, QPalette, QPainter, QPixmap,
    QRadialGradient)
from PySide2.QtWidgets import *


class Ui_Diary(object):
    def setupUi(self, Diary):
        if Diary.objectName():
            Diary.setObjectName(u"Diary")
        Diary.resize(1047, 643)
        self.centralwidget = QWidget(Diary)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName(u"horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(70, 80, 911, 80))
        self.horizontalLayout = QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.rb_background_music = QRadioButton(self.horizontalLayoutWidget)
        self.rb_background_music.setObjectName(u"rb_background_music")

        self.horizontalLayout.addWidget(self.rb_background_music)

        self.pb_time = QPushButton(self.horizontalLayoutWidget)
        self.pb_time.setObjectName(u"pb_time")

        self.horizontalLayout.addWidget(self.pb_time)

        self.pte_diary = QPlainTextEdit(self.centralwidget)
        self.pte_diary.setObjectName(u"pte_diary")
        self.pte_diary.setGeometry(QRect(70, 170, 911, 341))
        font = QFont()
        font.setFamily(u"\u65b9\u6b63\u5b57\u8ff9-\u6d77\u4f53\u6b63\u6977 \u7b80")
        font.setPointSize(14)
        self.pte_diary.setFont(font)
        self.title = QLabel(self.centralwidget)
        self.title.setObjectName(u"title")
        self.title.setGeometry(QRect(390, 10, 331, 61))
        font1 = QFont()
        font1.setFamily(u"\u65b9\u6b63\u5b57\u8ff9-\u6d77\u4f53\u6b63\u6977 \u7b80")
        font1.setPointSize(48)
        self.title.setFont(font1)
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 181, 20))
        font2 = QFont()
        font2.setFamily(u"\u9ed1\u4f53")
        font2.setPointSize(13)
        self.label.setFont(font2)
        self.horizontalLayoutWidget_2 = QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setObjectName(u"horizontalLayoutWidget_2")
        self.horizontalLayoutWidget_2.setGeometry(QRect(70, 520, 911, 80))
        self.horizontalLayout_2 = QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.pb_choose_file = QPushButton(self.horizontalLayoutWidget_2)
        self.pb_choose_file.setObjectName(u"pb_choose_file")

        self.horizontalLayout_2.addWidget(self.pb_choose_file)

        self.pb_finish = QPushButton(self.horizontalLayoutWidget_2)
        self.pb_finish.setObjectName(u"pb_finish")

        self.horizontalLayout_2.addWidget(self.pb_finish)

        Diary.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(Diary)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1047, 23))
        Diary.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(Diary)
        self.statusbar.setObjectName(u"statusbar")
        Diary.setStatusBar(self.statusbar)

        self.retranslateUi(Diary)

        QMetaObject.connectSlotsByName(Diary)
    # setupUi

    def retranslateUi(self, Diary):
        Diary.setWindowTitle(QCoreApplication.translate("Diary", u"\u65e5\u8bb0\u7f16\u8f91\u8f6f\u4ef6", None))
        self.rb_background_music.setText(QCoreApplication.translate("Diary", u"\u80cc\u666f\u97f3\u4e50", None))
        self.pb_time.setText(QCoreApplication.translate("Diary", u"\u73b0\u5728\u65f6\u95f4", None))
        self.pte_diary.setPlainText(QCoreApplication.translate("Diary", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.pte_diary.setPlaceholderText(QCoreApplication.translate("Diary", u"\u8bf7\u8f93\u5165\u5185\u5bb9", None))
        self.title.setText(QCoreApplication.translate("Diary", u"\u65e5\u8bb0\u7f16\u8f91\u5668", None))
        self.label.setText(QCoreApplication.translate("Diary", u"\u5341\u5b57\u5144\u5f1f\u6709\u9650\u516c\u53f8\u51fa\u54c1", None))
        self.pb_choose_file.setText(QCoreApplication.translate("Diary", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pb_finish.setText(QCoreApplication.translate("Diary", u"\u7f16\u8f91\u5b8c\u6210", None))
    # retranslateUi

