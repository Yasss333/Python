class Car:

    def __init__(self,type):
        self.type=type
    @staticmethod
    def start():
        print("Car started")
    
    @staticmethod
    def stop():
        print("Car stoped ...")

class BMW(Car):
    name="S-series"
    def __init__(self,name,type):
        self.name=name
        super().__init__(type)

class Factory:
    print("This is a Car factory")

car1=BMW("Verna", "electric")


print(car1.type)
# print(car1.stop())