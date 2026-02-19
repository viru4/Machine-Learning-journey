import numpy as np

data = np.array([[10,20,30],
                 [40,50,60],
                 [70,80,90]])
print(np.sum(data, axis=0))
# 0 for column wise
# 1 for row wise in 2D table