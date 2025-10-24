# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'batchfilelist.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

class Ui_BatchFileList(object):
    def setupUi(self, BatchFileList):
        if not BatchFileList.objectName():
            BatchFileList.setObjectName(u"BatchFileList")
        BatchFileList.setWindowModality(Qt.NonModal)
        BatchFileList.resize(600, 400)
        BatchFileList.setMinimumSize(QSize(600, 400))
        BatchFileList.setMaximumSize(QSize(800, 600))
        BatchFileList.setMouseTracking(False)
        BatchFileList.setAcceptDrops(False)
        icon = QIcon()
        icon.addFile(u"../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        BatchFileList.setWindowIcon(icon)
        self.centralWidget = QWidget(BatchFileList)
        self.centralWidget.setObjectName(u"centralWidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.detailTitlebar = QHBoxLayout()
        self.detailTitlebar.setObjectName(u"detailTitlebar")
        self.detailTitle = QLabel(self.centralWidget)
        self.detailTitle.setObjectName(u"detailTitle")
        self.detailTitle.setMinimumSize(QSize(0, 31))
        self.detailTitle.setAlignment(Qt.AlignVCenter)

        self.detailTitlebar.addWidget(self.detailTitle)

        self.detailTitle_spacer = QSpacerItem(20, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.detailTitlebar.addItem(self.detailTitle_spacer)

        self.detailActions = QHBoxLayout()
        self.detailActions.setObjectName(u"detailActions")
        self.addMoreBtn = QPushButton(self.centralWidget)
        self.addMoreBtn.setObjectName(u"addMoreBtn")
        self.addMoreBtn.setMinimumSize(QSize(81, 31))
        self.addMoreBtn.setMaximumSize(QSize(120, 31))

        self.detailActions.addWidget(self.addMoreBtn)

        self.clearBtn = QPushButton(self.centralWidget)
        self.clearBtn.setObjectName(u"clearBtn")
        self.clearBtn.setMinimumSize(QSize(81, 31))
        self.clearBtn.setMaximumSize(QSize(120, 31))

        self.detailActions.addWidget(self.clearBtn)

        self.selectAllBtn = QPushButton(self.centralWidget)
        self.selectAllBtn.setObjectName(u"selectAllBtn")
        self.selectAllBtn.setMinimumSize(QSize(100, 31))
        self.selectAllBtn.setMaximumSize(QSize(140, 31))

        self.detailActions.addWidget(self.selectAllBtn)

        self.closeDetailBtn = QPushButton(self.centralWidget)
        self.closeDetailBtn.setObjectName(u"closeDetailBtn")
        self.closeDetailBtn.setMinimumSize(QSize(81, 31))
        self.closeDetailBtn.setMaximumSize(QSize(120, 31))

        self.detailActions.addWidget(self.closeDetailBtn)


        self.detailTitlebar.addLayout(self.detailActions)


        self.verticalLayout_2.addLayout(self.detailTitlebar)

        self.fileCountBar = QHBoxLayout()
        self.fileCountBar.setObjectName(u"fileCountBar")
        self.fileCount = QLabel(self.centralWidget)
        self.fileCount.setObjectName(u"fileCount")
        self.fileCount.setMinimumSize(QSize(0, 28))
        self.fileCount.setAlignment(Qt.AlignVCenter)

        self.fileCountBar.addWidget(self.fileCount)


        self.verticalLayout_2.addLayout(self.fileCountBar)

        self.fileTable = QTableWidget(self.centralWidget)
        if (self.fileTable.columnCount() < 7):
            self.fileTable.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.fileTable.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        self.fileTable.setObjectName(u"fileTable")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.fileTable.sizePolicy().hasHeightForWidth())
        self.fileTable.setSizePolicy(sizePolicy)
        self.fileTable.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.fileTable.setAlternatingRowColors(True)
        self.fileTable.setSelectionMode(QAbstractItemView.ExtendedSelection)
        self.fileTable.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.fileTable.setShowGrid(True)
        self.fileTable.setRowCount(0)
        self.fileTable.setColumnCount(7)

        self.verticalLayout_2.addWidget(self.fileTable)

        BatchFileList.setCentralWidget(self.centralWidget)

        self.retranslateUi(BatchFileList)

        QMetaObject.connectSlotsByName(BatchFileList)
    # setupUi

    def retranslateUi(self, BatchFileList):
        BatchFileList.setStyleSheet(QCoreApplication.translate("BatchFileList", u"QWidget#BatchFileList {\n"
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
"    colo"
                        "r: #333;\n"
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
"    background: qlineargradie"
                        "nt(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 100), stop:1 rgba(255, 255, 255, 80));\n"
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
""
                        "    padding: 2px 5px 5px 5px;\n"
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
"    background: qlineargradient(x1:0, y1:0, "
                        "x2:1, y2:0, stop:0 #4facfe, stop:1 #00f2fe);\n"
"    border-radius: 5px;\n"
"    margin: 1px;\n"
"}", None))
        self.detailTitle.setText(QCoreApplication.translate("BatchFileList", u"\u6587\u4ef6\u5217\u8868", None))
        self.addMoreBtn.setText(QCoreApplication.translate("BatchFileList", u"\u8ffd\u52a0\u6587\u4ef6", None))
        self.clearBtn.setText(QCoreApplication.translate("BatchFileList", u"\u6e05\u7a7a\u5217\u8868", None))
        self.selectAllBtn.setText(QCoreApplication.translate("BatchFileList", u"\u5168\u9009/\u53cd\u9009", None))
        self.closeDetailBtn.setText(QCoreApplication.translate("BatchFileList", u"\u5173\u95ed", None))
        self.fileCount.setText(QCoreApplication.translate("BatchFileList", u"\u5df2\u9009\u62e9\u6587\u4ef6\uff1a0 \u4e2a", None))
        ___qtablewidgetitem = self.fileTable.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("BatchFileList", u"\u9009\u62e9", None));
        ___qtablewidgetitem1 = self.fileTable.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("BatchFileList", u"\u6587\u4ef6\u540d", None));
        ___qtablewidgetitem2 = self.fileTable.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("BatchFileList", u"\u6587\u4ef6\u8def\u5f84", None));
        ___qtablewidgetitem3 = self.fileTable.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("BatchFileList", u"\u7c7b\u578b", None));
        ___qtablewidgetitem4 = self.fileTable.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("BatchFileList", u"\u5927\u5c0f", None));
        ___qtablewidgetitem5 = self.fileTable.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("BatchFileList", u"\u72b6\u6001", None));
        ___qtablewidgetitem6 = self.fileTable.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("BatchFileList", u"\u79fb\u9664", None));
        self.fileTable.setStyleSheet(QCoreApplication.translate("BatchFileList", u"\n"
"         /* \u8ba9 fileTable \u7684\u6587\u672c\u989c\u8272\u4e3a\u767d\u8272\uff0c\u5e76\u4fdd\u6301\u900f\u660e\u80cc\u666f */\n"
"        QTableWidget#fileTable {\n"
"            color: white;\n"
"            background: transparent;\n"
"            border: 1px solid rgba(255, 255, 255, 50);\n"
"            gridline-color: rgba(255, 255, 255, 200);  \n"
"        }\n"
"        QTableWidget#fileTable::item {\n"
"            color: white;\n"
"            background-color: transparent;\n"
"        }\n"
"        QTableWidget#fileTable::item:selected { \n"
"            background: rgba(255, 255, 255, 40);\n"
"            color: white;\n"
"        }\n"
"\n"
"        QHeaderView::section {\n"
"            background: transparent;\n"
"            color: black;\n"
"            border: none;\n"
"            padding: 4px; \n"
"            border-right: 1px solid rgba(255, 255, 255, 120);\n"
"            border-bottom: 1px solid rgba(255, 255, 255, 120);\n"
"        } \n"
"            QHeaderView::section:horizonta"
                        "l {\n"
"                background: transparent;\n"
"            }\n"
"            QHeaderView::section:vertical {\n"
"                background: transparent;\n"
"            }\n"
"        QTableCornerButton::section {\n"
"            background: transparent;\n"
"            border: none;\n"
"            font-weight: normal;   \n"
"        }\n"
"        QHeaderView {\n"
"            font-weight: normal;\n"
"        }\n"
"\n"
"      /* \u5934\u90e8\u5bb9\u5668\u900f\u660e\uff0c\u540c\u65f6\u8865\u9f50\u4e0a\u3001\u5de6\u5916\u8fb9\u7ebf */\n"
"            QTableWidget#fileTable QHeaderView {\n"
"                background: transparent;\n"
"                background-color: transparent;\n"
"                border-top: 1px solid rgba(255, 255, 255, 120);\n"
"                border-left: 1px solid rgba(255, 255, 255, 120);\n"
"            }\n"
"\n"
"            /* \u6bcf\u4e2a\u5934\u90e8\u5206\u6bb5\uff1a\u53f3/\u4e0b\u8fb9\u7ebf\uff0c\u7528\u4e8e\u7f51\u683c\u6548\u679c */\n"
"            QTableWidget#fileTable"
                        " QHeaderView::section {\n"
"                background: transparent;\n"
"                background-color: transparent;\n"
"                border: none;\n"
"                padding: 4px;\n"
"                border-right: 1px solid rgba(255, 255, 255, 120);\n"
"                border-bottom: 1px solid rgba(255, 255, 255, 120);\n"
"                color: white;\n"
"            }\n"
"\n"
"            /* \u5de6\u4e0a\u89d2\u62d0\u89d2\uff1a\u8865\u9f50\u56db\u8fb9\u7ebf\uff0c\u907f\u514d\u7f3a\u53e3 */\n"
"            QTableWidget#fileTable QTableCornerButton::section {\n"
"                background: transparent;\n"
"                background-color: transparent;\n"
"                border-top: 1px solid rgba(255, 255, 255, 120);\n"
"                border-left: 1px solid rgba(255, 255, 255, 120);\n"
"                border-right: 1px solid rgba(255, 255, 255, 120);\n"
"                border-bottom: 1px solid rgba(255, 255, 255, 120);\n"
"            }\n"
"            QTableWidget#fileTable QHeaderView::section"
                        ":horizontal { background: transparent; }\n"
"            QTableWidget#fileTable QHeaderView::section:vertical { background: transparent; }\n"
"            QTableWidget#fileTable QTableCornerButton::section {\n"
"                background: transparent;\n"
"                background-color: transparent;\n"
"                border: none;\n"
"            }\n"
"\n"
"\n"
"        ", None))
    # retranslateUi

