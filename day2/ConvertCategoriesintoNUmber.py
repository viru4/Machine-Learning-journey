colors = ["red", "blue", "green", "blue", "red"]

unique = list(set(colors))
encoding = {color: i for i, color in enumerate(unique)}

encoded = [encoding[c] for c in colors]

print(encoding)
print(encoded)