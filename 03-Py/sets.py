# set is unique and is ummutable , unordered 
set ={1,2,3,4}


# print(type(set))
# print(len(set))
# print(set.pop())
# print(set)

# Empty set 

# emputset=set()

# print(type(emputset))

set1={1,2,3}
set2={4,5,6}

# set3=set1.union(set2)
set3=set1.intersection(set2)

# print(set3)


# Exercise
# 1
meanigs={
    "table":("a piece of furniture","listo fo fact tables"),
    "cat":"Asmal animal"
}

# 2
classromse={1,2,23,3,4,4,5,6,6}

# print("No of classroms required are ",len(classromse))

# 3

set9={9,(9.0,9)}

print(set9)


# 4

names={}

name1=input('Enter 1st name')
names.update({"names1":name1})
name2=input('Enter 2st name')
names.update({"names2":name2})
name3=input('Enter 3st name')
names.update({"names3":name3})


print(names)