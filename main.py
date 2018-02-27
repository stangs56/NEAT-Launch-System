#!/usr/bin/python3

import sys
from PyQt5.QtWidgets import QApplication
from MainScreen import *

def main():
    #create the application
    application = QApplication(sys.argv)

    main = MainScreen()
    main.create()

    #wait for application to exit
    sys.exit(application.exec_())

if __name__ == "__main__":
    main()
