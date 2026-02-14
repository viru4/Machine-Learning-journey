data = list(range(1, 21))
split= int (0.8*len(data))
Train= data[split:]
Test= data[:split]
print(Train, "Train")
print(Test, "Test")