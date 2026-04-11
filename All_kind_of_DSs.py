# =====================================================
#  PYTHON COLLECTIONS (BUILT-IN DATA STRUCTURES)
# =====================================================

# Step 1: Display heading
print("===== PYTHON COLLECTIONS DEMO =====")


# =====================================================
#  1. LIST (Mutable, Ordered)
# =====================================================

# Step 2: Create a list
numbers = [10, 20, 30, 20]

# Step 3: Perform operations
numbers.append(40)          # add element
numbers.remove(20)          # remove first occurrence

print("\nList:", numbers)


# =====================================================
#  2. TUPLE (Immutable, Ordered)
# =====================================================

# Step 4: Create tuple
data_tuple = (1, 2, 3, 4)

# Step 5: Access elements
print("\nTuple:", data_tuple)
print("First element:", data_tuple[0])


# =====================================================
#  3. SET (Unordered, No duplicates)
# =====================================================

# Step 6: Create set
data_set = {1, 2, 3, 3, 4}

# Step 7: Add element
data_set.add(5)

print("\nSet:", data_set)


# =====================================================
#  4. DICTIONARY (Key-Value Pair)
# =====================================================

# Step 8: Create dictionary
student = {
    "name": "Debmalya",
    "age": 21,
    "marks": 85
}

# Step 9: Access and update
student["age"] = 22

print("\nDictionary:", student)
print("Name:", student["name"])


# =====================================================
#  5. COLLECTIONS MODULE
# =====================================================

from collections import Counter, deque, defaultdict

# Step 10: Counter (count frequency)
text = "hello world"
counter = Counter(text)
print("\nCounter:", counter)

# Step 11: deque (queue operations)
dq = deque([1, 2, 3])
dq.appendleft(0)
dq.append(4)
print("Deque:", dq)

# Step 12: defaultdict (default values)
d = defaultdict(int)
d["a"] += 1
d["b"] += 2
print("DefaultDict:", dict(d))


# =====================================================
#  MINI PRACTICE (AI STYLE)
# =====================================================

# Step 13: Store features and weights
features = [2, 4, 6]
weights = [0.5, 0.2, 0.1]

# Step 14: Calculate prediction using loop
prediction = 0
for i in range(len(features)):
    prediction += features[i] * weights[i]

print("\nAI Prediction:", prediction)


# =====================================================
#  END OF PROGRAM
# =====================================================