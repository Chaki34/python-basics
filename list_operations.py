# list creation 

list = [1, 2, 3, 4, 5]

print(list)

print(type(list))

print(list[0])  # Accessing first element

print(list[-1]) # Accessing last element

print(list.__len__()-1)  # Length of the list;

# List slicing
# General syntax of slicing
# string[start : stop : step]

# Meaning:

# start → index where slicing begins (included)
# stop  → index where slicing ends (not included)
# step  → gap between characters (optional)

# Example 1:
print(list[1:3])  
# start = 1 → start from index 1 (value = 2)
# stop = 3 → go till index 2 (3 is NOT included)
# result = [2, 3]

# Example 2:
print(list[::2])
# start = default (0)
# stop = default (end of list)
# step = 2 → take every 2nd element
# result = [1, 3, 5]

print(list[1:-1:2]) # start = 1, stop = -1 (go till second last element), step = 2


# frequently used list methods

my_list = [3, 1, 4, 1, 5]

my_list.append(9) # Adds 9 at the end of the list
print(my_list)  # [3, 1, 4, 1, 5, 9]

my_list.insert(2, 10) # Inserts 10 at index 2
print(my_list)  # [3, 1, 10, 4, 1, 5, 9]

my_list.remove(1) # Removes the first occurrence of 1
print(my_list)  # [3, 10, 4, 1, 5, 9]

my_list.pop() # Removes and returns the last element
print(my_list)  # [3, 10, 4, 1, 5]

num = my_list.pop(1) # Removes and returns element at index 1
print(num)  # 10
print(my_list)  # [3, 4, 1, 5]  

my_list.sort() # Sorts the list in ascending order
print(my_list)  # [1, 3, 4, 5]

my_list.reverse() # Reverses the list
print(my_list)  # [5, 4, 3, 1]

# Descending order
my_list.sort(reverse=True)
print(my_list)  # [5, 4, 3, 1]


my_list.remove(3) # Removes the first occurrence of 3
print(my_list)  # [5, 4, 1] 

my_list.extend([6,7,8,9]) # Extends the list by adding elements from another list
print(my_list)  # [5, 4, 3, 1, 6, 7, 8, 9]

new_list = my_list.copy() # Creates a shallow copy of the list
print(new_list)  # [5, 4, 3, 1, 6, 7, 8, 9]

new_list.insert(4, 4) # Inserts 4 at index 4
new_list.append(10) # Adds 10 at the end of the list


print(new_list.__len__())  # 8

print("The count of 4 is: " + str(new_list.count(4)))  # Counts occurrences of 4 (1)

print("The index of 6 is: " + str(new_list.index(6)))  # Returns index of first occurrence of 6 (4)

print("max:", max(new_list))  # Returns maximum value in the list (10)

print("min:", min(new_list))  # Returns minimum value in the list (1)

print("sum:", sum(new_list))  # Returns sum of all elements in the list (39)



# list is mutable (can be changed after creation)

# Replace single item using index
my_list[0] = 10
print("my_list: " + str(my_list))  # [10, 4, 3, 1]

# Replace multiple items using slicing
my_list[1:3] = [20, 30]
print("my_list: " + str(my_list))  # [10, 20, 30, 1]

a = [1, 2, 3]

a[1:2] = [10, 20, 30]

print("a: " + str(a))
# [1, 10, 20, 30, 3]









