class Employee:
    role="QA Engineer"
    department="Quality Assurance"
    salary="25k"

    def showdetails(self):
        print("Role : ",self.role,"\n","Deparment : ",self.department,"\n","Self Salary : ",self.salary,)

class Engineer(Employee):
    name="Yash"
    age=21

    def __init__(self, name, age):
        print("Name :",self.name,"Age : ",self.age)
        # super.__class__()

E1=Engineer("Yahs",32)

E1.showdetails()


