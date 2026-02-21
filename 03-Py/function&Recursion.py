def sum(a,b):
    return a+b

# print(sum(2,3))
# list=[1,2,3,4,5]
# def lenghtofList(list=[2,3]):
#     for el in list:
#         print(el,'\n')
#         el+=1
      

# lenghtofList()

# n=int(input("ENter number ")
# el=n
# sum=1

# def Factorial(n=3):
#     while n-el!=0:
#         sum=sum*(n-el)
#         el=el-1
#     print(sum)

# currenty converter

# inr=int(input("Enter INR ruppe"))

# def inrToDollarCOnverter(inr=1):
#     print("Amount $",inr*90)

# inrToDollarCOnverter(inr)

# Recursion

# n=int(input("Enter number"))

# def recursion(n):
#     if(n==0):
#         return
#     print(n)
#     recursion(n-1)

# recursion(n)    



# Factorial recursion
# n=int(input("Enter number"))

def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)
    
# print(factorial(n))

# First n natural numbers using recursion 

# n=int(input("Enter number"))
# n=int(input("Enter number"))

# def sumnatural(n):
#     if(n==1 ):
#         return 1
#     elif(n==0):
#         return 0
#     else:
#         return n+sumnatural(n-1)
    

# print(sumnatural(n))



# recusriosn ot read number form lsit 
list=[1,2,3,4,5]

index=0
def printing(list,index):
    if(len(list)==0):
        return "No element "
    else:
        print(list[index])
        index+=1
        print(list, index)

printing(list,index)