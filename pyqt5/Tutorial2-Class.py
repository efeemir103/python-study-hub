from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow, self).__init__() # just inherit the super constructor.
        self.initUI() # set widgets for our window
        self.setGeometry(200, 200, 300, 300) # xpos, ypos, width, height
        self.setWindowTitle("Test Window 1 Title") # title bar

    def initUI(self):
        self.label = QtWidgets.QLabel(self)
        self.label.setText("my first label!")
        self.label.move(50, 50) # set label position to x = 50, y = 50

        self.b1 = QtWidgets.QPushButton(self) # Adding a button
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked) # add signal handler

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update() # Call here to fix

    def update(self):
        self.label.adjustSize()
        # Adjust size of the label since the new text after clicking is
        # overflown the label width.

def window():
    app = QApplication(sys.argv) # get arguments from system
    win = MyWindow() # Call to our class
    win.show() # show the window
    sys.exit(app.exec_()) # check if qt window exited then exit backend process.

window()
