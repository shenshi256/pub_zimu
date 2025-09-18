# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'splashscreen.ui'
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
    QProgressBar, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_SplashScreen(object):
    def setupUi(self, SplashScreen):
        if not SplashScreen.objectName():
            SplashScreen.setObjectName(u"SplashScreen")
        SplashScreen.resize(600, 400)
        SplashScreen.setMinimumSize(QSize(600, 400))
        SplashScreen.setMaximumSize(QSize(800, 600))
        # 再需要自定义背景、透明效果, 禁用窗口的自动背景填充
        SplashScreen.setAutoFillBackground(False)
        self.centralwidget = QWidget(SplashScreen)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.topLayout = QHBoxLayout()
        self.topLayout.setObjectName(u"topLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.topLayout.addItem(self.horizontalSpacer)

        self.closeButton = QLabel(self.centralwidget)
        self.closeButton.setObjectName(u"closeButton")
        self.closeButton.setMinimumSize(QSize(30, 30))
        self.closeButton.setMaximumSize(QSize(30, 30))
        font = QFont()
        font.setPointSize(16)
        font.setBold(True)
        self.closeButton.setFont(font)
        self.closeButton.setAlignment(Qt.AlignCenter)

        self.topLayout.addWidget(self.closeButton)


        self.verticalLayout_2.addLayout(self.topLayout)

        self.topSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.topSpacer)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.logoLabel = QLabel(self.centralwidget)
        self.logoLabel.setObjectName(u"logoLabel")
        self.logoLabel.setMinimumSize(QSize(64, 64))
        self.logoLabel.setMaximumSize(QSize(64, 64))
        font1 = QFont()
        font1.setPointSize(36)
        self.logoLabel.setFont(font1)
        self.logoLabel.setAlignment(Qt.AlignCenter)

        self.horizontalLayout.addWidget(self.logoLabel)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.appNameLabel = QLabel(self.centralwidget)
        self.appNameLabel.setObjectName(u"appNameLabel")
        font2 = QFont()
        font2.setPointSize(24)
        font2.setBold(True)
        self.appNameLabel.setFont(font2)
        self.appNameLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.appNameLabel)

        self.verticalSpacer = QSpacerItem(20, 10, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.subtitleLabel = QLabel(self.centralwidget)
        self.subtitleLabel.setObjectName(u"subtitleLabel")
        font3 = QFont()
        font3.setPointSize(10)
        self.subtitleLabel.setFont(font3)
        self.subtitleLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout_2.addWidget(self.subtitleLabel)

        self.middleSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_2.addItem(self.middleSpacer)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.loadingLabel = QLabel(self.centralwidget)
        self.loadingLabel.setObjectName(u"loadingLabel")
        font4 = QFont()
        font4.setPointSize(9)
        self.loadingLabel.setFont(font4)
        self.loadingLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.loadingLabel)

        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(250, 6))
        self.progressBar.setMaximumSize(QSize(250, 6))
        self.progressBar.setValue(0)
        self.progressBar.setTextVisible(False)

        self.verticalLayout.addWidget(self.progressBar, 0, Qt.AlignHCenter)

        self.bottomSpacer = QSpacerItem(20, 20, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.bottomSpacer)

        self.versionLabel = QLabel(self.centralwidget)
        self.versionLabel.setObjectName(u"versionLabel")
        font5 = QFont()
        font5.setPointSize(8)
        self.versionLabel.setFont(font5)
        self.versionLabel.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.versionLabel)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        SplashScreen.setCentralWidget(self.centralwidget)

        self.retranslateUi(SplashScreen)

        QMetaObject.connectSlotsByName(SplashScreen)
    # setupUi

    def retranslateUi(self, SplashScreen):
        SplashScreen.setWindowTitle(QCoreApplication.translate("SplashScreen", u"\u5b57\u5e55\u751f\u6210\u5668", None))
        SplashScreen.setStyleSheet(QCoreApplication.translate("SplashScreen", u"QWidget#SplashScreen {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border-radius: 8px;\n"
"}\n"
"QWidget#centralwidget {\n"
"    background: transparent; /* \u80cc\u666f\u900f\u660e */\n"
"    border-radius: 8px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white;\n"
"}\n"
"\n"
"#logoLabel {\n"
"    background: rgba(255, 255, 255, 30);\n"
"    border-radius: 5px;  \n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"}\n"
"\n"
"#progressBar {\n"
"    background: rgba(255, 255, 255, 50);\n"
"    border-radius: 3px;\n"
"    text-align: center;\n"
"}\n"
"\n"
"#progressBar::chunk {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border-radius: 3px;\n"
"}\n"
"\n"
"#closeButton {\n"
"    color: white;\n"
"    background: rgba(255, 255, 255, 20);\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"#closeButton:hover {\n"
"    background: rgba(255, 0, 0, 100);\n"
"    bor"
                        "der: 1px solid rgba(255, 0, 0, 150);\n"
"}", None))
        self.closeButton.setStyleSheet(QCoreApplication.translate("SplashScreen", u"QLabel#closeButton {\n"
"    color: white;\n"
"    background: rgba(255, 255, 255, 20);\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}\n"
"QLabel#closeButton:hover {\n"
"    background: rgba(255, 0, 0, 100);\n"
"    border: 1px solid rgba(255, 0, 0, 150);\n"
"}", None))
        self.closeButton.setText(QCoreApplication.translate("SplashScreen", u"\u00d7", None))
        self.logoLabel.setText(QCoreApplication.translate("SplashScreen", u"APP", None))
        self.appNameLabel.setText(QCoreApplication.translate("SplashScreen", u"\u5b57\u5e55\u751f\u6210\u5668", None))
        self.subtitleLabel.setText(QCoreApplication.translate("SplashScreen", u"\u57fa\u4e8e OpenAI Whisper \u7684\u667a\u80fd\u8bed\u97f3\u8f6c\u5b57\u5e55\u5de5\u5177", None))
        self.loadingLabel.setText(QCoreApplication.translate("SplashScreen", u"\u6b63\u5728\u521d\u59cb\u5316...", None))
        self.versionLabel.setText(QCoreApplication.translate("SplashScreen", u"Version 1.0.1", None))
    # retranslateUi

