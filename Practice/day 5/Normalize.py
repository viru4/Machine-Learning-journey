import numpy as np 

x = np.array([2,4,6,8,10])
normalize= (x-x.min())/(x.max()-x.min())
print(normalize)