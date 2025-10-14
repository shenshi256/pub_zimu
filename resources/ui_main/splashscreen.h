#ifndef SPLASHSCREEN_H
#define SPLASHSCREEN_H

#include <QMainWindow>

namespace Ui {
class SplashScreen;
}

class SplashScreen : public QMainWindow
{
    Q_OBJECT

public:
    explicit SplashScreen(QWidget *parent = 0);
    ~SplashScreen();

private:
    Ui::SplashScreen *ui;
};

#endif // SPLASHSCREEN_H
