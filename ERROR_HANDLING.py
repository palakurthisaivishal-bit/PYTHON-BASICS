# Error Handling:
# -> Errors are mistakes in a program that stop it from working correctly.
# -> Exception is a special type of error that occurs while the program is running.
# -> Python provides ways to handle exceptions so that the program doesn't crash suddenly.
# Types of error:
# 1. Compile-time Error: (Syntax Error)
# Errors that happen when the code is not written correctly(wrong syntax)

# 2. Logical Error:
# Errors when the program runs but gives wrong output because the logic is wrong.

# 3. Runtime Error: (Exceptions)
# Errors happens when the program is running.

# Types of exception in python:
# 1. ZeroDivisionError
# 2. ValueError
# 3. IndexError
# 4. KeyError
# 5. TypeError
# 6. FileNotFoundError

# 1. ZeroDivisionError: it is a exception which divides a number by zero
# try:
#     a = int(input("enter the numerator"))
#     b = int(input("enter the denominator"))
#     c = a//b
#     print(c)
# except ZeroDivisionError:
#     print("this is invalid")   
# #             (Or)
# try:
#     i = 2
#     n = int(input("Enter the n value: "))
#     if i%2 ==0:
#         print("yes, number is multiple of",n)

#     else:
#         print("no,number is not multiple of",n)

# except ZeroDivisionError:
#     print("Error: Division by zero is not possible")

#2 .value error:
try:
    rollno = int(input("Enter your rollNo: "))
except ZeroDivisionError:
    print("Error: Given value is not in the interger datatype. ")
  
# 3. IndexError:
try:
    List = [10,20,30] # 0 1 2
    n = int(input("Enter the index value: "))
    print(List[n])
except IndexError:
    print("Error: the given index is not from the list")

#4.KeyError:
try:
    Dict = {"name":"Akshay","RollNo":"M3"}
    print(Dict["age"])
except KeyError:
    print("Error: the given key is not from the list")

#5 .TypeError:
try:
    List = [10,20,30]
    Sum = List + 5
    print(Sum)
except TypeError:
    print("Invalid type operation.")

#6 .NameError:    
try:
    print(Mult)
except NameError:
    print("Variable not declared")