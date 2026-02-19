data = [10, 20, 30, 40, 50]
maximum = max(data)
minimum= min(data)
normalized = ((x-minimum)/(maximum-minimum) for x in data)
print(normalized)