/********************************************************************************
** Form generated from reading UI file 'batchfilelist.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_BATCHFILELIST_H
#define UI_BATCHFILELIST_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QTableWidget>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_BatchFileList
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *detailTitlebar;
    QLabel *detailTitle;
    QSpacerItem *detailTitle_spacer;
    QHBoxLayout *detailActions;
    QPushButton *addMoreBtn;
    QPushButton *clearBtn;
    QPushButton *selectAllBtn;
    QPushButton *closeDetailBtn;
    QHBoxLayout *fileCountBar;
    QLabel *fileCount;
    QTableWidget *fileTable;

    void setupUi(QMainWindow *BatchFileList)
    {
        if (BatchFileList->objectName().isEmpty())
            BatchFileList->setObjectName(QStringLiteral("BatchFileList"));
        BatchFileList->setWindowModality(Qt::NonModal);
        BatchFileList->resize(600, 400);
        BatchFileList->setMinimumSize(QSize(600, 400));
        BatchFileList->setMaximumSize(QSize(800, 600));
        BatchFileList->setMouseTracking(false);
        BatchFileList->setAcceptDrops(false);
        QIcon icon;
        icon.addFile(QStringLiteral("../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico"), QSize(), QIcon::Normal, QIcon::Off);
        BatchFileList->setWindowIcon(icon);
        centralWidget = new QWidget(BatchFileList);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        detailTitlebar = new QHBoxLayout();
        detailTitlebar->setObjectName(QStringLiteral("detailTitlebar"));
        detailTitle = new QLabel(centralWidget);
        detailTitle->setObjectName(QStringLiteral("detailTitle"));
        detailTitle->setMinimumSize(QSize(0, 31));
        detailTitle->setAlignment(Qt::AlignVCenter);

        detailTitlebar->addWidget(detailTitle);

        detailTitle_spacer = new QSpacerItem(20, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        detailTitlebar->addItem(detailTitle_spacer);

        detailActions = new QHBoxLayout();
        detailActions->setObjectName(QStringLiteral("detailActions"));
        addMoreBtn = new QPushButton(centralWidget);
        addMoreBtn->setObjectName(QStringLiteral("addMoreBtn"));
        addMoreBtn->setMinimumSize(QSize(81, 31));
        addMoreBtn->setMaximumSize(QSize(120, 31));

        detailActions->addWidget(addMoreBtn);

        clearBtn = new QPushButton(centralWidget);
        clearBtn->setObjectName(QStringLiteral("clearBtn"));
        clearBtn->setMinimumSize(QSize(81, 31));
        clearBtn->setMaximumSize(QSize(120, 31));

        detailActions->addWidget(clearBtn);

        selectAllBtn = new QPushButton(centralWidget);
        selectAllBtn->setObjectName(QStringLiteral("selectAllBtn"));
        selectAllBtn->setMinimumSize(QSize(100, 31));
        selectAllBtn->setMaximumSize(QSize(140, 31));

        detailActions->addWidget(selectAllBtn);

        closeDetailBtn = new QPushButton(centralWidget);
        closeDetailBtn->setObjectName(QStringLiteral("closeDetailBtn"));
        closeDetailBtn->setMinimumSize(QSize(81, 31));
        closeDetailBtn->setMaximumSize(QSize(120, 31));

        detailActions->addWidget(closeDetailBtn);


        detailTitlebar->addLayout(detailActions);


        verticalLayout_2->addLayout(detailTitlebar);

        fileCountBar = new QHBoxLayout();
        fileCountBar->setObjectName(QStringLiteral("fileCountBar"));
        fileCount = new QLabel(centralWidget);
        fileCount->setObjectName(QStringLiteral("fileCount"));
        fileCount->setMinimumSize(QSize(0, 28));
        fileCount->setAlignment(Qt::AlignVCenter);

        fileCountBar->addWidget(fileCount);


        verticalLayout_2->addLayout(fileCountBar);

        fileTable = new QTableWidget(centralWidget);
        if (fileTable->columnCount() < 7)
            fileTable->setColumnCount(7);
        QTableWidgetItem *__qtablewidgetitem = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(0, __qtablewidgetitem);
        QTableWidgetItem *__qtablewidgetitem1 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(1, __qtablewidgetitem1);
        QTableWidgetItem *__qtablewidgetitem2 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(2, __qtablewidgetitem2);
        QTableWidgetItem *__qtablewidgetitem3 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(3, __qtablewidgetitem3);
        QTableWidgetItem *__qtablewidgetitem4 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(4, __qtablewidgetitem4);
        QTableWidgetItem *__qtablewidgetitem5 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(5, __qtablewidgetitem5);
        QTableWidgetItem *__qtablewidgetitem6 = new QTableWidgetItem();
        fileTable->setHorizontalHeaderItem(6, __qtablewidgetitem6);
        fileTable->setObjectName(QStringLiteral("fileTable"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Expanding);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(1);
        sizePolicy.setHeightForWidth(fileTable->sizePolicy().hasHeightForWidth());
        fileTable->setSizePolicy(sizePolicy);
        fileTable->setEditTriggers(QAbstractItemView::NoEditTriggers);
        fileTable->setAlternatingRowColors(true);
        fileTable->setSelectionMode(QAbstractItemView::SingleSelection);
        fileTable->setSelectionBehavior(QAbstractItemView::SelectRows);
        fileTable->setShowGrid(true);
        fileTable->setRowCount(0);
        fileTable->setColumnCount(7);

        verticalLayout_2->addWidget(fileTable);

        BatchFileList->setCentralWidget(centralWidget);

        retranslateUi(BatchFileList);

        QMetaObject::connectSlotsByName(BatchFileList);
    } // setupUi

    void retranslateUi(QMainWindow *BatchFileList)
    {
        BatchFileList->setStyleSheet(QApplication::translate("BatchFileList", "QWidget#BatchFileList {\n"
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
"}", 0));
        detailTitle->setText(QApplication::translate("BatchFileList", "\346\226\207\344\273\266\345\210\227\350\241\250", 0));
        addMoreBtn->setText(QApplication::translate("BatchFileList", "\350\277\275\345\212\240\346\226\207\344\273\266", 0));
        clearBtn->setText(QApplication::translate("BatchFileList", "\346\270\205\347\251\272\345\210\227\350\241\250", 0));
        selectAllBtn->setText(QApplication::translate("BatchFileList", "\345\205\250\351\200\211/\345\217\215\351\200\211", 0));
        closeDetailBtn->setText(QApplication::translate("BatchFileList", "\345\205\263\351\227\255", 0));
        fileCount->setText(QApplication::translate("BatchFileList", "\345\267\262\351\200\211\346\213\251\346\226\207\344\273\266\357\274\2320 \344\270\252", 0));
        QTableWidgetItem *___qtablewidgetitem = fileTable->horizontalHeaderItem(0);
        ___qtablewidgetitem->setText(QApplication::translate("BatchFileList", "\351\200\211\346\213\251", 0));
        QTableWidgetItem *___qtablewidgetitem1 = fileTable->horizontalHeaderItem(1);
        ___qtablewidgetitem1->setText(QApplication::translate("BatchFileList", "\346\226\207\344\273\266\345\220\215", 0));
        QTableWidgetItem *___qtablewidgetitem2 = fileTable->horizontalHeaderItem(2);
        ___qtablewidgetitem2->setText(QApplication::translate("BatchFileList", "\346\226\207\344\273\266\350\267\257\345\276\204", 0));
        QTableWidgetItem *___qtablewidgetitem3 = fileTable->horizontalHeaderItem(3);
        ___qtablewidgetitem3->setText(QApplication::translate("BatchFileList", "\347\261\273\345\236\213", 0));
        QTableWidgetItem *___qtablewidgetitem4 = fileTable->horizontalHeaderItem(4);
        ___qtablewidgetitem4->setText(QApplication::translate("BatchFileList", "\345\244\247\345\260\217", 0));
        QTableWidgetItem *___qtablewidgetitem5 = fileTable->horizontalHeaderItem(5);
        ___qtablewidgetitem5->setText(QApplication::translate("BatchFileList", "\347\212\266\346\200\201", 0));
        QTableWidgetItem *___qtablewidgetitem6 = fileTable->horizontalHeaderItem(6);
        ___qtablewidgetitem6->setText(QApplication::translate("BatchFileList", "\347\247\273\351\231\244", 0));
        fileTable->setStyleSheet(QApplication::translate("BatchFileList", "\n"
"         /* \350\256\251 fileTable \347\232\204\346\226\207\346\234\254\351\242\234\350\211\262\344\270\272\347\231\275\350\211\262\357\274\214\345\271\266\344\277\235\346\214\201\351\200\217\346\230\216\350\203\214\346\231\257 */\n"
"        QTableWidget#fileTable {\n"
"            color: white;\n"
"            background: transparent;\n"
"            border: 1px solid rgba(255, 255, 255, 50);\n"
"            gridline-color: rgba(255, 255, 255, 200);  /* \346\226\260\345\242\236\357\274\232\345\215\225\345\205\203\346\240\274\350\276\271\347\272\277\344\270\272\347\231\275\350\211\262 */\n"
"        }\n"
"        QTableWidget#fileTable::item {\n"
"            color: white;\n"
"            background-color: transparent;\n"
"        }\n"
"        QTableWidget#fileTable::item:selected {\n"
"            color: white;\n"
"        }\n"
"\n"
"        QHeaderView::section {\n"
"            background: rgba(255, 255, 255, 50);\n"
"            color: black;\n"
"            border: none;\n"
"            padding: 4p"
                        "x;\n"
"            /* \350\256\251\350\241\250\345\244\264\345\210\206\351\232\224\347\272\277\344\271\237\346\216\245\350\277\221\347\231\275\350\211\262\350\247\206\350\247\211\357\274\210\344\270\215\345\275\261\345\223\215\347\275\221\346\240\274\357\274\211 */\n"
"            border-right: 1px solid rgba(255, 255, 255, 120);\n"
"            border-bottom: 1px solid rgba(255, 255, 255, 120);\n"
"        }\n"
"        QTableCornerButton::section {\n"
"            background: rgba(255, 255, 255, 50);\n"
"            border: none;\n"
"            font-weight: normal;   \n"
"        }\n"
"        QHeaderView {\n"
"            font-weight: normal;\n"
"        }\n"
"        ", 0));
    } // retranslateUi

};

namespace Ui {
    class BatchFileList: public Ui_BatchFileList {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_BATCHFILELIST_H
