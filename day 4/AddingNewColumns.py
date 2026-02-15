import pandas as pd

data = {
    "name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "age": [21, 22, None, 20, None],
    "marks": [85, 90, 78, 60, 88]
}
df= pd.DataFrame(data)
df["grade"]= df["marks"]/10 #adds a new column
print(df)