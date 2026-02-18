import numpy as np

data = np.array([[170,65],
                 [180,72],
                 [175,68],
                 [160,55]])
# find mean height
print(data[:,0].mean())
# find max weight
weight= data[:, 1]
print(weight.max())
# columnwise mean
print(data.mean(axis=0))