from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

def clicked():
    print("clicked")

def window():
    app = QApplication(sys.argv) # get arguments from system
    win = QMainWindow()
    win.setGeometry(200, 200, 300, 300) # xpos, ypos, width, height
    win.setWindowTitle("Test Window 1 Title")

    label = QtWidgets.QLabel(win)
    label.setText("my first label!")
    label.move(50, 50) # set label position to x = 50, y = 50

    b1 = QtWidgets.QPushButton(win) # Adding a button
    b1.setText("Click me")
    b1.clicked.connect(clicked) # add signal handler

    win.show() # show the window
    sys.exit(app.exec_()) # check if qt window exited then exit backend process.

window()
