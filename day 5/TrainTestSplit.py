import numpy as np

data = np.arange(20)
split=int(0.7*len(data))
Train=data[:split]
Test=data[split:]
print("train", Train)
print("Test", Test)