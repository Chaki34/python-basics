import numpy as np   # NumPy library (includes random module)

# -----------------------------
# WHAT: Random number generation
# -----------------------------
# NumPy provides pseudo-random numbers (PRNG)
# Used heavily in Machine Learning

# -----------------------------
# 1️ np.random.rand()
# -----------------------------
# Uniform distribution → values between 0 and 1

a = np.random.rand(3)

# Internally:
# Generates float values from Uniform(0,1)
print("Random floats (0 to 1):", a)


# -----------------------------
# 2️ np.random.randint()
# -----------------------------
# Random integers in range [low, high)

b = np.random.randint(1, 10, 5)

# Example: values from 1 to 9
print("Random integers:", b)


# -----------------------------
# 3️ np.random.seed()
# -----------------------------
# Fix randomness → reproducibility

np.random.seed(42)

c = np.random.rand(3)
print("After setting seed:", c)

# Same seed → same output every run


# -----------------------------
# 4️ np.random.randn()
# -----------------------------
# Normal distribution (mean=0, std=1)

d = np.random.randn(3)

# Used in ML for weight initialization
print("Normal distribution:", d)


# -----------------------------
# 5️ np.random.uniform()
# -----------------------------
# Custom range random floats

e = np.random.uniform(5, 10, 3)

# Range: 5 to 10
print("Uniform (5 to 10):", e)


# -----------------------------
# 6️ np.random.choice()
# -----------------------------
# Randomly pick elements from array

data = np.array([10, 20, 30, 40, 50])

choice = np.random.choice(data, 3)

# Picks 3 random values
print("Random choice:", choice)


# -----------------------------
# 7️ np.random.permutation()
# -----------------------------
# Shuffle data (VERY IMPORTANT in ML)

shuffled = np.random.permutation(data)

print("Shuffled data:", shuffled)


# -----------------------------
# 8️ np.random.shuffle()
# -----------------------------
# Shuffles array in-place

data2 = np.array([1, 2, 3, 4, 5])
np.random.shuffle(data2)

print("Shuffled in-place:", data2)


# -----------------------------
# 9️ np.random.normal()
# -----------------------------
# Normal distribution with custom mean & std

f = np.random.normal(loc=50, scale=5, size=3)

# Mean=50, std=5
print("Custom normal:", f)


# -----------------------------
#  ML USE CASES
# -----------------------------

# 1️ Weight Initialization
# Random weights help break symmetry
weights = np.random.randn(3)
print("Weights:", weights)


# 2️ Bias Initialization
bias = np.random.rand(1)
print("Bias:", bias)


# 3️ Mini-batch Sampling
dataset = np.arange(100)

# Random batch of 10 samples
batch_indices = np.random.choice(len(dataset), 10)
batch = dataset[batch_indices]

print("Mini batch:", batch)


# 4️ Train/Test Split (manual)
np.random.seed(0)

data = np.arange(10)
shuffled = np.random.permutation(data)

train = shuffled[:7]
test = shuffled[7:]

print("Train:", train)
print("Test:", test)


# -----------------------------
# HOW it works internally
# -----------------------------
# - Uses deterministic PRNG algorithm 
# - A deterministic PRNG (Pseudo-Random Number Generator) is an algorithm that generates 
#   numbers using a fixed mathematical formula starting from an initial value called a  
#   seed. Because it is deterministic, the same seed will always produce the same sequence 
#  of numbers, making the results reproducible.

# - Seed → starting state
# - Generates sequence using math formula
# - Fast execution in C (no Python loops)


# -----------------------------
# SIMPLE IDEA
# -----------------------------
# Random = controlled randomness

# Same seed → same numbers
# Different seed → different results