from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt, QDate

class Ui_AddRecord(object):
    def setupUi(self, AddRecord):
        AddRecord.setObjectName("AddRecord")
        AddRecord.resize(500, 600)
        AddRecord.setMinimumSize(QtCore.QSize(500, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(AddRecord)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(AddRecord)
        self.frame.setStyleSheet("background-color:rgb(26,31,37)")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.data = QtWidgets.QTextEdit(self.frame)
        self.data.setStyleSheet("border:none;\n"
                                "background-color: rgb(38, 45, 54);\n"
                                "font-family: Times New Roman;\n"
                                "font-size: 16px;\n"
                                "color: #fff;")
        self.data.setObjectName("data")
        current_date = QDate.currentDate()
        self.data.setPlainText(current_date.toString("dd.MM.yyyy"))

        self.data.setMaximumHeight(50)

        self.verticalLayout_2.addWidget(self.data)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setStyleSheet("border:none;\n"
                                    "background-color: rgb(38, 45, 54);\n"
                                    "font-family: Times New Roman;\n"
                                    "font-size: 16px;\n"
                                    "color: #fff;")
        self.textEdit.setReadOnly(True)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit)

        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setObjectName("save_button")
        self.save_button.setStyleSheet("background-color: rgb(230,179,51);\n"
                                       "font-size: 16px;\n"
                                       "font-family: Times New Roman;\n"
                                       "color:rgb(255,255,255);\n"
                                       "width: 200px;\n"
                                       "height: 40px;")
        self.save_button.setCursor(Qt.PointingHandCursor)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout.addWidget(self.save_button, alignment=Qt.AlignBottom)

        self.retranslateUi(AddRecord)
        QtCore.QMetaObject.connectSlotsByName(AddRecord)

    def retranslateUi(self, AddRecord):
        _translate = QtCore.QCoreApplication.translate
        AddRecord.setWindowTitle(_translate("AddRecord", "Dialog"))
        self.save_button.setText(_translate("AddRecord", "Save"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddRecord = QtWidgets.QDialog()
    ui = Ui_AddRecord()
    ui.setupUi(AddRecord)
    AddRecord.show()
    sys.exit(app.exec_())
