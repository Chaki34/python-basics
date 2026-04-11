
# 1. Create tuple
t = (10, 20, 30, 40, 20)
print("Tuple:", t)

# 2. Empty tuple
t_empty = ()
print("Empty tuple:", t_empty)

# 3. Single element tuple
t_single = (5,)
print("Single element tuple:", t_single)

# 4. Mixed tuple
t_mixed = (1, "hello", 3.5)
print("Mixed tuple:", t_mixed)

# 5. Access element
print("Index 1:", t[1])

# 6. Negative indexing
print("Last element:", t[-1])

# 7. Slicing
print("Slice [1:4]:", t[1:4])

# 8. Step slicing
print("Step slicing [::2]:", t[::2])

# 9. Length
print("Length:", len(t))

# 10. Count occurrences
print("Count 20:", t.count(20))

# 11. Index method
print("Index of 30:", t.index(30))

# 12. Membership
print("20 in tuple:", 20 in t)

# 13. Not in
print("50 not in tuple:", 50 not in t)

# 14. Loop through tuple
print("Loop:")
for i in t:
    print(i)

# 15. Concatenation
t1 = (1, 2)
t2 = (3, 4)
print("Concatenation:", t1 + t2)

# 16. Repetition
print("Repetition:", t1 * 3)

# 17. Minimum
print("Min:", min(t))

# 18. Maximum
print("Max:", max(t))

# 19. Sum
print("Sum:", sum(t))

# 20. Tuple is IMMUTABLE (important concept)
# t[0] = 100  ❌ ERROR (cannot modify tuple)
print("Tuple is immutable: cannot change values directly")

# 21. Convert tuple to list (to modify)
l = list(t)
print("Tuple to list:", l)

# 22. Append (only possible after conversion)
l.append(100)
print("After append in list:", l)

# 23. Convert list back to tuple
t_new = tuple(l)
print("List to tuple:", t_new)

# 24. String to tuple
s = "python"
t_str = tuple(s)
print("String to tuple:", t_str)

# 25. Tuple to string
t_words = ('p', 'y', 't', 'h', 'o', 'n')
word = "".join(t_words)
print("Tuple to string:", word)

# 26. Nested tuple
nested = (1, (2, 3), (4, 5))
print("Nested tuple:", nested)

# 27. Access nested tuple
print("Nested access:", nested[1][0])