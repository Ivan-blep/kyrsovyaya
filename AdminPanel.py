# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'admin.ui'
#
# Created by: PyQt5 UI code generator 5.15.10
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AdminPanel(object):
    def setupUi(self, AdminPanel):
        AdminPanel.setObjectName("AdminPanel")
        AdminPanel.resize(500, 600)
        self.verticalLayout = QtWidgets.QVBoxLayout(AdminPanel)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(AdminPanel)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.phone_number_2 = QtWidgets.QLineEdit(self.frame)
        self.phone_number_2.setObjectName("phone_number_2")
        self.verticalLayout_2.addWidget(self.phone_number_2)
        self.find_button = QtWidgets.QPushButton(self.frame)
        self.find_button.setMinimumSize(QtCore.QSize(200, 0))
        self.find_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.find_button.setObjectName("find_button")
        self.verticalLayout_2.addWidget(self.find_button)
        self.verticalLayout.addWidget(self.frame, 0, QtCore.Qt.AlignHCenter)
        self.frame_2 = QtWidgets.QFrame(AdminPanel)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.name = QtWidgets.QLabel(self.frame_4)
        self.name.setObjectName("name")
        self.verticalLayout_5.addWidget(self.name)
        self.phone_number_lable = QtWidgets.QLabel(self.frame_4)
        self.phone_number_lable.setObjectName("phone_number_lable")
        self.verticalLayout_5.addWidget(self.phone_number_lable)
        self.e_mail = QtWidgets.QLabel(self.frame_4)
        self.e_mail.setObjectName("e_mail")
        self.verticalLayout_5.addWidget(self.e_mail)
        self.verticalLayout_3.addWidget(self.frame_4)
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.rset_admin = QtWidgets.QRadioButton(self.frame_3)
        self.rset_admin.setObjectName("rset_admin")
        self.verticalLayout_4.addWidget(self.rset_admin)
        self.rset_doctor = QtWidgets.QRadioButton(self.frame_3)
        self.rset_doctor.setObjectName("rset_doctor")
        self.verticalLayout_4.addWidget(self.rset_doctor)
        self.rset_user = QtWidgets.QRadioButton(self.frame_3)
        self.rset_user.setObjectName("rset_user")
        self.verticalLayout_4.addWidget(self.rset_user)
        self.verticalLayout_3.addWidget(self.frame_3)
        self.frame_5 = QtWidgets.QFrame(self.frame_2)
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.save_button = QtWidgets.QPushButton(self.frame_5)
        self.save_button.setMinimumSize(QtCore.QSize(200, 0))
        self.save_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.save_button.setObjectName("save_button")
        self.verticalLayout_6.addWidget(self.save_button)
        self.verticalLayout_3.addWidget(self.frame_5, 0, QtCore.Qt.AlignHCenter)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(AdminPanel)
        QtCore.QMetaObject.connectSlotsByName(AdminPanel)

    def retranslateUi(self, AdminPanel):
        _translate = QtCore.QCoreApplication.translate
        AdminPanel.setWindowTitle(_translate("AdminPanel", "Dialog"))
        self.find_button.setText(_translate("AdminPanel", "Find"))
        self.name.setText(_translate("AdminPanel", "TextLabel"))
        self.phone_number_lable.setText(_translate("AdminPanel", "TextLabel"))
        self.e_mail.setText(_translate("AdminPanel", "TextLabel"))
        self.rset_admin.setText(_translate("AdminPanel", "admin"))
        self.rset_doctor.setText(_translate("AdminPanel", "doctor"))
        self.rset_user.setText(_translate("AdminPanel", "user"))
        self.save_button.setText(_translate("AdminPanel", "Save"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AdminPanel = QtWidgets.QDialog()
    ui = Ui_AdminPanel()
    ui.setupUi(AdminPanel)
    AdminPanel.show()
    sys.exit(app.exec_())