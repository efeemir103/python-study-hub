# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tutorial6.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(20, 30, 751, 491))
        font = QtGui.QFont()
        font.setPointSize(36)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 20))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.pushButton.clicked.connect(self.show_popup)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Show Popup"))

    def show_popup(self):
        msg = QMessageBox()
        msg.setWindowTitle("Tutorial on PyQt5")
        msg.setText("This is the main text!")
        # Default icons: Critical, Warning, Question, Information
        msg.setIcon(QMessageBox.Question)
        # Note that the buttons will not be passed in order.
        msg.setStandardButtons(QMessageBox.Cancel | \
            QMessageBox.Retry | QMessageBox.Ignore)
        # Set a button different than leftmost one to be selected as default.
        msg.setDefaultButton(QMessageBox.Ignore)

        # Informative text under the normal text.
        msg.setInformativeText("informative text, ya!")

        # Set a detailed text.
        msg.setDetailedText("details")

        # Handle clicked buttons.
        msg.buttonClicked.connect(self.popup_button)
        
        x = msg.exec_()

    def popup_button(self, i):
        # Print out the text of clicked button.
        print(i.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
