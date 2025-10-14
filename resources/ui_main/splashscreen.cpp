#include "splashscreen.h"
#include "ui_splashscreen.h"

SplashScreen::SplashScreen(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::SplashScreen)
{
    ui->setupUi(this);
}

SplashScreen::~SplashScreen()
{
    delete ui;
}
