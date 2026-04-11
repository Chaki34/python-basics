
#String cration 

# Single quoted string
a = 'harry'  
print(a, type(a))
# Used for simple strings
# Works same as double quotes
# Useful when string contains double quotes

# Double quoted string
b = "harry is an 'SDE' "  
print(b, type(b))
# Same as single quotes
# Useful when string contains single quotes (')

# Triple quoted string
c = '''harry
is a SDE
'''  
print(c, type(c))
# Used for multi-line strings
# Also used for documentation (docstrings)
# Can include both single and double quotes easily

#A string in python can be sliced for getting a part of the strings.

name = "Debmalya"

# Slicing the string

print(name[0])    # D
print(name[1])    # e

new_name = name[0:5]  # Slicing from index 0 to 4
print(new_name)  # Debma


#SLICING WITH SKIP VALUE

# string[start : stop : step]
# start → where slicing begins (included)
# stop → where slicing ends (excluded)
# step → how many characters to skip each time

print(name[0:8:3]) # Dm (every 3rd character from index 0 to 7)

print(name[0:8:2])  # Dmly (every 2nd character from index 0 to 7)


# useful string methods

my_string = "  Hello, World!  "

print(my_string.lower())

print(my_string.upper())

#title() First letter of each word capital
print("this is a title".title())
print(my_string.title())

# First letter only capital

print("this is a sentence".capitalize())

# Removes spaces from both sides

print("  hello  ")
print("  hello  ".strip())
print(my_string.strip())

# Removes spaces from left side

print("  hello  ".lstrip())

# Removes spaces from right side

print("  hello  ".rstrip())

# String is immutable (cannot be changed after creation)
# my_string[0] = 'h'  # This will raise an error
#for every change we need to create a new string

#Replace characters/words

print(my_string.replace("Hello", "Hi"))  # Replaces "Hello" with "Hi" in this case return new String "  Hi, World!  " not change the original string

#Find first position of substring

print(my_string.find("World"))  # Returns index of first occurrence of "World" (7)


#Find last occurrence

print(my_string.rfind("o"))  # Returns index of last occurrence of "o" (8)  

# Same as find but gives error if not found

print(my_string.index("o"))  # Returns index of first occurrence of "World" (7)
print(my_string.lower().index("w"))  # make it case insensitive by converting to lower case first

print("hello".count("l") ) # Counts how many times "l" appears in "hello" (2)

print("hello".startswith("he"))  # Checks if "hello" starts with "he" (True)
print("hello".endswith("l"))  # Checks if "hello" ends with "o" (false)    

# Split string into list of words
print("a b c".split())  # ['a', 'b', 'c']

# Join list of words into a string
print("-".join(["a", "b", "c"]))   # "a-b-c"

# Checks only letters

print("abc".isalpha() )  # True

# Checks only digits

print("123".isdigit())  # True

# Checks if string is alphanumeric (letters and digits)
print("abc123".isalnum())  # True

# Upper → lower, lower → upper

print("HElLo".swapcase())  # hELLO

# find a particular word in a string

print("hello world".find("r"))  # Returns index of first occurrence of "r" (8)

# replace a particular word in a string

print("hello world".replace("world", "there"))  # Replaces "world" with "there" (hello there)
