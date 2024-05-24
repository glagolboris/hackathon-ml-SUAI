from PyQt6 import QtCore, QtGui, QtWidgets
from recognize import Recognize_Window


class MainWindow(object):
    button_uploaded = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1000, 700)
        MainWindow.setMinimumSize(QtCore.QSize(1000, 700))
        MainWindow.setMaximumSize(QtCore.QSize(1000, 700))
        MainWindow.setToolTipDuration(0)
        MainWindow.setStyleSheet("background-color: rgb(225, 250, 252);")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.strip_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.strip_label.setGeometry(QtCore.QRect(0, 610, 1001, 101))
        self.strip_label.setStyleSheet("background-color: rgb(106, 106, 106);")
        self.strip_label.setText("")
        self.strip_label.setObjectName("strip_label")
        self.logo = QtWidgets.QLabel(parent=self.centralwidget)
        self.logo.setGeometry(QtCore.QRect(150, 10, 691, 241))
        self.logo.setStyleSheet("image: url(static/logo.png);")
        self.logo.setText("")
        self.logo.setObjectName("logo")
        self.main_button = QtWidgets.QPushButton(parent=self.centralwidget)
        self.main_button.setGeometry(QtCore.QRect(450, 320, 121, 111))
        self.main_button.setStyleSheet("border: none;\n"
                                       "image: url(static/upload_button.png);\n"
                                       "")
        self.main_button.setText("")
        self.main_button.setObjectName("main_button")

        self.uploaded_files = QtWidgets.QLabel(parent=self.centralwidget)
        self.uploaded_files.setGeometry(QtCore.QRect(20, 550, 961, 81))
        self.uploaded_files.setStyleSheet("background-color: none;\n"
                                          "color: rgb(0, 0, 0);")
        self.uploaded_files.setObjectName("uploaded_files")
        self.file_type_error_label = QtWidgets.QLabel(parent=self.centralwidget)
        self.file_type_error_label.setGeometry(QtCore.QRect(400, 420, 351, 20))
        self.file_type_error_label.setStyleSheet("color: rgb(155, 34, 18);")
        self.file_type_error_label.setObjectName("file_type_error_label")
        self.change_file = QtWidgets.QPushButton(parent=self.centralwidget)
        self.change_file.setGeometry(QtCore.QRect(420, 540, 161, 61))
        self.change_file.setStyleSheet("border: none;\n")
        self.change_file.setText("")
        self.change_file.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.main_button.clicked.connect(self.MainBttnClicked)
        self.change_file.clicked.connect(self.ChangeBttnClicked)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Хакатон ML ГУАП | Распознавание"))


    def MainBttnClicked(self):
        if not self.button_uploaded:
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл", "",
                                                                "All Files (*)")
            _translate = QtCore.QCoreApplication.translate
            if filename.endswith('.las'):
                self.uploaded_files.setText(
                    _translate("MainWindow", f"Файл {filename.split('/')[-1]} был успешно загружен"))
                self.file_type_error_label.setText(_translate("MainWindow", ""))
                self.main_button.setStyleSheet("border: none;\n"
                                               "image: url(static/recognize_button.png);\n"
                                               "")
                self.change_file.setStyleSheet("border: none;\n"
                                               "image: url(static/change_file.png);")
                self.button_uploaded = True
                self.filename = filename

            else:
                self.file_type_error_label.setText(_translate("MainWindow", "Поддерживаются только файлы .las"))
                self.uploaded_files.setText(_translate("MainWindow", ""))
                self.change_file.setStyleSheet("border: none;\n")

        else:
            print(1)
            self.recognize = Recognize_Window(mw_cls=self)
            self.recognize.show()

    def ChangeBttnClicked(self):
        if self.button_uploaded:
            filename, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Выберите файл", "",
                                                                "All Files (*)")
            _translate = QtCore.QCoreApplication.translate
            if filename.endswith('.las'):
                self.uploaded_files.setText(
                    _translate("MainWindow", f"Файл {filename.split('/')[-1]} был успешно загружен"))
                self.file_type_error_label.setText(_translate("MainWindow", ""))
                self.main_button.setStyleSheet("border: none;\n"
                                               "image: url(static/recognize_button.png);\n"
                                               "")
                self.change_file.setStyleSheet("border: none;\n"
                                               "image: url(static/change_file.png);")

                self.filename = filename

            else:
                self.file_type_error_label.setText(_translate("MainWindow", "Поддерживаются только файлы .las"))



    def reset(self):
        _translate = QtCore.QCoreApplication.translate
        self.main_button.setStyleSheet("border: none;\n"
                                       "image: url(static/upload_button.png);\n"
                                       "")
        self.change_file.setStyleSheet("border: none;\n")
        self.button_uploaded = False
        self.uploaded_files.setText(
            _translate("MainWindow", f""))
        self.file_type_error_label.setText(_translate("MainWindow", ""))
