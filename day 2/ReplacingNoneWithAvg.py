prices = [100, 200, None, 400, 500, None]
# replacing the None with the average
valid= [x for x in prices if x is not None]
avg= sum(valid)/ len(valid)
cleaned = [avg if x is None else x for x in prices]
print(cleaned)