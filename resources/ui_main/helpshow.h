#ifndef HELPSHOW_H
#define HELPSHOW_H

#include <QMainWindow>

namespace Ui {
class HelpShow;
}

class HelpShow : public QMainWindow
{
    Q_OBJECT

public:
    explicit HelpShow(QWidget *parent = 0);
    ~HelpShow();

private:
    Ui::HelpShow *ui;
};

#endif // HELPSHOW_H
