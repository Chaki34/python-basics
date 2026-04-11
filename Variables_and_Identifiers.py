
# ============================================
#  Author: Debmalya Chaki
#  Date: 2026-04-11
# Topic: Variables, Identifiers & Type Casting
# ============================================

# ============================================
#  1. VARIABLES IN PYTHON
# ============================================

# A variable is a container used to store data

# Creating variables
name = "Debmalya"       # String
age = 21               # Integer
height = 5.9           # Float
is_student = True      # Boolean

# Printing variables
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)

# Checking type of variables
print("\n--- Types of Variables ---")
print(type(name))
print(type(age))
print(type(height))
print(type(is_student))


# ============================================
#  2. IDENTIFIERS IN PYTHON
# ============================================

# Identifiers are names given to variables, functions, etc.

print("\n----- IDENTIFIERS RULES -----")

#  Valid Identifiers
student_name = "Rahul"
_marks = 90
totalMarks123 = 300

print("Valid Identifiers:", student_name, _marks, totalMarks123)

#  Invalid Identifiers (Uncomment to test errors)
# 1name = "Error"      # Cannot start with number
# class = "Error"      # 'class' is a keyword
# my-name = "Error"    # Hyphen not allowed

# Python Keywords (cannot be used as identifiers)
import keyword
print("\nPython Keywords are:")
print(keyword.kwlist)

# ============================================
#  3. TYPE CASTING IN PYTHON
# ============================================

print("\n----- TYPE CASTING -----")

# Type casting means converting one data type to another

#  Implicit Type Casting (automatic)
print("\n--- Implicit Casting ---")
a = 10       # int
b = 5.5      # float

c = a + b    # int + float -> float
print("Result:", c)
print("Type of result:", type(c))


#  Explicit Type Casting (manual)
print("\n--- Explicit Casting ---")

# String to Integer
x = "100"
y = int(x)
print("String to Int:", y, type(y))

# Integer to Float
a = 50
b = float(a)
print("Int to Float:", b, type(b))

# Float to Integer
num = 9.8
converted = int(num)
print("Float to Int:", converted, type(converted))

# Integer to String
num = 200
text = str(num)
print("Int to String:", text, type(text))

# Taking input from user
# By default input is always string

num1 = input("Enter first number: ")
num2 = input("Enter second number: ")

# Convert to integer
num1 = int(num1)
num2 = int(num2)

sum_result = num1 + num2

print("Sum is:", sum_result)


# Q1: Create 3 variables: name, age, marks and print them

name = "alice"
age = 22
marks = 85

print("Printing variables with corsponding Datatypes :",type(name), type(age), type(marks))

