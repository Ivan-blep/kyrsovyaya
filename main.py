from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem
from pymongo import MongoClient
import sys

from SignIn import Ui_SingIn
from Register import Ui_Register
from Card import Ui_Dialog


class SignInDialog(QtWidgets.QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_SingIn()
        self.ui.setupUi(self)
        self.ui.apply_sign_in.clicked.connect(self.applySignIn)
        self.ui.register_button.clicked.connect(self.openRegister)

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
            self.openCard(phone_number)
        else:
            print("Введите все данные")

    def openCard(self, phone_number):
        self.close()
        card_dialog = CardDialog(phone_number)
        card_dialog.exec()

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
        sign_in_dialog = SignInDialog()
        sign_in_dialog.exec()


class CardDialog(QtWidgets.QDialog):
    def __init__(self, phone_number):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.phone_number = phone_number
        self.ui.addItem.clicked.connect(self.addItemToTable)
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

        self.ui.addData.clear()
        self.ui.addDescription.clear()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sign_in_dialog = SignInDialog()
    sign_in_dialog.exec()
    sys.exit(app.exec_())
