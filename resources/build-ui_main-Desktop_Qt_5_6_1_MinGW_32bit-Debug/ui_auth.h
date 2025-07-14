/********************************************************************************
** Form generated from reading UI file 'auth.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_AUTH_H
#define UI_AUTH_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QCheckBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QLineEdit>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_Auth
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QSpacerItem *verticalSpacer;
    QVBoxLayout *verticalLayout;
    QLabel *label;
    QSpacerItem *verticalSpacer_3;
    QHBoxLayout *horizontalLayout;
    QLabel *lblMachineCode;
    QLineEdit *leMachineCode;
    QPushButton *pushButton;
    QSpacerItem *verticalSpacer_4;
    QHBoxLayout *horizontalLayout_2;
    QLabel *lblAuthCode;
    QLineEdit *leAuthCode;
    QPushButton *btnHelp;
    QSpacerItem *verticalSpacer_5;
    QHBoxLayout *horizontalLayout_3;
    QCheckBox *chkDebug;
    QSpacerItem *horizontalSpacer;
    QPushButton *btnOk;
    QSpacerItem *horizontalSpacer_3;
    QPushButton *btnTryUse;
    QSpacerItem *verticalSpacer_2;

    void setupUi(QMainWindow *Auth)
    {
        if (Auth->objectName().isEmpty())
            Auth->setObjectName(QStringLiteral("Auth"));
        Auth->resize(600, 400);
        Auth->setMinimumSize(QSize(600, 400));
        Auth->setMaximumSize(QSize(800, 600));
        QIcon icon;
        icon.addFile(QStringLiteral("../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico"), QSize(), QIcon::Normal, QIcon::Off);
        Auth->setWindowIcon(icon);
        centralwidget = new QWidget(Auth);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        verticalSpacer = new QSpacerItem(20, 0, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        label = new QLabel(centralwidget);
        label->setObjectName(QStringLiteral("label"));
        QFont font;
        font.setFamily(QStringLiteral("Arial Black"));
        font.setPointSize(24);
        font.setBold(true);
        font.setWeight(75);
        label->setFont(font);
        label->setTextFormat(Qt::AutoText);
        label->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(label);

        verticalSpacer_3 = new QSpacerItem(20, 18, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout->addItem(verticalSpacer_3);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        lblMachineCode = new QLabel(centralwidget);
        lblMachineCode->setObjectName(QStringLiteral("lblMachineCode"));
        QSizePolicy sizePolicy(QSizePolicy::Fixed, QSizePolicy::Preferred);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(lblMachineCode->sizePolicy().hasHeightForWidth());
        lblMachineCode->setSizePolicy(sizePolicy);
        lblMachineCode->setMinimumSize(QSize(0, 51));
        lblMachineCode->setMaximumSize(QSize(16777215, 51));
        QFont font1;
        font1.setFamily(QStringLiteral("Arial"));
        font1.setPointSize(16);
        lblMachineCode->setFont(font1);

        horizontalLayout->addWidget(lblMachineCode);

        leMachineCode = new QLineEdit(centralwidget);
        leMachineCode->setObjectName(QStringLiteral("leMachineCode"));
        leMachineCode->setMinimumSize(QSize(0, 51));
        leMachineCode->setMaximumSize(QSize(16777215, 51));
        leMachineCode->setReadOnly(true);

        horizontalLayout->addWidget(leMachineCode);

        pushButton = new QPushButton(centralwidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        pushButton->setMinimumSize(QSize(80, 51));
        pushButton->setMaximumSize(QSize(80, 51));

        horizontalLayout->addWidget(pushButton);


        verticalLayout->addLayout(horizontalLayout);

        verticalSpacer_4 = new QSpacerItem(20, 18, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout->addItem(verticalSpacer_4);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        lblAuthCode = new QLabel(centralwidget);
        lblAuthCode->setObjectName(QStringLiteral("lblAuthCode"));
        sizePolicy.setHeightForWidth(lblAuthCode->sizePolicy().hasHeightForWidth());
        lblAuthCode->setSizePolicy(sizePolicy);
        lblAuthCode->setMinimumSize(QSize(0, 51));
        lblAuthCode->setMaximumSize(QSize(16777215, 51));
        lblAuthCode->setFont(font1);

        horizontalLayout_2->addWidget(lblAuthCode);

        leAuthCode = new QLineEdit(centralwidget);
        leAuthCode->setObjectName(QStringLiteral("leAuthCode"));
        leAuthCode->setMinimumSize(QSize(0, 51));
        leAuthCode->setMaximumSize(QSize(16777215, 51));

        horizontalLayout_2->addWidget(leAuthCode);

        btnHelp = new QPushButton(centralwidget);
        btnHelp->setObjectName(QStringLiteral("btnHelp"));
        btnHelp->setMinimumSize(QSize(80, 51));
        btnHelp->setMaximumSize(QSize(80, 51));

        horizontalLayout_2->addWidget(btnHelp);


        verticalLayout->addLayout(horizontalLayout_2);

        verticalSpacer_5 = new QSpacerItem(17, 18, QSizePolicy::Minimum, QSizePolicy::Fixed);

        verticalLayout->addItem(verticalSpacer_5);

        horizontalLayout_3 = new QHBoxLayout();
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        chkDebug = new QCheckBox(centralwidget);
        chkDebug->setObjectName(QStringLiteral("chkDebug"));
        chkDebug->setMinimumSize(QSize(0, 51));
        chkDebug->setMaximumSize(QSize(16777215, 51));
        chkDebug->setFont(font1);

        horizontalLayout_3->addWidget(chkDebug);

        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer);

        btnOk = new QPushButton(centralwidget);
        btnOk->setObjectName(QStringLiteral("btnOk"));
        btnOk->setMinimumSize(QSize(150, 51));
        btnOk->setMaximumSize(QSize(150, 51));
        QFont font2;
        font2.setBold(true);
        font2.setWeight(75);
        btnOk->setFont(font2);

        horizontalLayout_3->addWidget(btnOk);

        horizontalSpacer_3 = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        horizontalLayout_3->addItem(horizontalSpacer_3);

        btnTryUse = new QPushButton(centralwidget);
        btnTryUse->setObjectName(QStringLiteral("btnTryUse"));
        btnTryUse->setMinimumSize(QSize(80, 51));
        btnTryUse->setMaximumSize(QSize(80, 51));

        horizontalLayout_3->addWidget(btnTryUse);


        verticalLayout->addLayout(horizontalLayout_3);


        verticalLayout_2->addLayout(verticalLayout);

        verticalSpacer_2 = new QSpacerItem(20, 1, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer_2);

        Auth->setCentralWidget(centralwidget);

        retranslateUi(Auth);

        QMetaObject::connectSlotsByName(Auth);
    } // setupUi

    void retranslateUi(QMainWindow *Auth)
    {
        Auth->setWindowTitle(QApplication::translate("Auth", "\345\255\227\345\271\225\347\224\237\346\210\220\345\231\250", 0));
        Auth->setStyleSheet(QApplication::translate("Auth", "QWidget#Auth {\n"
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
"}", 0));
        label->setText(QApplication::translate("Auth", "\346\254\242\350\277\216\344\275\277\347\224\250\345\255\227\345\271\225\347\224\237\346\210\220\345\231\250", 0));
        lblMachineCode->setText(QApplication::translate("Auth", "\346\234\272\345\231\250\347\240\201:", 0));
        pushButton->setText(QApplication::translate("Auth", "\347\202\271\345\207\273\345\244\215\345\210\266", 0));
        lblAuthCode->setText(QApplication::translate("Auth", "\346\216\210\346\235\203\347\240\201:", 0));
        btnHelp->setText(QApplication::translate("Auth", "\344\275\277\347\224\250\345\270\256\345\212\251", 0));
        chkDebug->setText(QApplication::translate("Auth", "\345\274\200\345\220\257\350\260\203\350\257\225", 0));
        btnOk->setText(QApplication::translate("Auth", "\346\216\210\346\235\203", 0));
        btnTryUse->setText(QApplication::translate("Auth", "\350\257\225\347\224\250\344\270\200\344\270\213", 0));
    } // retranslateUi

};

namespace Ui {
    class Auth: public Ui_Auth {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_AUTH_H
