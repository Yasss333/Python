array=[5,4,3,2,1,0]
list=[1,2,3]
# print(list.sort(reverse=True))
# print(list)
# print(array[-3:0])

array.sort()

# print(array)

array.append(6)

array.insert(1,0.5)
# print(array)

array.remove(0.5)
list.pop(2)
# print(array)

# //tuple


tup=(1,2,3,2)

# tup.pop()
# print(tup)

movies=[]

# movie1=input("Enter movie one name")
# movies.append(movie1)
# movie2=input("Enter movie 2 name")
# movies.append(movie2)
# movie3=input("Enter movie 3 name")
# movies.append(movie3)

# print(movies)

# Palindrome

array1=[1,2,1]

array2=array1.copy()

if(array1==array2):
    print("Palindrrome")
else:
    print("Not a Palindrome")
      

# COunt tuple

grade=["A","B","A","C","D","A"];

grade.sort()

result1=grade.count("A")

print(result1,"\n","\t")
print("\t",grade)