# Arrays in Python:
# An Array is collection of elements of the same datatype stored in a continuous memory location.
# Arrays are used to store multiple values in a single variable.
# Why Arrays?
# Easy to manage multiple values.
# Allows Faster operations like searching and sorting.
# Useful in mathematica and scientific problems.
# Saves memory.
# Array VS Lists:
#importing the array module:
import array as arr
  

#creating as array:
Numbers = arr.array('i',[1,2,3,4])
print(type(Numbers))
print((Numbers))
# Adding An element in Array:-
# Append():
Numbers.append(7)
print(Numbers)
# insert():
Numbers.insert(2,6)
print(Numbers)

#basic operations of a array:

