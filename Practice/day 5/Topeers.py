import numpy as np

scores = np.array([[85,78,92],
                   [60,65,70],
                   [95,88,91],
                   [40,50,45]])
# find students whose average is >80
avg=np.mean(scores, axis=1)
toppers=scores[avg>80]
print(toppers)