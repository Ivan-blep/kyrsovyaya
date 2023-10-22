# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Register.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(500, 600)
        Register.setMinimumSize(QtCore.QSize(500, 600))
        Register.setMaximumSize(QtCore.QSize(1000, 16777215))
        Register.setStyleSheet("background-color:rgb(26,31,37);\n"
"")
        self.verticalLayout = QtWidgets.QVBoxLayout(Register)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_3 = QtWidgets.QFrame(Register)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame_3)
        self.label.setStyleSheet("color: rgb(255,255,255);\n"
"font-size: 22px;\n"
"font-family: Times New Roman;\n"
"padding-left: 20px;")
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label, 0, QtCore.Qt.AlignBottom)
        self.sign_in_button = QtWidgets.QPushButton(self.frame_3)
        self.sign_in_button.setMinimumSize(QtCore.QSize(50, 20))
        self.sign_in_button.setMaximumSize(QtCore.QSize(152, 32))
        self.sign_in_button.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"max-width: 150px;\n"
"max-height: 30px;\n"
"color: rgba(255, 255, 255,100);\n"
"border: 1px solid rgba(255, 255, 255,50);")
        self.sign_in_button.setObjectName("sign_in_button")
        self.horizontalLayout.addWidget(self.sign_in_button, 0, QtCore.Qt.AlignBottom)
        self.verticalLayout.addWidget(self.frame_3)
        self.frame_2 = QtWidgets.QFrame(Register)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.full_name = QtWidgets.QLineEdit(self.frame_2)
        self.full_name.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgba(255, 255, 255,200);\n"
"border: 1px solid rgba(255, 255, 255,50);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"width: 150px;\n"
"height: 30px; \n"
"margin:10px;\n"
"padding:7px;")
        self.full_name.setObjectName("full_name")
        self.verticalLayout_3.addWidget(self.full_name)
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
        self.verticalLayout_3.addWidget(self.phone_number)
        self.e_mail = QtWidgets.QLineEdit(self.frame_2)
        self.e_mail.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: rgba(255, 255, 255,200);\n"
"border: 1px solid rgba(255, 255, 255,50);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"width: 150px;\n"
"height: 30px; \n"
"margin:10px;\n"
"padding:7px;")
        self.e_mail.setObjectName("e_mail")
        self.verticalLayout_3.addWidget(self.e_mail)
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
        self.frame = QtWidgets.QFrame(Register)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.apply_register = QtWidgets.QPushButton(self.frame)
        self.apply_register.setStyleSheet("background-color: rgb(230,179,51);\n"
"font-size: 16px;\n"
"font-family: Times New Roman;\n"
"color:rgb(255,255,255);\n"
"width: 200px;\n"
"height: 40px;")
        self.apply_register.setObjectName("apply_register")
        self.verticalLayout_2.addWidget(self.apply_register, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame)

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Dialog"))
        self.label.setText(_translate("Register", "Register"))
        self.sign_in_button.setText(_translate("Register", "Sign In"))
        self.full_name.setPlaceholderText(_translate("Register", "Full name"))
        self.phone_number.setPlaceholderText(_translate("Register", "Phone Number"))
        self.e_mail.setPlaceholderText(_translate("Register", "E-mail"))
        self.password.setPlaceholderText(_translate("Register", "Password"))
        self.apply_register.setText(_translate("Register", "Register"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())