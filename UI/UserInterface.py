from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt


class Ui_UserInterface(object):
    def setupUi(self, UserInterface):
        UserInterface.setObjectName("UserInterface")
        UserInterface.resize(1100, 600)
        UserInterface.setMinimumSize(QtCore.QSize(600, 600))
        UserInterface.setMaximumSize(QtCore.QSize(1100, 600))
        self.verticalLayout = QtWidgets.QVBoxLayout(UserInterface)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(UserInterface)
        self.frame.setMaximumSize(QtCore.QSize(16777215, 50))
        self.frame.setStyleSheet("background-color:rgb(38, 45, 54);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setMaximumSize(QtCore.QSize(60, 16777215))
        self.pushButton.setObjectName("Log out")
        self.pushButton.setText("Log out")
        self.pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                      "font-size: 16px;\n"
                                      "font-family: Times New Roman;\n"
                                      "min-width: 150px;\n"
                                      "min-height: 30px;\n"
                                      "color: rgba(255, 255, 255,100);\n"
                                      "border: 1px solid rgba(255, 255, 255,50);")
        self.pushButton.setCursor(Qt.PointingHandCursor)
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.horizontalLayout_2.setAlignment(QtCore.Qt.AlignRight)
        self.verticalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(UserInterface)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame_3 = QtWidgets.QFrame(self.frame_2)
        self.frame_3.setMaximumSize(QtCore.QSize(100, 16777215))
        self.frame_3.setStyleSheet("background-color: rgb(38, 45, 54);")
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_3)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.frame_5 = QtWidgets.QFrame(self.frame_3)
        self.frame_5.setMaximumSize(QtCore.QSize(16777215, 150))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.card_button = QtWidgets.QPushButton(self.frame_5)
        self.card_button.setMinimumSize(QtCore.QSize(50, 50))
        self.card_button.setObjectName("card_button")
        self.card_button.setStyleSheet("background-color: rgb(230,179,51);\n"
                                       "font-size: 16px;\n"
                                       "font-family: Times New Roman;\n"
                                       "color:rgb(255,255,255);\n"
                                       "width: 200px;\n"
                                       "height: 40px;")
        self.card_button.setCursor(Qt.PointingHandCursor)
        self.verticalLayout_3.addWidget(self.card_button)
        self.verticalLayout_2.addWidget(self.frame_5)
        self.horizontalLayout.addWidget(self.frame_3)

        self.frame_4 = QtWidgets.QFrame(self.frame_2)
        self.frame_4.setStyleSheet("background-color: rgb(26,31,37);")
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_5.setObjectName("verticalLayout_5")

        # Добавляем QLabel для имени (name_label)
        self.name_label = QtWidgets.QLabel(self.frame_4)
        self.name_label.setAlignment(QtCore.Qt.AlignCenter)
        self.name_label.setObjectName("name_label")
        self.name_label.setText("Name: ")
        self.name_label.setStyleSheet("font-size: 30px;\n"
                                      "font-family: Times New Roman;\n"
                                      "color: rgb(255, 255, 255);")
        self.verticalLayout_5.addWidget(self.name_label)

        self.frame_6 = QtWidgets.QFrame(self.frame_4)
        self.frame_6.setEnabled(False)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 300))
        self.frame_6.setMaximumSize(QtCore.QSize(600, 300))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.phone_number_by_card = QtWidgets.QLineEdit(self.frame_6)
        self.phone_number_by_card.setObjectName("phone_number_by_card")
        self.phone_number_by_card.setStyleSheet("background-color: rgba(0,0,0,0);\n"
                                                "color: rgba(255, 255, 255,200);\n"
                                                "border: 1px solid rgba(255, 255, 255,50);\n"
                                                "font-size: 16px;\n"
                                                "font-family: Times New Roman;\n"
                                                "width: 200px;\n"
                                                "height: 20px; \n"
                                                "padding:7px;")
        self.verticalLayout_4.addWidget(self.phone_number_by_card)
        self.find_button = QtWidgets.QPushButton(self.frame_6)
        self.find_button.setMinimumSize(QtCore.QSize(200, 0))
        self.find_button.setMaximumSize(QtCore.QSize(200, 16777215))
        self.find_button.setObjectName("find_button")
        self.find_button.setStyleSheet("background-color: rgb(230,179,51);\n"
                                       "font-size: 16px;\n"
                                       "font-family: Times New Roman;\n"
                                       "color:rgb(255,255,255);\n"
                                       "width: 200px;\n"
                                       "height: 40px;\n"
                                       "margin-left: 15px;")
        self.find_button.setCursor(Qt.PointingHandCursor)
        self.verticalLayout_4.addWidget(self.find_button)
        self.verticalLayout_5.addWidget(self.frame_6, 0, QtCore.Qt.AlignHCenter)
        self.horizontalLayout.addWidget(self.frame_4)
        self.verticalLayout.addWidget(self.frame_2)

        self.retranslateUi(UserInterface)
        QtCore.QMetaObject.connectSlotsByName(UserInterface)

    def retranslateUi(self, UserInterface):
        _translate = QtCore.QCoreApplication.translate
        UserInterface.setWindowTitle(_translate("UserInterface", "Dialog"))
        self.pushButton.setText(_translate("UserInterface", "PushButton"))
        self.card_button.setText(_translate("UserInterface", "Card"))
        self.find_button.setText(_translate("UserInterface", "Find"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    UserInterface = QtWidgets.QDialog()
    ui = Ui_UserInterface()
    ui.setupUi(UserInterface)
    UserInterface.show()
    sys.exit(app.exec_())
