# Additon =3
# print(1+3) 
#concatenation = YashMandhare
# print("Yash"+"Mandhare")
#mix
# print([1,2,3]+[4,5,6])


class Complex:
    def __init__(self,real,img):
        self.img=img
        self.real=real

    def showNumber(self):
        print(self.real,"i + ",self.img,"j")

    def add(self,num2):
        newReal=self.real+num2.real
        newImg=self.img+num2.img 
        print(newReal,"i + ",newImg,"j")
        # return Complex(newReal,newImg)   

c1=Complex(2,3)
c1.showNumber()
c2=Complex(3,2)
c2.showNumber()

c1.add(c2)

