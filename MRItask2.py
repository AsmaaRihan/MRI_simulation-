# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MRItask2.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1050, 534)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.splitter = QtWidgets.QSplitter(self.groupBox)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.splitter)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.showphantom = Label(self.verticalLayoutWidget)
        self.showphantom.setObjectName("showphantom")
        self.verticalLayout.addWidget(self.showphantom)
        self.label_2 = QtWidgets.QLabel(self.verticalLayoutWidget)
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.tabWidget = QtWidgets.QTabWidget(self.splitter)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.t2 = PlotWidget(self.tab)
        self.t2.setObjectName("t2")
        self.gridLayout_3.addWidget(self.t2, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.tab)
        self.label_3.setObjectName("label_3")
        self.gridLayout_3.addWidget(self.label_3, 0, 0, 1, 1)
        self.label = QtWidgets.QLabel(self.tab)
        self.label.setObjectName("label")
        self.gridLayout_3.addWidget(self.label, 1, 0, 1, 1)
        self.t1 = PlotWidget(self.tab)
        self.t1.setObjectName("t1")
        self.gridLayout_3.addWidget(self.t1, 0, 1, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.splitter_2 = QtWidgets.QSplitter(self.tab_2)
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.kspace = QtWidgets.QLabel(self.splitter_2)
        self.kspace.setScaledContents(True)
        self.kspace.setObjectName("kspace")
        self.constImage = QtWidgets.QLabel(self.splitter_2)
        self.constImage.setScaledContents(True)
        self.constImage.setObjectName("constImage")
        self.gridLayout_2.addWidget(self.splitter_2, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout_4.addWidget(self.splitter, 4, 0, 1, 6)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setScaledContents(True)
        self.label_7.setObjectName("label_7")
        self.horizontalLayout_4.addWidget(self.label_7, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.flipangle = QtWidgets.QLineEdit(self.groupBox)
        self.flipangle.setObjectName("flipangle")
        self.horizontalLayout_4.addWidget(self.flipangle, 0, QtCore.Qt.AlignHCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_4, 2, 5, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setScaledContents(True)
        self.label_6.setObjectName("label_6")
        self.horizontalLayout_3.addWidget(self.label_6, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TE = QtWidgets.QLineEdit(self.groupBox)
        self.TE.setObjectName("TE")
        self.horizontalLayout_3.addWidget(self.TE, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_3, 2, 3, 1, 1)
        self.comboBox = QtWidgets.QComboBox(self.groupBox)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.gridLayout_4.addWidget(self.comboBox, 2, 1, 1, 1)
        self.Browse = QtWidgets.QPushButton(self.groupBox)
        self.Browse.setObjectName("Browse")
        self.gridLayout_4.addWidget(self.Browse, 2, 0, 1, 1)
        self.comboBox_2 = QtWidgets.QComboBox(self.groupBox)
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.gridLayout_4.addWidget(self.comboBox_2, 2, 2, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setScaledContents(True)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_2.addWidget(self.label_5, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.TR = QtWidgets.QLineEdit(self.groupBox)
        self.TR.setObjectName("TR")
        self.horizontalLayout_2.addWidget(self.TR, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.gridLayout_4.addLayout(self.horizontalLayout_2, 2, 4, 1, 1)
        self.start = QtWidgets.QPushButton(self.groupBox)
        self.start.setObjectName("start")
        self.gridLayout_4.addWidget(self.start, 3, 0, 1, 2)
        self.gridLayout.addWidget(self.groupBox, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1050, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "GroupBox"))
        self.showphantom.setText(_translate("MainWindow", "TextLabel"))
        self.label_3.setText(_translate("MainWindow", "Mx"))
        self.label.setText(_translate("MainWindow", "Mz"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Tab 1"))
        self.kspace.setText(_translate("MainWindow", "TextLabel"))
        self.constImage.setText(_translate("MainWindow", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Tab 2"))
        self.label_7.setText(_translate("MainWindow", "flipangle"))
        self.label_6.setText(_translate("MainWindow", "TE"))
        self.comboBox.setItemText(0, _translate("MainWindow", "PD"))
        self.comboBox.setItemText(1, _translate("MainWindow", "T1"))
        self.comboBox.setItemText(2, _translate("MainWindow", "T2"))
        self.Browse.setText(_translate("MainWindow", "Browse"))
        self.comboBox_2.setItemText(0, _translate("MainWindow", "128"))
        self.comboBox_2.setItemText(1, _translate("MainWindow", "64"))
        self.comboBox_2.setItemText(2, _translate("MainWindow", "32"))
        self.label_5.setText(_translate("MainWindow", "TR"))
        self.start.setText(_translate("MainWindow", "start sequqnce"))

from pyqtgraph import PlotWidget
class Label(QtWidgets.QLabel):
    def __init__(self, parent=None):
        super(Label, self).__init__(parent=parent)
        self.paint = False
        self.paint1 = False
        self.x = 0
        self.y = 0
        self.count = 0
        self.point = []
        self.pixel = []
    def paintEvent(self, e):
        super().paintEvent(e)
        painter = QtGui.QPainter(self)
        painter.setRenderHint(QtGui.QPainter.Antialiasing)
        #if self.paint:
        for self.pixel in self.point:
            painter.setPen(self.pixel[2])
            painter.drawRect(self.pixel[0], self.pixel[1], 8, 8)