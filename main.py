from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtWidgets import QTableWidgetItem
from pymongo import MongoClient
import sys

from SignIn import Ui_SingIn
from Register import Ui_Register
from Card import Ui_Dialog
from AdminPanel import Ui_AdminPanel


class AdminPanelDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.root = None
        self.phone_number = None
        self.ui = Ui_AdminPanel()
        self.ui.setupUi(self)
        self.ui.frame_2.setVisible(False)

        self.ui.find_button.clicked.connect(self.findUser)
        self.ui.save_button.clicked.connect(self.saveRoot)

        self.radio_buttons = {
            self.ui.rset_admin: 'admin',
            self.ui.rset_doctor: 'doctor',
            self.ui.rset_user: 'user'
        }
        for radio_button in self.radio_buttons:
            radio_button.toggled.connect(self.updateRoot)

    def findUser(self):
        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        self.phone_number = self.ui.phone_number_2.text()

        if self.phone_number:
            query = {"phone_number": self.phone_number}
            document = collection.find_one(query)

            if document:
                self.ui.name.setText(document.get('name'))
                self.ui.phone_number_lable.setText(document.get('phone_number'))
                self.ui.e_mail.setText(document.get('e_mail'))
                self.ui.frame_2.setVisible(True)
                self.updateRadioButton(document.get('root'))

    def updateRadioButton(self, root):
        for radio_button in self.radio_buttons:
            check = self.radio_buttons.get(radio_button)
            if check == root:
                radio_button.setChecked(True)

    def updateRoot(self):
        sender = self.sender()
        if sender.isChecked():
            self.root = self.radio_buttons[sender]
            print(self.root)

    def saveRoot(self):
        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        query = {"phone_number": self.phone_number}
        new_root = {"$set": {"root": self.root}}

        collection.update_one(query, new_root)



class SignInDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SingIn()
        self.ui.setupUi(self)
        self.ui.apply_sign_in.clicked.connect(self.applySignIn)
        self.ui.register_button.clicked.connect(self.openRegister)

        enter_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        enter_shortcut.activated.connect(self.ui.apply_sign_in.click)

    def applySignIn(self):

        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        phone_number = self.ui.phone_number.text()
        password = self.ui.password.text()

        if phone_number != '' and password != '':
            query = {"phone_number": phone_number}
            document = collection.find_one(query)
            print(document)
            print(phone_number)
            # self.openCard(phone_number, document.get("root"))
            self.checkRoot(phone_number, document.get('root'))
        else:
            print("Введите все данные")

    def checkRoot(self, phone_number, root):
        if root == "admin":
            self.openAdminPanel()
        else:
            self.openCard(phone_number, root)

    def openCard(self, phone_number, root):
        self.close()
        card_dialog = CardDialog(phone_number, root)
        card_dialog.exec()

    def openAdminPanel(self):
        self.close()
        dialog = AdminPanelDialog()
        dialog.exec()

    def openRegister(self):
        self.close()
        register_dialog = RegisterDialog()
        register_dialog.exec()


class RegisterDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Register()
        self.ui.setupUi(self)
        self.ui.apply_register.clicked.connect(self.applyRegister)
        self.ui.sign_in_button.clicked.connect(self.openSignIn)
        self.ui.phone_number.setInputMask("+38(000)000-00-00")

    def applyRegister(self):

        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        full_name = self.ui.full_name.text()
        phone_number = self.ui.phone_number.text()
        e_mail = self.ui.e_mail.text()
        password = self.ui.password.text()

        if full_name != '' and phone_number != '' and e_mail != '' and password != '':
            new_document = {
                "phone_number": phone_number,
                "password": password,
                "e_mail": e_mail,
                "name": full_name
            }
            collection.insert_one(new_document)
            self.openSignIn()
        else:
            print("Введите все данные")

    def openSignIn(self):
        self.close()
        dialog = SignInDialog()
        dialog.exec()


class CardDialog(QtWidgets.QDialog):
    def __init__(self, phone_number, root):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        if root == "doctor":
            self.ui.frame.setEnabled(True)
            self.ui.addItem.clicked.connect(self.addItemToTable)
        else:
            self.ui.frame.setEnabled(False)
            self.ui.frame.setVisible(False)

        self.phone_number = phone_number
        self.getAllRecord()

    def getAllRecord(self):
        try:
            mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
            db = mongo["application"]
            collection = db["cards"]

            data = collection.find({"phone_number": self.phone_number}).sort("data", -1)
            row_count = collection.count_documents({"phone_number": self.phone_number})

            self.ui.tableWidget.setRowCount(row_count)

            for i, document in enumerate(data):
                print(document)
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(document.get('data')))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(document.get('description')))
        except Exception as e:
            print("Произошла ошибка:", str(e))

    def addItemToTable(self):
        data = self.ui.addData.text()
        description = self.ui.addDescription.text()

        current_row_count = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(current_row_count)

        self.ui.tableWidget.setItem(current_row_count, 0, QTableWidgetItem(data))
        self.ui.tableWidget.setItem(current_row_count, 1, QTableWidgetItem(description))

        # self.ui.addData.clear()
        # self.ui.addDescription.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sign_in_dialog = SignInDialog()
    sign_in_dialog.exec()
    sys.exit(app.exec_())
