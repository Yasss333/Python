class Person:
    name="Yash"
    age=21
    @staticmethod # these are called decroators  decorator

    def greet():
        print("hello !")

    @classmethod
    def changenme(parentcls,name):
        parentcls.name=name

    @property
    def changeAge(self):
        self.age=age

p1=Person()
# p1.changenme("okok")

# p1.greet()
# print(p1.name)

p1.changeAge(23 )

print(p1.age)