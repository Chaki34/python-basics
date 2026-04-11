# =====================================================
#  PYTHON LOOPS PRACTICE (LIST + ARRAY + NUMPY)
# =====================================================

import numpy as np
import array   # built-in array module

# Step 1: Display heading
print("===== LOOPS WITH LIST, ARRAY & NUMPY =====")


# =====================================================
#  1. CREATE DATA STRUCTURES
# =====================================================

# Step 2: Create a Python list
numbers_list = [10, 20, 30, 40]

# Step 3: Create array using array module
numbers_array = array.array('i', [1, 2, 3, 4])  # 'i' = integer type

# Step 4: Create NumPy array
numbers_numpy = np.array([5, 6, 7, 8])


# =====================================================
#  2. FOR LOOP (ALL THREE)
# =====================================================

print("\n--- For Loop (List) ---")
for num in numbers_list:
    print(num)

print("\n--- For Loop (Array Module) ---")
for num in numbers_array:
    print(num)

print("\n--- For Loop (NumPy Array) ---")
for num in numbers_numpy:
    print(num)


# =====================================================
#  3. FOR LOOP WITH INDEX
# =====================================================

print("\n--- For Loop with Index (List) ---")
for i in range(len(numbers_list)):
    print(i, numbers_list[i])

print("\n--- For Loop with Index (Array Module) ---")
for i in range(len(numbers_array)):
    print(i, numbers_array[i])

print("\n--- For Loop with Index (NumPy) ---")
for i in range(len(numbers_numpy)):
    print(i, numbers_numpy[i])


# =====================================================
#  4. WHILE LOOP (ALL THREE)
# =====================================================

print("\n--- While Loop (List) ---")
i = 0
while i < len(numbers_list):
    print(numbers_list[i])
    i += 1

print("\n--- While Loop (Array Module) ---")
i = 0
while i < len(numbers_array):
    print(numbers_array[i])
    i += 1

print("\n--- While Loop (NumPy) ---")
i = 0
while i < len(numbers_numpy):
    print(numbers_numpy[i])
    i += 1


# =====================================================
#  5. NESTED LOOP (2D DATA)
# =====================================================

# Step 5: 2D list
matrix_list = [[1, 2], [3, 4]]

# Step 6: 2D NumPy array
matrix_numpy = np.array([[5, 6], [7, 8]])

print("\n--- Nested Loop (List) ---")
for row in matrix_list:
    for val in row:
        print(val, end=" ")
    print()

print("\n--- Nested Loop (NumPy) ---")
for row in matrix_numpy:
    for val in row:
        print(val, end=" ")
    print()


# =====================================================
#  6. BREAK, CONTINUE, PASS
# =====================================================

print("\n--- Break Example (List) ---")
for num in numbers_list:
    if num == 30:
        break
    print(num)

print("\n--- Continue Example (Array Module) ---")
for num in numbers_array:
    if num == 2:
        continue
    print(num)

print("\n--- Pass Example (NumPy) ---")
for num in numbers_numpy:
    if num == 7:
        pass
    print(num)


# =====================================================
#  7. LIST COMPREHENSION
# =====================================================

print("\n--- List Comprehension ---")
squares = [x*x for x in numbers_list]
print("Squares:", squares)


# =====================================================
#  8. AI STYLE COMPUTATION (LOOP)
# =====================================================

print("\n--- AI Style Loop Example ---")

features = np.array([2, 4, 6])
weights = np.array([0.5, 0.2, 0.1])

# Step: Manual dot product using loop
result = 0
for i in range(len(features)):
    result += features[i] * weights[i]

print("Prediction:", result)


# =====================================================
#  END OF PROGRAM
# =====================================================