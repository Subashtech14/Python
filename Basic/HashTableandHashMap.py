#Hash table or a hashmap is a type of data structure that maps keys to its value pairs.
#Creating Dictionaries
#Using Curly Braces
my_dict={'subash':'001','devil':'002','God':'005'}
print(my_dict)
print(type(my_dict))
#Using dict()
new_dict=dict(Dave='001',Subash='002')
print(new_dict)
#Nested dictionaries
#Nested dictionaries are basically dictionaries that lie within other dictionaries
emp_details={"subash":{"Devil":{"ID":"444","Salery":"Infinity"}}}
print(emp_details)
#add update and removing elements in dictionary or hash table
#accessing using key value
my_dict={'subash':'001','devil':'002','God':'005'}
print(my_dict['subash'])
print(my_dict.keys())
print(my_dict.values())
print(my_dict.get('subash'))
#accessing using for loop
print("For loop for fetching the keys")
for x in my_dict:
    print(x)
print("For loop for fetching the values")
for x in my_dict.values():
    print(x)
print("Get both key and values")
for x,y in my_dict.items():
    print(x," ",y)
#Updating the dictionary
my_dict["subash"]="4444"
my_dict["Devil"]="141414"
print(my_dict)
print(my_dict.pop('Devil'))
print(my_dict)
#it will delete the last item
print(my_dict.popitem())
#using delete
del my_dict['subash']
print(my_dict)