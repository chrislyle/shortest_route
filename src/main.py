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
                scn = self.scene()
                self.vtx = QtGui.QGraphicsEllipseItem(0,0,40,40)
                
                self.vtx.setBrush(QtGui.QColor(255,0,0))
                scn.addItem(self.vtx)
                self.vtx.setPos(ev.pos())
                self.vtxt = QtGui.QGraphicsTextItem(text)
                
                scn.addItem(self.vtxt)
                
                self.vtxt.setPos(ev.pos())
                self.render(QtGui.QPainter())
            
                  
            

class MainWindow(QtGui.QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.scene = Scene()
        self.netView = NetView()
        self.netView.setScene(self.scene)
        self.netView.setViewport(QtOpenGL.QGLWidget())
        self.scene.setSceneRect(0,0,1600,1600)
        self.scene.setBackgroundBrush(QtGui.QColor(255,255,200))
        self.netView.render(QtGui.QPainter())
        
        self.ui.verticalLayout.addWidget(self.netView)

        
       

def main():
    app = QtGui.QApplication(sys.argv)
    wnd = MainWindow()
    wnd.show()
    
    sys.exit(app.exec_())
    

if __name__ == '__main__':
    main()