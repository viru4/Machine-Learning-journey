import pandas as pd
data = {
    "name": ["Aman", "Riya", "Karan", "Neha", "Rahul"],
    "age": [21, 22, None, 20, None],
    "marks": [85, 90, 78, 60, 88]
}
df= pd.DataFrame(data)
df["result"]= df["marks"]>80 #creates a column "result" with filtered values
print(df.groupby("result")["marks"].mean()) #analyze the result column and 
# give means of pass and fail students
print(df)