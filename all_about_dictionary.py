
# Dictionary is a collection of keys-value pairs

from psutil import users


mydict = {
    "physics": 98,
    "maths": 95,
    "chemistry": 97
}


# PROPERTIES OF PYTHON DICTIONARIES
# 1. It is unordered.
# 2. It is mutable.
# 3. It is indexed.
# 4. Cannot contain duplicate keys

mydict["english"] = 96 # adding new key-value pair to the dictionary

print(mydict)

myList = list(mydict.keys()) # converting dictionary keys to a list
print(myList)

mylist1 = list(mydict.values()) # returns a view object of the values in the dictionary
print(mylist1)


students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grade": "A"
    },
    "student2": {
        "name": "Bob",
        "age": 22,
        "grade": "B"
    },
    "student3": {
        "name": "Charlie",
        "age": 21,
        "grade": "A-"
    }
}


print(students["student1"]["name"]) # accessing nested dictionary values
print(students["student1"]["age"]) # accessing nested dictionary values
print(students["student2"]["age"]) # accessing nested dictionary values
print(students["student3"]["grade"]) # accessing nested dictionary values

print(students)

results = {

"physics": [98, 95, 97],

"maths": [95, 92, 90],

"chemistry": [97, 94, 96],

"grades" : ('A', 'B', 'A-')

}

print(results)

# List is ordered, mutable, and allows duplicate elements, while a set is unordered, mutable, and does not allow duplicate elements.

# so we midify lists and also insert vallues 

results["physics"].append(99) # adding new value to the list in the dictionary

results["grades"] = results["grades"] + ('B+',) # adding new value to the tuple in the dictionary

results["physics"][1] = 96 # modifying existing value in the list in the dictionary


print("modifed results: ", results)

# change whole list in the dictionary

results["chemistry"] = [100, 100, 100]
print(results["chemistry"])


print("\n\n")
print(results)

# in case of modification of the tuple it throws an error because tuples are immutable

# results["grades"][1] = 'A+' # this will throw an error because tuples are immutable

# if wee need to modify then we can convert the tuple to a list, modify it, and then convert it back to a tuple

grades_list = list(results["grades"])
grades_list[1] = 'A+'
results["grades"] = tuple(grades_list) # change the modified list back to a tuple and assign it to the dictionary key

print(results["grades"])  # this will print the modified grades tuple

# now our tuple is modified inside the results dictionary 

user = {

    "id": 1,
    "id2": 2,
   # "id2": 22, # this will overwrite the previous value of id2 because duplicate keys are not allowed in dictionaries (for test uncomment this line and see the output)
    "id3": 3,
    "id4": 4,
}

# Accessing dictionary values using keys
# Keys in a dictionary are unique, so accessing values is easy and fast.

# Dictionary access is done in constant time complexity O(1)
# because Python dictionaries are implemented using hash tables.

print(user)  

# Note:
# Dictionaries are unordered collections (in older concepts),
# so the output may not appear in the exact same order as defined,
# but all key-value pairs will be printed.



# to get ides corsponding keys like id , id1 , id2....
ids = user.keys() # this will return a view object of the keys in the dictionary
print(ids)

ids = user.values() # this will return a view object of the values in the dictionary
print(ids)

ids = user.items() # this will return a view object of the key-value pairs in the dictionary
print(ids)

user.pop("id2") # this will remove the key-value pair with the key "id2" from the dictionary

print(user)

print("value is  : ",user.get("id3")) # this will return the value of the key "id3" in the dictionary

user.update({"id5": 5}) # this will add a new key-value pair to the dictionary

user.update({"id3": 33}) # this will modify the value of the existing key "id3" in the dictionary

print(user)





