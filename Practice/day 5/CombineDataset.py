import numpy as np

maths = np.array([80,75,90])
science = np.array([70,85,88])
# combine them in a dataset like 
# [[80,70],
#  [75,85],
#  [90,88]]
dataset=np.column_stack((maths, science))
print(dataset) #column stack
data= np.row_stack((maths,science))
print(data) # row stack
# [[80 75 90]
#  [70 85 88]]