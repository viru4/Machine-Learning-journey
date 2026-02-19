import numpy as np

marks = np.array([35, 67, 90, 23, 89, 55, 100, 45, 72])
#  find average marks
print(np.mean(marks))
# find students who passed >=40
print(marks[marks >=40])
# count number of toppers 
print(len(marks[marks >=90]))
# convert into 3 columns dataset
print(marks.reshape(-1,3))
# normalize marks
# print((x-np.mean(marks)/np.std for x in marks))
normalized= (marks-np.mean(marks))/np.std(marks)
print(normalized)