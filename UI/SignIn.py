
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_SingIn(object):
    def setupUi(self, SingIn):
        SingIn.setObjectName("SingIn")
        SingIn.resize(500, 600)
        SingIn.setMinimumSize(QtCore.QSize(500, 600))
        SingIn.setMaximumSize(QtCore.QSize(1000, 16777215))
        SingIn.setStyleSheet("background-color:rgb(26,31,37);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(SingIn)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(SingIn)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(self.frame_3)
        self.label_2.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 22px;\n"
"font-family: Times New Roman;\n"
"padding-left: 20px;")
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2, 0, QtCore.Qt.AlignBottom)
        self.register_button = QtWidgets.QPushButton(self.frame_3)
        self.register_button.setMinimumSize(QtCore.QSize(50, 20))
        self.register_button.setMaximumSize(QtCore.QSize(152, 32))
        self.register_button.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"max-width: 150px;\n"
"max-height: 30px;\n"
"color: rgba(255, 255, 255,100);\n"
"border: 1px solid rgba(255, 255, 255,50);")
        self.register_button.setCursor(Qt.PointingHandCursor)
        self.register_button.setObjectName("register_button")
        self.horizontalLayout_2.addWidget(self.register_button, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(SingIn)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.phone_number = QtWidgets.QLineEdit(self.frame_2)
        self.phone_number.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgba(255, 255, 255,200);\n"
"border: 1px solid rgba(255, 255, 255,50);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"width: 150px;\n"
"height: 30px; \n"
"margin:10px;\n"
"padding:7px;")
        self.phone_number.setObjectName("phone_number")
        # self.phone_number.setInputMask("+38(000)000-00-00")
        self.phone_number.setCursorPosition(0)
        self.verticalLayout_3.addWidget(self.phone_number)
        self.password = QtWidgets.QLineEdit(self.frame_2)
        self.password.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgba(255, 255, 255,200);\n"
"border: 1px solid rgba(255, 255, 255,50);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"width: 150px;\n"
"height: 30px; \n"
"margin:10px;\n"
"padding:7px;")
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.password.setCursorMoveStyle(QtCore.Qt.VisualMoveStyle)
        self.password.setObjectName("password")
        self.verticalLayout_3.addWidget(self.password)
        self.verticalLayout.addWidget(self.frame_2)
        self.frame = QtWidgets.QFrame(SingIn)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.apply_sign_in = QtWidgets.QPushButton(self.frame)
        self.apply_sign_in.setStyleSheet("background-color: rgb(230,179,51);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"color:rgb(255,255,255);\n"
"width: 200px;\n"
"height: 40px;")
        self.apply_sign_in.setCursor(Qt.PointingHandCursor)
        self.apply_sign_in.setObjectName("apply_sign_in")
        self.verticalLayout_2.addWidget(self.apply_sign_in, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(SingIn)
        QtCore.QMetaObject.connectSlotsByName(SingIn)

    def retranslateUi(self, SingIn):
        _translate = QtCore.QCoreApplication.translate
        SingIn.setWindowTitle(_translate("SingIn", "Dialog"))
        self.label_2.setText(_translate("SingIn", "Sign in"))
        self.register_button.setText(_translate("SingIn", "Register"))
        self.phone_number.setPlaceholderText(_translate("SingIn", "Phone Number"))
        self.password.setPlaceholderText(_translate("SingIn", "Password"))
        self.apply_sign_in.setText(_translate("SingIn", "Sign In"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    SingIn = QtWidgets.QDialog()
    ui = Ui_SingIn()
    ui.setupUi(SingIn)
    SingIn.show()
    sys.exit(app.exec_())
