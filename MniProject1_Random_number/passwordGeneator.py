import random
import string

# random.choices()

# value=ord("A")
# value2=float(23)

# print(value)
# print(type(value2))


pass_len=12
availablevalues=string.ascii_letters+string.punctuation+string.digits

# print("len of sample space = ",availablevalues)

password=''
for i in range(pass_len):
    password+=random.choice(availablevalues)

# print("Password   : ",password)    



name="yas,hm,dh,jare"

# print(type(name))
str1=name.split(",")
print(str1)
# print(type(name))

