import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Hours_Studied":[1,2,3,4,5,6,7,8],
    "Marks":[15,20,35,40,50,65,70,90],
    "Sleep_Hours":[8,7,7,6,6,5,5,4]
}

df = pd.DataFrame(data)
# line plot Hours_Studied vs Marks
plt.plot(df["Hours_Studied"], df["Marks"])
plt.title("Hours_StudiedVsMarksAnalysis")
plt.xlabel("Hours_Studied")
plt.ylabel("Marks")
plt.show()

# Does marks increase steadily? 
# yes

# Is learning linear or non-linear?
# Linear

# Will Linear Regression work well?
# yes