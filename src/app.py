# -*- coding: utf-8 -*-

import sys
from PyQt4.QtGui import QApplication

from widget.MainWindow import MainWindow

def main(args):
    print '>>>>>>>>>>>>>>>>>>>>>>>    Main    <<<<<<<<<<<<<<<<<<<<<<<<<<<'
    app = QApplication(args)
    wm = MainWindow()
    wm.showMaximized()
    wm.iren.Initialize()
    rc = app.exec_()
    print '>>>>>>>>>>>>>>>>>>>>>>>    END     <<<<<<<<<<<<<<<<<<<<<<<<<<<'
    sys.exit(rc)


if __name__ == '__main__':
    main(sys.argv)