from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def window():
    app = QApplication(sys.argv) # get arguments from system
    win = QMainWindow() # Call to our class
    win.setGeometry(200, 200, 300, 300) # xpos, ypos, width, height
    win.setWindowTitle("Test Window 1 Title") # title bar

    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(50, 50)

    win.show() # show the window
    sys.exit(app.exec_()) # check if qt window exited then exit backend process.

window()
