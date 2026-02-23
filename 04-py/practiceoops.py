class Bank:
    def __init__(self,balance, acc):
        self.acc=acc
        self.bal=balance
    
    def debit(self,deb_amt):
        print("debited Amount: ",deb_amt)
        self.bal+=deb_amt
        print("Current Bal : ",self.bal)
    
    def credit(self,cred_amt):
        print("Credit amount : ",cred_amt)
        self.bal-=cred_amt
        print("Remaining balance : ",self.bal)


cust1=Bank(1000,1)

cust1.debit(500)

