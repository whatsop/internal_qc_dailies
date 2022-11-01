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

from PySide2 import QtUiTools, QtWidgets, QtCore, QtGui

import folder_utils



FOLDER_PATH = r"D:\PYTHON_ADVANCED_COURSE\folder_for_testing"
class InternalQcDailies(QtWidgets.QWidget):
    
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Internal QC Dailies")
        self.setMinimumSize(1250, 750)
        
        self.qvbox_layout = QtWidgets.QVBoxLayout()
        

        self.qline_filter = QtWidgets.QLineEdit()
        self.btn_hide_row = QtWidgets.QPushButton("Filter")
        self.btn_hide_row.setMaximumSize(100, 100)
        self.btn_unhide_row = QtWidgets.QPushButton("Clear")
        self.btn_unhide_row.setMaximumSize(100, 100)
        self.table = QtWidgets.QTableWidget()

        # set headers labels for the table
        self.table_header_elements = ["username", "show", "shot", "department", "date", "description", "daily"]
        self.table.setColumnCount(len(self.table_header_elements))
        self.table.setHorizontalHeaderLabels(self.table_header_elements)
        
        self.dailies = folder_utils.get_files(folder_path=FOLDER_PATH, file_type=".mp4")
        self.table.setRowCount(len(self.dailies))
        
        for row, data in enumerate(self.dailies):
            self.json_data = folder_utils.get_json_data(data.replace(".mp4", "_info.json"))["daily_info"]
            count = 0
            for key, val in self.json_data.items():
                self.table.setItem(row, count, QtWidgets.QTableWidgetItem(val))
                
                count += 1
            
            self.btn_rv = QtWidgets.QPushButton("play")
            self.table.setCellWidget(row, len(self.table_header_elements) - 1, self.btn_rv)
            

        self.table.setEditTriggers(QtWidgets.QTableWidget.NoEditTriggers)
        self.table.resizeColumnsToContents()
        self.table.resizeRowsToContents()
        
        
        self.rows_not_hidden = []
        self.btn_hide_row.clicked.connect(self.hide_rows)
        self.btn_unhide_row.clicked.connect(self.unhide_rows)
        
        self.qvbox_layout.addWidget(self.qline_filter)
        self.qvbox_layout.addWidget(self.btn_hide_row)
        self.qvbox_layout.addWidget(self.btn_unhide_row)
        self.qvbox_layout.addWidget(self.table)
        self.setLayout(self.qvbox_layout)


    def hide_rows(self):
        filter_text = self.qline_filter.text()

        
        rows = self.table.rowCount()
        columns = self.table.columnCount()
        for row in range(rows):
            for column in range(columns - 1):
                item = self.table.item(row, column).text()
                if filter_text in item:
                    self.rows_not_hidden.append(row)
                    
        for row in range(rows):
            if not row in self.rows_not_hidden:
                self.table.setRowHidden(row, True)
        
        self.rows_not_hidden.clear()
        
    def unhide_rows(self):
        rows = self.table.rowCount()
        for row in range(rows):
                self.table.setRowHidden(row, False)
        self.rows_not_hidden.clear()
        self.qline_filter.setText("")


def start():
    app = QtWidgets.QApplication(sys.argv)
    win = InternalQcDailies()
    win.show()
    sys.exit(app.exec_())

start()
        