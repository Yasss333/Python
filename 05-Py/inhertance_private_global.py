class Account:
    __name="Yash Mandhare"   # Atribute
    password=1233
    def __init__(self,acc, pswd):
        self.acc=acc
        self.__password=pswd
    def showpassword(self):
        print(self.__password)
    def changepassword(self,newpassword):
        self.__class__.password=newpassword
        print(self.password)

ac1=Account("Yhas",123)
ac1.showpassword()
ac1.changepassword(9999)
ac1.showpassword()

# print("Account NUmber",ac1.acc,"Passwrod",ac1.__password)

        