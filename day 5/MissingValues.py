import numpy as np

# replace -ve values with 0
data = np.array([5,-3,8,-1,10,-7])
data[data<0]=0
print(data)