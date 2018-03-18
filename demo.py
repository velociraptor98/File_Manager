#NOT FINAL CODE 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QAction
from PyQt5.QtGui import QIcon, QFont
import os


class demo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('File_Manager_Demo')
        dirn=os.path.dirname(__file__)
        dirn=dirn+"/Icon"
        self.setWindowIcon(QIcon(dirn+'/files_ico32.png'))   
        menu=self.menuBar()
        fileM=menu.addMenu("File")
        editM=menu.addMenu("Edit")
        searchM=menu.addMenu("search")
        helpM=menu.addMenu("Help")
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = demo()
    sys.exit(app.exec_())