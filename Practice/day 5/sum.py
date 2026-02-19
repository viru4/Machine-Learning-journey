import numpy as np

marks = np.array([35, 67, 90, 23, 89, 55, 100, 45, 72])

passed = np.len(marks >= 40)

print(passed)
print(np.sum(marks))