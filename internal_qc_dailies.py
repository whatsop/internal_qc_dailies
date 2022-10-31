"""
content : a tool where artists can publish their flipbooks/playblast/renders, 
and leads/sups can review/qc, add a comment for any retakes before publishing 
to any external production tool like Shotgun 

version : 0.1.0
date : 10/25/2022

how to : start()
dependencies : 

author : Arup Kasimov
"""

import os
import sys

from PySide2 import QtUiTools, QtWidgets, QtCore


class InternalQcDailies(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Internal QC Dailies")
        
    
    



def start():
    app = QtWidgets.QApplication(sys.argv)
    win = InternalQcDailies()
    win.show()
    sys.exit(app.exec_())

start()
        