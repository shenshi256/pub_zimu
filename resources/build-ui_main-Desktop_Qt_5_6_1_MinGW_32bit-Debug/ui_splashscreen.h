/********************************************************************************
** Form generated from reading UI file 'splashscreen.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_SPLASHSCREEN_H
#define UI_SPLASHSCREEN_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QSpacerItem>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_SplashScreen
{
public:
    QWidget *centralwidget;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *topLayout;
    QSpacerItem *horizontalSpacer;
    QLabel *closeButton;
    QSpacerItem *topSpacer;
    QHBoxLayout *horizontalLayout;
    QLabel *logoLabel;
    QLabel *appNameLabel;
    QSpacerItem *verticalSpacer;
    QLabel *subtitleLabel;
    QSpacerItem *middleSpacer;
    QVBoxLayout *verticalLayout;
    QLabel *loadingLabel;
    QProgressBar *progressBar;
    QSpacerItem *bottomSpacer;
    QLabel *versionLabel;

    void setupUi(QMainWindow *SplashScreen)
    {
        if (SplashScreen->objectName().isEmpty())
            SplashScreen->setObjectName(QStringLiteral("SplashScreen"));
        SplashScreen->resize(600, 400);
        SplashScreen->setMinimumSize(QSize(600, 400));
        SplashScreen->setMaximumSize(QSize(800, 600));
        SplashScreen->setAutoFillBackground(false);
        centralwidget = new QWidget(SplashScreen);
        centralwidget->setObjectName(QStringLiteral("centralwidget"));
        verticalLayout_2 = new QVBoxLayout(centralwidget);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        topLayout = new QHBoxLayout();
        topLayout->setObjectName(QStringLiteral("topLayout"));
        horizontalSpacer = new QSpacerItem(40, 20, QSizePolicy::Expanding, QSizePolicy::Minimum);

        topLayout->addItem(horizontalSpacer);

        closeButton = new QLabel(centralwidget);
        closeButton->setObjectName(QStringLiteral("closeButton"));
        closeButton->setMinimumSize(QSize(30, 30));
        closeButton->setMaximumSize(QSize(30, 30));
        QFont font;
        font.setPointSize(16);
        font.setBold(true);
        font.setWeight(75);
        closeButton->setFont(font);
        closeButton->setAlignment(Qt::AlignCenter);

        topLayout->addWidget(closeButton);


        verticalLayout_2->addLayout(topLayout);

        topSpacer = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(topSpacer);

        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        logoLabel = new QLabel(centralwidget);
        logoLabel->setObjectName(QStringLiteral("logoLabel"));
        logoLabel->setMinimumSize(QSize(64, 64));
        logoLabel->setMaximumSize(QSize(64, 64));
        QFont font1;
        font1.setPointSize(36);
        logoLabel->setFont(font1);
        logoLabel->setAlignment(Qt::AlignCenter);

        horizontalLayout->addWidget(logoLabel);


        verticalLayout_2->addLayout(horizontalLayout);

        appNameLabel = new QLabel(centralwidget);
        appNameLabel->setObjectName(QStringLiteral("appNameLabel"));
        QFont font2;
        font2.setPointSize(24);
        font2.setBold(true);
        font2.setWeight(75);
        appNameLabel->setFont(font2);
        appNameLabel->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(appNameLabel);

        verticalSpacer = new QSpacerItem(20, 10, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(verticalSpacer);

        subtitleLabel = new QLabel(centralwidget);
        subtitleLabel->setObjectName(QStringLiteral("subtitleLabel"));
        QFont font3;
        font3.setPointSize(10);
        subtitleLabel->setFont(font3);
        subtitleLabel->setAlignment(Qt::AlignCenter);

        verticalLayout_2->addWidget(subtitleLabel);

        middleSpacer = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout_2->addItem(middleSpacer);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        loadingLabel = new QLabel(centralwidget);
        loadingLabel->setObjectName(QStringLiteral("loadingLabel"));
        QFont font4;
        font4.setPointSize(9);
        loadingLabel->setFont(font4);
        loadingLabel->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(loadingLabel);

        progressBar = new QProgressBar(centralwidget);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setMinimumSize(QSize(250, 6));
        progressBar->setMaximumSize(QSize(250, 6));
        progressBar->setValue(0);
        progressBar->setTextVisible(false);

        verticalLayout->addWidget(progressBar, 0, Qt::AlignHCenter);

        bottomSpacer = new QSpacerItem(20, 20, QSizePolicy::Minimum, QSizePolicy::Expanding);

        verticalLayout->addItem(bottomSpacer);

        versionLabel = new QLabel(centralwidget);
        versionLabel->setObjectName(QStringLiteral("versionLabel"));
        QFont font5;
        font5.setPointSize(8);
        versionLabel->setFont(font5);
        versionLabel->setAlignment(Qt::AlignCenter);

        verticalLayout->addWidget(versionLabel);


        verticalLayout_2->addLayout(verticalLayout);

        SplashScreen->setCentralWidget(centralwidget);

        retranslateUi(SplashScreen);

        QMetaObject::connectSlotsByName(SplashScreen);
    } // setupUi

    void retranslateUi(QMainWindow *SplashScreen)
    {
        SplashScreen->setWindowTitle(QApplication::translate("SplashScreen", "\345\255\227\345\271\225\347\224\237\346\210\220\345\231\250", 0));
        SplashScreen->setStyleSheet(QApplication::translate("SplashScreen", "QWidget#SplashScreen {\n"
"    background: qlineargradient(x1:0, y1:0, x2:1, y2:1, stop:0 #667eea, stop:1 #764ba2);\n"
"    border-radius: 8px;\n"
"}\n"
"QWidget#centralwidget {\n"
"    background: transparent; /* \350\203\214\346\231\257\351\200\217\346\230\216 */\n"
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
"    background: rgba(255,"
                        " 0, 0, 100);\n"
"    border: 1px solid rgba(255, 0, 0, 150);\n"
"}", 0));
        closeButton->setStyleSheet(QApplication::translate("SplashScreen", "QLabel#closeButton {\n"
"    color: white;\n"
"    background: rgba(255, 255, 255, 20);\n"
"    border-radius: 15px;\n"
"    border: 1px solid rgba(255, 255, 255, 30);\n"
"}\n"
"QLabel#closeButton:hover {\n"
"    background: rgba(255, 0, 0, 100);\n"
"    border: 1px solid rgba(255, 0, 0, 150);\n"
"}", 0));
        closeButton->setText(QApplication::translate("SplashScreen", "\303\227", 0));
        logoLabel->setText(QApplication::translate("SplashScreen", "APP", 0));
        appNameLabel->setText(QApplication::translate("SplashScreen", "\345\255\227\345\271\225\347\224\237\346\210\220\345\231\250", 0));
        subtitleLabel->setText(QApplication::translate("SplashScreen", "\345\237\272\344\272\216 OpenAI Whisper \347\232\204\346\231\272\350\203\275\350\257\255\351\237\263\350\275\254\345\255\227\345\271\225\345\267\245\345\205\267", 0));
        loadingLabel->setText(QApplication::translate("SplashScreen", "\346\255\243\345\234\250\345\210\235\345\247\213\345\214\226...", 0));
        versionLabel->setText(QApplication::translate("SplashScreen", "Version 1.0.1", 0));
    } // retranslateUi

};

namespace Ui {
    class SplashScreen: public Ui_SplashScreen {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_SPLASHSCREEN_H
