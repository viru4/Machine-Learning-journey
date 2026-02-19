import numpy as np

marks = np.array([12,85,90,34,100,29,300,78])
# remove impossible marks >100
print(marks[marks>100])
marks=marks[marks<=100]
print(marks)