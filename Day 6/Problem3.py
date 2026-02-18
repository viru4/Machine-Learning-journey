import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8],
    "Marks":[15,20,35,40,50,65,70,90],
    "Sleep_Hours":[8,7,7,6,6,5,5,4]
}

df = pd.DataFrame(data)
# CReate Histogram of marks
plt.hist(df["Marks"])
plt.show()

# Normal distribution / skewed?
# slightly right skewed

# Any outlier?
# 90 looks like mild outlier

# Do we need normalization?
# yes recommended will be good