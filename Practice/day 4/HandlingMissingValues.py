import pandas as pd

data = {
    "name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "age": [21, 22, None, 20, None],
    "marks": [85, 90, 78, 60, 88]
}
df = pd.DataFrame(data)
print(df.isnull().sum()) #returns number of null (None) in a column 

# to handle these null values use these methods
