import numpy as np

# -----------------------------
# SYNTAX
# -----------------------------
# Creating a NumPy array (1D array / vector)
a = np.array([1, 2, 3])

# Creating a scalar (single number)
b = 2

# -----------------------------
# OPERATION: a + b
# -----------------------------
# This is called BROADCASTING in NumPy

# Internally:
# NumPy "expands" scalar b to match shape of array a
# So b behaves like: [2, 2, 2]

# Then element-wise addition happens:
# result[i] = a[i] + b
# → [1+2, 2+2, 3+2] = [3, 4, 5]

result = a + b

print("Result:", result)


# -----------------------------
# HOW IT WORKS INTERNALLY
# -----------------------------
# 1. NumPy checks shapes:
#    a.shape = (3,)
#    b is scalar → treated as compatible
#
# 2. Broadcasting rule:
#    scalar → stretched to (3,)
#
# 3. Fast C-level loop:
#    for i:
#        result[i] = a[i] + b



# Example: Adding bias to features

# Suppose 'a' represents feature values
# and 'b' is a bias term in a model

features = np.array([1, 2, 3])   # input features
bias = 2                         # model bias

# In ML (like linear models):
# output = feature + bias
output = features + bias

print("ML Output:", output)



# Linear model: y = x + b (simplified)

x = np.array([10, 20, 30])  # input data
b = 5                       # bias

y = x + b  # broadcasting used here

print("Predictions:", y)


# Q2 : Linear Model with Weight (y = wx + b)

x = np.array([1, 2, 3])  # features
w = 2                    # weight
b = 1                    # bias

# Step 1: Multiply (broadcasting)
# w → [2, 2, 2]
# [1*2, 2*2, 3*2] = [2, 4, 6]

# Step 2: Add bias
# b → [1, 1, 1]
# [2+1, 4+1, 6+1] = [3, 5, 7]
y = w * x + b

print("y = wx + b:", y)


#Q3 : Feature Scaling (Normalization)

x = np.array([10, 20, 30])

mean = 20
std = 10

# Broadcasting:
# mean → [20, 20, 20]
# std → [10, 10, 10]

# Step 1: subtract mean
# [10-20, 20-20, 30-20] = [-10, 0, 10]

# Step 2: divide by std
# [-10/10, 0/10, 10/10] = [-1, 0, 1]
normalized = (x - mean) / std

print("Normalized:", normalized)

# Q4 : Vector + Vector (Feature-wise operation)



a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# No broadcasting needed (same shape)
# Element-wise:
# [1+4, 2+5, 3+6] = [5, 7, 9]
result = a + b

print("Element-wise add:", result)

# Q5 : Dot Product 



x = np.array([1, 2, 3])  # features
w = np.array([4, 5, 6])  # weights

# Dot product:
# (1*4) + (2*5) + (3*6)
# = 4 + 10 + 18 = 32
y = np.dot(x, w)

print("Dot product:", y)


# Matrix Form



# Each row = one data sample
X = np.array([
    [1, 2],
    [3, 4],
    [5, 6]
])

w = np.array([2, 3])  # weights
b = 1                 # bias

# Matrix multiplication:
# X @ w →
# [
#  (1*2 + 2*3),
#  (3*2 + 4*3),
#  (5*2 + 6*3)
# ]
# = [8, 18, 28]

# Then add bias (broadcasting):
# → [9, 19, 29]
y = X @ w + b

print("Predictions:", y)