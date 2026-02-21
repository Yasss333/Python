list=[0,2,3,4]
# i=list[0]
# while i<len(list):
#     if(i%2==0):
#         continue 
#         print("FOund the element",i)
#     else:
#         print("odd")
#         i=i+1


# for i in list:
#     print("Element",i)
#     i+=1
# else:
#     print('End')    


list1=[1,2,3,4,5,6,7,8,9,10]

# for el in list1:
#     if(el==4):
#         print("Elemet found")
#         break
#     else:
#         print("Element",el)

# Range

# for el in range(3,8,2):
    # print(el)

# n=int(input("Tabel number"))
# for el in range(1,10):
    # print(n ," 8 ",el," = ",n*el);

# Pass word

# for el in range(10):
#     if(el!=5):
#         print("okok",el)
#     else:
#         pass    

# wap to fir sn naturak number
# n=int(input("ENter number = "))
# sum=0
# el=0
# while el<n:
#     sum+=el
#     el=el+1
# print("SUm = ",sum)    


# factorial of number 

n=int(input("ENter number = "))
ans=1
for el in range(1,n):
    ans+=n*(n-el)

print("Ans",ans)
