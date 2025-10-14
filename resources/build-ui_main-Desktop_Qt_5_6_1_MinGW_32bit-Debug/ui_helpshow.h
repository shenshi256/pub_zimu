/********************************************************************************
** Form generated from reading UI file 'helpshow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_HELPSHOW_H
#define UI_HELPSHOW_H

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

class Ui_HelpShow
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout;
    QLabel *lblHelp;
    QTextBrowser *textBrowser;
    QHBoxLayout *horizontalLayout;
    QSpacerItem *horizontalSpacer;
    QPushButton *pushButton;
    QSpacerItem *horizontalSpacer_2;

    void setupUi(QMainWindow *HelpShow)
    {
        if (HelpShow->objectName().isEmpty())
            HelpShow->setObjectName(QStringLiteral("HelpShow"));
        HelpShow->resize(600, 400);
        HelpShow->setMinimumSize(QSize(600, 400));
        HelpShow->setMaximumSize(QSize(800, 600));
        centralwidget = new QWidget(HelpShow);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        verticalLayout = new QVBoxLayout(centralwidget);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        lblHelp = new QLabel(centralwidget);
        lblHelp->setObjectName(QStringLiteral("lblHelp"));
        QFont font;
        font.setFamily(QStringLiteral("Arial Black"));
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        lblHelp->setFont(font);
        lblHelp->setTextFormat(Qt::AutoText);
        lblHelp->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(lblHelp);

        textBrowser = new QTextBrowser(centralwidget);
        textBrowser->setObjectName(QStringLiteral("textBrowser"));
        textBrowser->setVerticalScrollBarPolicy(Qt::ScrollBarAlwaysOn);

        verticalLayout->addWidget(textBrowser);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer);

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setMinimumSize(QSize(144, 31));
        pushButton->setMaximumSize(QSize(16777215, 31));
        QFont font1;
        font1.setBold(true);
        font1.setWeight(75);
        pushButton->setFont(font1);

        horizontalLayout->addWidget(pushButton);

        horizontalSpacer_2 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout->addItem(horizontalSpacer_2);


        verticalLayout->addLayout(horizontalLayout);

        HelpShow->setCentralWidget(centralwidget);

        retranslateUi(HelpShow);

        QMetaObject::connectSlotsByName(HelpShow);
    } // setupUi

    void retranslateUi(QMainWindow *HelpShow)
    {
        HelpShow->setWindowTitle(QApplication::translate("HelpShow", "MainWindow", 0));
        HelpShow->setStyleSheet(QApplication::translate("HelpShow", "QWidget#HelpShow {\n"
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
"    border: 2px solid r"
                        "gba(255, 255, 255, 100);\n"
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
        lblHelp->setText(QApplication::translate("HelpShow", "\346\250\241\345\236\213\344\275\277\347\224\250\345\270\256\345\212\251", 0));
        pushButton->setText(QApplication::translate("HelpShow", "\345\205\263\351\227\255", 0));
    } // retranslateUi

};

namespace Ui {
    class HelpShow: public Ui_HelpShow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_HELPSHOW_H
