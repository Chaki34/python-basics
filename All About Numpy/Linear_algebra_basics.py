import numpy as np

# -----------------------------
# Example Matrix
# -----------------------------
a = np.array([[1, 2],
              [3, 4]])

# -----------------------------
# 1️ Matrix Multiplication (np.dot)
# -----------------------------
# Rule: row × column

# Internally:
# [[1 2]      [[1 2]
#  [3 4]]  ×   [3 4]]

# = [
#   (1*1 + 2*3)   (1*2 + 2*4)
#   (3*1 + 4*3)   (3*2 + 4*4)
# ]

# = [[7, 10],
#    [15, 22]]

dot_result = np.dot(a, a)
print("Dot Product:\n", dot_result)


# -----------------------------
# 2️ Matrix Inverse (np.linalg.inv)
# -----------------------------
# Gives matrix that "undoes" original matrix

inv_a = np.linalg.inv(a)

# Check:
# a × inv_a = Identity matrix
identity = np.dot(a, inv_a)

print("Inverse:\n", inv_a)
print("Check Identity:\n", identity)


# -----------------------------
# 3️ Determinant (np.linalg.det)
# -----------------------------
# Formula (2x2):
# |a b|
# |c d| → ad - bc

# For matrix:
# (1*4 - 2*3) = 4 - 6 = -2

det_a = np.linalg.det(a)
print("Determinant:", det_a)


# -----------------------------
# 4️ Transpose (VERY COMMON)
# -----------------------------
# Rows ↔ Columns

# [[1 2]
#  [3 4]]
# → [[1 3]
#    [2 4]]

transpose = a.T
print("Transpose:\n", transpose)


# -----------------------------
# 5 Eigenvalues (Advanced ML)
# -----------------------------
# Used in PCA, dimensionality reduction

eigenvalues, eigenvectors = np.linalg.eig(a)

print("Eigenvalues:", eigenvalues)
print("Eigenvectors:\n", eigenvectors)


# -----------------------------
#  ML USE CASES
# -----------------------------

# 1️ Neural Network Calculation
X = np.array([[1, 2]])     # input
W = np.array([[3], [4]])   # weights

# Matrix multiplication:
# (1*3 + 2*4) = 11
output = np.dot(X, W)

print("NN Output:", output)


# 2️ Linear Regression (simplified)
# y = Xw

X = np.array([[1, 1],
              [1, 2],
              [1, 3]])

w = np.array([[1],
              [2]])

y = np.dot(X, w)

print("Predictions:\n", y)


# -----------------------------
#  SIMPLE IDEA
# -----------------------------
# Matrix = data
# Dot product = combine data
# Inverse = undo
# Determinant = check validity