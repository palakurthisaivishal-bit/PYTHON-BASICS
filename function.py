# Functions:
# A Function is a block of code that performs a specific task.
# It allows us to group instructions together the reuse them whenever we needed.
# Instead of writing the same code again ans again, we just define a function once and call it whenever required.
# Syntax:
def function_name(parameters):
    # function body code
    return value # optional
#function_name()
# example:
def greet():
    print("Hello World1")

# Calling a Function:
# Calling a Function means telling python to run the
#  code inside a function by using it's name followed by paranthese().
# If the function needs input (parameter), we provide values (argument) inside the parantheses.
# when we call a function,python jumps to the function,executes it's code,and then 
#  comes back to continue the program.
def greet(name,branch): # function name 
    print("Hello World1",name,branch) #
greet("Akshay","CSM-AI&ML") # calling a function.

# Passing Parameters and Arguments:
# Parameters: 
# -> A variable declared inside the function defination.
# -> It's acts like an empty container waiting to receive a value.
# Arguments:
# -> The actual value we pass into the function when calling it.
# -> It fills the empty container(Parameter).
# Example:
def greet(name,rollno): # name = parameter
    print("Hello",name,"your rollno is",rollno) #
greet("Akshay","M3")
# same task without function.
name = "Akshay" # here name is input variable(Parameter), and "Akshay" is value to the parameter (Argument).
print("Hello",name)

# Types of functions Arguments :
# A. Positional Arguments:
# When we pass arguments in the same order as the function parameter, they are called positional Arguments.
# here the order(position) is very important.
def greet(name,rollno):# step 2 values stores
    print("Hello",name,"your rollno is",rollno) # step3: execute the line
greet("M3","Akshay") # step1: function calling

# B. Keyword Arguments:
# When we pass values or Arguments by writing the parameters(variable = value), they are called as keywords argument.
def greet(rollno,name):
    print("Hello",name,"your rollno is",rollno)
greet(name="Akshay",rollno="M3")

# Default Arguments:
# When a parameter has default value(aaigning the value in parameter) in the function definition,it becomes a default argument.
def greet(name="Student"):
    print("Hello",name)
greet()
greet(name="Akshay")

# def range(start_value=0, end_value, step_value=1):
#  print(start_value,end_value,step_value)

# D. Variable-Length Arguments:
# Sometimes we don't know how many arguments will be passed to a function.
# Python provides two special ways to handle this:
# 1. *args:(Variable-length Arguments):
# Collects multiple values into a tuple.
# L = 10,20,30,40,50
def sum1(*List1):
    sum2 = 0
    for i in range(len(List1)):
        sum2 = sum2 + List1[i]
    print(sum2) # 150
    print(type(List1)) # <class 'tuple'>
sum1(10,20,30,40,50)

# 2. **kwargs:(Keyword Variable-Length Arguments)
# Collects multiple key=value pair into a dictionary.
def details(**info):
    for key,value in info.items():
        print(key,"=",value)
details(Name="Akshay",Rollno="M3",Branch="CSM")

#scope of the variable:
#local variable = fun which is inside a function
#global variable = fun which is outside a function 

# The scope of a variable means the part of the program where that variable can be accessed or used.
# In python, variables can be local and global, depending on where they are created.
# Local variable:
# A Variable declared inside a function is called a local function.
# It exists only while the function is running.
# It cannot be used outside that function.
# Global function:
# A Variable declared outside all function is called a global variable.
# It can be accessed anywhere in the program(inside or outside functions).
# example1:
x = 10 # Global variable
def var1():
    x = 5 # Local variable
    print("inside var1 function",x) # inside var1 function 5
var1()
def var2():
    print("inside var2 function",x) # inside var2 function 10
var2()    

print("outside function",x) # outside function 10
# Example2:
x = 10 # Global variable
def var1():
    y = 5 # Local variable
    print("inside var1 function",x,y) # inside var1 function 10,5
var1()
def var2():
    print("inside var2 function",x) 
var2()    

print("outside function",x)

# Lambda function:
# normal function
def sqe(a):
    print(a*a) # 25
sqe(5)
# lambda function
squ = lambda a:a*a
print(squ(5)) # 25