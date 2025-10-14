#-------------------------------------------------
#
# Project created by QtCreator 2025-06-19T16:25:19
#
#-------------------------------------------------

QT       += core gui

greaterThan(QT_MAJOR_VERSION, 4): QT += widgets

TARGET = ui_main
TEMPLATE = app


SOURCES += main.cpp\
        mainwindow.cpp \
    auth.cpp \
    helpshow.cpp \
    splashscreen.cpp

HEADERS  += mainwindow.h \
    auth.h \
    helpshow.h \
    splashscreen.h

FORMS    += mainwindow.ui \
    auth.ui \
    helpshow.ui \
    disclaimers.ui \
    splashscreen.ui
