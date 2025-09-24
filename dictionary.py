# My_dict = {
#     "key1":"value1",
#     "key1":"value2",
#     "key1":"value3",
#     "key1":"value4",
# }
# print(My_dict)

# A = {"n":"vishal","n1":"sai"}
# print(A)

# My_dict = {
#    10:"value1",
#    132.51:"value2",
#     "vishal":"value3",
#    True:"value4",
# }
# print(My_dict)

#normal dictionary
# Biodata = {
#     "Name":"vishal",
#     "Roll No":"P6",
#     "Branch":"CSE-AIML",
#     "place":"karimnagar"
    
#}

# dictionary using construction:
# Biodata1 =dict(Name="vishal",Roll_No="P6",Branch="CSE-AIML",place="karimnagar")

# empty dictionary:
# e_d = {}

#accessing dictionary: we use key names inside the square brackets (or)get() method
# Biodata ={
#     "Name":"vishal",
#     "Roll No":"P6",
#     "Branch":"CSE-AIML",
#     "place":"karimnagar"
    
# }

#square brackets[]
# print(Biodata["Name"])
# print(Biodata["Roll No"])
# print(Biodata["Branch"])
                #(Or)
#using get() method:
# print(Biodata.get("Name"))
# print(Biodata.get("Roll.No"))
# print(Biodata.get("Branch"))

# Adding and Updating Dictionary:
# Adding: You can insert a new key-value pair into a dictionary.
# Updating: You can update or change the values using exsisted keys in the dictionary.
# BioData = {
#     "Name":"Akshay",
#     "Roll.No":"5M3",
#     "Branch": "CSE-AI&ML",
#     "place":"Siddipet"
# }    
# BioData["age"] = 18  # Adding the new key and values
# print(BioData)
# BioData["place"] = "Hyderabad" # changing or updating the exsisted key's value.
# print(BioData)
BioData = {
     "Name":"Akshay",
     "Roll.No":"5M3",
     "Branch": "CSE-AI&ML",
     "place":"Siddipet",
     "Role":"siddipet_don"
 }
# Removing in Dictionary:
# python gives multiple ways to delete items from a dictionary.
# pop(),popitem(),clear(),del(delete)
#
# print(BioData)
# # pop(): Removes the key value
# BioData .pop("Roll.No")
# print(BioData)
# # popitem(): Remove the last inserted item from the dictionary.
# BioData.popitem()
# print(BioData)
# # del(delete)
# del BioData["Branch"]
# print(BioData)
# #clear():
# BioData .clear()
# print(BioData)

# # Dictionary methods:
# # Methods allow you to access dictionary data easily.
# # Key(),values(), items()
# BioData = {
#     "Name":"Akshay",
#     "Roll.No":"5M3",
#     "Branch": "CSE-AI&ML",
#     "place":"Siddipet",
#     "Role":"siddipet_don"
# }
# # Keys(): It prints only the keys of dictionary.
# print(BioData.keys())
# # Values(): It prints only the values of dictionary.
# print(BioData.values())
# # Items(): It prints only the items of dictionary.
# print(BioData.items())

# # Updating update(): update the multiple values 
# BioData.update({"Role":"Web Developer","Place":"Hyderabad"})
# print(BioData)

# # loops for dictionary:
for i in BioData:
  print(i)

#NESTED TUPLE:
s =(10,(20,30),(40,50)) 
#i = [0    1       2]
#ii= [0   0,1     0,1]
print(s[1][1])

