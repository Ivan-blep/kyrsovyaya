from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_Record(object):
    def setupUi(self, Record):
        Record.setObjectName("Record")
        Record.resize(500, 600)
        Record.setMinimumSize(QtCore.QSize(500, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(Record)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Record)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.frame.setStyleSheet("background-color:rgb(26,31,37)")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.data = QtWidgets.QTextEdit(self.frame)
        self.data.setStyleSheet("border:none;\n"
                                "background-color: rgb(38, 45, 54);\n"
                                "font-family: Times New Roman;\n"
                                "font-size: 16px;\n"
                                "color: #fff;")
        self.data.setFixedHeight(50)
        self.data.setObjectName("data")
        self.verticalLayout_2.addWidget(self.data)

        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setStyleSheet("border:none;\n"
                                    "background-color: rgb(38, 45, 54);\n"
                                    "font-family: Times New Roman;\n"
                                    "font-size: 16px;\n"
                                    "color: #fff;")
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout_2.addWidget(self.textEdit, 1)

        self.save_button = QtWidgets.QPushButton(self.frame)
        self.save_button.setObjectName("save_button")
        self.save_button.setStyleSheet("background-color: rgb(230,179,51);\n"
                                       "font-size: 16px;\n"
                                       "font-family: Times New Roman;\n"
                                       "color:rgb(255,255,255);\n"
                                       "width: 200px;\n"
                                       "height: 40px;")
        self.save_button.setCursor(Qt.PointingHandCursor)

        self.verticalLayout_2.addWidget(self.save_button, alignment=Qt.AlignBottom)

        self.verticalLayout.addWidget(self.frame)
        self.retranslateUi(Record)
        QtCore.QMetaObject.connectSlotsByName(Record)

    def retranslateUi(self, Record):
        _translate = QtCore.QCoreApplication.translate
        Record.setWindowTitle(_translate("Record", "Dialog"))
        self.save_button.setText(_translate("Record", "Save"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    Record = QtWidgets.QDialog()
    ui = Ui_Record()
    ui.setupUi(Record)
    Record.show()
    sys.exit(app.exec_())
