import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8],
    "Marks":[15,20,35,40,50,65,70,90],
    "Sleep_Hours":[8,7,7,6,6,5,5,4]
}

df = pd.DataFrame(data)
# Create Scatterplot between Sleep_Hours Vs Marks
plt.scatter(df["Sleep_Hours"], df["Marks"])
plt.xlabel("Sleep_Hours")
plt.ylabel("Marks")
plt.show()

# Positive or negative relation?
# -ve relation

# Does more sleep mean more marks?
# MOre Sleep --> Less Marks

# Should this feature be used in ML model?
# No Weak Predictor. can lead to confusion