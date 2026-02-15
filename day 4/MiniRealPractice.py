import pandas as pd

data = {
    "name": ["Aman","Riya","Karan","Neha","Rahul","Sneha","Arjun","Pooja"],
    "age": [21,22,None,20,21,None,23,22],
    "math": [85,90,78,60,88,92,None,75],
    "science": [80,None,70,65,90,95,85,60],
    "english": [78,88,72,None,85,91,79,74]
}

df = pd.DataFrame(data)
print(df)
# print first five rows
print(df.head())
#dataset shape
print(df.shape) #returns no. of rows and columns
# column names
print(df.columns)
# print full info
print(df.info())
# statistics
print(df.describe())
# finding missing values
print(df.isnull().sum())

# replace missing age with average age
df["age"].fillna(df["age"].mean(), inplace=True)
# print(df)

# replace missing marks with subject average
df["math"].fillna(df["math"].mean(), inplace=True)
df["science"].fillna(df["science"].mean(), inplace=True)
df["english"].fillna(df["age"].mean(), inplace=True)
# print(df)

# Create a new column of total marks and percentage
df["totalmarks"]= df["english"]+df["math"]+df["science"]
df["percentage"]= df["totalmarks"]/3
df["result"]= df["percentage"]>=70 
df["result"] = df["result"].map({True:"Pass", False:"Fail"})

print(df)

# top 3 students
print(df.sort_values("percentage", ascending=False).head(3))
# avg percentage of class
print(df["percentage"].mean())
# total no. of passed students
print(df["result"].value_counts())
# average percentage of passed and failed students
print(df.groupby("result")["percentage"].mean())