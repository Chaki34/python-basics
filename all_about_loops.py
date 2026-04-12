"""
===========================================
 PYTHON LOOPS + DATA STRUCTURES DEMO
===========================================
"""

# ===========================================
# 1. FOR LOOP (Basic)
# ===========================================
print("FOR LOOP (Basic):")
for i in range(5):   # loop from 0 to 4
    print("Value:", i)


# ===========================================
# 2. WHILE LOOP
# ===========================================
print("\nWHILE LOOP:")
j = 0
while j < 5:
    print("Value:", j)
    j += 1   # increment


# ===========================================
# 3. LOOP CONTROL STATEMENTS
# ===========================================
print("\nBREAK, CONTINUE, PASS:")

# BREAK → stops loop completely
for i in range(5):
    if i == 3:
        break
    print("Break Example:", i)

# CONTINUE → skip current iteration
for i in range(5):
    if i == 2:
        continue
    print("Continue Example:", i)

# PASS → does nothing (placeholder)
for i in range(3):
    pass   # used when loop required syntactically but no logic


# ===========================================
# 4. LIST (Like Array in Java)
# ===========================================
print("\nLIST:")

my_list = [10, 20, 30, 40]

# Loop through list
for item in my_list:
    print("Item:", item)

# Using index
for i in range(len(my_list)):
    print("Index:", i, "Value:", my_list[i])

# List comprehension (short loop)
squares = [x*x for x in my_list]
print("Squares:", squares)


# ===========================================
# 5. SET (Unique values, unordered)
# ===========================================
print("\nSET:")

my_set = {1, 2, 3, 4, 4, 2}  # duplicates removed automatically

for item in my_set:
    print("Set Item:", item)

# Add and remove using loop
for i in range(5, 8):
    my_set.add(i)

print("Updated Set:", my_set)


# ===========================================
# 6. DICTIONARY (Like Map in Java)
# ===========================================
print("\nDICTIONARY:")

my_dict = {
    "name": "Debmalya",
    "age": 21,
    "course": "B.Tech"
}

# Loop through keys
for key in my_dict:
    print("Key:", key, "Value:", my_dict[key])

# Loop through values
for value in my_dict.values():
    print("Value:", value)

# Loop through key-value pairs
for key, value in my_dict.items():
    print(key, "=>", value)


# ===========================================
# 7. TUPLE (Immutable list)
# ===========================================
print("\nTUPLE:")

my_tuple = (100, 200, 300)

# Loop through tuple
for item in my_tuple:
    print("Tuple Item:", item)

# Access using index
for i in range(len(my_tuple)):
    print("Index:", i, "Value:", my_tuple[i])


# ===========================================
# 8. NESTED LOOPS
# ===========================================
print("\nNESTED LOOP:")

for i in range(3):
    for j in range(2):
        print(f"i={i}, j={j}")


# ===========================================
# 9. ENUMERATE (Index + Value together)
# ===========================================
print("\nENUMERATE:")

for index, value in enumerate(my_list):
    print("Index:", index, "Value:", value)


# ===========================================
# 10. ZIP (Multiple lists together)
# ===========================================
print("\nZIP:")

names = ["A", "B", "C"]
marks = [90, 85, 88]

for name, mark in zip(names, marks):
    print(name, "scored", mark)


# ===========================================
# 11. COMPREHENSIONS (Advanced Loop Usage)
# ===========================================

# List comprehension
even_numbers = [x for x in range(10) if x % 2 == 0]
print("\nEven Numbers:", even_numbers)

# Set comprehension
set_comp = {x*x for x in range(5)}
print("Set Comprehension:", set_comp)

# Dictionary comprehension
dict_comp = {x: x*x for x in range(5)}
print("Dict Comprehension:", dict_comp)


# ===========================================
# 12. ITERATING STRING (Bonus)
# ===========================================
print("\nSTRING LOOP:")

text = "Python"
for char in text:
    print(char)


# ===========================================
# END
# ===========================================
print("\nAll loops and data structures covered successfully!")