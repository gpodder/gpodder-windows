/**
 * gPodder for Windows
 * 2014-02-22 Thomas Perl <thp.io/about>
 * All rights reserved.
 **/

#include <QGuiApplication>
#include <QQuickView>
#include <QQmlEngine>
#include <QQmlError>
#include <QDir>
#include <QFile>
#include <QDebug>

static QUrl findResource(QString root, QString filename)
{
    QDir d(root);
    foreach (QString entry, d.entryList()) {
        QString path = d.filePath(entry);
        if (QDir(path).exists()) {
            QUrl candidate = findResource(path, filename);
            if (candidate.isValid()) {
                return candidate;
            }
        } else {
            if (path.endsWith("/" + filename)) {
                return QUrl("qrc" + path);
            }
        }
    }
    return QUrl();
}

int main(int argc, char *argv[])
{
    _putenv("PYTHONPATH=gpodder.zip");
    QGuiApplication app(argc, argv);
    QQuickView view;
    view.setResizeMode(QQuickView::SizeRootObjectToView);
    QUrl url = findResource(":/", "gpodder.qml");
    qDebug() << url;
    view.setSource(url);
    foreach (QQmlError error, view.errors()) {
        FILE *fp = fopen("errors.txt", "a");
        fprintf(fp, "%s\n", qPrintable(error.toString()));
        fclose(fp);
    }
    view.show();
    return app.exec();
}
