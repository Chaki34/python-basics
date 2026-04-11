# ============================================
#  Author: Debmalya Chaki
#  Date: 2026-04-11
#  Topic: Variables, Identifiers & Type Casting
# ============================================

# ============================================
#  1. VARIABLES IN PYTHON
# ============================================

# A variable is a container used to store data

# Creating variables
name1 = "Debmalya"       # String
age1 = 21                # Integer
height1 = 5.9            # Float
is_student1 = True       # Boolean

# Printing variables
print("Name:", name1)
print("Age:", age1)
print("Height:", height1)
print("Is Student:", is_student1)

# Checking type of variables
print("\n--- Types of Variables ---")
print("Type of name:", type(name1))
print("Type of age:", type(age1))
print("Type of height:", type(height1))
print("Type of is_student:", type(is_student1))


# ============================================
#  2. IDENTIFIERS IN PYTHON
# ============================================

print("\n----- IDENTIFIERS RULES -----")

# Valid Identifiers
student_name = "Rahul"
_marks = 90
totalMarks123 = 300

print("Valid Identifiers:", student_name, _marks, totalMarks123)

# Invalid Identifiers (Uncomment to test errors)
# 1name = "Error"
# class = "Error"
# my-name = "Error"

# Python Keywords
import keyword
print("\nPython Keywords are:")
print(keyword.kwlist)


# ============================================
#  3. TYPE CASTING IN PYTHON
# ============================================

print("\n----- TYPE CASTING -----")

# Implicit Type Casting
print("\n--- Implicit Casting ---")
a = 10
b = 5.5

c = a + b
print("Result:", c)
print("Type of result:", type(c))


# Explicit Type Casting
print("\n--- Explicit Casting ---")

# String to Integer
x = "100"
y = int(x)
print("String to Int:", y, type(y))

# Integer to Float
a2 = 50
b2 = float(a2)
print("Int to Float:", b2, type(b2))

# Float to Integer
num_float = 9.8
converted = int(num_float)
print("Float to Int:", converted, type(converted))

# Integer to String
num_int = 200
text = str(num_int)
print("Int to String:", text, type(text))


# ============================================
#  4. USER INPUT WITH SAFE HANDLING
# ============================================

print("\n----- USER INPUT -----")

try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    print("Sum is:", num1 + num2)
except ValueError:
    print("Invalid input! Please enter numbers only.")
except KeyboardInterrupt:
    print("\nInput interrupted by user.")


# ============================================
#  5. PRACTICE QUESTIONS
# ============================================

print("\n----- PRACTICE QUESTIONS -----")

# Q1: Create 3 variables and print their types
name2 = "Alice"
age2 = 22
marks2 = 85

print("Q1 Types:", type(name2), type(age2), type(marks2))


# Q2: Convert string "50" into integer and multiply by 2
value = "50"
value_int = int(value)
print("Q2 Result:", value_int * 2)


# Q3: Convert float 7.9 into integer
print("Q3 Result:", int(7.9))


# Q4: Take user input and convert to float (safe)
try:
    user_input = float(input("Enter a decimal number: "))
    print("Q4:", user_input, type(user_input))
except ValueError:
    print("Invalid decimal input!")
except KeyboardInterrupt:
    print("\nInput interrupted by user.")


# ============================================
# 🎯 END OF PROGRAM
# ============================================