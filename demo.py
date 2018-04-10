
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QToolTip, QMainWindow, QAction, QFileSystemModel, QTreeView, QVBoxLayout, QMessageBox, QInputDialog ,QFileDialog
from PyQt5.QtGui import QIcon, QFont
import webbrowser
import os

"""view class allows the creation of the path struture of the disk"""
class view(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setGeometry(0,0,800,600)
        self.model = QFileSystemModel()
        self.model.setReadOnly(False)
        self.model.setRootPath("")
        self.tree = QTreeView()
        self.tree.setModel(self.model)
        self.tree.setAnimated(True)
        self.tree.setIndentation(10)
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
        dirn=os.path.dirname(__file__)
        dirn1=dirn+"/Icon"
        os.chdir(dirn+"/ test")
        print(os.getcwd())
        self.setWindowIcon(QIcon(dirn1+'/files_ico32.png'))   
        menu=self.menuBar()
        menu.setNativeMenuBar(False)
        fileM=menu.addMenu("File")
        editM=menu.addMenu("Edit")
        searchM=menu.addMenu("Search")
        searchA=QAction(QIcon(dirn1+"/search_ico24.png"),"Search",self)
        searchA.setStatusTip("search for a file")
        searchA.setShortcut("Ctrl+Q")
        searchA.triggered.connect(self.search)
        searchM.addAction(searchA)
        helpM=menu.addMenu("Help")
        newA=QAction(QIcon(dirn1+"/new_ico24.png"),"New",self)
        newA.setShortcut("Ctrl+N")
        newA.triggered.connect(self.newFile)
        openA=QAction(QIcon(dirn1+"/open_ico24.png"),"Open",self)
        openA.setShortcut("Ctrl+O")
        openA.setStatusTip("Opens a file in its native application")
        openA.triggered.connect(self.openFile)
        fileM.addAction(openA)
        renameA=QAction(QIcon(dirn1+"/rename_ico24.png"),"rename",self)
        renameA.setShortcut("Ctrl+R")
        renameA.triggered.connect(self.rename)
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
        aboutA.triggered.connect(self.openurl)
        helpM.addAction(aboutA)
        self.setCentralWidget(view())
        self.show()
        #self.commands()
        
    def openurl(self):
       webbrowser.open("https://github.com/velociraptor98/File_Manager")
    
    def search(self):
        a=False
        fileN,ok=QInputDialog.getText(self,"File search","enter the name of the file")
        if ok:
            dirN,okp=QInputDialog.getText(self,"File Search","enter the directory you want to search");
            if okp:
                dirN=dirN+"\\"
                for root, dirs, files in os.walk(dirN):
                    self.statusBar().showMessage(root)
                    if fileN in files:
                     a=True
                     QMessageBox.about(self,"result",os.path.join(root,fileN))
                     break
                if(a==False):
                    QMessageBox.about(self,"Result","File not found")
                    
    def newFile(self):
     options=QFileDialog.Options()
     fileName, _ = QFileDialog.getSaveFileName(self,"New","","All Files (*);;Text Files (*.txt);;Python(*.py);;C++(*.cpp);;Java(*.java)", options=options)
     if fileName:
         f=open(fileName,"w+")
         f.close()
    
    def openFile(self):
        options=QFileDialog.Options()
        fileName,_=QFileDialog.getOpenFileName(self,"Open","","All Files (*)",options=options)
        if(fileName):
            os.startfile(fileName)
    
    def rename(self):
        QMessageBox.about(self,"IMPORTANT","Double Click on the file name you want to change in the tree and rename .")
        
        
if __name__ == '__main__':
    
    app = QApplication(sys.argv)
    ex = demo()
    sys.exit(app.exec_())