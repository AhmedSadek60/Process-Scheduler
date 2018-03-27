# -*- coding: utf-8 -*-
"""
Created on Mon Mar 26 21:23:27 2018

@author: mohamed hussien
"""

import sys
#from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import(QApplication,QTabWidget,QTableWidget,QWidgetItem,QMainWindow,QPushButton,QVBoxLayout,QCheckBox,QHBoxLayout,QLabel,QLineEdit,QRadioButton,QWidget)
#from PyQt5.uic import loadUi

class MyTable(QTableWidget):
    def __init__(self, r, c):
        super().__init__(r, c)
        self.show()
class Window (QWidget):
    
    def __init__ (self):
        super().__init__()
        self.l1 = QLabel("algorithms")
        self.l2 = QLabel("no_processes")
        self.le = QLineEdit()
        self.r1 = QRadioButton("FCFS")
        self.r2 = QRadioButton("RB")
        self.r3 = QRadioButton("SJF NON PREEMPTIVE")
        self.r4 = QRadioButton("SJF PREEMPTIVE")
        self.r5 = QRadioButton("PRIORITY NON PREEMPTIVE")
        self.r6 = QRadioButton("PRIORITY PREEMPTIVE")
        self.psh1 = QPushButton("go to table")
        self.psh2 = QPushButton("ok")
        self.psh3 = QPushButton("cancel")
        self.init_gui()
        
    def init_gui(self):
        self.setWindowTitle("Schedular Simulator")
        v1 = QVBoxLayout()
        h3 = QHBoxLayout()
        h4 = QHBoxLayout()
        h5 = QHBoxLayout()
        h3.addWidget(self.l2)
        h3.addStretch()
        h3.addWidget(self.le)
        h4.addStretch()
        h4.addWidget(self.psh1)
        h4.addStretch()
        h5.addWidget(self.psh2)
        h5.addStretch()
        h5.addWidget(self.psh3)
        v1.addWidget(self.l1)
        v1.addWidget(self.r1)
        v1.addWidget(self.r2)
        v1.addWidget(self.r3)
        v1.addWidget(self.r4)
        v1.addWidget(self.r5)
        v1.addWidget(self.r6)
        v1.addLayout(h3)
        v1.addLayout(h4)
        v1.addLayout(h5)
        self.psh1.clicked.connect(self.btn_click) 
        self.setLayout(v1)
        self.show()
        
    def btn_click (self):
        self.form_widget = MyTable(int(self.le.text()), 4)
        col_headers = ['process name', 'arrival time', 'burst time', 'priority']
        self.form_widget.setHorizontalHeaderLabels(col_headers)
        if(self.r1.isChecked()):
            return(self.r1.text())
        elif(self.r2.isChecked()):
            return(self.r2.text())
        elif(self.r3.isChecked()):
            return(self.r3.text())
        elif(self.r4.isChecked()):
            return(self.r4.text())
        elif(self.r5.isChecked()):
            return(self.r5.text())
        else:
            return(self.r6.text())

app = QApplication(sys.argv)
w = Window()
sys.exit(app.exec_())
    


