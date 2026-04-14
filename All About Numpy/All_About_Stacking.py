import numpy as np   

# Create two 1D arrays (vectors)
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])

# -----------------------------
# WHAT: Vertical stacking
# -----------------------------
# np.vstack stacks arrays "on top of each other"
# Converts 1D arrays into rows (2D) and joins along axis=0 (rows)

# Internally:
# a → [1 2 3]
# b → [4 5 6]

# Becomes:
# [[1 2 3]
#  [4 5 6]]

v = np.vstack([a, b])


# -----------------------------
# WHAT: Horizontal stacking
# -----------------------------
# np.hstack joins arrays side-by-side

# For 1D arrays:
# Just concatenates elements

# Internally:
# [1 2 3] + [4 5 6]
# → [1 2 3 4 5 6]

h = np.hstack([a, b])


# -----------------------------
# OUTPUT
# -----------------------------
print("vstack:\n", v)
print("hstack:\n", h)


# why actually need - 

# 1. Combine data

# Suppose:
# a = feature1 (e.g., age)
# b = feature2 (e.g., salary)

# Combine features into one dataset
X = np.vstack([a, b])   # or hstack depending on shape

#2.  avoid loops 

# using loops - # slow way ❌
result = []
for i in range(len(a)):
    result.append(a[i])


# fast vectorized way 
np.hstack([a, b])