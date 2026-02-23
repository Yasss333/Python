class Student:
    fullname="Yash Mandhare1"  # class attribute
    def __init__(self,fullname):
        self.name=fullname # object attribute>class 

    def greet(self):
        print("hello",self.name)


s1=Student("")


# s1.greet()
# print(s1.fullname)


# class college:
#     def __init__(self,collegeName):
#         self.name=collegeName


# col1=college("VESIT")

# print(col1.name)

class Stud:
    @staticmethod
    def greet():
        print("Hello Student")
    def __init__(self,name, s1, s2, s3):
        self.name=name
        self.subm1=s1
        self.subm2=s1
        self.subm3=s1
    
    def avergae(self):
        print(((self.subm1+self.subm2+self.subm3)/3)*100)


s2=Stud("yash",12,12,12)
s2.greet()
s2.avergae()