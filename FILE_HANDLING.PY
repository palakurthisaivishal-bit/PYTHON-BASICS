# file = open("students.txt","w")
# print(file.close())   # to create a file 
# similarly to read we must type in the created file and use the file "r" to read the file and rb,wb,r+,a..so on

#TYPES OF READ:-
# 1. file read:
# file=open("students.txt","r")
# print(file.read())
# file.close()

# # 2. readline:
# file=open("students.txt","r")
# content=file.readline()
# content1=file.readline()
# content2=file.readline()
# content3=file.readline()
# print(content)
# print(content1)
# print(content2)
# print(content3)
# file.close()

file=open("students.txt","w")
#write,writelines
file.write("hello c++")
file.write("hello c++\n")  # this function is used to write the statements in the created txt file 
file.write("hii") # this fun deletes the older data and prints the new ones whereas append is used to add the new data to older file
lines=["hello uhith\n","hello kumar\n","hiii\n","heyy\n"]
file.writelines(lines)
file.close()            

file=open("students.txt","a")
# write,writelines
file.write("hello c++")
file.write("hello c++\n")
file.write("hii")
lines=["hello uhith\n","hello kumar\n","hiii\n","heyy\n"]
file.writelines(lines)
file.close()