import os
os.remove("file.txt")
# print(os.getcwd())
# f = open(
#     # r"C:\dev\projects\YT\Python_apna_college\03-Py\fileinput\file.txt",
#     "file.txt",
#     "r"
# )
# data = f.read()
# print(data)


f =open("file.txt",'r+')
f.write("okook     okok   ")
print(f.read())
f.close()
