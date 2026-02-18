import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# box plot total_bill vs day
sns.boxplot((df["total_bill"], df["day"]))
plt.title("total_bill vs day")
plt.xlabel("total_bill")
plt.ylabel("day")
plt.show()

# Which day has highest spending?
# weekends

# Are outliers present?
# many outliers

# Should we remove them?
#  yes but not all