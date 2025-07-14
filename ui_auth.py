# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'auth.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QVBoxLayout, QWidget)

class Ui_Auth(object):
    def setupUi(self, Auth):
        if not Auth.objectName():
            Auth.setObjectName(u"Auth")
        Auth.resize(600, 400)
        Auth.setMinimumSize(QSize(600, 400))
        Auth.setMaximumSize(QSize(800, 600))
        icon = QIcon()
        icon.addFile(u"../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        Auth.setWindowIcon(icon)
        self.centralwidget = QWidget(Auth)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalSpacer = QSpacerItem(20, 0, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setFamilies([u"Arial Black"])
        font.setPointSize(24)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setTextFormat(Qt.AutoText)
        self.label.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label)

        self.verticalSpacer_3 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_3)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lblMachineCode = QLabel(self.centralwidget)
        self.lblMachineCode.setObjectName(u"lblMachineCode")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lblMachineCode.sizePolicy().hasHeightForWidth())
        self.lblMachineCode.setSizePolicy(sizePolicy)
        self.lblMachineCode.setMinimumSize(QSize(0, 51))
        self.lblMachineCode.setMaximumSize(QSize(16777215, 51))
        font1 = QFont()
        font1.setFamilies([u"Arial"])
        font1.setPointSize(16)
        self.lblMachineCode.setFont(font1)

        self.horizontalLayout.addWidget(self.lblMachineCode)

        self.leMachineCode = QLineEdit(self.centralwidget)
        self.leMachineCode.setObjectName(u"leMachineCode")
        self.leMachineCode.setMinimumSize(QSize(0, 51))
        self.leMachineCode.setMaximumSize(QSize(16777215, 51))
        self.leMachineCode.setReadOnly(True)

        self.horizontalLayout.addWidget(self.leMachineCode)

        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(80, 51))
        self.pushButton.setMaximumSize(QSize(80, 51))

        self.horizontalLayout.addWidget(self.pushButton)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.verticalSpacer_4 = QSpacerItem(20, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.lblAuthCode = QLabel(self.centralwidget)
        self.lblAuthCode.setObjectName(u"lblAuthCode")
        sizePolicy.setHeightForWidth(self.lblAuthCode.sizePolicy().hasHeightForWidth())
        self.lblAuthCode.setSizePolicy(sizePolicy)
        self.lblAuthCode.setMinimumSize(QSize(0, 51))
        self.lblAuthCode.setMaximumSize(QSize(16777215, 51))
        self.lblAuthCode.setFont(font1)

        self.horizontalLayout_2.addWidget(self.lblAuthCode)

        self.leAuthCode = QLineEdit(self.centralwidget)
        self.leAuthCode.setObjectName(u"leAuthCode")
        self.leAuthCode.setMinimumSize(QSize(0, 51))
        self.leAuthCode.setMaximumSize(QSize(16777215, 51))

        self.horizontalLayout_2.addWidget(self.leAuthCode)

        self.btnHelp = QPushButton(self.centralwidget)
        self.btnHelp.setObjectName(u"btnHelp")
        self.btnHelp.setMinimumSize(QSize(80, 51))
        self.btnHelp.setMaximumSize(QSize(80, 51))

        self.horizontalLayout_2.addWidget(self.btnHelp)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.verticalSpacer_5 = QSpacerItem(17, 18, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer_5)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.chkDebug = QCheckBox(self.centralwidget)
        self.chkDebug.setObjectName(u"chkDebug")
        self.chkDebug.setMinimumSize(QSize(0, 51))
        self.chkDebug.setMaximumSize(QSize(16777215, 51))
        self.chkDebug.setFont(font1)

        self.horizontalLayout_3.addWidget(self.chkDebug)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.btnOk = QPushButton(self.centralwidget)
        self.btnOk.setObjectName(u"btnOk")
        self.btnOk.setMinimumSize(QSize(150, 51))
        self.btnOk.setMaximumSize(QSize(150, 51))
        font2 = QFont()
        font2.setBold(True)
        self.btnOk.setFont(font2)

        self.horizontalLayout_3.addWidget(self.btnOk)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_3)

        self.btnTryUse = QPushButton(self.centralwidget)
        self.btnTryUse.setObjectName(u"btnTryUse")
        self.btnTryUse.setMinimumSize(QSize(80, 51))
        self.btnTryUse.setMaximumSize(QSize(80, 51))

        self.horizontalLayout_3.addWidget(self.btnTryUse)


        self.verticalLayout.addLayout(self.horizontalLayout_3)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 1, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer_2)

        Auth.setCentralWidget(self.centralwidget)

        self.retranslateUi(Auth)

        QMetaObject.connectSlotsByName(Auth)
    # setupUi

    def retranslateUi(self, Auth):
        Auth.setWindowTitle(QCoreApplication.translate("Auth", u"\u5b57\u5e55\u751f\u6210\u5668", None))
        Auth.setStyleSheet(QCoreApplication.translate("Auth", u"QWidget#Auth {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border-radius: 5px;\n"
"}\n"
"QWidget#centralwidget {\n"
"    background: transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"QLabel#label {\n"
"    color: white;\n"
"    font-weight: bold;\n"
"}\n"
"\n"
"QLabel#lblMachineCode, QLabel#lblAuthCode {\n"
"    color: white;\n"
"    background: rgba(255, 255, 255, 10);\n"
"    border-radius: 5px;\n"
"    padding: 5px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    color: #333;\n"
"    font-size: 14px;\n"
"}\n"
"\n"
"QLineEdit:focus {\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"    background: rgba(255, 255, 255, 95);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 2"
                        "55, 60));\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 5px;\n"
"    color: white;\n"
"    font-weight: bold;\n"
"    padding: 8px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 60), stop:1 rgba(255, 255, 255, 40));\n"
"}\n"
"\n"
"QPushButton#btnOk {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border: 1px solid rgba(79, 172, 254, 150);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#btnOk:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5fbdff, stop:1 #10f3ff);\n"
"    border: 1px solid rgba(95, 189, 255, 200);\n"
"}\n"
"\n"
"QCheckBox {\n"
"    color: white;\n"
"    spacing: 8px;\n"
"}\n"
"\n"
"QCheckBox::indica"
                        "tor {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 3px;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    background: rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border: 1px solid rgba(79, 172, 254, 150);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5fbdff, stop:1 #10f3ff);\n"
"}", None))
        self.label.setText(QCoreApplication.translate("Auth", u"\u6b22\u8fce\u4f7f\u7528\u5b57\u5e55\u751f\u6210\u5668", None))
        self.lblMachineCode.setText(QCoreApplication.translate("Auth", u"\u673a\u5668\u7801:", None))
        self.pushButton.setText(QCoreApplication.translate("Auth", u"\u70b9\u51fb\u590d\u5236", None))
        self.lblAuthCode.setText(QCoreApplication.translate("Auth", u"\u6388\u6743\u7801:", None))
        self.btnHelp.setText(QCoreApplication.translate("Auth", u"\u4f7f\u7528\u5e2e\u52a9", None))
        self.chkDebug.setText(QCoreApplication.translate("Auth", u"\u5f00\u542f\u8c03\u8bd5", None))
        self.btnOk.setText(QCoreApplication.translate("Auth", u"\u6388\u6743", None))
        self.btnTryUse.setText(QCoreApplication.translate("Auth", u"\u8bd5\u7528\u4e00\u4e0b", None))
    # retranslateUi

