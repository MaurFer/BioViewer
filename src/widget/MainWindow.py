# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import vtk
from vtk.qt4.QVTKRenderWindowInteractor import QVTKRenderWindowInteractor

class MainWindow(QtGui.QMainWindow):
    '''
    Main-Window
    '''
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self._initWidget()
        self._createActions()
        self._createMenu()
        self._createToolbar()
        self._createStatusbar()


    def _initWidget(self):
        centralWidget = QtGui.QWidget(self)
        layout = QtGui.QVBoxLayout()

        vtkWidget = QVTKRenderWindowInteractor(centralWidget)
        layout.addWidget(vtkWidget)

        centralWidget.setLayout(layout)

        self.setCentralWidget(centralWidget)

        ren = vtk.vtkRenderer()
        vtkWidget.GetRenderWindow().AddRenderer(ren)
        self.iren = vtkWidget.GetRenderWindow().GetInteractor()
        self.ren = ren
        self.renWin = vtkWidget.GetRenderWindow()

    def _createActions(self):
        self._actions = []
        self._actions.append(QtGui.QAction('&Load',self))

    def _createMenu(self):
        fileMenu = self.menuBar().addMenu("&File")
        fileMenu.addAction(self._actions[0])

    def _createToolbar(self):
        fileToolbar = self.addToolBar("File")
        fileToolbar.addAction(self._actions[0])

    def _createStatusbar(self):
        self.statusBar().showMessage("Ready")





