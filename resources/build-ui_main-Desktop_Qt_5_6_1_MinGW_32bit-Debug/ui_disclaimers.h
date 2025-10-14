/********************************************************************************
** Form generated from reading UI file 'disclaimers.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_DISCLAIMERS_H
#define UI_DISCLAIMERS_H

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
#include <QtWidgets/QTextBrowser>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QLabel *lblProjectHelp;
    QTextBrowser *textBrowser;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *btnClose;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->resize(600, 400);
        MainWindow->setMinimumSize(QSize(600, 400));
        MainWindow->setMaximumSize(QSize(800, 600));
        centralwidget = new QWidget(MainWindow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        lblProjectHelp = new QLabel(centralwidget);
        lblProjectHelp->setObjectName(QStringLiteral("lblProjectHelp"));
        QFont font;
        font.setFamily(QStringLiteral("Arial Black"));
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        lblProjectHelp->setFont(font);
        lblProjectHelp->setTextFormat(Qt::AutoText);
        lblProjectHelp->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(lblProjectHelp);

        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));

        verticalLayout->addWidget(textBrowser);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        btnClose = new QPushButton(centralwidget);
        btnClose->setObjectName(QStringLiteral("btnClose"));
        btnClose->setMinimumSize(QSize(0, 31));
        btnClose->setMaximumSize(QSize(16777215, 31));
        QFont font1;
        font1.setFamily(QStringLiteral("Arial"));
        font1.setPointSize(16);
        btnClose->setFont(font1);

        horizontalLayout->addWidget(btnClose);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout);

        MainWindow->setCentralWidget(centralwidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setWindowTitle(QApplication::translate("MainWindow", "MainWindow", 0));
        MainWindow->setStyleSheet(QApplication::translate("MainWindow", "QWidget#MainWindow {\n"
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
"QLabel#lblProjectHelp {\n"
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
"    vertical-scroll-bar-policy: always;\n"
"}\n"
"\n"
"QTextBrowser:focus {\n"
"    border: 2px solid rgba(255, 255, 255, 150);\n"
"    background: rgba(255, 255, 255, 95);\n"
"}\n"
"\n"
"QPushButton {\n"
"    background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0 rgba(255, 255, 255, 80), stop:1 rgba(255, 255, 255, 60));\n"
"    border: 2p"
                        "x solid rgba(255, 255, 255, 100);\n"
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
"}", 0));
        lblProjectHelp->setText(QApplication::translate("MainWindow", "\351\241\271\347\233\256\344\275\277\347\224\250\345\270\256\345\212\251", 0));
        btnClose->setText(QApplication::translate("MainWindow", "\345\205\263\351\227\255", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_DISCLAIMERS_H
