import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt

df = sns.load_dataset("tips")
# print(df)
sns.countplot(x="sex", data=df)
plt.show()

# If you train model to predict sex → will model be biased?
# in graph male>female
# so model will be biased towards males