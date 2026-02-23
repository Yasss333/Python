class Order:
    def __init__(self,item,price):
        self.item=item
        self.price=price
        print("Item : ",self.item,"Price :",self.price)

    # def greaterWho(self,order2):
    #     if(self.price>order2.price):
    #         print("Order 1 is Priority")
    #     else:
    #         print("Order 2 is Priority")
    def __gt__(self,order2):
        if(self.price>order2.price):
            print("Order 1 is Priority")
        else:
            print("Order 2 is Priority")


o1=Order("Milk",100)
o2=Order("Dahi",200)

o1>o2
