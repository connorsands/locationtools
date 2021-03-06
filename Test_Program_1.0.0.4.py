# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Test_Program_1.0.0.0.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import pandas as pd
import matplotlib
import glob
from IPython.display import display
matplotlib.use('Qt5Agg')
import matplotlib.pyplot as plt
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog, QDialog, QPushButton, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QIcon, QPalette, QColor
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from PyQt5.QtWidgets import *
from datetime import datetime
from PyQt5.QtGui import *
import os

class Ui_mainWindow(object):
    def Plotcsv(self):
        """self.figure.clear()"""
        var = pd.read_csv("PlotT.csv")
        print(var)
    
        x = list(var['xcoord'])
        y = list(var['ycoord'])
        annotations1 = list(var['Line Number'])
        annotations2 = list(var['Station Number'])
        plt.figure(figsize=(10,10))
        plt.style.use('seaborn')
        plt.scatter(x,y,marker=".",s=100,edgecolors="black",c="blue")
        plt.title("Locations Viewer")
        plt.xlabel("Easting")
        plt.ylabel("Northing")
        for i, label in enumerate(annotations1):
            plt.annotate(label, (x[i], y[i]), textcoords="offset points", xytext=(1,36), size=13, weight="bold", rotation=-90)
    
        for i, label in enumerate(annotations2):
            plt.annotate(label, (x[i], y[i]), textcoords="offset points", xytext=(1,5), size=13, weight="bold", rotation=-90)
    
        
        plt.show()

    def Mergecsv(self):
        path = r'C:\Users\ConnorSands\OneDrive - DIAS Geophysical\Documents\Test Program\Location Spreadsheets'
        path2 = r'C:\Users\ConnorSands\OneDrive - DIAS Geophysical\Documents\Test Program\Master Spreadsheets'
        all_files = glob.glob(path + "/*.csv")

        li = []

        for filename in all_files:
            df = pd.read_csv(filename, index_col=None, header=0)
            li.append(df)

        frame = pd.concat(li, axis=0, ignore_index=True)

        current_date_and_time = datetime.date(datetime.now())
        print(current_date_and_time)
        current_date_and_time_string = str(current_date_and_time)
        currenttime = datetime.now()
        dt_string = currenttime.strftime("%H%M%S")
        print(dt_string)
        extension = ".csv"

        file_name = "Master Spreadsheet" + " " + current_date_and_time_string + " " + dt_string + extension

        print('Final Sheet:')
        display(li)
 
        frame.to_csv(os.path.join(path2,file_name), index=False, mode='w+')

    def filebrowse(self):
        wig = app()

    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.setEnabled(True)
        mainWindow.resize(872, 756)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        mainWindow.setFont(font)
        mainWindow.setAutoFillBackground(False)
        mainWindow.setDocumentMode(False)
        """self.setWindowIcon(QtGui.QIcon('LVicon.ico'))"""
        """self.setStyleSheet("background-color: #F5F5DC;")"""
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.Mergecsv)
        self.gridLayout.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.graphicsView = QtWidgets.QGraphicsView(self.centralwidget)
        self.graphicsView.setObjectName("graphicsView")
        self.gridLayout.addWidget(self.graphicsView, 0, 1, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.Plotcsv)
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 4, 0, 1, 1)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout.addWidget(self.lineEdit, 3, 1, 1, 1)
        """self.figure = plt.figure()
        self.canvas = FigureCanvas(self.figure)
        layout = QVBoxLayout()
        layout.addWidget(self.canvas)
        widget = QtWidgets.QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.show()"""
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_4.clicked.connect(self.filebrowse)
        self.gridLayout.addWidget(self.pushButton_4, 3, 2, 1, 1)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 872, 22))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(mainWindow)
        self.pushButton_3.clicked.connect(mainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Test Program 1.0.0.0"))
        self.pushButton_2.setText(_translate("mainWindow", "Merge Spreadsheets"))
        self.pushButton.setText(_translate("mainWindow", "Plot Locations"))
        self.pushButton_3.setText(_translate("mainWindow", "Close Program"))
        self.pushButton_4.setText(_translate("mainWindow", "Browse"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
