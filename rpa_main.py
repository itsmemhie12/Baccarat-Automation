# -*- coding: utf-8 -*-
"""
Created on Tue Nov  9 18:39:06 2021

@author: michael
"""
#Installation of Packages
import sys
sys.path.append('./scripts')
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import  *
import os
import datetime as date
import pandas as pd
import time 
from main import run


class betwayRPA(QDialog):
    def __init__(self):
        super(betwayRPA, self).__init__()
        loadUi('./UI/rpa bacarrat.ui', self)
        widget.setFixedHeight(215)
        widget.setFixedWidth(400)
        self.pushButton.clicked.connect(self.run)
        self.pushButton_2.clicked.connect(self.inputFile)
    
    def inputFile(self):
        path = os.getcwd()
        file_path = QFileDialog.getOpenFileName(self,  'Open File', path, filter="Excels files (*.xlsx *.xls)")  
        self.lineEdit.setText(file_path[0])
        self.input_file = file_path[0]
        
    def run(self):
        run_rpa = run(self.input_file)
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = QtWidgets.QStackedWidget()                   #Stacking all the UI file into one list
    main = betwayRPA()
    widget.addWidget(main)                               #Adding main class into the stackedwidgets
    widget.show()
    sys.exit(app.exec_())
