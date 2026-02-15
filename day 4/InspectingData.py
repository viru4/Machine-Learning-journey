import pandas as pd

data = {
    "name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "age": [21, 22, None, 20, None],
    "marks": [85, 90, 78, 60, 88]
}

df = pd.DataFrame(data)
print(df)
print(df.head(1))
print(df.shape)
print(df.info())
print(df.describe())