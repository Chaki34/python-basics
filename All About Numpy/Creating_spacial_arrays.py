import numpy as np 

special_array = np.zeros((2,3))


print(special_array)
print(type(special_array))

special_Array2 = np.ones((2,4))
print(special_Array2)


# crate a identity metrix - 
print("\n Identitity Mastrix : \n")
print(np.eye(6))


print(np.arange(0,10,2))   # range syntax - np.arnage(start , stop , step) step means how many diff b/w two number for here prent only even numbers  

a = np.array([1,2,3,4,5,6])
a_array = np.array([[3,2,3],[7,5,7]])

print(a[0])       # first element
print(a[1:5])     # slicing  syntax - a[start : end] here end is 3 means print before index 5 means upto 4th idex 

# for 2-D arrays -

print((f"the dimention of the array  : {a_array.ndim}"))
array = a_array[0:1]  
print("for 2d array",array)


# Element wise operations - 

a = np.array([1,2,3])
b = np.array([4,5,6])

# NumPy performs element-wise addition:
# Internally loops (in optimized C) over each index:
# result[i] = a[i] + b[i]
# → [1+4, 2+5, 3+6] = [5, 7, 9]
print(f"element wise add {a + b}")

# Element-wise subtraction:
# result[i] = a[i] - b[i]
# → [1-4, 2-5, 3-6] = [-3, -3, -3]
print(f"element wise sub {a - b}")


# '&' is a bitwise AND operation:
# It compares binary representation of each element:
# 1 & 4 → 001 & 100 = 000 → 0
# 2 & 5 → 010 & 101 = 000 → 0
# 3 & 6 → 011 & 110 = 010 → 2
print(f"element wise AND {a & b}")

#csimilarly perfrom or, not,  xor  

# Element-wise multiplication:
# result[i] = a[i] * b[i]
# → [1*4, 2*5, 3*6] = [4, 10, 18]
print(f"element wise mul {a * b}")

# Element-wise division:
# result[i] = a[i] / b[i]
# NumPy converts to float automatically
# → [1/4, 2/5, 3/6] = [0.25, 0.4, 0.5]
print(f"element wise div {a / b}")

# Mathematical Functions

print(np.sum(a))
print(np.mean(a))
print(np.min(a))
print(np.max(a))
print(np.std(a))

# reshaping arrays - 

a = np.array([1,2,3,4])

print(a.ndim)

a = a.reshape(2,2)
print((a.ndim))

print(a)  








