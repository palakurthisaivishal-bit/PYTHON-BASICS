# creating a set:
# s1 = {1,2,3}
# s2 = {10,12.5,"hello",True}
# empty set:
# s3 = {} #prints as dict
# s31 = set() # prints as set
# print(type(s31))
 
 #accesing elements:
# A = {"rajini","nagarjuna","uppendra"}
# for role in A:
#     print(role)

# #adding elements:
# s = {12,4,5,44}
# s.add(25) # to add a single value only
# # s.update([34,29]) #{34, 4, 5, 12, 44, 25, 29} # to add multiple values
# # print(s)

# #deleting the elements in set:
# #remove:
# s.remove(25) #removes a element and prints a error if we enetered the value which is not present in the set
# print(s)
# # discard:
# s.discard(26) # removes a element and do not prints a error if we enetered the value which is not present in the set
# print(s)
# #pop:
# s.pop()
# print (s) #removes the random element from a set 

#mathematical operations:
#union:     "U = |"
# A = {1,2,3}     #(or)  #  can also be used as:
# B = {4,5,6}              
# print(A | B)             #  print(A.union(B))
# #intersection:  "n = &"
# A = {1,2,3,4}             #can also be used as:
# B = {4,5,6}
# print(A & B)               #  print(A.intersection(B))
# #difference:    "- = -"
# A = {1,2,3,4}             #  can also be used as:
# B = {4,5,6}
# print(A - B)                #  print(A.difference(B))
# #symmetric difference: "delta = ^"
# A = {1,2,3,4,5}                      #  can also be used as:
# B = {4,5,6,7}
# print(A ^ B)                      #  print(A.symmetric difference(B))

# #len():
# s = {1,2,3,4,5,6,7,8,0}
# print(len(s))
# #max():
# s = {1,2,3,4,5,6,7,8}
# print(max(s))
# #min():
# s = {1,2,3,4,5,6,7,8}
# print(min(s))
# #sum():
# s = {1,2,3,4,5,6,7,8}
# print(sum(s))

