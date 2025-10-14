#include "helpshow.h"
#include "ui_helpshow.h"

HelpShow::HelpShow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::HelpShow)
{
    ui->setupUi(this);
}

HelpShow::~HelpShow()
{
    delete ui;
}
