#NOT FINAL CODE 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QAction 
from PyQt5.QtGui import QIcon, QFont
import os


class demo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.statusBar()
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
        searchM=menu.addMenu("Search")
        searchA=QAction(QIcon(dirn+"/search_ico24.png"),"Search",self)
        searchA.setStatusTip("search for a file")
        searchA.setShortcut("Ctrl+Q")
        searchM.addAction(searchA)
        helpM=menu.addMenu("Help")
        newA=QAction(QIcon(dirn+"/new_ico24.png"),"New",self)
        newA.setShortcut("Ctrl+N")
        renameA=QAction(QIcon(dirn+"/rename_ico24.png"),"rename",self)
        renameA.setShortcut("Ctrl+R")
        renameA.setStatusTip("Renames a file")
        editM.addAction(renameA)
        deleteA=QAction(QIcon(dirn+"/delete_ico24.png"),"delete",self)
        deleteA.setShortcut("Ctrl+D")
        deleteA.setStatusTip("Deletes a file")
        editM.addAction(deleteA)
        newA.setStatusTip("Creates a new file")
        fileM.addAction(newA)
        exitA=QAction(QIcon(dirn+"/exit_ico24.png"),"&Exit",self)
        exitA.setShortcut("Ctrl+E")
        exitA.setStatusTip("closes the file manager")
        exitA.triggered.connect(self.close)
        fileM.addAction(exitA)
        aboutA=QAction(QIcon(dirn+"/about_ico24.png"),"About",self)
        aboutA.setStatusTip("Displays Information about the applicatin")
        helpM.addAction(aboutA)
        self.show()
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = demo()
    sys.exit(app.exec_())