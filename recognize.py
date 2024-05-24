from PyQt6 import QtCore, QtWidgets
from PyQt6.QtWidgets import QMainWindow


class Recognize_Window(QMainWindow):
    def __init__(self, mw_cls):
        self.mv_cls = mw_cls
        super(Recognize_Window, self).__init__()
        self.setObjectName("MainWindow")
        self.resize(480, 640)
        self.setMinimumSize(QtCore.QSize(480, 640))
        self.setMaximumSize(QtCore.QSize(480, 640))
        self.setStyleSheet("background-color: rgb(225, 250, 252);")
        self.centralwidget = QtWidgets.QWidget(parent=self)
        self.centralwidget.setObjectName("centralwidget")
        self.strip = QtWidgets.QLabel(parent=self.centralwidget)
        self.strip.setGeometry(QtCore.QRect(0, 580, 511, 61))
        self.strip.setStyleSheet("background-color: rgb(106, 106, 106);")
        self.strip.setText("")
        self.strip.setObjectName("strip")
        self.label_2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(-20, 0, 481, 211))
        self.label_2.setStyleSheet("image: url(static/logo.png);")
        self.label_2.setText("")
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(parent=self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 220, 361, 151))
        self.label.setStyleSheet("image: url(static/recognizing.png);")
        self.label.setText("")
        self.label.setObjectName("label")
        self.setCentralWidget(self.centralwidget)

        self.retranslateUi(self)
        QtCore.QMetaObject.connectSlotsByName(self)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

    def closeEvent(self, a0):
        self.mv_cls.reset()
        super(Recognize_Window, self).closeEvent(a0)

