# Numpy:
# Numpy(Numerical python) is a python library used for scientific and mathematical computing.
# It provides:
# -> Powerfull array objects(more effective than python lists.)
# -> Vectorized operations (Fast element-wise calculations.)
# -> Support for linear algebra, statistics,Random numbers operations etc...
# importing the numpy librabry.
import numpy as np
import array as arr
#CREATING AM ARRAY WITH NUMPY:
A1D = np.array([1,2,3,4,5])
# print(A1D) #1D ARRAY 
# print(A1D.ndim) #1D ARRAY 
# print(A1D.shape) #1D ARRAY 
# print(A1D.size) #1D ARRAY 
# print(A1D.dtype) #1D ARRAY 

#A2D = np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(A2D) #2D ARRAY 
# print(A2D.shape)
# print(A2D.ndim)
# print(A2D.size)
# print(A2D.dtype)
 
 #zeros:
# print(np.zeros(6))
#ones:
# print(np.ones(6))
#ARANGE: funs as "range" in for loop        # divide only in integer form
# print(np.arange(1,11,2)) # [1 3 5 7 9]     
#Linspace:
# print(np.linspace(1,5,6))             # can divide in both "int" and "decimal" form

#mathematical operations:
# print(A1D+6)
# print(A1D-6)
# print(A1D//6)
# print(A1D**5)
# print(A1D/6)

#Aggregate function:
# print(np.sum(A1D))
# print(np.mean(A1D))
# print(np.min(A1D))
# print(np.max(A1D))
# print(np.median(A1D))
# print(np.std(A1D))
# print(np.cumprod(A1D))

# matrix operations :
# Mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
# Mat2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
# print(Mat1+Mat2)
# print(Mat1**2)
# print(Mat1**Mat2) # will not be the corect ans as we do
# print(np.dot(Mat1,Mat2))
# print(np.transpose(Mat1))