# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from MRItask2 import Ui_MainWindow
import sys
import math
from math import exp, cos, sin, pi, sqrt
import traceback
import cv2
import numpy as np
from matplotlib import pyplot as plt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage,QMouseEvent
from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication, QFileDialog
from PyQt5.QtGui import QImage, QColor, QBrush, QPainter, QPen, QDragEnterEvent
from PyQt5.QtCore import Qt
from PIL import Image, ImageEnhance
from imageio import imsave, imread
import scipy.io as sio
import io
from time import sleep
import pyqtgraph as pg
from matplotlib.mlab import psd
import sk_dsp_comm.sigsys as ss
from sk_dsp_comm.sigsys import delta_eps
#import pyqtgraph.exporters




class ApplicationWindow(QtWidgets.QMainWindow):
    global myImg
    
    def __init__(self):
        super(ApplicationWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        self.ui.Browse.clicked.connect(self.Browse_clicked)
        
        self.ui.showphantom.setMouseTracking(False)
        self.ui.comboBox.currentIndexChanged.connect(self.choose)
        self.ui.comboBox_2.currentIndexChanged.connect(self.choose_2)

        self.brit = 0
        self.points = QtGui.QPolygon()  
        self.estna = False
        self.size = "64"
        self.state = "PD"
        self.label_height= self.ui.showphantom.geometry().height()      
        self.label_width= self.ui.showphantom.geometry().width()
        self.ui.TE.clear()
        self.ui.TR.clear()
        self.ui.flipangle.clear()
        self.ui.TE.editingFinished.connect(self.Kspace)
        self.ui.TR.editingFinished.connect(self.Kspace)
        self.ui.flipangle.editingFinished.connect(self.Kspace)

        self.ui.tabWidget.setCurrentIndex(0)

        self.ui.showphantom.installEventFilter(self)
        self.pen=[QtGui.QPen(QtCore.Qt.green),QtGui.QPen(QtCore.Qt.red),QtGui.QPen(QtCore.Qt.yellow),QtGui.QPen(QtCore.Qt.blue)]
        self.Pen1=[pg.mkPen('g'),pg.mkPen('r'),pg.mkPen('y'),pg.mkPen('b')]
        self.counter=-1
        self.point1x=0
        self.point2x=0
        self.point3x=0
        self.point4x=0
        self.point1y=0
        self.point2y=0
        self.point3y=0
        self.point4y=0
        

        
        
    def Browse_clicked(self):
       self.fileName,_ = QFileDialog.getOpenFileName(self," "," ", "All Files (*) ;; Python Files (*.jpg)")
       if self.fileName:
         All =np.load(self.fileName)
         PD=All[0]
         self.T1=All[1]
         self.T2=All[2]
         
         imsave("Pd.png", PD)
         imsave("T1.png", self.T1)
         imsave("T2.png", self.T2)
         
         self.myImage = cv2.imread("Pd.png" , cv2.IMREAD_GRAYSCALE)
         
         self.fileName0 = "Pd.png"
         self.fileName1 = "T1.png"
         self.fileName2 = "T2.png"
         
         self.height, self.width = self.myImage.shape
         
         self.pixmap = QtGui.QPixmap(self.fileName0)
         
         self.ui.showphantom.setScaledContents(True)
         self.ui.constImage.setScaledContents(True)
         self.ui.kspace.setScaledContents(True)

         self.ui.showphantom.setMouseTracking(False)
         
         self.ui.showphantom.mouseMoveEvent = self.changeBrit
         self.ui.showphantom.mouseDoubleClickEvent = self.getClick
         
         self.ui.comboBox.currentIndexChanged.connect(self.choose)
         self.ui.comboBox_2.currentIndexChanged.connect(self.choose_2)
         
         self.label_height= self.ui.showphantom.geometry().height()      
         self.label_width= self.ui.showphantom.geometry().width()
         
         
         
         
         self.estna = True
         self.Kspace()
         self.plot()
         
    def mousePressEvent(self, e):
        self.points << e.pos()
        self.update()

    def eventFilter (self,source,event):
        
        if event.type() == event.MouseButtonDblClick and QMouseEvent.button(event) == Qt.LeftButton:
            self.counter += 1
            self.x = event.pos().x()
            self.y = event.pos().y()
            
            self.label_width=self.ui.showphantom.geometry().width()
            self.label_height=self.ui.showphantom.geometry().height()

            self.scaled_x=self.label_width/self.height
            self.scaled_y=self.label_height/self.height
            
            
            self.x1=math.floor((self.x/self.label_width)*self.height)
            self.y1=math.floor((self.y/self.label_height)*self.height)
            
            self.plot()
            
        if event.type() == event.Resize:
            
            self.NH= self.ui.showphantom.geometry().height()      
            self.NW= self.ui.showphantom.geometry().width()
            
            self.scaled_x=self.NW/self.label_width
            self.scaled_y=self.NH/self.label_height


            self.ui.showphantom.point = []
            
            
            if  self.point1x != 0 and  self.point1y != 0:
                self.point1x_s=self.point1x*self.scaled_x
                self.point1y_s=self.point1y*self.scaled_y
                
                self.ui.showphantom.point.append([self.point1x_s ,self.point1y_s,QtCore.Qt.green])

                
            if  self.point1x != 0 and  self.point1y != 0:
                self.point2x_s=self.point2x*self.scaled_x
                self.point2y_s=self.point2y*self.scaled_y
                self.ui.showphantom.point.append([self.point2x_s ,self.point2y_s,QtCore.Qt.red])
            
            if  self.point1x != 0 and  self.point1y != 0:
                self.point3x_s=self.point3x*self.scaled_x
                self.point3y_s=self.point3y*self.scaled_y
                self.ui.showphantom.point.append([self.point3x_s ,self.point3y_s,QtCore.Qt.yellow])
            
            if  self.point1x != 0 and  self.point1y != 0:
                self.point4x_s=self.point4x*self.scaled_x
                self.point4y_s=self.point4y*self.scaled_y
                self.ui.showphantom.point.append([self.point4x_s ,self.point4y_s,QtCore.Qt.blue])

                
         
    def getClick(self, event):
        #contrast
        if event.button() == Qt.LeftButton:
            self.left = True
            self.right = False
        if event.button() == Qt.RightButton:
            self.right = True
            self.left = False
           
        if event.button() == Qt.RightButton:            
            self.ui.showphantom.point = []
            self.ui.t1.clear()
            self.ui.t2.clear()
            self.counter=-1
            
            self.point1x=0
            self.point2x=0
            self.point3x=0
            self.point4x=0
            self.point1y=0
            self.point2y=0
            self.point3y=0
            self.point4y=0
            

    def plot(self):
             
            if self.counter== 0 :
                self.point1x=self.x
                self.point1y=self.y
                
            if self.counter== 1 :
                self.point2x=self.x
                self.point2y=self.y
               
            if self.counter== 2 :
                self.point3x=self.x
                self.point3y=self.y
        
            if self.counter== 3 :
                self.point4x=self.x
                self.point4y=self.y
                
                
            self.ui.showphantom.point.append([ self.x, self.y,self.pen[self.counter]])

    
            
            t = np.arange (0. , 500. ,1.)
            Mx = np.exp(-t /self.T2[self.x1][self.y1])
            Mz = 1-np.exp(-t/self.T1[self.x1][self.y1])
            
            self.ui.t1.plot(t ,np.ravel(Mx),pen=self.Pen1[self.counter])
            self.ui.t2.plot(t ,np.ravel(Mz),pen=self.Pen1[self.counter])
            #self.ui.tab3.plot(t,pen=self)
            
        

       
    def choose(self):
        self.state = self.ui.comboBox.currentText()
        if self.state == 'PD':
                self.pixmap = QtGui.QPixmap(self.fileName0)
        if self.state == 'T1':
                self.pixmap = QtGui.QPixmap(self.fileName1)
        if self.state == 'T2':
                self.pixmap = QtGui.QPixmap(self.fileName2)
       


    def choose_2 (self) :
        self.size = self.ui.comboBox_2.currentText()
     
    def paintEvent(self, event):
        if self.estna:
            pixmap = self.pixmap
            if self.size == '128':
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '64':
                pixmap = pixmap.scaled(64,64)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '32':
                pixmap = pixmap.scaled(32,32)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-
            if self.size == '2':
                pixmap = pixmap.scaled(3,3)
                self.ui.showphantom.setPixmap(pixmap)# -*- coding: utf-8 -*-

# To change the brightness
    def changeBrit(self, event):
        if self.left:
           self.brit += 0.01
           im = Image.open(self.fileName0)
           enhancer = ImageEnhance.Brightness(im)
           enhanced_im = enhancer.enhance(self.brit)
           enhanced_im.save('enhanced_pic.jpg')
           fileName1 = "enhanced_pic.jpg"
           self.pixmap = QtGui.QPixmap(fileName1)
        if self.right:
           self.brit -= 0.01
           im = Image.open(self.fileName0)
           enhancer = ImageEnhance.Brightness(im)
           enhanced_im = enhancer.enhance(self.brit)
           enhanced_im.save('enhanced_pic.jpg')
           fileName1 = "enhanced_pic.jpg"
           self.pixmap = QtGui.QPixmap(fileName1)
    
            
    def Kspace(self):
        
                self.width
#                print(phSize)
                TR=int(self.ui.TR.text())
#                print(TR)
                self.TRline = TR 
                TE=int(self.ui.TE.text())
#                print(TE)
                self.TEline = TE 
                theta=int(self.ui.flipangle.text())               
#                print(theta)
                theta=(theta*pi)/180
                Signal=np.zeros((self.height,self.width,3))
                Signal[0:self.height,0:self.width,0]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,1]=np.zeros((self.height,self.width))
                Signal[0:self.height,0:self.width,2]=np.ones((self.height,self.width)) 
                Kspace=np.zeros((self.height,self.width),dtype=np.complex)
                RX=np.array([[1,0,0],[0,cos(theta),sin(theta)],[0,-sin(theta),cos(theta)]])
                
                # Kspace 
                for i in range(self.height):   ## enter Kspace rows 
                    for k in range(self.height):
                        for m in range(self.width):
                            Signal[k][m]=np.matmul(RX,Signal[k][m])  #3*1
                            Decay=np.array([[exp(-TE/self.T2[k][m]),0,0],[0,exp(-TE/self.T2[k][m]),0],[0,0,exp(-TE/self.T1[k][m])]]) #3*3
                            Signal[k][m]=np.matmul(Decay,Signal[k][m])  #3*1                        
                    QtGui.QApplication.processEvents()
                    for j in range(self.height): # enter Kspace columns
                         Gy=(j/self.height)*(2*pi) #multi in cols
                         Gx= (i/self.width)*(2*pi) # *rows
                         for k in range(self.height):
                             for m in range (self.width):          
                                 alpha=Gx*k+Gy*m
                                 x=Signal[k][m][0]
                                 y=Signal[k][m][1]
                                 z=sqrt(x**2+y**2)
                                 Kspace[i][j]+=z*complex(cos(alpha),sin(alpha)) #remember to divied on 180 and make GX,Gy degrees
                    QtGui.QApplication.processEvents()    
                    Signal[0:self.height][0:self.width][0]=0
                    Signal[0:self.height][0:self.width][1]=0
                    for k in range(self.height):
                        for m in range (self.width):                    #print(Kspace)
                            Signal[k][m][2]=(1-exp(-TR/self.T1[k][m]))
                            #kspace finished 
                
                
                # start to constrcted Phantom
                Phantom=np.fft.fft2(Kspace)
                Phantom1=abs(Phantom)
                imsave("phantom.png", Phantom1)
                Kspace1=abs(Kspace)
                imsave("Kspace.png", Kspace1)
                ks = QtGui.QPixmap("Kspace.png")
                ks=ks.scaled(300,200)
                pixmap = QtGui.QPixmap("phantom.png")
                pixmap = pixmap.scaled(300, 200, QtCore.Qt.KeepAspectRatio) 
                self.ui.constImage.setPixmap(pixmap)
                self.ui.kspace.setPixmap(ks)
                QtGui.QApplication.processEvents()
                print('kspace')
#           
def main():
     app = QtWidgets.QApplication(sys.argv)
     application = ApplicationWindow()
     application.show()
     sys.exit(app.exec_())


if __name__ == "__main__":
    main()        
