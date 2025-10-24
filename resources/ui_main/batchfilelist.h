#ifndef BATCHFILELIST_H
#define BATCHFILELIST_H

#include <QMainWindow>

namespace Ui {
class BatchFileList;
}

class BatchFileList : public QMainWindow
{
    Q_OBJECT

public:
    explicit BatchFileList(QWidget *parent = 0);
    ~BatchFileList();

private:
    Ui::BatchFileList *ui;
};

#endif // BATCHFILELIST_H
