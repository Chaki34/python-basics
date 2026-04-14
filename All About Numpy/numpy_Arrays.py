import numpy as np

# 1D Array
arr_1d = np.array([1, 2])
print(arr_1d)
print(type(arr_1d))
print(f"this array is  : {arr_1d.ndim}D")

# 2D Array
arr_2d = np.array([[1, 2],
                   [3, 4]])
print(arr_2d)
print(type(arr_2d))
print(f"this array is  : {arr_2d.ndim}D")

# 3D Array
arr_3d = np.array([[[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]])

print(arr_3d)
print(type(arr_3d))
print(f"this array is  : {arr_3d.ndim}D")


# a.shape    # dimensions
# a.ndim     # number of dimensions
# a.size     # total elements
# a.dtype    # data type

# use for How your data is arranged basically show dimention with items 
# (2,) --> 1D (elements,)
#(2, 2) --> 2D (rows, columns)
#(1, 3, 3) --> 3D (layers, rows, columns)
print(arr_1d.shape)             
print(arr_2d.shape)
print(arr_3d.shape)  

a = np.array([[1,2],[3,4],[5,6],[7,8],[10,20]])
print(type(a))
print(a)

print(a.ndim) # to know exact shape means dimention 

print(a.size) # count/size of total items 

print(a.dtype)

# if we need to make particular datatype array and u want to mention it  

new_a= np.array([[[1,2],[3,4],[6,7]]], dtype=float)

print(new_a.dtype)

a = np.array([1,2,3,4])

new_array = a[a > 2] # say starting from 2th index 

print(new_array)
