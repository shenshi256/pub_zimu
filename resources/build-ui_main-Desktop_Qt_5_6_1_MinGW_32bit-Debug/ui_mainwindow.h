/********************************************************************************
** Form generated from reading UI file 'mainwindow.ui'
**
** Created by: Qt User Interface Compiler version 5.6.1
**
** WARNING! All changes made in this file will be lost when recompiling UI file!
********************************************************************************/

#ifndef UI_MAINWINDOW_H
#define UI_MAINWINDOW_H

#include <QtCore/QVariant>
#include <QtWidgets/QAction>
#include <QtWidgets/QApplication>
#include <QtWidgets/QButtonGroup>
#include <QtWidgets/QComboBox>
#include <QtWidgets/QGroupBox>
#include <QtWidgets/QHBoxLayout>
#include <QtWidgets/QHeaderView>
#include <QtWidgets/QLabel>
#include <QtWidgets/QMainWindow>
#include <QtWidgets/QProgressBar>
#include <QtWidgets/QPushButton>
#include <QtWidgets/QRadioButton>
#include <QtWidgets/QTextEdit>
#include <QtWidgets/QVBoxLayout>
#include <QtWidgets/QWidget>

QT_BEGIN_NAMESPACE

class Ui_MainWindow
{
public:
    QWidget *centralWidget;
    QVBoxLayout *verticalLayout_2;
    QHBoxLayout *horizontalLayout;
    QTextEdit *textEdit;
    QPushButton *pushButton;
    QPushButton *pushButton_selectDir;
    QPushButton *pushButton_4;
    QHBoxLayout *horizontalLayout_2;
    QComboBox *comboBox;
    QPushButton *pushButton_2;
    QPushButton *pushButton_3;
    QHBoxLayout *horizontalLayout_6;
    QGroupBox *outputType;
    QWidget *layoutWidget;
    QHBoxLayout *horizontalLayout_5;
    QRadioButton *srtType;
    QRadioButton *txtType;
    QRadioButton *vttType;
    QRadioButton *jsonType;
    QGroupBox *groupBox;
    QHBoxLayout *horizontalLayout_3;
    QLabel *memoryRate;
    QHBoxLayout *horizontalLayout_4;
    QGroupBox *isDebug;
    QRadioButton *noDebug;
    QRadioButton *yesDebug;
    QGroupBox *isChineseSimplified;
    QRadioButton *noSimple;
    QRadioButton *yesSimple;
    QGroupBox *overAfter;
    QWidget *layoutWidget_overAfter;
    QHBoxLayout *horizontalLayout_overAfter;
    QRadioButton *radioShutdown;
    QRadioButton *radioDoNothing;
    QVBoxLayout *verticalLayout;
    QProgressBar *progressBar;
    QTextEdit *textEdit_2;
    QHBoxLayout *horizontalLayout_statusBar;
    QLabel *selectedSummary;
    QPushButton *viewDetailBtn;

    void setupUi(QMainWindow *MainWindow)
    {
        if (MainWindow->objectName().isEmpty())
            MainWindow->setObjectName(QStringLiteral("MainWindow"));
        MainWindow->setWindowModality(Qt::NonModal);
        MainWindow->resize(600, 400);
        MainWindow->setMinimumSize(QSize(600, 400));
        MainWindow->setMaximumSize(QSize(800, 600));
        MainWindow->setMouseTracking(false);
        MainWindow->setAcceptDrops(false);
        QIcon icon;
        icon.addFile(QStringLiteral("../../../../CsharpProject/20250218_com.wxy.toutiao/Resources/favicon.ico"), QSize(), QIcon::Normal, QIcon::Off);
        MainWindow->setWindowIcon(icon);
        centralWidget = new QWidget(MainWindow);
        centralWidget->setObjectName(QStringLiteral("centralWidget"));
        verticalLayout_2 = new QVBoxLayout(centralWidget);
        verticalLayout_2->setSpacing(6);
        verticalLayout_2->setContentsMargins(11, 11, 11, 11);
        verticalLayout_2->setObjectName(QStringLiteral("verticalLayout_2"));
        horizontalLayout = new QHBoxLayout();
        horizontalLayout->setSpacing(6);
        horizontalLayout->setObjectName(QStringLiteral("horizontalLayout"));
        textEdit = new QTextEdit(centralWidget);
        textEdit->setObjectName(QStringLiteral("textEdit"));
        QSizePolicy sizePolicy(QSizePolicy::Expanding, QSizePolicy::Fixed);
        sizePolicy.setHorizontalStretch(0);
        sizePolicy.setVerticalStretch(0);
        sizePolicy.setHeightForWidth(textEdit->sizePolicy().hasHeightForWidth());
        textEdit->setSizePolicy(sizePolicy);
        textEdit->setMinimumSize(QSize(311, 31));
        textEdit->setMaximumSize(QSize(16777215, 31));
        textEdit->setAcceptDrops(true);
        textEdit->setHorizontalScrollBarPolicy(Qt::ScrollBarAlwaysOff);
        textEdit->setLineWrapMode(QTextEdit::NoWrap);

        horizontalLayout->addWidget(textEdit);

        pushButton = new QPushButton(centralWidget);
        pushButton->setObjectName(QStringLiteral("pushButton"));
        QSizePolicy sizePolicy1(QSizePolicy::Fixed, QSizePolicy::Fixed);
        sizePolicy1.setHorizontalStretch(0);
        sizePolicy1.setVerticalStretch(0);
        sizePolicy1.setHeightForWidth(pushButton->sizePolicy().hasHeightForWidth());
        pushButton->setSizePolicy(sizePolicy1);
        pushButton->setMinimumSize(QSize(81, 31));
        pushButton->setMaximumSize(QSize(81, 31));

        horizontalLayout->addWidget(pushButton);

        pushButton_selectDir = new QPushButton(centralWidget);
        pushButton_selectDir->setObjectName(QStringLiteral("pushButton_selectDir"));
        sizePolicy1.setHeightForWidth(pushButton_selectDir->sizePolicy().hasHeightForWidth());
        pushButton_selectDir->setSizePolicy(sizePolicy1);
        pushButton_selectDir->setMinimumSize(QSize(81, 31));
        pushButton_selectDir->setMaximumSize(QSize(81, 31));

        horizontalLayout->addWidget(pushButton_selectDir);

        pushButton_4 = new QPushButton(centralWidget);
        pushButton_4->setObjectName(QStringLiteral("pushButton_4"));
        pushButton_4->setMinimumSize(QSize(100, 31));
        pushButton_4->setMaximumSize(QSize(100, 31));

        horizontalLayout->addWidget(pushButton_4);


        verticalLayout_2->addLayout(horizontalLayout);

        horizontalLayout_2 = new QHBoxLayout();
        horizontalLayout_2->setSpacing(6);
        horizontalLayout_2->setObjectName(QStringLiteral("horizontalLayout_2"));
        comboBox = new QComboBox(centralWidget);
        comboBox->setObjectName(QStringLiteral("comboBox"));
        sizePolicy.setHeightForWidth(comboBox->sizePolicy().hasHeightForWidth());
        comboBox->setSizePolicy(sizePolicy);
        comboBox->setMinimumSize(QSize(300, 31));

        horizontalLayout_2->addWidget(comboBox);

        pushButton_2 = new QPushButton(centralWidget);
        pushButton_2->setObjectName(QStringLiteral("pushButton_2"));
        sizePolicy1.setHeightForWidth(pushButton_2->sizePolicy().hasHeightForWidth());
        pushButton_2->setSizePolicy(sizePolicy1);
        pushButton_2->setMinimumSize(QSize(81, 31));
        pushButton_2->setMaximumSize(QSize(81, 31));

        horizontalLayout_2->addWidget(pushButton_2);

        pushButton_3 = new QPushButton(centralWidget);
        pushButton_3->setObjectName(QStringLiteral("pushButton_3"));
        pushButton_3->setMinimumSize(QSize(100, 31));
        pushButton_3->setMaximumSize(QSize(100, 31));

        horizontalLayout_2->addWidget(pushButton_3);


        verticalLayout_2->addLayout(horizontalLayout_2);

        horizontalLayout_6 = new QHBoxLayout();
        horizontalLayout_6->setSpacing(6);
        horizontalLayout_6->setObjectName(QStringLiteral("horizontalLayout_6"));
        outputType = new QGroupBox(centralWidget);
        outputType->setObjectName(QStringLiteral("outputType"));
        outputType->setMinimumSize(QSize(0, 61));
        outputType->setMaximumSize(QSize(16777215, 61));
        layoutWidget = new QWidget(outputType);
        layoutWidget->setObjectName(QStringLiteral("layoutWidget"));
        layoutWidget->setGeometry(QRect(10, 21, 371, 33));
        horizontalLayout_5 = new QHBoxLayout(layoutWidget);
        horizontalLayout_5->setSpacing(6);
        horizontalLayout_5->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_5->setObjectName(QStringLiteral("horizontalLayout_5"));
        horizontalLayout_5->setContentsMargins(0, 0, 0, 0);
        srtType = new QRadioButton(layoutWidget);
        srtType->setObjectName(QStringLiteral("srtType"));
        srtType->setMinimumSize(QSize(0, 31));
        srtType->setSizeIncrement(QSize(0, 31));
        srtType->setChecked(true);

        horizontalLayout_5->addWidget(srtType);

        txtType = new QRadioButton(layoutWidget);
        txtType->setObjectName(QStringLiteral("txtType"));
        txtType->setMinimumSize(QSize(0, 31));
        txtType->setMaximumSize(QSize(16777215, 31));
        txtType->setSizeIncrement(QSize(0, 31));

        horizontalLayout_5->addWidget(txtType);

        vttType = new QRadioButton(layoutWidget);
        vttType->setObjectName(QStringLiteral("vttType"));
        vttType->setMinimumSize(QSize(0, 31));
        vttType->setMaximumSize(QSize(16777215, 31));
        vttType->setSizeIncrement(QSize(0, 31));

        horizontalLayout_5->addWidget(vttType);

        jsonType = new QRadioButton(layoutWidget);
        jsonType->setObjectName(QStringLiteral("jsonType"));
        jsonType->setMinimumSize(QSize(0, 31));
        jsonType->setMaximumSize(QSize(16777215, 31));
        jsonType->setSizeIncrement(QSize(0, 31));

        horizontalLayout_5->addWidget(jsonType);


        horizontalLayout_6->addWidget(outputType);

        groupBox = new QGroupBox(centralWidget);
        groupBox->setObjectName(QStringLiteral("groupBox"));
        groupBox->setMinimumSize(QSize(200, 61));
        groupBox->setMaximumSize(QSize(200, 61));
        horizontalLayout_3 = new QHBoxLayout(groupBox);
        horizontalLayout_3->setSpacing(6);
        horizontalLayout_3->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_3->setObjectName(QStringLiteral("horizontalLayout_3"));
        horizontalLayout_3->setContentsMargins(0, 0, 0, 0);
        memoryRate = new QLabel(groupBox);
        memoryRate->setObjectName(QStringLiteral("memoryRate"));
        sizePolicy.setHeightForWidth(memoryRate->sizePolicy().hasHeightForWidth());
        memoryRate->setSizePolicy(sizePolicy);
        memoryRate->setMinimumSize(QSize(0, 35));
        memoryRate->setMaximumSize(QSize(16777215, 35));
        memoryRate->setSizeIncrement(QSize(0, 0));
        memoryRate->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        horizontalLayout_3->addWidget(memoryRate);


        horizontalLayout_6->addWidget(groupBox);


        verticalLayout_2->addLayout(horizontalLayout_6);

        horizontalLayout_4 = new QHBoxLayout();
        horizontalLayout_4->setSpacing(6);
        horizontalLayout_4->setObjectName(QStringLiteral("horizontalLayout_4"));
        isDebug = new QGroupBox(centralWidget);
        isDebug->setObjectName(QStringLiteral("isDebug"));
        isDebug->setMinimumSize(QSize(0, 51));
        isDebug->setMaximumSize(QSize(16777215, 51));
        noDebug = new QRadioButton(isDebug);
        noDebug->setObjectName(QStringLiteral("noDebug"));
        noDebug->setGeometry(QRect(90, 20, 61, 31));
        noDebug->setMinimumSize(QSize(0, 31));
        noDebug->setMaximumSize(QSize(16777215, 31));
        noDebug->setChecked(true);
        yesDebug = new QRadioButton(isDebug);
        yesDebug->setObjectName(QStringLiteral("yesDebug"));
        yesDebug->setGeometry(QRect(10, 20, 61, 31));
        yesDebug->setMinimumSize(QSize(0, 31));
        yesDebug->setMaximumSize(QSize(16777215, 31));
        yesDebug->setChecked(false);

        horizontalLayout_4->addWidget(isDebug);

        isChineseSimplified = new QGroupBox(centralWidget);
        isChineseSimplified->setObjectName(QStringLiteral("isChineseSimplified"));
        isChineseSimplified->setMinimumSize(QSize(0, 51));
        isChineseSimplified->setMaximumSize(QSize(16777215, 51));
        noSimple = new QRadioButton(isChineseSimplified);
        noSimple->setObjectName(QStringLiteral("noSimple"));
        noSimple->setGeometry(QRect(100, 20, 81, 31));
        noSimple->setMinimumSize(QSize(0, 31));
        noSimple->setSizeIncrement(QSize(0, 31));
        noSimple->setChecked(true);
        yesSimple = new QRadioButton(isChineseSimplified);
        yesSimple->setObjectName(QStringLiteral("yesSimple"));
        yesSimple->setGeometry(QRect(10, 20, 71, 31));
        yesSimple->setMinimumSize(QSize(0, 31));
        yesSimple->setSizeIncrement(QSize(0, 31));
        yesSimple->setChecked(false);

        horizontalLayout_4->addWidget(isChineseSimplified);

        overAfter = new QGroupBox(centralWidget);
        overAfter->setObjectName(QStringLiteral("overAfter"));
        overAfter->setMinimumSize(QSize(0, 51));
        overAfter->setMaximumSize(QSize(16777215, 51));
        layoutWidget_overAfter = new QWidget(overAfter);
        layoutWidget_overAfter->setObjectName(QStringLiteral("layoutWidget_overAfter"));
        layoutWidget_overAfter->setGeometry(QRect(10, 21, 220, 33));
        horizontalLayout_overAfter = new QHBoxLayout(layoutWidget_overAfter);
        horizontalLayout_overAfter->setSpacing(6);
        horizontalLayout_overAfter->setContentsMargins(11, 11, 11, 11);
        horizontalLayout_overAfter->setObjectName(QStringLiteral("horizontalLayout_overAfter"));
        horizontalLayout_overAfter->setContentsMargins(0, 0, 0, 0);
        radioShutdown = new QRadioButton(layoutWidget_overAfter);
        radioShutdown->setObjectName(QStringLiteral("radioShutdown"));
        radioShutdown->setMinimumSize(QSize(0, 31));

        horizontalLayout_overAfter->addWidget(radioShutdown);

        radioDoNothing = new QRadioButton(layoutWidget_overAfter);
        radioDoNothing->setObjectName(QStringLiteral("radioDoNothing"));
        radioDoNothing->setMinimumSize(QSize(0, 31));
        radioDoNothing->setChecked(true);

        horizontalLayout_overAfter->addWidget(radioDoNothing);


        horizontalLayout_4->addWidget(overAfter);


        verticalLayout_2->addLayout(horizontalLayout_4);

        verticalLayout = new QVBoxLayout();
        verticalLayout->setSpacing(6);
        verticalLayout->setObjectName(QStringLiteral("verticalLayout"));
        progressBar = new QProgressBar(centralWidget);
        progressBar->setObjectName(QStringLiteral("progressBar"));
        progressBar->setMinimumSize(QSize(0, 10));
        progressBar->setMaximumSize(QSize(16777215, 10));
        progressBar->setValue(24);

        verticalLayout->addWidget(progressBar);

        textEdit_2 = new QTextEdit(centralWidget);
        textEdit_2->setObjectName(QStringLiteral("textEdit_2"));
        textEdit_2->setVerticalScrollBarPolicy(Qt::ScrollBarAsNeeded);

        verticalLayout->addWidget(textEdit_2);


        verticalLayout_2->addLayout(verticalLayout);

        horizontalLayout_statusBar = new QHBoxLayout();
        horizontalLayout_statusBar->setSpacing(8);
        horizontalLayout_statusBar->setObjectName(QStringLiteral("horizontalLayout_statusBar"));
        horizontalLayout_statusBar->setContentsMargins(0, 0, 0, 0);
        selectedSummary = new QLabel(centralWidget);
        selectedSummary->setObjectName(QStringLiteral("selectedSummary"));
        sizePolicy.setHeightForWidth(selectedSummary->sizePolicy().hasHeightForWidth());
        selectedSummary->setSizePolicy(sizePolicy);
        selectedSummary->setMinimumSize(QSize(0, 31));
        selectedSummary->setMaximumSize(QSize(16777215, 31));
        selectedSummary->setAlignment(Qt::AlignLeading|Qt::AlignLeft|Qt::AlignVCenter);

        horizontalLayout_statusBar->addWidget(selectedSummary);

        viewDetailBtn = new QPushButton(centralWidget);
        viewDetailBtn->setObjectName(QStringLiteral("viewDetailBtn"));
        sizePolicy1.setHeightForWidth(viewDetailBtn->sizePolicy().hasHeightForWidth());
        viewDetailBtn->setSizePolicy(sizePolicy1);
        viewDetailBtn->setMinimumSize(QSize(81, 31));
        viewDetailBtn->setMaximumSize(QSize(81, 31));

        horizontalLayout_statusBar->addWidget(viewDetailBtn);


        verticalLayout_2->addLayout(horizontalLayout_statusBar);

        MainWindow->setCentralWidget(centralWidget);

        retranslateUi(MainWindow);

        QMetaObject::connectSlotsByName(MainWindow);
    } // setupUi

    void retranslateUi(QMainWindow *MainWindow)
    {
        MainWindow->setStyleSheet(QApplication::translate("MainWindow", "QWidget#MainWindow {\n"
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
"}", 0));
#ifndef QT_NO_TOOLTIP
        textEdit->setToolTip(QApplication::translate("MainWindow", "\350\257\267\351\200\211\346\213\251\351\237\263\350\247\206\351\242\221\346\226\207\344\273\266", 0));
#endif // QT_NO_TOOLTIP
        pushButton->setText(QApplication::translate("MainWindow", "\351\200\211\346\213\251\346\226\207\344\273\266", 0));
        pushButton_selectDir->setText(QApplication::translate("MainWindow", "\351\200\211\346\213\251\347\233\256\345\275\225", 0));
        pushButton_4->setText(QApplication::translate("MainWindow", "\351\241\271\347\233\256\344\275\277\347\224\250\350\257\264\346\230\216", 0));
        comboBox->clear();
        comboBox->insertItems(0, QStringList()
         << QApplication::translate("MainWindow", "\350\257\267\351\200\211\346\213\251\346\250\241\345\236\213", 0)
         << QApplication::translate("MainWindow", "large-v3", 0)
         << QApplication::translate("MainWindow", "small", 0)
        );
        comboBox->setCurrentText(QApplication::translate("MainWindow", "\350\257\267\351\200\211\346\213\251\346\250\241\345\236\213", 0));
        pushButton_2->setText(QApplication::translate("MainWindow", "\345\274\200\345\247\213\347\224\237\346\210\220", 0));
        pushButton_3->setText(QApplication::translate("MainWindow", "\346\250\241\345\236\213\344\275\277\347\224\250\345\270\256\345\212\251", 0));
        outputType->setTitle(QApplication::translate("MainWindow", "\350\276\223\345\207\272\347\261\273\345\236\213", 0));
#ifndef QT_NO_TOOLTIP
        srtType->setToolTip(QApplication::translate("MainWindow", "\345\270\246\346\227\266\351\227\264\346\235\241, \346\224\257\346\214\201\345\257\274\345\205\245\345\210\260\345\211\252\350\276\221\345\267\245\345\205\267\344\270\255", 0));
#endif // QT_NO_TOOLTIP
        srtType->setText(QApplication::translate("MainWindow", "srt", 0));
#ifndef QT_NO_TOOLTIP
        txtType->setToolTip(QApplication::translate("MainWindow", "\347\272\257\345\255\227\345\271\225\346\226\207\346\234\254", 0));
#endif // QT_NO_TOOLTIP
        txtType->setText(QApplication::translate("MainWindow", "txt", 0));
        vttType->setText(QApplication::translate("MainWindow", "vtt", 0));
        jsonType->setText(QApplication::translate("MainWindow", "json", 0));
        groupBox->setTitle(QApplication::translate("MainWindow", "\347\263\273\347\273\237\344\277\241\346\201\257", 0));
        memoryRate->setText(QApplication::translate("MainWindow", "\350\277\233\347\250\213: \345\206\205\345\255\230 321M,CPU: 0% \n"
"\347\263\273\347\273\237: \345\206\205\345\255\230 92%, CPU: 0%", 0));
        isDebug->setTitle(QApplication::translate("MainWindow", "\345\274\200\345\220\257\350\260\203\350\257\225", 0));
#ifndef QT_NO_TOOLTIP
        noDebug->setToolTip(QApplication::translate("MainWindow", "\345\271\263\346\227\266\347\232\204\346\227\266\345\200\231, \345\272\224\350\257\245\345\205\263\351\227\255\346\227\245\345\277\227", 0));
#endif // QT_NO_TOOLTIP
        noDebug->setText(QApplication::translate("MainWindow", "\345\220\246", 0));
#ifndef QT_NO_TOOLTIP
        yesDebug->setToolTip(QApplication::translate("MainWindow", "\350\256\260\345\275\225\346\227\245\345\277\227, \345\270\270\347\224\250\344\272\216\347\250\213\345\272\217\350\260\203\350\257\225", 0));
#endif // QT_NO_TOOLTIP
        yesDebug->setText(QApplication::translate("MainWindow", "\346\230\257", 0));
        isChineseSimplified->setTitle(QApplication::translate("MainWindow", "\344\270\255\346\226\207\346\227\266\346\200\273\346\230\257\347\256\200\344\275\223", 0));
#ifndef QT_NO_TOOLTIP
        noSimple->setToolTip(QApplication::translate("MainWindow", "\347\224\261\346\250\241\345\236\213\350\207\252\350\241\214\346\216\250\346\226\255\347\256\200\344\275\223\347\271\201\344\275\223, \346\270\257\345\217\260\350\205\224\345\244\232\344\274\232\346\216\250\346\210\220\347\271\201\344\275\223", 0));
#endif // QT_NO_TOOLTIP
        noSimple->setText(QApplication::translate("MainWindow", "\345\220\246", 0));
#ifndef QT_NO_TOOLTIP
        yesSimple->setToolTip(QApplication::translate("MainWindow", "\347\273\237\344\270\200\344\275\277\347\224\250\347\256\200\344\275\223, \345\246\202\346\236\234\346\230\257\347\271\201\344\275\223\345\210\231\350\207\252\345\212\250\350\275\254\346\215\242\346\210\220\347\256\200\344\275\223", 0));
#endif // QT_NO_TOOLTIP
        yesSimple->setText(QApplication::translate("MainWindow", "\346\230\257", 0));
        overAfter->setTitle(QApplication::translate("MainWindow", "\345\256\214\346\210\220\345\220\216\345\205\263\346\234\272", 0));
        radioShutdown->setText(QApplication::translate("MainWindow", "\346\230\257", 0));
        radioDoNothing->setText(QApplication::translate("MainWindow", "\345\220\246", 0));
        selectedSummary->setText(QApplication::translate("MainWindow", "\345\267\262\351\200\211\346\213\251 0 \344\270\252\346\226\207\344\273\266", 0));
        viewDetailBtn->setText(QApplication::translate("MainWindow", "\346\237\245\347\234\213\350\257\246\346\203\205", 0));
    } // retranslateUi

};

namespace Ui {
    class MainWindow: public Ui_MainWindow {};
} // namespace Ui

QT_END_NAMESPACE

#endif // UI_MAINWINDOW_H
