#include "mainwindow.h"
#include "auth.h"
#include "helpshow.h"
#include "splashscreen.h"
#include "batchfilelist.h"
#include <QApplication>

int main(int argc, char *argv[])
{
    QApplication a(argc, argv);

    //主窗体
//    MainWindow w;
//    w.show();

    BatchFileList b;
    b.show();

    // 帮助窗体
//HelpShow h;
//h.show();

    //授权窗体
//    Auth w;
//       w.show();

//    SplashScreen s;
//    s.show();

    return a.exec();
}
