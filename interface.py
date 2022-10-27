# Online Python-3 Compiler (Interpreter)
#!/bin/bash
pip3 install PyQt5

#!/usr/bin/env python3
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import *

app = QApplication([])
app.setStyle('Fusion')
app.setStyleSheet("QPushButton { margin: 10ex; color: red; }")

# Palette
palette = QPalette()
app.setPalette(palette)


# Window layout
window = QWidget()
layout = QVBoxLayout()

layout.addWidget(QLabel('Hello World'))
layout.addWidget(QPushButton('Top'))
layout.addWidget(QPushButton('Bottom'))
window.setLayout(layout)

def main():
    table = self.updateTable(Big21,3,1)
    table.show()
    self.table = table

def createTable():
    
    
    
    
# Table output
def updateTable(self, data, *args):
    columns = ['A','B']
    
    tbl = QTableWidget()
    tbl.setHorizontalHeaderLabels(columns)
    tbl.setRowCount(len(data))
    tbl.setColumnCount(len(data.columns))
    
    for i in range (0,len(data)):
        for j in range (0,len(data.columns)):
            item1 = str(data.iloc[i,j])
            tbl.setItem(i, j,  QTableWidgetItem(item1))
    
    return tableWidget

# Commands
button = QPushButton('Click')
def on_button_clicked():
    alert = QMessageBox()
    alert.setText('You clicked the button!')
    alert.exec()

button.clicked.connect(on_button_clicked)


window.show()
app.exec()



##############################################################
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QAction, QTableWidget,QTableWidgetItem,QVBoxLayout
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'Counter Stalk'
        self.left = 0
        self.top = 0
        self.width = 960
        self.height = 540
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        
        self.createTable()

        # Add box layout, add table to box layout and add box layout to widget
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.tableWidget) 
        self.setLayout(self.layout) 

        # Show widget
        self.show()

    def createTable(self):
       # Create table
        self.tableWidget = QTableWidget()
        self.tableWidget.setRowCount(4)
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setItem(0,0, QTableWidgetItem("Cell (1,1)"))
        self.tableWidget.setItem(0,1, QTableWidgetItem("Cell (1,2)"))
        self.tableWidget.setItem(1,0, QTableWidgetItem("Cell (2,1)"))
        self.tableWidget.setItem(1,1, QTableWidgetItem("Cell (2,2)"))
        self.tableWidget.setItem(2,0, QTableWidgetItem("Cell (3,1)"))
        self.tableWidget.setItem(2,1, QTableWidgetItem("Cell (3,2)"))
        self.tableWidget.setItem(3,0, QTableWidgetItem("Cell (4,1)"))
        self.tableWidget.setItem(3,1, QTableWidgetItem("Cell (4,2)"))
        self.tableWidget.move(0,0)

        # table selection change
        self.tableWidget.doubleClicked.connect(self.on_click)

    @pyqtSlot()
    def on_click(self):
        print("\n")
        for currentQTableWidgetItem in self.tableWidget.selectedItems():
            print(currentQTableWidgetItem.row(), currentQTableWidgetItem.column(), currentQTableWidgetItem.text())
 
if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())  



































