#NOT FINAL CODE 
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QAction, QFileSystemModel, QTreeView, QVBoxLayout 
from PyQt5.QtGui import QIcon, QFont
import os

"""view class allows the creation of the path struture of the disk"""
class view(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,800,600)
        self.model = QFileSystemModel()
        self.model.setRootPath("")
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(True)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        self.tree.setWindowTitle("Dir View")
        self.tree.resize(640, 480)
        windowLayout = QVBoxLayout()
        windowLayout.addWidget(self.tree)
        self.setLayout(windowLayout)
        self.show()
        

"""" creates the main window for displaying the various elements"""
class demo(QMainWindow):
    
    def __init__(self):
        super().__init__()
        self.statusBar()
        self.initUI()
        
        
    def initUI(self):
        
        self.setGeometry(300, 300, 800, 600)
        self.setWindowTitle('File_Manager')
        self.model=QFileSystemModel()
        dirn=os.path.dirname(__file__)
        dirn1=dirn+"/Icon"
        os.chdir(dirn+"/ test")
        print(os.getcwd())
        self.model.setRootPath("")
        self.tree=QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(False)
        self.tree.setIndentation(20)
        self.tree.setSortingEnabled(True)
        windowsLayout=QVBoxLayout()
        windowsLayout.addWidget(self.tree)
        self.setLayout(windowsLayout)
        self.setWindowIcon(QIcon(dirn1+'/files_ico32.png'))   
        menu=self.menuBar()
        menu.setNativeMenuBar(False)
        fileM=menu.addMenu("File")
        editM=menu.addMenu("Edit")
        searchM=menu.addMenu("Search")
        searchA=QAction(QIcon(dirn1+"/search_ico24.png"),"Search",self)
        searchA.setStatusTip("search for a file")
        searchA.setShortcut("Ctrl+Q")
        searchM.addAction(searchA)
        helpM=menu.addMenu("Help")
        newA=QAction(QIcon(dirn1+"/new_ico24.png"),"New",self)
        newA.setShortcut("Ctrl+N")
        renameA=QAction(QIcon(dirn1+"/rename_ico24.png"),"rename",self)
        renameA.setShortcut("Ctrl+R")
        renameA.setStatusTip("Renames a file")
        editM.addAction(renameA)
        deleteA=QAction(QIcon(dirn1+"/delete_ico24.png"),"delete",self)
        deleteA.setShortcut("Ctrl+D")
        deleteA.setStatusTip("Deletes a file")
        editM.addAction(deleteA)
        newA.setStatusTip("Creates a new file")
        fileM.addAction(newA)
        exitA=QAction(QIcon(dirn1+"/exit_ico24.png"),"&Exit",self)
        exitA.setShortcut("Ctrl+E")
        exitA.setStatusTip("closes the file manager")
        exitA.triggered.connect(self.close)
        fileM.addAction(exitA)
        aboutA=QAction(QIcon(dirn1+"/about_ico24.png"),"About",self)
        aboutA.setStatusTip("Displays Information about the applicatin")
        helpM.addAction(aboutA)
        self.setCentralWidget(view())
        self.show()
        #self.commands()
        
        
    """def commands(self):
        a=input("enter the name of the new file")+".txt"
        file=open(a,"a")"""
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = demo()
    sys.exit(app.exec_())