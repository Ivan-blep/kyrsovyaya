from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem

from SignIn import Ui_SingIn
from Register import Ui_Register
from Card import Ui_Dialog


import hashlib
from pymongo import MongoClient

import sys
app = QtWidgets.QApplication(sys.argv)
SingIn = QtWidgets.QDialog()
ui = Ui_SingIn()
ui.setupUi(SingIn)
SingIn.show()


def applySignIn():
    mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
    db = mongo["application"]
    collection = db["users"]

    phone_number = ui.phone_number.text()
    password = ui.password.text()



    if phone_number != '' and password !='':
        query = {"phone_number": phone_number}
        document = collection.find_one(query)
        print(document)
        Card(phone_number)
    else:
        print("Введите все данные")

    mongo.close()

    SingIn.close()



def Card(phone_number):
    global CardWindow
    CardWindow = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(CardWindow)
    CardWindow.show()

    def getAllRecord():
        try:
            mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
            db = mongo["application"]
            collection = db["cards"]

            data = collection.find({"phone_number": phone_number}).sort("data", -1)
            row_count = collection.count_documents({"phone_number": phone_number})

            ui.tableWidget.setRowCount(row_count)

            for i, document in enumerate(data):
                print(document)
                ui.tableWidget.setItem(i, 0, QTableWidgetItem(document.get('data')))
                ui.tableWidget.setItem(i, 1, QTableWidgetItem(document.get('description')))
        except Exception as e:
            print("Произошла ошибка:", str(e))

    getAllRecord()




def openRegister():
    global RegisterWindow
    RegisterWindow = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(RegisterWindow)
    SingIn.close()
    RegisterWindow.show()

    def applyRegister():

        mongo = MongoClient("mongodb+srv://ivanchiktumko:qwaeszrdxtfcygv@cluster0.dlvy14y.mongodb.net/")
        db = mongo["application"]
        collection = db["users"]

        full_name = ui.full_name.text()
        phone_number = ui.phone_number.text()
        e_mail = ui.e_mail.text()
        password = ui.password.text()

        if full_name != '' and phone_number != '' and e_mail != '' and password !='':
            new_document = {
                "phone_number": phone_number,
                "password": password,
                "e_mail": e_mail,
                "name": full_name
            }
            collection.insert_one(new_document)
        else:
            print("Введите все данные")


        mongo.close()


    def openSignIn():
        RegisterWindow.close()
        SingIn.open()

    ui.apply_register.clicked.connect(applyRegister)
    ui.sign_in_button.clicked.connect(openSignIn)


ui.apply_sign_in.clicked.connect(applySignIn)
ui.register_button.clicked.connect(openRegister)
sys.exit(app.exec_())

