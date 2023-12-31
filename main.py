from PyQt5 import QtWidgets, QtGui, QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QTableWidgetItem, QMessageBox
from bson import ObjectId
from pymongo import MongoClient
import sys

from pymongo.errors import PyMongoError

from UI.SignIn import Ui_SingIn
from UI.Register import Ui_Register
from UI.Card import Ui_Dialog
from UI.AdminPanel import Ui_AdminPanel
from UI.UserInterface import Ui_UserInterface
from UI.Record import Ui_Record
from UI.AddRecord import Ui_AddRecord


class User:
    def __init__(self, phone_number):
        self.phone_number = phone_number


user = None


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
        self.ui.phone_number.setInputMask("+38(000)000-00-00")

        enter_shortcut = QtWidgets.QShortcut(QtGui.QKeySequence(QtCore.Qt.Key_Return), self)
        enter_shortcut.activated.connect(self.ui.apply_sign_in.click)

    def applySignIn(self):
        global user

        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        phone_number = self.ui.phone_number.text()
        password = self.ui.password.text()

        if phone_number != '':
            query = {"phone_number": phone_number}
            document = collection.find_one(query)
            if document:
                if password == document.get('password'):
                    user = User(phone_number)
                    try:
                        self.checkRoot(phone_number, document.get('root'), document.get('name'))
                    except Exception as e:
                        print(str(e))


                else:
                    msg = QMessageBox()
                    msg.setIcon(QMessageBox.Warning)
                    msg.setText("Wrong password")
                    msg.setWindowTitle("Error")
                    msg.exec_()
            else:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("The user with the specified phone number was not found")
                msg.setWindowTitle("Error")
                msg.exec_()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter all details")
            msg.setWindowTitle("Error")
            msg.exec()

    def checkRoot(self, phone_number, root, user_name):
        if root == "admin":
            self.openAdminPanel()
        else:
            self.openUserInterface(phone_number, root, user_name)

    def openUserInterface(self, phone_number, root, user_name):
        self.close()
        card_dialog = UserInterface(phone_number, root, user_name)
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
            existing_user = collection.find_one({"phone_number": phone_number})
            if existing_user:
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("This phone number is already registered.")
                msg.setWindowTitle("Error")
                msg.exec()
            else:
                new_document = {
                    "phone_number": phone_number,
                    "password": password,
                    "e_mail": e_mail,
                    "name": full_name,
                    "root": "user"
                }
                collection.insert_one(new_document)
                self.openSignIn()
        else:
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("Enter all details")
            msg.setWindowTitle("Error")
            msg.exec()

    def openSignIn(self):
        self.close()
        dialog = SignInDialog()
        dialog.exec()


class UserInterface(QtWidgets.QDialog):
    def __init__(self, phone_number, root, user_name):
        super().__init__()
        self.ui = Ui_UserInterface()
        self.ui.setupUi(self)
        self.user_name = user_name
        self.root = root
        self.ui.pushButton.setText("Log out")
        self.ui.frame_6.setVisible(False)
        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        self.collection = db["users"]
        self.ui.pushButton.clicked.connect(self.openSignIn)

        if root == 'doctor':
            self.ui.name_label.setText("Hello doctor " + user_name)
            self.ui.card_button.clicked.connect(self.openFindByUser)
            self.ui.find_button.clicked.connect(self.openCardByFindUser)
        else:
            self.ui.name_label.setText("Hello " + user_name)
            self.ui.card_button.clicked.connect(self.openCardByUser)

    def openSignIn(self):
        self.close()
        sign_in_dialog = SignInDialog()
        sign_in_dialog.exec()

    def openFindByUser(self):
        self.ui.name_label.setVisible(False)
        self.ui.name_label.setEnabled(False)
        self.ui.frame_6.setVisible(True)
        self.ui.frame_6.setEnabled(True)
        self.ui.phone_number_by_card.setInputMask("+38(000)000-00-00")

    def openCardByUser(self):
        try:
            phone_number = user.phone_number

            if phone_number:
                query = {"phone_number": phone_number}
                document = self.collection.find_one(query)

                if document:
                    self.ui.phone_number_by_card.clear()
                    dialog = CardDialog(phone_number, self.root, self.user_name)
                    dialog.exec()
        except Exception as e:
            print(e)

    def openCardByFindUser(self):
        user_phone_number = self.ui.phone_number_by_card.text()

        if user_phone_number:
            query = {"phone_number": user_phone_number}
            document = self.collection.find_one(query)

            if document:
                self.ui.phone_number_by_card.clear()
                if self.root == "doctor":
                    dialog = CardDialog(user_phone_number, self.root, self.user_name)
                else:
                    dialog = CardDialog(user_phone_number, self.root, self.user_name)
                dialog.exec()
            else:
                error_message = "The phone number was not found."
                QMessageBox.warning(self, "Error", error_message)
        else:
            error_message = "Please enter a phone number."
            QMessageBox.warning(self, "Error", error_message)


class AddRecordDialog(QtWidgets.QDialog):
    def __init__(self, card):
        super().__init__()
        self.ui = Ui_AddRecord()
        self.ui.setupUi(self)

        self.card = card
        self.ui.textEdit.setReadOnly(False)
        self.ui.save_button.setText("Add to table")
        self.ui.save_button.clicked.connect(self.addToTable)

    def addToTable(self):
        data = self.ui.data.toPlainText()
        description = self.ui.textEdit.toPlainText()
        try:
            success_message = "Record successfully added."
            QMessageBox.information(self, "Success", success_message)
            self.card.addRecordToTable(data, description)
        except Exception as e:
            print(e)
        self.card.getAllRecord()
        self.close()


class RecordDialog(QtWidgets.QDialog):
    def __init__(self, card, item, root, doctor):

        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        self.collection = db["cards"]

        super().__init__()
        self.ui = Ui_Record()
        self.ui.setupUi(self)

        self.dataOfRow = item["data"]
        self.description = item["description"]
        self._id = item["_id"]
        self.card = card
        self.ui.save_button.clicked.connect(self.changeData)
        if root == "doctor" and doctor == True:
            self.ui.save_button.setVisible(True)
            self.ui.save_button.setEnabled(True)
            self.ui.textEdit.setReadOnly(False)
            self.ui.data.setReadOnly(True)
        else:
            self.ui.save_button.setVisible(False)
            self.ui.save_button.setEnabled(False)
            self.ui.textEdit.setReadOnly(True)
            self.ui.data.setReadOnly(True)

        self.setData()

    def changeData(self):
        try:
            result = self.collection.update_one({
                "_id": ObjectId(self._id)
            },
                {
                    "$set":
                        {
                            "description": self.ui.textEdit.toPlainText(),
                            "status": "modify"
                        }
                })
            if result.modified_count > 0:
                success_message = "Successfully updated."
                QMessageBox.information(self, "Success", success_message)
                self.card.getAllRecord()
                self.close()
            else:
                error_message = "Record not found or not modified."
                QMessageBox.warning(self, "Error", error_message)
        except PyMongoError as e:
            print(e)

    def setData(self):
        self.ui.data.setText(self.dataOfRow)
        self.ui.textEdit.setText(self.description)


class CardDialog(QtWidgets.QDialog):
    def __init__(self, phone_number, root, user_name):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.user_name = user_name
        self.mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        self.db = self.mongo["application"]
        self.collection = self.db["cards"]
        self.root = root
        if root == "doctor":
            self.ui.frame.setEnabled(True)
            self.ui.addItem.clicked.connect(self.openRecord)
        else:
            self.ui.frame.setEnabled(False)
            self.ui.frame.setVisible(False)

        self.phone_number = phone_number
        self.getAllRecord()

        self.ui.tableWidget.cellClicked.connect(self.rowClicked)

    def getAllRecord(self):
        try:
            self.ui.tableWidget.clearContents()
            self.ui.tableWidget.setRowCount(0)

            data = self.collection.find({"phone_number": self.phone_number}).sort("data", 1)
            row_count = self.collection.count_documents({"phone_number": self.phone_number})

            self.ui.tableWidget.setRowCount(row_count)
            for i, document in enumerate(data):
                self.ui.tableWidget.setItem(i, 0, QTableWidgetItem(str(document.get("_id"))))
                self.ui.tableWidget.setItem(i, 1, QTableWidgetItem(document.get('data')))
                self.ui.tableWidget.setItem(i, 2, QTableWidgetItem(document.get('description')))
                self.ui.tableWidget.setItem(i, 3, QTableWidgetItem(document.get('name_doctor')))

        except Exception as e:
            print(str(e))

    def openRecord(self):
        try:
            dialog = AddRecordDialog(self)
            dialog.exec()
        except Exception as e:
            print(e)

    def addRecordToTable(self, data, description):
        current_row_count = self.ui.tableWidget.rowCount()

        self.ui.tableWidget.insertRow(current_row_count)

        self.ui.tableWidget.setItem(current_row_count, 1, QTableWidgetItem(data))
        self.ui.tableWidget.setItem(current_row_count, 2, QTableWidgetItem(description))
        self.ui.tableWidget.setItem(current_row_count, 3, QTableWidgetItem(self.user_name))

        self.addItemToDataBase(data, description, self.user_name)

    def addItemToDataBase(self, data, description, user_name):
        if self.phone_number and data and description:
            new_document = {
                "phone_number": self.phone_number,
                "data": data,
                "description": description,
                "name_doctor": user_name
            }
            self.collection.insert_one(new_document)

    def rowClicked(self, row, col):
        if row >= 0:
            data_item = self.ui.tableWidget.item(row, 1)
            description_item = self.ui.tableWidget.item(row, 2)

            if data_item is not None and description_item is not None:
                data = data_item.text()
                description = description_item.text()
                _id = self.ui.tableWidget.item(row, 0).text()

                item = {"data": data, "description": description, "_id": _id}
                doctor = False
                if self.user_name == self.ui.tableWidget.item(row, 3).text():
                    doctor = True

                dialog = RecordDialog(self, item, self.root, doctor)
                dialog.exec()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    sign_in_dialog = SignInDialog()
    sign_in_dialog.exec()
    sys.exit(app.exec_())
