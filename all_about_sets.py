

# set cration

my_set = {1, 2, 3, 4, 5} # it not contains duplicate elements
print(type(my_set))

my_set1 = set([1, 2, 3, 4, 5]) # creating a set from a list
print(type(my_set1))

# PROPERTIES OF PYTHON SETS
# 1. It is unordered.
# 2. It is mutable.
# 3. It is not indexed.
# 4. Cannot contain duplicate elements
my_set.add(6) # adding an element to the set
print(my_set)

my_set.remove(3) # removing an element from the set but raises an error if the element is not present
print(my_set)

my_set.discard(4) # removing an element from the set, but does not raise an error if the element is not present
print(my_set)

# set to tuple 

my_tuple = tuple(my_set) # converting a set to a tuple
print(type(my_tuple))

# set to dictionary

set1 = {"a", "b", "c"}
set2 = {1, 2, 3}

# creating a dictionary from two sets using zip function

my_dict = dict(zip(set2, set1)) # creating a dictionary from two sets using zip function
print(my_dict)
print(type(my_dict))


# ============================================
# SET OPERATIONS IN PYTHON (AI/ML/DL USEFUL) (SET THEORY) 
# ============================================

setA = {1, 2, 3, 4, 5}
setB = {4, 5, 6, 7, 8}

# --------------------------------------------
# 1. Intersection (Common elements)
# Used in ML: finding common features, overlap
# --------------------------------------------
print(setA.intersection(setB))      # OR setA & setB


# --------------------------------------------
# 2. Union (All unique elements)
# Used in ML: combining datasets/features
# --------------------------------------------
print(setA.union(setB))             # OR setA | setB


# --------------------------------------------
# 3. Difference (Elements in A not in B)
# Used in ML: filtering data, removing overlap
# --------------------------------------------
print(setA.difference(setB))        # OR setA - setB


# --------------------------------------------
# 4. Reverse Difference (B - A)
# --------------------------------------------
print(setB.difference(setA))


# --------------------------------------------
# 5. Symmetric Difference (Non-common elements)
# Used in ML: finding mismatched data
# --------------------------------------------
print(setA.symmetric_difference(setB))   # OR setA ^ setB


# --------------------------------------------
# 6. Subset (Check if A is inside B)
# Used in ML: checking feature inclusion
# --------------------------------------------
print(setA.issubset(setB))          # OR setA <= setB


# --------------------------------------------
# 7. Superset (Check if A contains B)
# --------------------------------------------
print(setA.issuperset(setB))        # OR setA >= setB


# --------------------------------------------
# 8. Disjoint (No common elements)
# Used in ML: checking independent datasets
# --------------------------------------------
print(setA.isdisjoint(setB))


# --------------------------------------------
# 9. Add element
# --------------------------------------------
setA.add(10)
print(setA)


# --------------------------------------------
# 10. Remove element (error if not found)
# --------------------------------------------
setA.remove(10)


# --------------------------------------------
# 11. Discard element (no error if not found)
# --------------------------------------------
setA.discard(100)


# --------------------------------------------
# 12. Pop random element
# --------------------------------------------
setA.pop()


# --------------------------------------------
# 13. Clear set
# --------------------------------------------
setA.clear()


# --------------------------------------------
# 14. Copy set
# --------------------------------------------
new_set = setB.copy()


# --------------------------------------------
# 15. Update (add multiple elements)
# --------------------------------------------
setB.update([9, 10, 11])
print(setB)