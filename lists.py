# #  #list of numeric values:-
# x = [10,20,30,40,50]
# print(x)
# fruits = ["apple","banana","mango"]
# print(fruits[0:3])
# list4 = [10,20.5,"hello",True,"False"]
# print(list4)
# #index - In python, every element in a list is stored with a positive numbers called as index.
# #Example:-0,1,2,3,4,5,6,......,n-1
# list1 = [10,20,30,40,50]
# print(list1[0])
# print(list1[1])
# print(list1[2])
# print(list1[3])
# print(list1[4])
# #By negative values:-
# print(list1[-1])
# print(list1[-2])
# print(list1[-3])
# print(list1[-4])
# print(list1[-5])

# #Slicing in lists
# # Slicing is taking out of a part from the main list.
# # Slicing will extracts the part or sublist using [start idx : end idx]
# #example:-
# s1c1 = ["Prabhas","Balayya","Pspk","BOB","Bhai"]
# print(s1c1[:3])
# print(s1c1[1:4])
# #Slicing in lists
# # Slicing is taking out of a part from the main list.
# # Slicing will extracts the part or sublist using [start idx : end idx]
# #example:-
# s1c1 = ["Prabhas","Balayya","Pspk","BOB","Bhai"]
# print(s1c1[:3])
# print(s1c1[1:4])
# #Slicing in lists
# # Slicing is taking out of a part from the main list.
# # Slicing will extracts the part or sublist using [start idx : end idx]
# #example:-
# s1c1 = ["Prabhas","Balayya","Pspk","BOB","Bhai"]
# print(s1c1[:3])
# print(s1c1[1:4])
# print(s1c1[-3:])
# #Adding elements in list:-
# # We can add new values to a list in different ways:-
# # 1. Append : Adds a single value at the end of the list.
# kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
# kalkicast.append("Deesha patani")
# print(kalkicast)
# # 2. Insert : Adds a single value at particular place of the list.
# kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
# kalkicast.insert(5, "Deesha patani")
# print(kalkicast)
# # 3. Extending : Adds multiple values at once by combining the lists.
# kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
# kalkicast.extend(["Anudeep","Mrunal T","Bujji"])
# print(kalkicast)
# # example: Add bhramanandham, after the deepika p
# kalkicast = ["Prabhas","Kamal hasan","Amitha Bhachan","Deepika p","SSR"]
# kalkicast.insert(4, "Bhramanandham")
# print(kalkicast)
# #Removing Elements in list:-
# # Removes the items in the list in different ways.
# # 1. remove(): Removes or delefruits = ["apple","banana",tes the first occurrence of the specific items.
# fruits = ["apple","banana","mango"]
# fruits.remove("apple")
# print(fruits)
# # 2. pop(): Deletes the items from list at the particular position.
# fruits = ["apple","banana","mango"]
# fruits.pop(2)
# print(fruits)
# # 3. clear(): Deletes the all items from the list.
# #Removing Elements in list:-
# # Removes the items in the list in different ways.
# # 1. remove(): Removes or deletes the first occurrence of the specific items.
# fruits = ["apple","banana","mango"]
# fruits.remove("apple")
# print(fruits)
# # 2. pop(): Deletes the items from list at the particular position.
# fruits = ["apple","banana","mango"]
# fruits.pop(2)
# print(fruits)
# # 3. clear(): Deletes the all items from the list.
# fruits = ["apple","banana","mango"]
# fruits.clear()
# print(fruits)

# # Changing The Elements:-
# # Lists are mutable, we can change the values after creating the lists using index.
# fruits = ["apple","banana","mango"]
# fruits[1] = "watermelon"
# print(fruits)
# # This changing is mainly used for replace a data in the list.
# # i.e; replace the "watermelon" with "banana".

# # Mathematical Operations in Lists:- 
# # 1. Concatenation: Joins the two lists together in one list.
# a = [1,2]
# b = [3,4]
# c = a+b
# print(c)
# # 2. Repetition: Repeats the elements of a list multiple times.
# a = [1,2]
# n = int(input("Enter the n value:"))
# b = a*n
# print(b) 

# # Searching and Checking an Element in the list:-
# # We can check if an elements or values exists in a list or not.
# # In Operator:-
# # It is a membership operator, which returns the true values if the elements exists in the lists.
# fruits = ["apple","banana","mango"]
# print("banana" in fruits)
# print("grapes" in fruits)

# # Not in operator:-
# # It is a membership Operator,which returns the true values if the elements is not exist in the list.
# fruits = ["apple","banana","mango"]     
# print("banana" not in fruits)
# print("grapes" not in fruits)

# # Index():- Which gives the position of the first occurence of an element or value.
# fruits = ["apple","banana","mango"]
# print(fruits.index("banana")) 

# # Count():- Which gives the number of elements in the lists.
# fruits = ["apple","banana","mango","apple","banana"]            
# print(fruits.count("apple"))    
# #example: count how many times "banana" is repeated in the list.
# # (or)
# a = [2,4,6,8,8,8,10,12,14]
# cnt = 0
# print(a.count(8))
# for i in range(10):
#     if i == 8:
#         cnt = cnt + 1
# print(cnt)        

# # Sorting:- sort()
# # It arranges elements either in ascending order (or) descending order.
# #reversing the list:-
# # reverse() method :- it arranges the list in descending order.     
# fruits = ["apple","orange","mango","banana"]
# fruits.sort()  #ascending order   
# print(fruits)
# fruits.reverse()  #descending order
# print(fruits)
# #example: sort the list in descending order.
# numbers = [5,3,8,6,7,2]
# numbers.sort(reverse=True)
# print(numbers)

# # Copying the list:- it copies the list to another list.
# fruits = ["apple","banana","mango"]
# newlist = fruits.copy()
# print(newlist)

# # Built-in Functions with loops:-
# # Python Programming provides many ready-made functions to work with the items.
# #1. len():- it returns the length of the list.
# fruits = ["apple","banana","mango"]
# print(len(fruits))
# #example: find the length of the list.
# #2. min():- it returns the minimum value from the list.
# numbers = [5,6,4,8,9,2,33,3,7]
# print(min(numbers))
# #3. max():- it returns the maximum value from the list.
# numbers = [5,6,4,8,9,2,33,3,7]
# print(max(numbers))
# #example: find the maximum value from the list.
# #4. sum():- it returns the sum of all values in the list.   
# numbers = [5,6,4,8,9,2,33,3,7]
# print(sum(numbers))
# #example: find the sum of all values in the list.

# #split:-
# #The split() method splits a string into a list.    
# a = "hello world to the python programming"
# b = a.split()
# print(b)

# # Multiple values using input data to the list :-
# a = input("enter the multiple values:").split() # 10 20 30 40 50
# print(a) # ['10','20','30','40','50'] # String values

# # Traversing a list:-
# #1. using for loop:-
# fruits = ["apple","banana","mango"]
# for x in fruits:
#     print(x)
# #example: print all the values in the list using for loop.
# #2. using while loop:-
# fruits = ["apple","banana","mango"]
# i = 0
# while i < len(fruits):
#     print(fruits[i])
#     i = i + 1
# #example: print all the values in the list using while loop.
# #3. using list comprehension:-
# fruits = ["apple","banana","mango"] 
# [print(x) for x in fruits]
# #example: print all the values in the list using list comprehension.

# # Adding elements using a for loop:-
# numbers = [1,2,3,4,5]
# sum = 0
# for x in numbers:
#     sum = sum + x
# print(sum)
# #example: find the sum of all values in the list using for loop.

# # Adding elements using while loop:-
# numbers = [1,2,3,4,5]
# sum = 0
# i = 0
# while i < len(numbers):
#     sum = sum + numbers[i]
#     i = i + 1
# print(sum)
# #example: find the sum of all values in the list using while loop.

# #adding elements using list comprehension:-
# numbers = [1,2,3,4,5]
# sum = (x for x in numbers)
# print(sum)
# #example: find the sum of all values in the list using list comprehension.

# #finding the related ones:-
# lis1 = ["sai","vishal","ram","kishore","rohith"]
# lis2 = []
# for x in lis1 :
#  if "a" in x:
#   lis2.append(x)
# print(lis2)  

# # Give the input values to the lists from 0 to 10:-
# num = []
# for i in range(11):
#     num.append(i)
# print(num)
# #example: create a list of even numbers from 0 to 20.
# even = []
# for i in range(21):
#     if i % 2 == 0:
#         even.append(i)
# print(even)
# #example: create a list of odd numbers from 0 to 20.
# odd = []
# for i in range(21):
#     if i % 2 != 0:
#         odd.append(i)
# print(odd)
# #example: create a list of squares of numbers from 0 to 10.
# squares = []
# for i in range(11):
#     squares.append(i**2)
# print(squares)
# #example: create a list of cubes of numbers from 0 to 10.
# cubes = []
# for i in range(11):
#     cubes.append(i**3)
# print(cubes)
# #example: create a list of factorials of numbers from 0 to 10.
# factorials = []
# fact = 1
# for i in range(11):
#     if i == 0:
#         factorials.append(1)
#     else:
#         fact = fact * i
#         factorials.append(fact)

# #sum of list items:
# list1 = [10,20,30,40,50]
# sum = 0       
# for i in list1:
#  sum = sum + i     
# print(sum) #150 

# #convert["p","y","t","h","o","n"] to python:
# list1 = ["y","t","h","o","n"]
# sum = "p"      
# for i in list1:
#  sum = sum + i     
# print(sum) 

# #find the max and min number from list without using max() and min():-
# list1 = [33,3,6,2,546,5,1,6,4,5,34,]
# max_num = list1[0]
# min_num = list1[0]

# for num in list1:
#     if num > max_num:
#         max_num = num
#     if num < min_num:
#         min_num = num

# print("Maximum number:", max_num)
# print("Minimum number:", min_num)

#                   #     (or)  
                    
# list1 = [33,3,6,2,546,5,1,6,4,5,34]               
# list1.sort()
# print(list1)
# print("max of list is ", list1[10])
# print("min of list is ", list1[0])

# #SEARCHING FOR AN ELEMENT IN A LIST:
# names = ["mlr","kcr","modi"]
# searching_names = input("enter the name found:")
# found = False 
# for i in names:
#    if searching_names == i:
#       found = True  

# if found:
#    print("yes")
# else:
#    print("no")         

# #count even and odd numbers
# numbers = [7,8,4,5,43,8,34,67,56,3,75,78,3,]  

# evn_cnt = 0
# odd_cnt = 0
 
# for i in range(len(numbers)):
#    if numbers[i]%2 == 0:
#       evn_cnt +=1
# else:
#     odd_cnt +=1 
# print ("number of even numbers are:",evn_cnt)
# print ("number of odd numbers are:",odd_cnt)

# #reversing a list without reverse:
# num = [2, 5, 3, 5, 6, 7, 4, 8]
# reversed_num = []
# for i in range(len(num)-1, -1, -1):
#     reversed_num.append(num[i])
# print(reversed_num)

#removing all negative numbers using loop :
# num1 = [-3,-4,5,4,58,34,-54,57]
# num2 = []
# for i in range(len(num1)):
#       if num1[i]>0:
#        num2.append(num1[i])
# print(num2)

#multiply each element in list:
# num1 = [2,45,6,3,6,2,7,]
# for i in range(len(num1)):      
#    num1 [i] *= 2
# print(num1)  
              # or
# num1 = [2,45,6,3,6,2,7,]
# n = int(input("enter a numer to be multiplied: "))
# after_mul = [] 
# for i in num1:
#    after_mul.append(i*n)
# print(after_mul)

#avg of numbers in a list:
# num1 = [5,6,3,7,2,7,3,7]
# sum = 0
# for i in num1:
#     sum = sum + i
# print(sum)
# sum = sum/8
# print(sum)    

#count no.of +,-,xero values in a list:
num1 = [-34,6,8,54,-0,7,0,5,-7,84,0]
num2 = []
num3 = []
num4 = []

positive_cnt = 0
negative_cnt = 0
zero_cnt = 0

num1 = [-34, 6, 8, 54, -0, 7, 0, 5, -7, 84, 0]
num2 = []  
num3 = []  
num4 = []  

positive_cnt = 0
negative_cnt = 0
zero_cnt = 0

for i in range(len(num1)):
    if num1[i] > 0:
        num2.append(num1[i])
        positive_cnt += 1
    elif num1[i] < 0:
        num3.append(num1[i])
        negative_cnt += 1
    else:
        num4.append(num1[i])
        zero_cnt += 1

print("Positive count:", positive_cnt)
print("Negative count:", negative_cnt)
print("Zero count:", zero_cnt)

