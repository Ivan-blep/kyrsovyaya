class User:
    def __init__(self, phone_number, e_mail, name, root):
        self.phone_number = phone_number
        self.e_mail = e_mail
        self.name = name
        self.root = root

    def getPhoneNumber(self):
        return self.phone_number

    def getMail(self):
        return self.e_mail

    def getName(self):
        return self.name

    def getRoot(self):
        return self.root
