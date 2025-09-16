# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QGroupBox, QHBoxLayout,
    QLabel, QMainWindow, QProgressBar, QPushButton,
    QRadioButton, QSizePolicy, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.setWindowModality(Qt.WindowModality.NonModal)
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QSize(600, 400))
        MainWindow.setMaximumSize(QSize(800, 600))
        MainWindow.setMouseTracking(False)
        MainWindow.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralWidget = QWidget(MainWindow)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setContentsMargins(11, 11, 11, 11)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.textEdit = QTextEdit(self.centralWidget)
        self.textEdit.setObjectName(u"textEdit")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit.sizePolicy().hasHeightForWidth())
        self.textEdit.setSizePolicy(sizePolicy)
        self.textEdit.setMinimumSize(QSize(381, 31))
        self.textEdit.setMaximumSize(QSize(16777215, 31))
        self.textEdit.setAcceptDrops(True)
        self.textEdit.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.textEdit.setLineWrapMode(QTextEdit.NoWrap)

        self.horizontalLayout.addWidget(self.textEdit)

        self.pushButton = QPushButton(self.centralWidget)
        self.pushButton.setObjectName(u"pushButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy1)
        self.pushButton.setMinimumSize(QSize(81, 31))
        self.pushButton.setMaximumSize(QSize(81, 31))

        self.horizontalLayout.addWidget(self.pushButton)

        self.pushButton_4 = QPushButton(self.centralWidget)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setMinimumSize(QSize(100, 31))
        self.pushButton_4.setMaximumSize(QSize(100, 31))

        self.horizontalLayout.addWidget(self.pushButton_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox = QComboBox(self.centralWidget)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy)
        self.comboBox.setMinimumSize(QSize(300, 31))

        self.horizontalLayout_2.addWidget(self.comboBox)

        self.pushButton_2 = QPushButton(self.centralWidget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        sizePolicy1.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy1)
        self.pushButton_2.setMinimumSize(QSize(81, 31))
        self.pushButton_2.setMaximumSize(QSize(81, 31))

        self.horizontalLayout_2.addWidget(self.pushButton_2)

        self.pushButton_3 = QPushButton(self.centralWidget)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setMinimumSize(QSize(100, 31))
        self.pushButton_3.setMaximumSize(QSize(100, 31))

        self.horizontalLayout_2.addWidget(self.pushButton_3)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(6)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.outputType = QGroupBox(self.centralWidget)
        self.outputType.setObjectName(u"outputType")
        self.outputType.setMinimumSize(QSize(0, 61))
        self.outputType.setMaximumSize(QSize(16777215, 61))
        self.layoutWidget = QWidget(self.outputType)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 21, 371, 33))
        self.horizontalLayout_5 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.srtType = QRadioButton(self.layoutWidget)
        self.srtType.setObjectName(u"srtType")
        self.srtType.setMinimumSize(QSize(0, 31))
        self.srtType.setSizeIncrement(QSize(0, 31))
        self.srtType.setChecked(True)

        self.horizontalLayout_5.addWidget(self.srtType)

        self.txtType = QRadioButton(self.layoutWidget)
        self.txtType.setObjectName(u"txtType")
        self.txtType.setMinimumSize(QSize(0, 31))
        self.txtType.setMaximumSize(QSize(16777215, 31))
        self.txtType.setSizeIncrement(QSize(0, 31))

        self.horizontalLayout_5.addWidget(self.txtType)

        self.vttType = QRadioButton(self.layoutWidget)
        self.vttType.setObjectName(u"vttType")
        self.vttType.setMinimumSize(QSize(0, 31))
        self.vttType.setMaximumSize(QSize(16777215, 31))
        self.vttType.setSizeIncrement(QSize(0, 31))

        self.horizontalLayout_5.addWidget(self.vttType)

        self.jsonType = QRadioButton(self.layoutWidget)
        self.jsonType.setObjectName(u"jsonType")
        self.jsonType.setMinimumSize(QSize(0, 31))
        self.jsonType.setMaximumSize(QSize(16777215, 31))
        self.jsonType.setSizeIncrement(QSize(0, 31))

        self.horizontalLayout_5.addWidget(self.jsonType)


        self.horizontalLayout_6.addWidget(self.outputType)

        self.groupBox = QGroupBox(self.centralWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(200, 61))
        self.groupBox.setMaximumSize(QSize(200, 61))
        self.horizontalLayout_3 = QHBoxLayout(self.groupBox)
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setContentsMargins(11, 11, 11, 11)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.memoryRate = QLabel(self.groupBox)
        self.memoryRate.setObjectName(u"memoryRate")
        sizePolicy.setHeightForWidth(self.memoryRate.sizePolicy().hasHeightForWidth())
        self.memoryRate.setSizePolicy(sizePolicy)
        self.memoryRate.setMinimumSize(QSize(0, 35))
        self.memoryRate.setMaximumSize(QSize(16777215, 35))
        self.memoryRate.setSizeIncrement(QSize(0, 0))
        self.memoryRate.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_3.addWidget(self.memoryRate)


        self.horizontalLayout_6.addWidget(self.groupBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_6)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.isDebug = QGroupBox(self.centralWidget)
        self.isDebug.setObjectName(u"isDebug")
        self.isDebug.setMinimumSize(QSize(0, 51))
        self.isDebug.setMaximumSize(QSize(16777215, 51))
        self.noDebug = QRadioButton(self.isDebug)
        self.noDebug.setObjectName(u"noDebug")
        self.noDebug.setGeometry(QRect(90, 20, 61, 31))
        self.noDebug.setMinimumSize(QSize(0, 31))
        self.noDebug.setMaximumSize(QSize(16777215, 31))
        self.noDebug.setChecked(True)
        self.yesDebug = QRadioButton(self.isDebug)
        self.yesDebug.setObjectName(u"yesDebug")
        self.yesDebug.setGeometry(QRect(10, 20, 61, 31))
        self.yesDebug.setMinimumSize(QSize(0, 31))
        self.yesDebug.setMaximumSize(QSize(16777215, 31))
        self.yesDebug.setChecked(False)

        self.horizontalLayout_4.addWidget(self.isDebug)

        self.isChineseSimplified = QGroupBox(self.centralWidget)
        self.isChineseSimplified.setObjectName(u"isChineseSimplified")
        self.isChineseSimplified.setMinimumSize(QSize(0, 51))
        self.isChineseSimplified.setMaximumSize(QSize(16777215, 51))
        self.noSimple = QRadioButton(self.isChineseSimplified)
        self.noSimple.setObjectName(u"noSimple")
        self.noSimple.setGeometry(QRect(100, 20, 81, 31))
        self.noSimple.setMinimumSize(QSize(0, 31))
        self.noSimple.setSizeIncrement(QSize(0, 31))
        self.noSimple.setChecked(True)
        self.yesSimple = QRadioButton(self.isChineseSimplified)
        self.yesSimple.setObjectName(u"yesSimple")
        self.yesSimple.setGeometry(QRect(10, 20, 71, 31))
        self.yesSimple.setMinimumSize(QSize(0, 31))
        self.yesSimple.setSizeIncrement(QSize(0, 31))
        self.yesSimple.setChecked(False)

        self.horizontalLayout_4.addWidget(self.isChineseSimplified)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.progressBar = QProgressBar(self.centralWidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setMinimumSize(QSize(0, 10))
        self.progressBar.setMaximumSize(QSize(16777215, 10))
        self.progressBar.setValue(24)

        self.verticalLayout.addWidget(self.progressBar)

        self.textEdit_2 = QTextEdit(self.centralWidget)
        self.textEdit_2.setObjectName(u"textEdit_2")
        self.textEdit_2.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        self.verticalLayout.addWidget(self.textEdit_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setStyleSheet(QCoreApplication.translate("MainWindow", u"QWidget#MainWindow {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QWidget#centralWidget {\n"
"    background: transparent;\n"
"    border-radius: 5px;\n"
"}\n"
"\n"
"QLabel {\n"
"    color: white; \n"
"}\n"
"\n"
"QLabel#memoryRate {\n"
"    color: white;\n"
"    background: rgba(255, 255, 255, 15);\n"
"    border-radius: 5px;\n"
"    padding: 0px 10px 0px 0px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    background: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    padding: 8px;\n"
"    color: #333;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QTextEdit:focus {\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"    background: rgba(255, 255, 255, 95);\n"
"}\n"
"QComboBox {\n"
"    background: rgba(255, 255, 255, 90);\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    padding: 8px 30px 8px 12px;\n"
"    color: "
                        "#333;\n"
"    font-size: 12px; \n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    \n"
"     background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QComboBox:focus {\n"
"     border: 1px solid rgba(255, 255, 255, 150);\n"
"    background: rgba(255, 255, 255, 95);\n"
"    outline: none;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"    background: rgba(255, 255, 255, 0.95);\n"
"    border: 1px solid rgba(255, 255, 255, 0.3);\n"
"    border-radius: 5px;\n"
"    selection-background-color: #4CAF50;\n"
"    color: #333;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    border-radius: 5px;\n"
"    color: white; \n"
"    padding: 8px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qlineargradient("
                        "x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));\n"
"    border: 1px solid rgba(255, 255, 255, 150);\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 60), stop:1 rgba(255, 255, 255, 40));\n"
"}\n"
"\n"
"QPushButton#pushButton_2 {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border: 1px solid rgba(79, 172, 254, 150);\n"
"    color: white;\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 #5fbdff, stop:1 #10f3ff);\n"
"    border: 1px solid rgba(95, 189, 255, 200);\n"
"}\n"
"\n"
"QGroupBox {\n"
"    color: white; \n"
"    font-size: 12px;\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    margin-top: 10px;\n"
"    background: rgba(255, 255, 255, 10);\n"
"}\n"
"\n"
"QGroupBox::title {\n"
"    subcontrol-origin: margin;\n"
"    left: 10px;\n"
"   "
                        " padding: 2px 5px 5px 5px;\n"
"    background: transparent;\n"
"}\n"
"\n"
"QRadioButton {\n"
"    color: white;\n"
"    spacing: 8px;\n"
"    font-size: 12px;\n"
"}\n"
"\n"
"QRadioButton::indicator {\n"
"    width: 18px;\n"
"    height: 18px;\n"
"    border-radius: 9px;\n"
"    border: 1px solid rgba(255, 255, 255, 100);\n"
"    background: rgba(255, 255, 255, 30);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border: 1px solid rgba(79, 172, 254, 150);\n"
"}\n"
"\n"
"QRadioButton::indicator:checked:hover {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #5fbdff, stop:1 #10f3ff);\n"
"}\n"
"\n"
"QProgressBar {\n"
"    border: 1px solid rgba(255, 255, 255, 50);\n"
"    border-radius: 5px;\n"
"    background: rgba(255, 255, 255, 20);\n"
"    text-align: center;\n"
"    color: white; \n"
"    font-size:8px;\n"
"}\n"
"\n"
"QProgressBar::chunk {\n"
"    background: qlineargradient(x1:0, y1:0, x2:"
                        "1, y2:0, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border-radius: 5px;\n"
"    margin: 1px;\n"
"}", None))
#if QT_CONFIG(tooltip)
        self.textEdit.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u97f3\u89c6\u9891\u6587\u4ef6", None))
#endif // QT_CONFIG(tooltip)
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u6587\u4ef6", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u9879\u76ee\u4f7f\u7528\u8bf4\u660e", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6a21\u578b", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"large-v3", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"small", None))

        self.comboBox.setCurrentText(QCoreApplication.translate("MainWindow", u"\u8bf7\u9009\u62e9\u6a21\u578b", None))
        self.pushButton_2.setText(QCoreApplication.translate("MainWindow", u"\u5f00\u59cb\u751f\u6210", None))
        self.pushButton_3.setText(QCoreApplication.translate("MainWindow", u"\u6a21\u578b\u4f7f\u7528\u5e2e\u52a9", None))
        self.outputType.setTitle(QCoreApplication.translate("MainWindow", u"\u8f93\u51fa\u7c7b\u578b", None))
#if QT_CONFIG(tooltip)
        self.srtType.setToolTip(QCoreApplication.translate("MainWindow", u"\u5e26\u65f6\u95f4\u6761, \u652f\u6301\u5bfc\u5165\u5230\u526a\u8f91\u5de5\u5177\u4e2d", None))
#endif // QT_CONFIG(tooltip)
        self.srtType.setText(QCoreApplication.translate("MainWindow", u"srt", None))
#if QT_CONFIG(tooltip)
        self.txtType.setToolTip(QCoreApplication.translate("MainWindow", u"\u7eaf\u5b57\u5e55\u6587\u672c", None))
#endif // QT_CONFIG(tooltip)
        self.txtType.setText(QCoreApplication.translate("MainWindow", u"txt", None))
        self.vttType.setText(QCoreApplication.translate("MainWindow", u"vtt", None))
        self.jsonType.setText(QCoreApplication.translate("MainWindow", u"json", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u7cfb\u7edf\u4fe1\u606f", None))
        self.memoryRate.setText(QCoreApplication.translate("MainWindow", u"\u8fdb\u7a0b: \u5185\u5b58 321M,CPU: 0% \n"
"\u7cfb\u7edf: \u5185\u5b58 92%, CPU: 0%", None))
        self.isDebug.setTitle(QCoreApplication.translate("MainWindow", u"\u5f00\u542f\u8c03\u8bd5", None))
#if QT_CONFIG(tooltip)
        self.noDebug.setToolTip(QCoreApplication.translate("MainWindow", u"\u5e73\u65f6\u7684\u65f6\u5019, \u5e94\u8be5\u5173\u95ed\u65e5\u5fd7", None))
#endif // QT_CONFIG(tooltip)
        self.noDebug.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
#if QT_CONFIG(tooltip)
        self.yesDebug.setToolTip(QCoreApplication.translate("MainWindow", u"\u8bb0\u5f55\u65e5\u5fd7, \u5e38\u7528\u4e8e\u7a0b\u5e8f\u8c03\u8bd5", None))
#endif // QT_CONFIG(tooltip)
        self.yesDebug.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
        self.isChineseSimplified.setTitle(QCoreApplication.translate("MainWindow", u"\u4e2d\u6587\u65f6\u603b\u662f\u7b80\u4f53", None))
#if QT_CONFIG(tooltip)
        self.noSimple.setToolTip(QCoreApplication.translate("MainWindow", u"\u7531\u6a21\u578b\u81ea\u884c\u63a8\u65ad\u7b80\u4f53\u7e41\u4f53, \u6e2f\u53f0\u8154\u591a\u4f1a\u63a8\u6210\u7e41\u4f53", None))
#endif // QT_CONFIG(tooltip)
        self.noSimple.setText(QCoreApplication.translate("MainWindow", u"\u5426", None))
#if QT_CONFIG(tooltip)
        self.yesSimple.setToolTip(QCoreApplication.translate("MainWindow", u"\u7edf\u4e00\u4f7f\u7528\u7b80\u4f53, \u5982\u679c\u662f\u7e41\u4f53\u5219\u81ea\u52a8\u8f6c\u6362\u6210\u7b80\u4f53", None))
#endif // QT_CONFIG(tooltip)
        self.yesSimple.setText(QCoreApplication.translate("MainWindow", u"\u662f", None))
    # retranslateUi

