# =====================================================
#  PYTHON OPERATORS FULL PRACTICE PROGRAM
# =====================================================

# Step 1: Display heading
print("===== PYTHON OPERATORS DEMO =====")

# =====================================================
#  1. ARITHMETIC OPERATORS
# =====================================================
print("\n--- Arithmetic Operators ---")

a = 10
b = 3

print("Addition (a + b):", a + b, "Type:", type(a + b))         # int
print("Subtraction (a - b):", a - b, "Type:", type(a - b))     # int
print("Multiplication (a * b):", a * b, "Type:", type(a * b))  # int
print("Division (a / b):", a / b, "Type:", type(a / b))        # float
print("Floor Division (a // b):", a // b, "Type:", type(a // b)) # int
print("Modulus (a % b):", a % b, "Type:", type(a % b))         # int
print("Exponent (a ** b):", a ** b, "Type:", type(a ** b))     # int

# =====================================================
#  2. COMPARISON OPERATORS
# =====================================================
print("\n--- Comparison Operators ---")

print("a > b:", a > b, "Type:", type(a > b))     # bool
print("a < b:", a < b, "Type:", type(a < b))     # bool
print("a == b:", a == b, "Type:", type(a == b))  # bool
print("a != b:", a != b, "Type:", type(a != b))  # bool
print("a >= b:", a >= b, "Type:", type(a >= b))  # bool
print("a <= b:", a <= b, "Type:", type(a <= b))  # bool

# =====================================================
#  3. LOGICAL OPERATORS
# =====================================================
print("\n--- Logical Operators ---")

x = True
y = False

print("x AND y:", x and y, "Type:", type(x and y))  # bool
print("x OR y:", x or y, "Type:", type(x or y))     # bool
print("NOT x:", not x, "Type:", type(not x))        # bool


# =====================================================
#  4. ASSIGNMENT OPERATORS
# =====================================================
print("\n--- Assignment Operators ---")

num = 5
print("Initial value:", num)

num += 3
print("num += 3:", num)

num -= 2
print("num -= 2:", num)

num *= 4
print("num *= 4:", num)

num /= 2
print("num /= 2:", num, "Type:", type(num))  # float

# =====================================================
#  5. BITWISE OPERATORS
# =====================================================
print("\n--- Bitwise Operators ---")

p = 5   # 0101
q = 3   # 0011

print("p & q:", p & q)
print("p | q:", p | q)
print("p ^ q:", p ^ q)
print("~p:", ~p)
print("p << 1:", p << 1)
print("p >> 1:", p >> 1)

# =====================================================
#  6. MEMBERSHIP OPERATORS
# =====================================================
print("\n--- Membership Operators ---")

list_data = [1, 2, 3, 4]

print("2 in list:", 2 in list_data)        # bool
print("5 not in list:", 5 not in list_data) # bool


# =====================================================
#  7. IDENTITY OPERATORS
# =====================================================
print("\n--- Identity Operators ---")

a1 = [1, 2]
b1 = [1, 2]
c1 = a1

print("a1 is b1:", a1 is b1)   # False (different objects)
print("a1 is c1:", a1 is c1)   # True (same object)


# =====================================================
#  8. OPERATOR PRECEDENCE DEMO
# =====================================================
print("\n--- Operator Precedence ---")

result = 10 + 2 * 3
print("10 + 2 * 3 =", result)  # multiplication first

result = (10 + 2) * 3
print("(10 + 2) * 3 =", result)  # brackets first


# =====================================================
#  PRACTICE PROBLEMS
# =====================================================
print("\n===== PRACTICE QUESTIONS =====")

# Q1: Probability threshold check (classification)
prob = 0.7
threshold = 0.5
print("Q1: Is prediction positive?", prob > threshold)

# Q2: Accuracy calculation
correct = 45
total = 50
accuracy = correct / total
print("Q2: Accuracy =", accuracy)

# Q3: Loss comparison (lower is better)
loss1 = 0.25
loss2 = 0.30
print("Q3: Is model1 better?", loss1 < loss2)

# Q4: Feature presence check
features = ["age", "income", "score"]
print("Q4: 'income' used?", "income" in features)

# Q5: Logical decision (AI rule-based system)
is_logged_in = True
has_permission = False
print("Q5: Access granted?", is_logged_in and has_permission)
