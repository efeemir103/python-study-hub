# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tutorial5.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        # Setting a label that we will use to show photo after.
        self.photo = QtWidgets.QLabel(self.centralwidget)
        self.photo.setGeometry(QtCore.QRect(7, 4, 791, 411))
        self.photo.setText("")
        # Setting a photo.
        self.photo.setPixmap(QtGui.QPixmap("imgs/areyoustillinpain.jpg"))
        # Autoscaling to fit photo to label.
        self.photo.setScaledContents(True)
        self.photo.setObjectName("photo")
        self.changeToPhoto_1 = QtWidgets.QPushButton(self.centralwidget)
        self.changeToPhoto_1.setGeometry(QtCore.QRect(0, 420, 371, 161))
        self.changeToPhoto_1.setObjectName("changeToPhoto_1")
        self.changeToPhoto_2 = QtWidgets.QPushButton(self.centralwidget)
        self.changeToPhoto_2.setGeometry(QtCore.QRect(420, 420, 371, 161))
        self.changeToPhoto_2.setObjectName("changeToPhoto_2")
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

        # Linking up buttons with events
        self.changeToPhoto_1.clicked.connect(self.show_photo_1)
        self.changeToPhoto_2.clicked.connect(self.show_photo_2)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.changeToPhoto_1.setText(_translate("MainWindow", "Are you still in pain?"))
        self.changeToPhoto_2.setText(_translate("MainWindow", "Pepe"))

    def show_photo_1(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/areyoustillinpain.jpg"))

    def show_photo_2(self):
        self.photo.setPixmap(QtGui.QPixmap("imgs/pepe_bad_wallpaper.png"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
