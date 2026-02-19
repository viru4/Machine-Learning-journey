import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8],
    "Marks":[15,20,35,40,50,65,70,90],
    "Sleep_Hours":[8,7,7,6,6,5,5,4]
}

df = pd.DataFrame(data)
# create a column and plot count plot
df["Performance"] = ["Low","Low","Medium","Medium","Medium","High","High","High"]
# print(df)
sns.countplot(df["Performance"])
plt.show()

# Is dataset balanced or biased?
# almost balanced 