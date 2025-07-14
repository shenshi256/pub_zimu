# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'helpshow.ui'
##
## Created by: Qt User Interface Compiler version 6.9.1
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QSpacerItem, QTextBrowser,
    QVBoxLayout, QWidget)

class Ui_HelpShow(object):
    def setupUi(self, HelpShow):
        if not HelpShow.objectName():
            HelpShow.setObjectName(u"HelpShow")
        HelpShow.resize(600, 400)
        HelpShow.setMinimumSize(QSize(600, 400))
        HelpShow.setMaximumSize(QSize(800, 600))
        self.centralwidget = QWidget(HelpShow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.lblHelp = QLabel(self.centralwidget)
        self.lblHelp.setObjectName(u"lblHelp")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(24)
        font.setBold(True)
        self.lblHelp.setFont(font)
        self.lblHelp.setTextFormat(Qt.AutoText)
        self.lblHelp.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.lblHelp)

        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)

        self.verticalLayout.addWidget(self.textBrowser)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(144, 31))
        self.pushButton.setMaximumSize(QSize(16777215, 31))
        font1 = QFont()
        font1.setBold(True)
        self.pushButton.setFont(font1)

        self.horizontalLayout.addWidget(self.pushButton)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout.addLayout(self.horizontalLayout)

        HelpShow.setCentralWidget(self.centralwidget)

        self.retranslateUi(HelpShow)

        QMetaObject.connectSlotsByName(HelpShow)
    # setupUi

    def retranslateUi(self, HelpShow):
        HelpShow.setWindowTitle(QCoreApplication.translate("HelpShow", u"MainWindow", None))
        HelpShow.setStyleSheet(QCoreApplication.translate("HelpShow", u"QWidget#HelpShow {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border-radius: 8px;\n"
"}\n"
"QWidget#centralwidget {\n"
"    background: transparent;\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#lblHelp {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    margin:10px;\n"
"}\n"
"\n"
"QTextBrowser {\n"
"    background: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    padding: 15px;\n"
"    color: #333;\n"
"    font-size: 14px;\n"
"    selection-background-color: rgba(79, 172, 254, 100);\n"
"}\n"
"\n"
"QTextBrowser::vertical-scroll-bar {\n"
"    background: rgba(255, 255, 255, 30);\n"
"    width: 12px;\n"
"    border-radius: 6px;\n"
"}\n"
"\n"
"QTextBrowser::vertical-scroll-bar:hover {\n"
"    background: rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"QTextBrowser::handle:vertical {\n"
"    background: rgba(100, 100, 100, 150);\n"
"    border-rad"
                        "ius: 6px;\n"
"    min-height: 20px;\n"
"}\n"
"\n"
"QTextBrowser::handle:vertical:hover {\n"
"    background: rgba(100, 100, 100, 200);\n"
"}\n"
"\n"
"QTextBrowser::add-line:vertical, QTextBrowser::sub-line:vertical {\n"
"    border: none;\n"
"    background: none;\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));\n"
"    border: 2px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-size: 12px;\n"
"\n"
"    font-weight: bold;\n"
"    padding: 8px 20px;\n"
"    min-width: 100px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 60), stop:1 rgba(255, 255, 255, 40));\n"
"}", None))
        self.lblHelp.setText(QCoreApplication.translate("HelpShow", u"\u6a21\u578b\u4f7f\u7528\u5e2e\u52a9", None))
        self.pushButton.setText(QCoreApplication.translate("HelpShow", u"\u5173\u95ed", None))
    # retranslateUi

