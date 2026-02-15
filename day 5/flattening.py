import numpy as np

arr=np.arange(12)
print(arr.reshape(3,4))
# auto reshaping
# numpy automatically calculates columns
print(arr.reshape(2,-1))

# flattening --> converting to 1D
print(arr.flatten()) #slow , creates a copy of data
print(arr.ravel()) #fast, doesnt create a copy(used commonally)