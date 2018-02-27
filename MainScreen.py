from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSlot

class MainScreen(QWidget):

    def __init__(self):

        super().__init__()



    def create(self):

        #create main window
        #left, top, width, height
        self.setGeometry(300, 300, 750, 450)
        self.setWindowTitle('NEAT Launch System')

        self.show()
