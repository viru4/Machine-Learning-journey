import matplotlib.pyplot as plt
import pandas as pd

data = [10,12,13,15,15,16,18,20,21,21,22,25,30]

plt.hist(data, bins=5)
plt.title("Data Distribution")
plt.show()
