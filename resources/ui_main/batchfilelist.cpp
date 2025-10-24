#include "batchfilelist.h"
#include "ui_batchfilelist.h"

BatchFileList::BatchFileList(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::BatchFileList)
{
    ui->setupUi(this);
}

BatchFileList::~BatchFileList()
{
    delete ui;
}
