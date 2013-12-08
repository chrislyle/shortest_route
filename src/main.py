#!/usr/bin/env python
# encoding: utf-8

import os, sys, time

from PyQt4 import QtCore, QtGui, QtOpenGL

from DijkstraWnd_Ui import Ui_MainWindow
from random import randint, shuffle

class Scene(QtGui.QGraphicsScene):
    def __init__(self, parent=None):
        super(Scene, self).__init__(parent)



class NetView(QtGui.QGraphicsView):
    def __init__(self, parent=None):
        super(NetView, self).__init__(parent)
        self.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        
    def contextMenuEvent(self, event):
        menu = QtGui.QMenu()
        self.actCreateVertex = menu.addAction('Create Vertex')
        self.actCreateLink = menu.addAction('Create Link')
        action = menu.exec_(event.globalPos())
        
        self.processAction(action, event)   
        
    def processAction(self, act, ev):
        if act == self.actCreateVertex:
            text, ok = QtGui.QInputDialog.getText(self, 'Create Vertex',
            'Label:')
        
            if ok:
                self.addVertexToScene(ev.pos(), text)
                

    def addVertexToScene(self, pos, text):
        scn = self.scene()
        self.vtx = QtGui.QGraphicsEllipseItem(0, 0, 40, 40)
        
        self.vtx.setBrush(QtGui.QColor(90, 170, 255))
        scn.addItem(self.vtx)
        self.vtx.setPos(pos)
        
        self.vtxt = QtGui.QGraphicsTextItem(text)
        scn.addItem(self.vtxt)
        
        tw = self.vtxt.boundingRect().width()
        vw = self.vtx.boundingRect().width()
        th = self.vtxt.boundingRect().height()
        vh = self.vtx.boundingRect().height()
        
        self.vtxt.setPos(pos.x() + (vw / 2 - tw / 2), pos.y() + (vh / 2 - th / 2))
                  
            

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.scene = Scene()
        self.netView = NetView()
        self.netView.setScene(self.scene)
        self.netView.setViewport(QtOpenGL.QGLWidget())
        self.scene.setSceneRect(0, 0, 1600, 1600)
        self.scene.setBackgroundBrush(QtGui.QColor(255, 255, 200))
        self.netView.render(QtGui.QPainter())
        
        self.ui.verticalLayout.addWidget(self.netView)

        
       

def main():
    app = QtGui.QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()
