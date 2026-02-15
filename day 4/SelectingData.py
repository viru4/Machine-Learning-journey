import pandas as pd

data = {
    "name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "age": [21, 22, None, 20, None],
    "marks": [85, 90, 78, 60, 88]
}

df = pd.DataFrame(data)
print(df) # prints whole table
print(df["marks"]) #prints single column
print(df[["name", "marks"]]) # prints multiple columns
print(df.iloc[2]) #prints row with index 2
print(df.loc[2]) #prints row location based