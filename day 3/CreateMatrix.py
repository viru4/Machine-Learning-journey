# create a 5*5 matrix of random numbers
import numpy as np

a= np.random.randint(1, 9, 25)
print(a.reshape(5,5))