import matplotlib.pyplot as plt
import pandas as pd

subjects = ["Math","Physics","Chemistry"]
marks = [80,65,90]

plt.bar(subjects, marks)
plt.title("Marks Comparison")
plt.show()
