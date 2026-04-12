"""
===========================================
 PYTHON FUNCTIONS + RECURSION DEMO
 + DATA STRUCTURES + AI/ML USAGE NOTES
===========================================
"""

# ===========================================
# 1. BASIC FUNCTION
# ===========================================
print("1. BASIC FUNCTION:")

def greet(name):
    # Function is reusable block of code
    return f"Hello {name}"

print(greet("Debmalya"))


# ===========================================
# 2. FUNCTION WITH LIST (VERY IMPORTANT FOR AI/ML)
# ===========================================
print("\n2. FUNCTION WITH LIST:")

data = [10, 20, 30, 40, 50]

def square_list(lst):
    # Used in ML for feature scaling, preprocessing
    result = []
    for x in lst:
        result.append(x * x)
    return result

print("Squared Data:", square_list(data))


# ===========================================
# 3. FUNCTION WITH DICTIONARY (DATA LABELS)
# ===========================================
print("\n3. FUNCTION WITH DICTIONARY:")

student = {"name": "A", "marks": 90}

def update_marks(d, extra):
    # Used in ML for updating feature values
    d["marks"] += extra
    return d

print(update_marks(student, 5))


# ===========================================
# 4. FUNCTION WITH SET (UNIQUE FEATURES)
# ===========================================
print("\n4. FUNCTION WITH SET:")

features = {1, 2, 3, 3, 2}

def add_feature(s, value):
    # Used in AI feature selection (unique features only)
    s.add(value)
    return s

print(add_feature(features, 10))


# ===========================================
# 5. TUPLE USAGE (IMMUTABLE DATA - VERY IMPORTANT IN ML)
# ===========================================
print("\n5. TUPLE:")

point = (10, 20)

def distance_from_origin(pt):
    # tuples used for fixed data like coordinates
    x, y = pt
    return (x**2 + y**2) ** 0.5

print("Distance:", distance_from_origin(point))


# ===========================================
# 6. LAMBDA FUNCTION (USED IN ML PIPELINES)
# ===========================================
print("\n6. LAMBDA FUNCTION:")

square = lambda x: x * x
print("Square:", square(5))

# Used in ML for quick transformations
numbers = [1, 2, 3, 4]
print("Map Square:", list(map(lambda x: x*x, numbers)))


# ===========================================
# 7. RECURSION (VERY IMPORTANT IN AI/GRAPH/SEARCH)
# ===========================================
print("\n7. RECURSION:")

def factorial(n):
    # Used in probability, ML optimization, deep learning math
    if n == 0:
        return 1
    return n * factorial(n - 1)

print("Factorial:", factorial(5))


# Fibonacci (used in DP, AI search problems)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

print("Fibonacci:", fibonacci(6))


# ===========================================
# 8. RECURSION + TREE STYLE THINKING (AI USE CASE)
# ===========================================

def dfs_tree(node):
    """
    Simulating DFS (Depth First Search)
    Used in:
    - AI decision trees
    - Game AI
    - Graph traversal in ML
    """
    if node is None:
        return

    print("Visiting node:", node)

    # pretend children (tree structure)
    left = node * 2
    right = node * 2 + 1

    if node < 3:  # stopping condition
        dfs_tree(left)
        dfs_tree(right)


print("\nDFS Simulation:")
dfs_tree(1)


# ===========================================
# 9. FUNCTION RETURNING FUNCTION (CLOSURE)
# ===========================================
print("\n9. CLOSURE:")

def multiplier(n):
    # Used in ML for dynamic feature scaling
    def multiply(x):
        return x * n
    return multiply

double = multiplier(2)
print("Double of 10:", double(10))


# ===========================================
# 10. FUNCTION IN AI / ML / DL REAL USE
# ===========================================

def normalize(data):
    """
    Very important in ML:
    scaling data between 0 and 1
    """
    max_val = max(data)
    min_val = min(data)

    return [(x - min_val) / (max_val - min_val) for x in data]


ml_data = [10, 20, 30, 40]
print("\nNormalized Data (ML Preprocessing):", normalize(ml_data))


# ===========================================
# SUMMARY (IMPORTANT FOR YOU)
# ===========================================

"""
WHERE FUNCTIONS + RECURSION ARE USED:

AI / ML:
- Data preprocessing (normalize, scale)
- Feature engineering
- Map/Reduce operations
- Model pipelines

Deep Learning:
- Tensor transformations
- Activation functions
- Backpropagation logic (recursive math thinking)

Algorithms:
- DFS / BFS (Graph AI)
- Dynamic Programming
- Search problems

Python Programming:
- Code reuse
- Clean architecture
- Modular design
"""