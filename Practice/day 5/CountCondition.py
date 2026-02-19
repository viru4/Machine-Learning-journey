import numpy as np

a = np.array([10,20,30,40,50])
# count how many values are greater than average
avg=a.mean()
values=a[a>avg]
print(len(values))